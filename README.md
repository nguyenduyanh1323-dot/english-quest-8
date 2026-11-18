# English Quest 8 — Bản hoàn thiện (12 Unit)

Ứng dụng web học tiếng Anh cho học sinh lớp 8 Việt Nam, đủ **12 Unit** bám theo chủ đề chương trình lớp 8 (Global Success), toàn bộ nội dung **tự sáng tác** (không sao chép sách giáo khoa):

| Unit | Chủ đề | Trọng tâm ngữ pháp |
|---|---|---|
| 1 | Leisure Time | Động từ chỉ sở thích + V-ing / to-V |
| 2 | Life in the Countryside | So sánh hơn của trạng từ |
| 3 | Teenagers | Câu đơn & câu ghép (and, but, so) |
| 4 | Ethnic Groups of Viet Nam | Câu hỏi Wh- / Yes-No, danh từ đếm được |
| 5 | Our Customs and Traditions | Mạo từ a, an, the |
| 6 | Lifestyles | Tương lai đơn & câu điều kiện loại 1 |
| 7 | Environmental Protection | Mệnh đề thời gian (when, while, before…) |
| 8 | Shopping | Trạng từ tần suất, hiện tại đơn chỉ tương lai |
| 9 | Natural Disasters | Quá khứ tiếp diễn |
| 10 | Communication in the Future | Đại từ sở hữu (mine, yours, theirs…) |
| 11 | Science and Technology | Câu tường thuật (said that…) |
| 12 | Life on Other Planets | may/might & câu hỏi tường thuật |

Mỗi Unit là một hành trình 6 chặng đủ 4 kỹ năng: **Nghe** (hội thoại karaoke + **video luyện nghe dựng sẵn** trong thư mục `videos/`) → **Từ vựng** (10 thẻ có phiên âm/nghĩa/ví dụ) → **Nói** (shadowing + nhận diện giọng nói, chấm % khớp) → **Đọc** (đoạn văn gốc + trắc nghiệm) → **Viết** (máy nhận xét, có kiểm tra cấu trúc ngữ pháp trọng tâm của Unit) → **Ôn tập** (lịch ôn ngắt quãng 1–3–7 ngày). Tiến độ và lịch ôn lưu riêng từng Unit, điểm XP cộng chung.

Giáo viên mặc định là **Ms. Mia** (nữ, giọng Anh–Mỹ — theo quyết định của chủ dự án ngày 30/10/2026); học sinh vẫn chọn được Mr. Ethan, Ms. Sofia hoặc tải ảnh giáo viên của riêng mình (ảnh chỉ lưu trên máy người học).

## Cài đặt app vào điện thoại / máy tính

Khi mở app bằng link HTTPS (ví dụ GitHub Pages) hoặc localhost, bấm nút **"📲 Cài đặt app vào điện thoại / máy tính"** ở đầu trang để cài app vào màn hình chính như một ứng dụng thật (Android/Windows: hiện hộp thoại cài đặt; iPhone/iPad: app sẽ hiện hướng dẫn Thêm vào Màn hình chính). Đã cài rồi thì mở app từ biểu tượng ngoài màn hình chính, học được cả khi mất mạng.

## Cách chạy (chọn 1 trong 2)

**Cách 1 — mở trực tiếp:** mở file `index.html` bằng trình duyệt Chrome hoặc Edge.
(Giọng đọc hoạt động; tính năng ghi âm nhận giọng và cài PWA cần cách 2 hoặc đưa lên web HTTPS.)

**Cách 2 — chạy bằng Python (khuyên dùng):**
```bash
python3 server.py
```
Rồi mở trình duyệt tại `http://localhost:8000`.

## Tính năng chính
- **Toàn khóa học 12 Unit:** thẻ tổng quan đầu trang cho thấy % hoàn thành từng Unit, bấm để nhảy tới học.
- **Bảng theo dõi cho giáo viên & phụ huynh:** tổng XP, số Unit đã hoàn thành, tổng số từ đã thuộc, chi tiết từng Unit; có nút **xuất báo cáo tiến độ (JSON)** và **xóa toàn bộ tiến độ**. Hoàn thành đủ 12 Unit sẽ hiện lời chúc mừng tốt nghiệp khóa học trong bảng này.
- **Video luyện nghe dựng sẵn (mới):** mỗi Unit có 1 video MP4 ở mục Nghe — giọng đọc chuẩn Anh–Mỹ dựng bằng Piper TTS ở phía soạn bài (giọng nữ Amy, giọng nam Ryan), phụ đề theo từng câu thoại, ảnh Ms. Mia minh họa. Xem được cả khi không có mạng và không phụ thuộc giọng của thiết bị.
- **Chọn giáo viên như người thật:** 3 chân dung phong cách ảnh thực của nhân vật hư cấu do dự án tạo riêng — Ms. Mia (nữ, Anh–Mỹ), Mr. Ethan (nam, Anh–Mỹ), Ms. Sofia (nữ, Anh–Anh). Giọng đọc trực tiếp trong app dùng Web Speech API của trình duyệt; logic chọn giọng đã được sửa (tháng 11/2026) để chọn đúng giọng nữ cho cô và giọng nam cho thầy trên các máy Windows/Chrome phổ biến.
- **Tải ảnh giáo viên của riêng mình:** ảnh của chính người dùng hoặc người đã đồng ý; thu nhỏ và lưu trên máy đang học (localStorage), không gửi lên máy chủ.
- Bản đồ hành trình, điểm XP, huy hiệu, hiệu ứng ăn mừng; tiến độ lưu local-first, không cần tài khoản, không thu thập dữ liệu học sinh.

## Giới hạn còn lại (nói rõ, không giấu)
- **Khẩu hình khớp từng âm vị (video giáo viên nói như người thật bằng SadTalker/MuseTalk) chưa render được trong đợt này** vì cần máy có GPU NVIDIA; máy làm việc hiện tại không có GPU. Các video hiện tại là video luyện nghe (giọng chuẩn + phụ đề + ảnh tĩnh của giáo viên), không phải video khẩu hình. Chân dung trong `teachers/` đã sẵn sàng làm đầu vào render khi có máy GPU.
- Giọng đọc trực tiếp (ngoài video) vẫn là giọng có sẵn của trình duyệt/thiết bị nên chất lượng tùy máy; nếu máy không có giọng nữ tiếng Anh, app sẽ nâng cao độ giọng làm phương án dự phòng.
- Chấm phát âm ở mức so khớp câu nói (đúng từ, đủ từ), chưa phân tích từng âm vị như faster-whisper.
- Nhận diện giọng nói dùng dịch vụ của trình duyệt Chrome; không có dữ liệu giọng nào được app lưu lại.

## Giấy phép & phát hành
- Mã nguồn và nội dung bài học của English Quest 8: © 2026 Bảo Anh. Xem file `LICENSE.md`.
- Thành phần bên thứ ba: xem `THIRD-PARTY-LICENSES.md` — toàn bộ đều là thư viện chuẩn của trình duyệt/Python hoặc giấy phép cho phép thương mại. Âm thanh video dựng bằng Piper TTS ở phía soạn bài; phía học sinh không gọi API nào và app không chứa khóa API.
- Thiết kế “sẵn sàng thương mại”: nội dung tự sáng tác, riêng tư theo thiết kế (dữ liệu lưu trên máy người học).
