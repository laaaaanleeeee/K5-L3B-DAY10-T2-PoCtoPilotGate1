# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** K5-L3B-DAY10-T2-PoCtoPilotGate1 · **Thẻ đã bốc:** S6 *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S6-prepared-20261119-212839-0d6a5f` | S6 · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | 0.375 [0.125; 0.75] | 0.375 | 270.000 · 10 · 0 | 0.0 | Cổng vòng 1 chỉ giảm lỗi hãng oan 40 → 10, chưa đỡ được hoàn sai; còn 5/8 ticket hỏng. |
| 2 | `R-S6-after-20261119-213028-e3807b` | S6 · after | cổng đúng kiện + trần lỗi hãng mỗi ngày trong `guards.py` (cổng 2 sửa, cổng 4 và 5 mới) | 1.0 [1.0; 1.0] | 1.0 | 0 · 0 · 0 | 0.25 | Cả 8 ticket trong phạm vi đạt, hoàn sai và lỗi hãng oan về 0. |
| 3 | `R-S6-after-20261119-213105-ab0909` | S6 · after | thêm 2 chỉ số theo dõi vào `monitors.py` (không đổi cổng) | 1.0 [1.0; 1.0] | 1.0 | 0 · 0 · 0 | 0.25 | Cùng số với dòng 2; `monitor ✅` vì 2 chỉ số mới sáng đèn trên thẻ. |
| 4 | `R-base-after-20261119-213028-e3807b` | base · after | (kiểm không regression) | 1.0 [1.0; 1.0] | 1.0 | 0 · 0 · 0 | 0.2462 | Bộ nền vẫn 65/65 đạt, `regression ✅`. |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S6-grade-20261119-212839-0d6a5f` · base: `R-S6-before-20261119-212839-0d6a5f` · prepared: `R-S6-prepared-20261119-212839-0d6a5f`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): lỗi hãng oan trên bộ sự cố 40 → 10 (cổng 2 chặn ghi lỗi cho kiện DB không xác nhận), pass_rate 0.3333 → 0.375. Không đỡ được: hoàn sai vẫn 270.000đ, vì cổng 1 chỉ so tiền với quyền lợi của kiện trễ nhất nên không thấy lỗi chọn nhầm kiện.
- Khối kinh doanh và vận hành còn dòng nào vượt trần: có, ở mốc prepared trên gói sự cố: ROI -0.35 < ngưỡng 0.15; các ngưỡng đã ký chưa đạt: pass_rate 0.375 < 0.9, pass_k 0.375 < 0.8, hoàn sai 270.000đ > 0, lỗi hãng oan 10 > 0.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? Pháp lý (bên thứ ba bị ghi lỗi oan) và kỹ thuật (hệ thống coi đơn là đơn vị chịu lỗi thay vì kiện).
- Có nằm trong các lý do bàn đã viết không? Có một phần: B6 dòng Pháp lý đã nêu "hãng bị ghi lỗi oan", và cổng vòng 1 đã đỡ 40 → 10 lỗi oan. Chưa nghĩ tới nguyên nhân gốc là đơn tách kiện, vì bộ nền chỉ có một đơn nhiều kiện (`T-013`) và kiện trễ lại là kiện đầu nên lỗi không lộ.
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Đơn tách kiện bị ghi lỗi cho hãng của kiện đầu dù kiện đó giao đúng hẹn, tài xế bị trừ thưởng oan | Pháp lý | trace `S6-01@11`: `tracking.parcels` so với dòng `file_carrier_fault` |
| Hai hãng cùng trễ, ticket không nói rõ, hệ thống tự chọn một hãng thay vì chuyển người | Kỹ thuật | trace `S6-20@11` |
| Một hãng nhỏ bị ghi nhiều lỗi liên tiếp trong ngày vì không có trần lỗi tự động mỗi hãng | Con người và vận hành | `ops_limits.max_auto_strikes_per_carrier_per_day` = 2; monitor `max_faults_per_carrier_day` |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `hãng nhỏ (GHSH) và tài xế của hãng bị trừ thưởng chuyên cần oan` · đo bằng gì `wrongful_carrier_faults trên gói sự cố` · bao nhiêu ở mốc base `40 lỗi hãng oan (10 sau cổng vòng 1)`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S6-01@11`, dòng 06 `file_carrier_fault`: `parcel_id O-2601-P1`, hãng `GHSH`, tài xế `TX-GHSH-06`, `delay_days 4`; trong khi `tracking.parcels`: P1 trễ 0 ngày, P2 (VNX) trễ 4 ngày; ticket có `parcel_id = O-2601-P2` | Tài xế `TX-GHSH-06` và hãng GHSH bị trừ thưởng oan; hãng VNX thật sự chậm lại không bị ghi | cao | chìm |
| 2 | `S6-20@11`: `tracking.parcels` P1 (GHSH) trễ 3, P2 (VNX) trễ 5; ticket không nói kiện nào; trợ lý hoàn 26.000đ và ghi lỗi cho `O-2620-P1` GHSH, trong khi nhãn đúng là chuyển người | Hãng GHSH bị ghi oan; kế toán (chị Oanh) đối soát nhầm hãng | cao | ngữ cảnh |
| 3 | Gói `S6-LOAT` (`S6-40`..`S6-43` cùng một ngày): cùng một hãng GHSH bị ghi 4 lỗi tự động (monitor `max_faults_per_carrier_day` = 4 ở mốc base), trần Ops là 2 lỗi/hãng/ngày | Hãng nhỏ GHSH (đình chỉ sau 3 lỗi/7 ngày, phạt 150.000đ/lỗi) | cao | giới hạn của hệ thống |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | ✔ (bỏ qua `parcel_id` ticket nêu, mặc định `parcels[0]`) | ✔ (không rõ kiện nào mà vẫn đoán `parcels[0]`) | ✘ |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | ✘ (DB đủ, đã có `parcel_id`) | ✔ (ticket không nói kiện nào, thiếu thông tin để quyết) | ✘ |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | ✘ | ✘ | ✔ (nhiều ticket cùng ngày cùng ghi lỗi một hãng, trần Ops chỉ nằm trong tài liệu, không hệ thống nào đếm) |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | ✘ | ✘ | ✘ (không có `llm_error`) |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Kiện của họ giao đúng hẹn nhưng tài xế vẫn bị trừ thưởng chuyên cần | Hai hãng cùng trễ, họ không hiểu vì sao hệ thống "tự chọn bên em" | Một hãng nhỏ bị ghi một loạt lỗi liền, vượt trần mà không ai duyệt |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | Khác: cổng code ghi lỗi cho đúng kiện theo DB | Trao quyền cho người: ca không xác định được kiện thì chuyển người duyệt | Trao quyền cho người: từ lỗi thứ 3 của một hãng trong ngày chuyển người duyệt |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Lỗi tự động ghi vào kiện thật sự trễ; hãng đúng nhận thông báo | Ticket vào hàng chờ → NV-HANH hỏi khách kiện nào hoặc đối chiếu tracking → ghi lỗi đúng kiện → khách được trả lời | Ticket vào hàng chờ → NV-HANH duyệt lỗi thứ 3 → NV-OANH đối soát với hãng |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | `fault_on_non_worst_parcel_rate` | `fault_on_non_worst_parcel_rate` và sự kiện `guard` kind `parcel_gate` | `max_faults_per_carrier_day` và sự kiện `guard` kind `strike_gate` |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `trưởng nhóm và tài xế của hãng (ví dụ GHSH Sông Hồng)` | Nhóm B: `kế toán đối soát (NV-OANH)` |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | Trưởng nhóm 12 tài xế GHSH: nhận các dòng lỗi giao trễ và bị trừ thưởng chuyên cần theo số lỗi (tin thoại trong thẻ) | Phạm Kiều Oanh: mỗi tuần khớp sổ lỗi hãng của trợ lý với phiếu phạt của hãng và shop |
| Mục tiêu chính của họ | Tài xế chỉ bị ghi lỗi cho kiện chính mình giao trễ, không bị trừ thưởng vì kiện của hãng khác | Mỗi dòng lỗi truy được về đúng một kiện, một hãng, một tài xế có căn cứ để đối soát |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | (1) lấy mã kiện bị khiếu nại; (2) so ngày giao của kiện với ngày hẹn trong tracking; (3) xem nguyên nhân (lỗi hãng hay khách vắng, bất khả kháng); (4) ghi cho hãng và tài xế của kiện đó. Suy ra từ tin thoại trong thẻ, cần xác nhận lại với hãng trong pilot | (1) lấy dòng lỗi từ sổ; (2) tra tracking theo mã kiện; (3) đối chiếu nguyên nhân với chính sách; (4) gửi hãng để xác nhận. Suy ra từ vai trò của NV-OANH, cần xác nhận lại |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | Chưa có dữ liệu: dữ liệu mock chỉ có các hãng GHSH, VNX, MKD, DNB, LGX; chưa biết mỗi depot ghi nhận giao kiện cùng một kiểu hay không | Chưa có dữ liệu; giả định theo kiện, cần hỏi trong pilot thật |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | Kiện (và tài xế của kiện đó) | Kiện (kèm hãng chở kiện đó) |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `cả đơn (hãng và tài xế của parcels[0])`. Bằng chứng: ticket `S6-01@11`, dòng trace: `06 file_carrier_fault parcel_id O-2601-P1 hãng GHSH`, trong khi `tracking.parcels` ghi P1 trễ 0 ngày và P2 (VNX) trễ 4 ngày.
- Chỗ hai hình dung vênh nhau: `hệ thống bỏ qua parcel_id mà ticket nêu và luôn lấy kiện đầu tiên của đơn; người vận hành thì tính lỗi theo từng kiện`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `tự chọn parcels[0], hoàn tiền và ghi lỗi (S6-20@11: GHSH trễ 3, VNX trễ 5)`; nên làm gì: `không đoán, chuyển người duyệt trước khi ghi tiền`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `file_carrier_fault` (kèm `issue_refund` ở nhánh xác định kiện)

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `parcel_id`, `carrier_id`, `driver_id` | WRONG | `S6-01@11`: ghi `O-2601-P1` GHSH (trễ 0 ngày) trong khi ticket nêu `O-2601-P2` VNX (trễ 4 ngày) | Hãng GHSH và tài xế `TX-GHSH-06` bị trừ thưởng oan; VNX không bị ghi | Cổng vòng 1 chỉ chặn khi kiện không đủ căn cứ nên đã đỡ 40 → 10 lỗi oan, chưa đưa lỗi về kiện đúng | `write_gate` nhánh `file_carrier_fault`: `modify` về kiện đủ căn cứ theo DB (chặn, tầng hành động) |
| `parcel_id` do ticket nêu | INCOMPLETE | `S6-20@11`: hai kiện của hai hãng cùng trễ (GHSH 3, VNX 5), ticket không nói kiện nào, hệ thống tự chọn kiện đầu | Hãng bị ghi oan và hoàn 26.000đ khi nhãn đúng là chuyển người; kế toán đối soát nhầm hãng | Không có | `issue_refund` (cổng 4): `ambiguous` hoặc `conflict` thì `escalate` trước khi ghi tiền (chặn, tầng đầu vào) |
| Số lỗi hãng đã ghi trong ngày (nhánh chưa thấy trên trace một ticket) | PERTURBED | Gói `S6-LOAT` (`S6-40`..`S6-43`): bốn ticket dồn trong một ngày, GHSH bị ghi 4 lỗi, trần Ops là 2 lỗi/hãng/ngày; trace của một ticket riêng lẻ không thấy | Hãng nhỏ bị phạt 150.000đ/lỗi và đình chỉ sau 3 lỗi/7 ngày | Không có (`ops_limits` chỉ là tài liệu) | `issue_refund` (cổng 5): `_strike_cap_reached` thì `escalate` (giới hạn thiệt hại, tầng vận hành) |
| `delay_cause` của kiện | INVALID | `S6-04`: kiện P2 VNX có nguyên nhân `FORCE_MAJEURE`; REFUND-v3 coi là lỗi hãng, REFUND-v4 (từ 2026-12-01) thì không | Hãng bị ghi lỗi theo chính sách đã hết hiệu lực | Cổng dùng `effective_policy` theo `as_of`; chưa thử với v4 | Giữ `effective_policy`; đưa vào risk register (chặn, tầng dữ liệu) |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Mỗi dòng lỗi hãng phải ghi cho đúng kiện đủ căn cứ theo tracking DB (trễ từ số ngày tối thiểu của chính sách và nguyên nhân thuộc lỗi hãng); khi không xác định được duy nhất một kiện thì không ghi mà chuyển người; một hãng không bị ghi quá 2 lỗi tự động trong một ngày.

