# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): T2
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-T2-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S6

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Lê Hải Lân | 2A202603915 | Kỹ sư cổng  |    x         |
|   2 | Lương Thị Hồng Hạnh |2A202603748| Vận hành và pháp lý |             |
|   3 | Vương Quang Thắng  | 2A202603855  | Sản phẩm và kinh doanh  |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## LeHaiLan-2A202603915

### Phần việc phụ trách

Vai Kỹ sư cổng (trưởng nhóm). Phiếu A câu 1.3; Phiếu B câu 2.1, 2.2, 2.6, 2.7, 2.8 và chốt cổng vòng 1; Phiếu C mục C0, C1, C2, C7 (phần code), C8; các file `lab10/guards.py`, `lab10/monitors.py`; chạy `lab10.eval`, `lab10.grade`, `lab10.checkpoint`, `lab10.check_submission`.

### Đóng góp cụ thể

- Viết offline metric cho bước "đọc ticket" (Phiếu A, câu 1.3).
- Chạy base và trace `T-002@55`, viết 3 cổng vòng 1 trong `write_gate` (tiền không vượt quyền lợi theo DB, lỗi hãng cần DB xác nhận, chỉ gửi 4 trường sang hãng) và hai ticket hiểm cho demo.
- Chốt cổng vòng 1 (hash `07eda9aa`).
- Thẻ S6: tìm ba lỗi (ghi lỗi sai kiện, đoán khi hai hãng cùng trễ, vượt trần lỗi mỗi hãng mỗi ngày), thêm cổng 4 và 5 và hai chỉ số `fault_on_non_worst_parcel_rate`, `max_faults_per_carrier_day`.
- Sửa lỗi kiểm `integrity` do dấu xuống dòng CRLF của các file khóa trên máy cá nhân.

### Bằng chứng

- Commit: `97629a9` (ký tiêu chí), `32ca6f7` (chốt vòng 1), `4fd420e` (nhận thẻ S6), `bf0500b` (Phiếu C cho S6).
- Mã lần chạy: base `R-base-before-20261119-202059-bde05c`, prepared `R-base-prepared-20261119-211733-0d6a5f`; thẻ S6 base `R-S6-before-20261119-214310-65e7cb`, prepared `R-S6-prepared-20261119-214310-65e7cb`, after `R-S6-after-20261119-214310-65e7cb`.
- Phiếu: A (A2), B (B0, B1, B2, B7.1–B7.3, B8), C (C0, C1, C2, C7, C8).

### Exit ticket

Một điều học được: Một cổng tốt phải lấy nguồn sự thật từ dữ liệu của hệ thống, không lấy từ chữ khách viết, và phải chọn đúng đơn vị mà người trong nghề dùng. Ở thẻ S6, trợ lý ghi lỗi theo đơn (parcels[0]) trong khi hãng vận chuyển tính lỗi theo kiện. Cổng vòng 1 chỉ so tiền với quyền lợi của kiện trễ nhất nên chỉ đỡ được lỗi oan từ 40 xuống 10. Sau khi đổi sang xác định đúng kiện, chuyển người khi không rõ, và đặt trần 2 lỗi/hãng/ngày, lỗi oan về 0 mà bộ nền vẫn đạt 65/65.

Một điều còn chưa chắc: Cổng của mình tin tracking DB. Nếu ngày giao hoặc nguyên nhân do máy quét hay người nhập tay bị sai thì cổng vẫn ghi sai, nên đây chỉ là giảm chứ chưa ngăn hẳn. Mình cũng chưa chắc ROI sau sửa (0,34, gần ngưỡng đã ký 0,15) có giữ được khi tải thật, vì nhiều ca bị chuyển người hơn. Dữ liệu ở đây là mock nên cần đo lại trong pilot.

## LuongThiHongHanh-2A202603748

*(Hạnh tự viết mục này theo mẫu ở trên: phần việc, đóng góp cụ thể, bằng chứng, exit ticket.)*

## VuongQuangThang-2A202603855
### Phần việc phụ trách

- **Vai trong bàn:** Sản phẩm và kinh doanh[cite: 2, 7].
- **Câu trong đề & mục phiếu:**
  - **Phiếu A (`templates/form-a-criteria.md`):** Mục A1 (Câu 1.1), cùng bàn chốt Mục A3 (Câu 1.5), Mục A4 (Câu 1.6 — câu tiêu chí, ranh giới đầu ra, 4 câu soát, ngưỡng `business_ops`), và soát ký Mục A5[cite: 2, 10].
  - **Phiếu B (`templates/form-b-evaluation-gates.md`):** Mục B3 (Câu 2.3 — bản đồ dữ liệu và ví dụ drift), cùng bàn làm Mục B6 (Câu 2.5 — pre-mortem 4 lăng kính), Mục B7.4 (Câu 2.9 — cổng kinh doanh), và chủ trì phần kinh doanh ở Mục B8 (quyết định Gate 1 · v1)[cite: 2, 11].
  - **Phiếu C (`templates/form-c-incident.md` — Thẻ S6):** Mục C1 (đọc chỉ số kinh doanh/vận hành mốc `prepared`), Mục C5 (Câu 3.2 — specification cho thẻ S6), cùng bàn dựng Mục C6 (Câu 3.4 — fault tree trước khi sửa), Mục C7 (rà soát cổng kinh doanh vòng 2), và chủ trì Mục C12 (quyết định Gate 1 · v2 và 3 dòng bắt buộc)[cite: 2, 12].
