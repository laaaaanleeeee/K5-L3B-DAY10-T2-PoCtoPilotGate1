# Checklist theo checkpoint · LAB 10

Mốc quan trọng nhất: **ký tiêu chí ở phút 60–65, trước khi chạy `eval` lần nào.**

## CP1 · Cài đặt và chia vai (phút 0–15)

- [ ] Fork repo, đặt tên `K5-L3B-DAY10-<TenNhom>-PoCtoPilotGate1`, mời thành viên quyền Write — **L**
- [ ] Clone, đặt git config, chạy `python3 -m unittest discover -s tests` thấy `Ran 13 tests … OK`, kiểm `git remote -v` — **L**
- [ ] Điền bảng thành viên `TEAM.md` (tên nhóm, lớp, họ tên, MSSV, vai) — **L** điền, **H** bổ sung thông tin của mình
- [ ] Chốt eval card và PRD v1.1 làm bản chung (sửa run ID `4bfb`/`497a`, tên `pass_5`/`pass_hat_5`) — **Cả bàn**, **T** dẫn

## CP2 · Viết và ký tiêu chí (phút 15–65, Phiếu A)

- [ ] Câu 1.1: mục tiêu cấp hệ thống (A1) — **T**
- [ ] Câu 1.2: mục tiêu của chị Oanh và chị Hạnh (A1) — **H**
- [ ] Câu 1.3: offline metric cho một bước của agent (A2) — **L**
- [ ] Câu 1.4: telemetry production (A2) — **H**
- [ ] Câu 1.5: đọc khoảng tin cậy (A3) — **Cả bàn**
- [ ] Câu 1.6: viết Bản tiêu chí, điền `config/acceptance_criteria.json` (A4) — **T**
- [ ] Soát lần cuối, rồi chạy `python3 -m lab10.criteria sign`, commit và push (A5) — **T** soát, **L** chạy lệnh

## CP3 · Đo, rủi ro, cổng vòng 1, quyết định v1 (phút 65–115, Phiếu B)

- [ ] Câu 2.1: chạy base, `gate`, ghi mã run (B0, B1) — **L**
- [ ] Câu 2.2: trace `T-002@55`, bảng soát lỗi (B2) — **L**
- [ ] Câu 2.3: bản đồ dữ liệu, ví dụ drift (B3) — **T**
- [ ] Câu 2.4: HAZOP vòng 1 và checklist 9 nhóm có PIC (B4, B5) — **H**
- [ ] Câu 2.5: pre-mortem bốn lăng kính (B6) — **Cả bàn** (L kỹ thuật, T kinh doanh, H con người và pháp lý)
- [ ] Câu 2.6: code 2–3 cổng trong `lab10/guards.py` (B7.1) — **L**
- [ ] Câu 2.7: 2 bước tránh rò rỉ dữ liệu (B7.2) — **L**
- [ ] Câu 2.8: behavioral test và 2 ticket hiểm (B7.3) — **L** cùng **H**
- [ ] Câu 2.9: điền `business` trong `config/operating_gates.json` (B7.4) — **T**
- [ ] Câu 2.10: điền `operations`, `legal`, runbook 1–3, giờ cao điểm (B7.5, B7.6) — **H**
- [ ] Chạy `checkpoint`, `eval --stage prepared`, `gate` — **L**
- [ ] Điền cột v1 ở B8, commit và push — **T** điền, **Cả bàn** chốt

## CP4 · Sự cố (phút 125–185, Phiếu C)

- [ ] Nhận thẻ (3 lệnh git), chạy `grade --incident Sx` trước khi sửa, ghi `Thẻ đã bốc` (C0, C1) — **L** chạy, **Cả bàn** đọc kết quả
- [ ] Câu 3.1: dò ≥ 2 ticket hỏng, bảng soát lỗi (C2) — **L**
- [ ] Phần riêng theo thẻ (C3) và HAZOP của thẻ (C4) — **H**
- [ ] Câu 3.2: specification (C5) — **T**
- [ ] Câu 3.3: giả định môi trường (C5) — **H**
- [ ] Câu 3.4: fault tree trước khi sửa (C6) — **Cả bàn**
- [ ] Câu 3.5: sửa code trong `guards.py` (C7) — **L**
- [ ] Câu 3.5: sửa `business` (phạm vi, trần, ngân sách) (C7) — **T**
- [ ] Câu 3.5: sửa `operations` và `legal` (người trực, kiểm mẫu, pháp lý) (C7) — **H**
- [ ] Câu 3.6: thêm chỉ số trong `lab10/monitors.py` (C8) — **L**
- [ ] Câu 3.7: fault tree sau, risk register, checklist, runbook 4–5 (C9–C11) — **H**
- [ ] Chạy `eval` cho thẻ và base, `grade`; cần `monitor ✅` và `regression ✅` — **L**

## CP5 · Quyết định v2, demo, nộp (phút 185–240)

- [ ] Quyết định v2 và 3 dòng bắt buộc (C12) — **T** viết, **Cả bàn** chốt
- [ ] Điền `submission/submission.json` — **H**
- [ ] Chạy `python3 -m lab10.check_submission --collect` tới khi in `ĐỦ THÀNH PHẦN` — **H** chạy, **L** hỗ trợ khi report lỗi
- [ ] Demo ba cột base/prepared/after, trình bày phần sửa — **L** (kỹ thuật), **T** (quyết định và con số)
- [ ] Phản biện bàn kia bằng ticket hiểm — **L**
- [ ] Sau demo: trả các con số đã đổi thử về bản v2, chạy lại lệnh 6 và 7 — **H**
- [ ] Đẩy bài, gửi link repo — **L**
- [ ] Viết mục cá nhân và exit ticket trong `TEAM.md`, nộp link repo trên LMS — **Mỗi người tự làm**

## Luật cần nhớ

- Không sửa tiêu chí sau khi ký; không sửa `guards_round1.py` và `operating_gates.round1.json`.
- Không xử lý riêng theo mã ticket, vì có bộ test ẩn.
- Không làm hỏng ca đang đúng; không chặn hết hay thu hẹp phạm vi về 0.
- Chọn "Tiếp tục" khi report còn vượt trần là quyết định không đạt.