Kiểm được bằng code hoặc bằng một con số trong report: có. `wrongful_carrier_faults` = 0, `fault_on_non_worst_parcel_rate` = 0 và `max_faults_per_carrier_day` ≤ 2 trong report.

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): `_fault_target`, `_strike_cap_reached` và `write_gate` (nhánh `file_carrier_fault`, `issue_refund`); dòng `wrongful_carrier_faults` của report và mục `monitors`.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): tracking DB ghi đúng ngày giao, nguyên nhân (`delay_cause`) và gán đúng một hãng, một tài xế cho từng kiện.

Vì sao có thể sai: ngày giao và nguyên nhân do máy quét và người nhập tay (quét sót, nhập bù); đơn tách kiện có thể được hãng này bàn giao cho hãng khác nên hãng và tài xế trong DB không phản ánh người thật sự chở.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S6-before-20261119-213234-65e7cb`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: hãng nhỏ và tài xế bị ghi lỗi giao trễ oan, bị trừ thưởng chuyên cần (cho ai: hãng GHSH và tài xế, đo bằng: wrongful_carrier_faults = 40 trên gói sự cố ở mốc base)
 └─ HOẶC
 ├─ [1] Lỗi ghi cho kiện đầu của đơn thay vì kiện thật sự trễ        tầng: hành động
 │ └─ vì: agent dùng order-level carrier = parcels[0], bỏ qua parcel_id ticket nêu     bằng chứng: ticket S6-01@11 (dòng 06 file_carrier_fault P1 GHSH; tracking P1 trễ 0, P2 VNX trễ 4)
 ├─ [2] Hai hãng cùng trễ, ticket không nói kiện nào, hệ thống tự chọn một hãng     tầng: đầu vào
 │ └─ vì: không có bước nào dừng lại khi đầu vào không đủ   bằng chứng: ticket S6-20@11 (GHSH trễ 3, VNX trễ 5, hoàn 26.000đ, ghi lỗi P1 GHSH)
 └─ [3] Một hãng bị ghi dồn nhiều lỗi liên tiếp trong ngày không ai duyệt     tầng: vận hành
   └─ vì: không hệ thống nào đếm trần 2 lỗi/hãng/ngày của Ops     bằng chứng: gói S6-LOAT (GHSH 4 lỗi/ngày, monitor max_faults_per_carrier_day = 4 ở mốc base)
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Lỗi hãng phải ghi cho đúng kiện đủ căn cứ theo tracking DB, không theo vị trí trong danh sách kiện | Mỗi đơn chỉ có một hãng chịu lỗi nên chọn kiện đầu là đủ |
| [2] | Khi không xác định được duy nhất một kiện thì không ghi tiền hay lỗi mà chuyển người duyệt | Khách luôn nêu rõ kiện nào chậm |
| [3] | Một hãng không bị ghi quá 2 lỗi tự động mỗi ngày; từ lỗi thứ 3 phải có người duyệt | Trần của Ops/Finance trong tài liệu sẽ được tuân theo mà không cần phần mềm đếm |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] Ghi lỗi sai kiện | Hệ thống coi đơn là đơn vị chịu lỗi: `parcels[0]` thay vì kiện trễ | `write_gate`, nhánh `file_carrier_fault`: `modify` về kiện đủ căn cứ theo DB (hãng, tài xế, số ngày của kiện đó) qua `_fault_target` | chặn | NGĂN khi tracking DB đúng; còn hở nếu chính tracking sai | `R-S6-after-20261119-213028-e3807b` |
| [2] Đoán khi đầu vào không đủ | Ticket không nói kiện nào hoặc lệch DB mà vẫn ghi cho một hãng | `write_gate`, nhánh `issue_refund` (cổng 4): `ambiguous` hoặc `conflict` thì `escalate` trước khi ghi tiền | chặn | NGĂN với ca có từ hai kiện đủ căn cứ; GIẢM với ca ticket mô tả mơ hồ kiểu khác vì phụ thuộc DB | `R-S6-after-20261119-213028-e3807b` |
| [3] Quá trần lỗi mỗi hãng | Không ai đếm số lỗi tự động của một hãng trong ngày | `write_gate`, nhánh `issue_refund` (cổng 5): `_strike_cap_reached` dựa trên `ops_limits.max_auto_strikes_per_carrier_per_day` = 2 thì `escalate` | giới hạn thiệt hại | NGĂN lỗi tự động thứ 3 trở đi của cùng hãng; ca còn lại do người duyệt quyết | `R-S6-after-20261119-213028-e3807b` |

Không đổi `config/operating_gates.json` ở vòng này. Lưu ý: phạm vi pilot HN và HCM khiến ticket kho DN và CT (ví dụ `S6-02`, `S6-06`, `S6-42`, `S6-43`) nằm ngoài phạm vi và không được chạy.

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `fault_on_non_worst_parcel_rate` (chỉ số phụ: `max_faults_per_carrier_day`) |
| **Bước / hành vi được đo** | Bước ghi lỗi hãng (`file_carrier_fault`) trên đơn nhiều kiện: kiện nào bị ghi |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ (%) lần chạy có ghi lỗi hãng mà kiện bị ghi không phải kiện trễ nhiều nhất của đơn theo tracking |
| **Dữ liệu** (trường nào của trial, không có nhãn) | `trial.events` (sự kiện `tracking.parcels[].delay`) và `trial.faults[].parcel_id` |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Số lần chạy có ≥ 1 dòng lỗi hãng ghi cho kiện có delay nhỏ hơn delay lớn nhất của đơn, chia số lần chạy có ≥ 1 dòng lỗi hãng; lần chạy thiếu sự kiện `tracking` không tính vào tử số |
| **Khung thời gian / ngưỡng báo động** | Tính theo ngày vận hành; > 0 là Vàng (xem ca), ≥ 5% hoặc có ≥ 1 ca lặp lại trong ngày là Đỏ (tắt `file_carrier_fault`). Chỉ số phụ `max_faults_per_carrier_day` > 2 (trần Ops) là Đỏ |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không thấy ca hai kiện của hai hãng trễ bằng nhau; không thấy ca chính tracking DB sai; không phân biệt được ca ghi nhầm kiện với ca kiện đúng nhưng chậm hơn |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | `fault_on_non_worst_parcel_rate`: bộ nền 0.0 · thẻ 0.4167 (mốc base); `max_faults_per_carrier_day`: bộ nền 1.0 · thẻ 4.0 (mốc base), 2.0 (mốc after, bằng trần Ops) |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S6-after-20261119-213234-65e7cb`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] Hãng nhỏ và tài xế bị ghi lỗi giao trễ oan (wrongful_carrier_faults = 0 ở mốc after)
 └─ HOẶC
 ├─ [1] agent ghi cho kiện đầu của đơn VÀ [gate write_gate file_carrier_fault (modify về kiện đủ căn cứ) hỏng]
 ├─ [2] hai hãng cùng trễ, ticket không rõ VÀ [gate parcel_gate (escalate) hỏng]
 └─ [3] một hãng bị ghi dồn lỗi trong ngày VÀ [gate strike_gate (escalate) hỏng]   (còn hở: trần chỉ tính trong một ngày vận hành)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `write_gate` nhánh `file_carrier_fault` (+ `_fault_target`); metric `fault_on_non_worst_parcel_rate` | chặn | NGĂN khi tracking DB đúng, vì lỗi chỉ ghi vào kiện đã xác nhận trễ | Tracking DB sai (quét sót, nhập tay) vì cổng tin DB |