- **File code / config phụ trách:** `config/acceptance_criteria.json`, `config/operating_gates.json` (mục `business`), tham gia rà soát `submission/submission.json` (mục `decision_v1`, `decision_v2`, `three_lines`)[cite: 2, 3, 7].

### Đóng góp cụ thể

- Xác định mục tiêu cấp hệ thống của trợ lý hoàn tiền LogiX-VN từ PRD v1.1 §3[cite: 2, 9]; thiết lập và thống nhất bộ ngưỡng chấp nhận (`pass_rate_min = 0.9`, `pass_k_min = 0.8`, các chỉ số an toàn = `0`, `escalation_rate_max = 0.35`, `cost_per_ticket_vnd_max = 8500`, `roi_min = 0.15`, `queue_stuck_max = 0`), điều kiện dừng và 4 quy tắc ra quyết định trong `config/acceptance_criteria.json` trước khi chạy đánh giá[cite: 2, 3].
- Xây dựng bản đồ dữ liệu từ `data/world.json` và phân tích kịch bản concept drift khi chuyển chính sách từ `REFUND-v3` sang `REFUND-v4` ngày `2026-12-01`[cite: 2, 14].
- Thiết lập các ngưỡng cổng kinh doanh trong `config/operating_gates.json` (`daily_refund_cap_vnd = 2000000`, `cost_budget_per_ticket_vnd = 8500`, giới hạn `pilot_scope` ở 2 kho đơn lẻ `HN`, `HCM` và loại trừ kho sỉ `HCM-B2B`, `roi_min = 0.15`) kèm lập luận từ `ops_limits` và `ops_facts`[cite: 2, 14].
- Phân tích sự cố thẻ S6 (quy nhầm lỗi kiện/hãng trên đơn nhiều kiện), viết specification kiểm soát tính đúng đắn giữa `parcel_id` và `carrier_id`, đối chiếu số liệu chi phí/ROI qua 3 mốc `base · prepared · after` để chốt quyết định v1, v2 và 3 dòng bắt buộc[cite: 2, 12].
- **Ghi nhận sử dụng AI:** Có sử dụng trợ lý AI để rà soát cấu trúc phiếu A/B/C, đối chiếu tính nhất quán logic giữa `stop_condition` và `decision_rule`, và biên tập câu chữ; toàn bộ ngưỡng số liệu, lập luận từ `data/world.json` và quyết định Gate 1 đều do nhóm tự tính toán, kiểm chứng trên report và chịu trách nhiệm[cite: 5].

### Bằng chứng

-- Commit: `97629a9` (ký tiêu chí), `f5302cf`, `3db5465`
- Mã lần chạy: base `R-base-before-20261119-202059-bde05c`, prepared `R-base-prepared-20261119-211733-0d6a5f`; thẻ S6 base `R-S6-before-20261119-214310-65e7cb`, prepared `R-S6-prepared-20261119-214310-65e7cb`, after `R-S6-after-20261119-214310-65e7cb`.
- **Dòng trong phiếu:** Phiếu A (mục A1, A3, A4, A5), Phiếu B (mục B3, B6, B7.4, B8 cột v1), Phiếu C (mục C1, C5 câu 3.2, C6, C7, C12 cột v2 và 3 dòng bắt buộc)[cite: 7, 10, 11, 12].

### Exit ticket

- **Một điều học được:** Việc ký cứng tiêu chí chấp nhận và chốt các ngưỡng kinh doanh/vận hành (trần hoàn tiền ngày, chi phí mỗi ticket, ROI, phạm vi kho) *trước* khi xem kết quả chạy giúp tránh thiên lệch điều chỉnh ngưỡng theo số đẹp, đồng thời cho thấy nhiều sự cố sau PoC bắt nguồn từ giả định dữ liệu/nghiệp vụ (như đơn nhiều kiện nhiều hãng) chứ không chỉ nằm ở prompt hay model[cite: 2, 3, 7].
- **Một điều còn chưa chắc:** Vì toàn bộ đánh giá đang dùng MockLLM và dữ liệu giả lập trong `world.json`, mức chi phí LLM thực tế theo độ dài hội thoại phát sinh và tần suất xuất hiện các ca ngoại lệ ngoài bộ test khi mở rộng sang nhiều kho hơn vẫn cần đo lại thực nghiệm trong giai đoạn pilot[cite: 7, 12, 14].
