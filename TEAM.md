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

*(Thắng tự viết mục này theo mẫu ở trên: phần việc, đóng góp cụ thể, bằng chứng, exit ticket.)*