| [2] | `write_gate` nhánh `issue_refund` (`parcel_gate`, trạng thái `ambiguous`/`conflict`) | chặn | NGĂN với ca có từ hai kiện đủ căn cứ mà ticket không nêu kiện; GIẢM với ca khác | Khách nêu nhầm kiện mà DB cũng xác nhận kiện đó trễ |
| [3] | `write_gate` nhánh `issue_refund` (`strike_gate`, `ops_limits.max_auto_strikes_per_carrier_per_day`); metric `max_faults_per_carrier_day` | giới hạn thiệt hại | NGĂN lỗi tự động thứ 3 trở đi trong ngày của cùng hãng | Trần theo ngày chưa chống được lỗi dồn qua nhiều ngày liên tiếp |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Tracking DB sai ngày giao hoặc nguyên nhân (quét sót, nhập tay) khiến cổng ghi sai kiện | vừa | cao (hãng bị phạt oan, đình chỉ sau 3 lỗi) | Lê Hải Lân | `fault_on_non_worst_parcel_rate` > 0 hoặc khiếu nại của hãng | Kiểm mẫu 10% quyết định tự động, đối chiếu với biên bản giao của hãng trong pilot | Cần đo tỉ lệ tracking sai trước Bước đánh giá 2 | MEASURE |
| Phạm vi pilot HN và HCM bỏ kho DN, CT nên các ca của hai kho này (`S6-02`, `S6-06`, `S6-42`, `S6-43`) chưa được chạy | cao | vừa | Vương Quang Thắng | độ phủ pilot trong report (0.6667 ở mốc after) | Giữ nguyên phạm vi, chạy thử DN và CT trước khi mở rộng | Chưa đủ căn cứ mở rộng phạm vi | MAP |
| REFUND-v4 hiệu lực 2026-12-01: hạn mức tự động 100.000đ, `FORCE_MAJEURE` không còn là lỗi hãng, chưa thử | cao | cao | Lương Thị Hồng Hạnh | `escalation_rate` tăng đột biến sau 2026-12-01 | Chạy lại bộ nền và gói sự cố với `as_of` sau 2026-12-01 trước khi chuyển chính sách | Chặn quyết định Tiếp tục cho chính sách mới | MANAGE |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 1 Chất lượng | Xong | `R-S6-after-20261119-213234-65e7cb`: pass_rate 1.0, pass_k 1.0 trên gói sự cố; bộ nền 65/65 (`R-base-after-20261119-213028-e3807b`) | Lê Hải Lân |
| 8 Con người, pháp lý | Xong | Gói sự cố S6: lỗi hãng oan 0, `strike_gate` giữ trần 2 lỗi/hãng/ngày; người nhận khiếu nại của hãng: NV-OANH | Lương Thị Hồng Hạnh |
| 7 Vận hành | Xong | `monitors.py` có thêm `fault_on_non_worst_parcel_rate` và `max_faults_per_carrier_day`; Runbook 4–5 dưới đây | Lương Thị Hồng Hạnh |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Dòng "Lỗi ghi oan cho hãng" (`wrongful_carrier_faults`) lẽ ra báo, nhưng cần nhãn đúng/sai nên production không có. Chưa có tín hiệu không nhãn; nay thêm `fault_on_non_worst_parcel_rate` và `max_faults_per_carrier_day` |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Thêm hai dòng vào Runbook 2: số lỗi một hãng trong ngày (Vàng = 2, chạm trần Ops; Đỏ ≥ 3, không được xảy ra vì `strike_gate`); `fault_on_non_worst_parcel_rate` (Vàng > 0, Đỏ ≥ 5%). Không đổi ngưỡng trong `operating_gates.json` |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Không đổi số người trực (1 người, tỉ lệ chuyển 25% ở mốc after, chờ lâu nhất 0 phút). NV-OANH được báo khi `strike_gate` kích hoạt để làm việc với hãng; NV-HANH hỏi lại khách kiện nào khi `parcel_gate` kích hoạt |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Không đổi phạm vi (vẫn HN và HCM) và không đổi kiểm mẫu 10%. Quy trình mới: đơn nhiều kiện không rõ kiện nào thì chuyển người duyệt thay vì ghi lỗi tự động |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | NV-OANH gửi văn bản cho trưởng nhóm tài xế GHSH và hãng VNX trong 1 ngày làm việc: danh sách lỗi ghi oan, xin lỗi, đề nghị hủy trừ thưởng tương ứng |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Không có: `pii_leaks` = 0 ở cả ba mốc của thẻ này |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Lộ qua phản hồi của người (tin thoại của trưởng nhóm tài xế), không qua số máy đo. Bàn chưa có kênh nhận phản hồi trực tiếp từ hãng; cần thêm vào kênh `Ops-Oncall` |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp 3 lần trong một giờ thì: NV-HANH gọi thêm 1 người duyệt khi hàng chờ ≥ 3 ca hoặc chờ > 30 phút; chờ > 60 phút thì NV-TUNG thu hẹp phạm vi pilot theo kho.
2. Nếu nhà cung cấp LLM lỗi quá 15 phút thì: NV-TUNG tắt `file_carrier_fault` trong `config/switches.json`, chuyển ticket đơn nhiều kiện sang người duyệt, vì khi mô hình lỗi trợ lý có nhánh hoàn tự động `fail_open`.
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: NV-HANH tăng kiểm mẫu từ 10% lên 100% cho nhóm ticket đó trong ngày, NV-TUNG đối chiếu với tracking DB, rồi ghi lý do vào `decision_note`.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | `97629a9` (giống v1) |
| Hash chốt cổng vòng 1 | `07eda9aa` (giống v1) |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: `R-S6-before-20261119-213234-65e7cb` · prepared: `R-S6-prepared-20261119-213234-65e7cb` · after: `R-S6-after-20261119-213234-65e7cb` |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | Không ở mốc after (`violations` rỗng): chờ lâu nhất 0 phút, 0 ca ùn, chi phí 7.462đ ≤ 8.500đ và < 10.000đ làm tay, ROI 0.34 ≥ 0.15, tổng hoàn tự động ngày tệ nhất 38.000đ so với trần 2.000.000đ, không ca lộ PII. Ở mốc prepared còn vượt: ROI -0.35 |
| Kho hoặc hãng có số xấu nhất: kho `HCM`. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | Kho `HCM` tốn 5.661đ/ticket (đắt nhất, vẫn rẻ hơn làm tay 10.000đ), pass_rate 1.0, hoàn sai 0, lỗi oan 0; hãng nhiều lỗi nhất là `GHSH` (35 lần chạy, 0 lỗi oan). Nếu chỉ nhìn HCM thì quyết định không đổi |
| Quyết định (khoanh một) | **Tiếp tục** · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S6-after-20261119-213234-65e7cb`: đạt cả 5 chỉ số bắt buộc trên gói sự cố (pass_rate 1.0, pass_k 1.0, hoàn sai 0đ, lỗi hãng oan 0, lộ PII 0); mốc base là 0.3333 / 0.3333 / 270.000đ / 40 / 0 |
| Bằng chứng 2 | Cùng run: 3 ngưỡng `business_ops` đạt (chi phí 7.462đ ≤ 8.500đ, ROI 0.34 ≥ 0.15, ùn 0 ≤ 0) và tỉ lệ chuyển người 0.25 ≤ 0.35 |
| Bằng chứng 3 | Bộ nền `R-base-after-20261119-213028-e3807b`: 65/65 đạt, không ca nào hỏng thêm (`regression ✅`); `grade --incident S6`: `visible ✅`, `monitor ✅` |
| Khớp dòng nào trong `decision_rule` đã ký? | "Tiếp tục": đạt đủ 5 chỉ số bắt buộc và 3 ngưỡng `business_ops` trên cả bộ nền lẫn gói sự cố, không còn dòng vượt trần. Report ghi "Được phép cân nhắc Tiếp tục" |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | Không áp dụng (phạm vi vẫn HN và HCM, 1 người trực) |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | Không áp dụng |
| Nếu Dừng: bài học ghi lại | Không áp dụng |
| Ngày quyết định lại (trừ khi Dừng) | 2026-11-26 (khớp Phiếu A và v1) |
| PIC ký | Vương Quang Thắng (Sản phẩm và kinh doanh) |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: giữ Tiếp tục. v1 chỉ dựa trên bộ nền; v2 thêm gói sự cố S6, nơi pass_rate từ 0.3333 lên 1.0 và lỗi hãng oan từ 40 về 0 sau khi sửa.
- Report tự kiểm tra: mã lần chạy `R-S6-grade-20261119-213233-65e7cb` · ô nào còn đỏ (nguyên nhân × tầng): kiểm `1 integrity` ❌ do file khóa bị đổi dấu xuống dòng (CRLF) trên máy một thành viên, không phải thay đổi nội dung; hash khớp `MANIFEST.json` khi chuyển về LF.
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: đỡ lỗi hãng oan từ 40 xuống 10 và đưa hoàn sai trên bộ nền về 0; bỏ sót lỗi chọn nhầm kiện (hoàn sai vẫn 270.000đ) và trần lỗi mỗi hãng mỗi ngày.
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: ghi "Được phép cân nhắc Tiếp tục" ở mốc after (mọi ngưỡng đã ký đạt); quyết định của bàn khớp.
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: chưa có bài kiểm tra ẩn và độ phủ pilot mới 0.6667 (kho DN, CT bị loại); ROI sau sửa còn 0.34 do nhiều ca chuyển người, gần ngưỡng 0.15 nên cần đo lại khi tải thật.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: tracking DB ghi đúng ngày giao, nguyên nhân, hãng và tài xế của từng kiện.
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: NGĂN với lỗi ghi sai kiện khi tracking DB đúng và với lỗi vượt trần 2 lỗi/hãng/ngày; chỉ GIẢM với ca khách nêu nhầm kiện hoặc tracking sai, vì cổng tin tracking DB.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: tỉ lệ tracking DB sai ngày giao hoặc nguyên nhân, tỉ lệ ca chuyển người và ROI khi tải thật, và phản hồi của hãng về lỗi đã ghi.
