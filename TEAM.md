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
|   1 | Lê Hải Lân | 2A202603915 | Kỹ sư cổng  |    x         |
|   2 | Lương Thị Hồng Hạnh |2A202603748| Vận hành và pháp lý |             |
|   3 | Vương Quang Thắng  | 2A202603855  | Sản phẩm và kinh doanh  |             |

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

- CP1: bổ sung thông tin cá nhân và vai trò vào bảng thành viên.
- CP2: Phiếu A câu 1.2 (mục tiêu của chị Oanh và chị Hạnh) và câu 1.4 (telemetry production).

### Đóng góp cụ thể

- Xác định mục tiêu của kế toán đối soát và trưởng ca theo khả năng truy vết, tính chính xác và SLA.
- Đề xuất telemetry production không cần nhãn tức thời: theo dõi hoàn sai, lỗi ghi oan cho hãng, PII leak và ticket chờ quá SLA; nêu nguồn dữ liệu, cách tính, cửa sổ đo và điểm mù.

### Bằng chứng

- `TEAM.md`: thông tin thành viên.
- `templates/form-a-criteria.md` và `submission/docs/form-a-criteria.md`: Phiếu A mục A1 câu 1.2 và A2 câu 1.4.
- Chưa có mã eval/run; việc đo runtime thuộc các checkpoint tiếp theo.

### Exit ticket

Một điều học được: telemetry production có thể phát hiện rủi ro bằng tín hiệu vận hành và sự kiện audit dù chưa có nhãn đúng/sai tức thời.

Một điều còn chưa chắc: khách hàng hoặc bên thứ ba có thể chưa báo thiệt hại; cần thêm cách xác nhận độc lập ngoài trace nội bộ.
