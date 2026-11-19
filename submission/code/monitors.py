"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def fault_on_non_worst_parcel_rate(trials):
    """Thẻ S6. Thước đo: tỉ lệ lần chạy có ghi lỗi hãng mà kiện bị ghi KHÔNG phải kiện trễ nhiều nhất của đơn
    theo tracking (đơn vị chịu lỗi của hệ thống là đơn, của người vận hành là kiện).
    Dữ liệu: sự kiện `tracking.parcels` (delay từng kiện) và dòng lỗi hãng `faults` trong trial, không cần nhãn.
    Cách tính: số lần chạy có ≥ 1 dòng lỗi hãng ghi cho kiện có delay < delay lớn nhất của đơn, chia số lần chạy có ≥ 1 dòng lỗi hãng.
    Điểm mù: không thấy ca hai kiện của hai hãng trễ bằng nhau, và không thấy ca chính tracking sai."""
    with_fault = bad = 0
    for t in trials:
        if not t["faults"]:
            continue
        with_fault += 1
        tracking = next((e for e in t["events"] if e["type"] == "tracking"), None)
        if tracking is None:
            continue
        delay = {p["parcel_id"]: p["delay"] for p in tracking["parcels"]}
        worst = max(delay.values(), default=0)
        if any(delay.get(f["parcel_id"], 0) < worst for f in t["faults"]):
            bad += 1
    return bad / max(1, with_fault)


def max_faults_per_carrier_day(trials):
    """Thẻ S6. Thước đo: số lỗi hãng nhiều nhất mà MỘT hãng bị ghi tự động trong MỘT ngày vận hành (trần Ops: 2).
    Dữ liệu: dòng lỗi hãng `faults` của mỗi trial, nhóm theo (day, seed, carrier_id); không cần nhãn.
    Cách tính: đếm dòng lỗi theo nhóm rồi lấy giá trị lớn nhất; ngày không có lỗi nào cho 0.
    Điểm mù: không thấy lỗi ghi đúng nhưng dồn dập do sự cố thật của hãng."""
    count: dict = {}
    for t in trials:
        for f in t["faults"]:
            key = (t["day"], t["seed"], f["carrier_id"])
            count[key] = count.get(key, 0) + 1
    return max(count.values(), default=0)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "fault_on_non_worst_parcel_rate": fault_on_non_worst_parcel_rate,
    "max_faults_per_carrier_day": max_faults_per_carrier_day,
}
STARTER_MONITORS = ("escalation_rate",)
