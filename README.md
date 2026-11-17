# English Quest 8 — Bản MVP

Ứng dụng web học tiếng Anh cho học sinh lớp 8 Việt Nam, gồm 2 unit: **Unit 1 — Leisure Time** và **Unit 2 — Life in the Countryside** (chuyển unit bằng 2 nút ở đầu trang; tiến độ, điểm chặng và lịch ôn từ vựng được lưu riêng cho từng unit, điểm XP là chung).
Học cùng giáo viên — mặc định là **Ms. Mia** (giọng Anh–Mỹ, theo quyết định của chủ dự án ngày 30/10/2026), đủ 4 kỹ năng nghe – nói – đọc – viết.

Unit 2 có nội dung tự sáng tác mới: từ vựng đời sống nông thôn (countryside, paddy field, harvest, buffalo…), hội thoại Anna thăm làng của Phong với cảnh làng quê, bài đọc "A Weekend in Grandma's Village", và trọng tâm ngữ pháp **so sánh hơn của trạng từ** (more slowly, more happily, earlier, harder…) được lồng vào cả phần nói và phần viết (máy nhận xét có kiểm tra việc dùng cấu trúc này).

## Cách chạy (chọn 1 trong 2)

**Cách 1 — mở trực tiếp:** mở file `index.html` bằng trình duyệt Chrome hoặc Edge.
(Giọng đọc hoạt động; tính năng ghi âm nhận giọng và cài PWA cần cách 2 hoặc đưa lên web HTTPS.)

**Cách 2 — chạy bằng Python (khuyên dùng):**
```bash
python3 server.py
```
Rồi mở trình duyệt tại `http://localhost:8000`.

## Tính năng của bản MVP
- Bản đồ hành trình 6 chặng, điểm XP, huy hiệu, hiệu ứng ăn mừng.
- **Chọn giáo viên như người thật:** 3 chân dung phong cách ảnh thực của nhân vật hư cấu do dự án tạo riêng — Ms. Mia (nữ, Anh–Mỹ), Mr. Ethan (nam, Anh–Mỹ), Ms. Sofia (nữ, Anh–Anh). Chọn ai thì người đó đọc mẫu và nhận xét, với giọng nam/nữ và ngữ điệu tương ứng (Web Speech API của trình duyệt, miễn phí). Khi đang nói, ảnh chuyển động nhẹ kèm sóng âm.
- **Tải ảnh giáo viên của riêng mình:** tải ảnh chân dung của chính người dùng hoặc người đã đồng ý cho dùng ảnh; ảnh được thu nhỏ và lưu ngay trên máy đang học (localStorage), không gửi lên máy chủ. Chỉ dùng ảnh của người đã đồng ý — không dùng ảnh người nổi tiếng/người khác khi chưa được phép.
- Nghe: hội thoại có phụ đề karaoke tô sáng từng từ, 2 giọng nhân vật, chỉnh tốc độ; câu hỏi trắc nghiệm chấm ngay.
- Từ vựng: 10 thẻ từ có phiên âm, nghĩa tiếng Việt, câu ví dụ, nút nghe.
- Nói: nghe mẫu → nói theo (shadowing) → trình duyệt nghe và chấm % độ khớp, góp ý từ còn thiếu (Chrome hỗ trợ nhận giọng tiếng Anh, cần micro và internet).
- Đọc: đoạn văn gốc tự sáng tác + trắc nghiệm.
- Viết: viết đoạn ngắn, máy nhận xét theo tiêu chí (từ nối, từ vựng của bài, số câu, chính tả cơ bản) và cho điểm khích lệ.
- Ôn tập: lịch ôn rút gọn theo nguyên lý lặp lại ngắt quãng (1–3–7 ngày), tiến độ lưu trên máy người học (localStorage), không cần tài khoản.

## Giới hạn đã biết của bản MVP (nói rõ, không giấu)
- Giọng đọc là giọng có sẵn của trình duyệt/thiết bị nên chất lượng tùy máy; giai đoạn sau sẽ thay bằng file giọng tạo sẵn bằng Kokoro/Gemini ở phía soạn bài.
- Giáo viên ảnh thực dùng hiệu ứng chuyển động nhẹ + sóng âm khi nói, chưa phải khẩu hình khớp từng âm vị; khẩu hình thật cho các bài học dạng video sẽ render bằng SadTalker/MuseTalk ở giai đoạn 2 (chính các ảnh chân dung trong thư mục `teachers/` và ảnh người dùng tải lên — khi có sự đồng ý — sẽ là đầu vào cho bước render đó).
- Chấm phát âm ở mức so khớp câu nói (đúng từ, đủ từ), chưa phân tích từng âm vị như faster-whisper ở giai đoạn sau.
- Nhận diện giọng nói dùng dịch vụ của trình duyệt Chrome; không có dữ liệu giọng nào được app lưu lại.

## Giấy phép & phát hành
- Mã nguồn và nội dung bài học của English Quest 8: © 2026 Bảo Anh. Xem file `LICENSE.md`.
- Thành phần bên thứ ba: xem `THIRD-PARTY-LICENSES.md` — toàn bộ đều là thư viện chuẩn của trình duyệt/Python hoặc giấy phép cho phép thương mại.
- Thiết kế “sẵn sàng thương mại”: không nhúng khóa API, phía học sinh không gọi Gemini API, nội dung tự sáng tác.
