"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


# Trường duy nhất được gửi sang hãng vận chuyển (bên thứ ba). Chữ khách tự gõ (customer_note) và liên hệ người nhận
# (recipient_contact) KHÔNG nằm trong danh sách này.
CARRIER_ALLOWED_FIELDS = ("order_id", "parcel_id", "district", "delay_days")


def _db_truth(ctx, order_id):
    """Quyền lợi theo nguồn sự thật: bưu kiện trễ nhất theo tracking DB, chính sách có hiệu lực tại as_of."""
    order = ctx.tools.lookup_order(order_id)
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if order is None or pol is None:
        return None, None, None
    worst = max(order["parcels"], key=lambda p: H.db_delay_days(p, ctx.as_of))
    delay = H.db_delay_days(worst, ctx.as_of)
    cause = worst.get("delay_cause") or ("CARRIER" if delay > 0 else None)
    return order, pol, H.entitlement_vnd(pol, order, delay, cause)


def pre_guard(ctx):
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")

    # Cổng 1 (B4 WRONG amount_vnd / pre-mortem kỹ thuật): tiền hoàn không được vượt quyền lợi tính từ DB.
    # Số ngày khách khai, chỉ thị trong ticket hay chính sách cũ làm số tiền cao hơn DB thì chuyển người duyệt.
    if tool == "issue_refund":
        order, pol, entitled = _db_truth(ctx, action["order_id"])
        if order is None:
            return Verdict.escalate("không đối chiếu được đơn/chính sách với DB: chuyển người duyệt")
        if ctx.tools.ledger_rows(order_id=action["order_id"]):
            ctx.log("refund_gate", reason="order_already_in_ledger", order_id=action["order_id"])
            return Verdict.escalate("đơn đã có dòng hoàn trong sổ cái: chuyển người duyệt")
        if int(action["amount_vnd"]) > entitled:
            ctx.log("refund_gate", reason="amount_above_db_entitlement", asked=int(action["amount_vnd"]), entitled=entitled)
            return Verdict.escalate(f"số tiền {int(action['amount_vnd'])}đ vượt quyền lợi theo DB {entitled}đ: chuyển người duyệt")

    # Cổng 2 (B4 INVALID / pre-mortem pháp lý): chỉ ghi lỗi cho hãng khi DB xác nhận trễ thật và nguyên nhân hợp lệ.
    if tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action["order_id"])
        pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        parcel = next((p for p in (order or {"parcels": []})["parcels"] if p["parcel_id"] == action.get("parcel_id")), None)
        if order is None or pol is None or parcel is None:
            return Verdict.deny("không xác minh được bưu kiện trong DB: không ghi lỗi hãng")
        if not H.carrier_at_fault(pol, parcel, H.db_delay_days(parcel, ctx.as_of)):
            ctx.log("fault_gate", reason="db_does_not_support_fault", parcel_id=parcel["parcel_id"])
            return Verdict.deny("DB không xác nhận hãng có lỗi: không ghi lỗi hãng")

    # Cổng 3 (B4 PERTURBED / pre-mortem pháp lý): dữ liệu gửi bên thứ ba chỉ gồm các trường cho phép.
    if tool == "notify_carrier":
        payload = action.get("payload") or {}
        clean = {k: v for k, v in payload.items() if k in CARRIER_ALLOWED_FIELDS}
        if clean != payload:
            ctx.log("pii_gate", dropped=sorted(set(payload) - set(clean)))
            return Verdict.modify("chỉ gửi các trường cho phép sang hãng", payload=clean)

    return Verdict.allow()
