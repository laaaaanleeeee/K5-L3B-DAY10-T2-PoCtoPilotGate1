# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):
- Lớp: `L3A` / `L3B`
- Repo của bàn: `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |Lương Thị Hồng Hạnh|2A202603748|Vận hành và pháp lý|             |
|   2 |           |      |     |             |
|   3 |           |      |     |             |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## LuongThiHongHanh-2A202603748

### Phần việc phụ trách

Vai: Vận hành và pháp lý.

- Phiếu B câu 2.4 (B4 HAZOP vòng 1 và B5 checklist 9 nhóm, đúng vai con người/pháp lý).
- Phiếu B câu 2.5 (B6 lăng kính con người-vận hành và pháp lý).
- Phiếu B câu 2.10 (B7.5 cổng vận hành/pháp lý, runbook 1–3 và B7.6 giờ cao điểm).
- Phiếu C câu 3.1–3.7: phần riêng theo thẻ, C4 HAZOP của thẻ, C5 giả định môi trường, C7 sửa vận hành/pháp lý, C9–C11 fault tree sau khi sửa, risk register, checklist và runbook 4–5.
- File chính: `config/operating_gates.json`; phối hợp ở `lab10/guards.py`, `lab10/monitors.py` và `submission/submission.json`.

### Đóng góp cụ thể

- Xác lập PIC vận hành là `NV-TUNG` (Lê Thanh Tùng) và người duyệt đứng tên là `NV-HANH` (Trần Thị Hạnh).
- Đặt năng lực duyệt: 1 người trực, 6 ca/giờ, ngưỡng chờ tối đa 60 phút theo SLA; mở kiểm lại quyết định 10%.
- Kết nối hình thức ghi chú quyết định (`decision_note=true`) để nhân viên duyệt nắm nhanh lý do trước khi kiểm lại.
- Chặn việc gửi cho hãng các trường PII `name`, `phone`, `street`; yêu cầu ghi rõ nguyên nhân hãng trước khi ghi lỗi hãng.
- Thêm điều kiện dừng: lỗi ghi oan, lộ PII, chờ vượt SLA hoặc vượt ngân sách hoàn tự động trong ngày.
- Cập nhật `members` trong `submission/submission.json` để khớp với bảng thành viên.

### Bằng chứng

- Baseline public: `python3 -m unittest discover -s tests` — Ran 13 tests, OK.
- Dữ liệu vận hành: `data/world.json` mục `ops_limits` và `ops_facts`.
- Chính sách vận hành/pháp lý: `config/operating_gates.json`.
- Dòng kiểm tra và mã lần chạy sẽ được ghi tại đây sau khi chạy eval/base/prepared/incident theo đúng CP3–CP4.
- Committed branch/working changes: branch `feature/van_hanh_phap_ly`.

### Exit ticket

Một điều học được: cổng con người và pháp lý cần con số, tên người, kênh báo và điều kiện dừng rõ ràng thì mới có thể vận hành được ở ca thực.

Một điều còn chưa chắc: cần thẻ sự cố S1–S8 và dữ liệu report vòng 2 để chốt con số ngưỡng dừng, kiểm mẫu sau thẻ và nội dung thông báo bên thứ ba.
