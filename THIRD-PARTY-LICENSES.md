# THIRD-PARTY LICENSES — English Quest 8 (bản hoàn thiện 12 Unit)

Bản phát hành sử dụng các thành phần sau. Không có thư viện ngoài nào bị nhúng vào mã nguồn phía học sinh.

| Thành phần | Dùng để làm gì | Giấy phép / điều kiện |
|---|---|---|
| Web Speech API (speechSynthesis & SpeechRecognition) của trình duyệt | Đọc tiếng Anh giọng en-US và nghe học sinh nói | API chuẩn của trình duyệt (Chrome/Edge); không phải thư viện phân phối kèm app |
| Python 3 standard library (`http.server`) | Chạy máy chủ tĩnh `server.py` | Python Software Foundation License — cho phép thương mại |
| HTML/CSS/JavaScript/SVG tự viết | Toàn bộ giao diện, nhân vật Ms. Mia, cảnh công viên | Tác phẩm gốc của dự án, xem LICENSE.md |
| Nội dung bài học (hội thoại, đoạn đọc, từ vựng, câu hỏi) | Nội dung 12 Unit | Tự sáng tác cho dự án, xem LICENSE.md |
| Piper TTS (chỉ dùng ở phía soạn bài, không nhúng vào app) | Dựng sẵn giọng đọc cho 12 video luyện nghe trong `videos/` (giọng nữ en-US “Amy”, giọng nam en-US “Ryan” từ dự án piper-voices của Rhasspy) | Mã nguồn Piper theo giấy phép MIT; app chỉ chứa các file âm thanh/video thành phẩm, không chứa mô hình |
| FFmpeg (chỉ dùng ở phía soạn bài) | Ghép âm thanh + phụ đề + hình ảnh thành video MP4 | Bản dựng LGPL (không bật --enable-gpl / --enable-nonfree) |
| 3 ảnh chân dung trong thư mục `teachers/` | Hình ảnh Ms. Mia, Mr. Ethan, Ms. Sofia | Ảnh do dự án tạo bằng công cụ sinh ảnh, là nhân vật hư cấu không phải người thật cụ thể; thuộc tài sản nội dung của dự án, xem LICENSE.md |
| Ảnh do người dùng tải lên trong app | Giáo viên tùy chọn | Thuộc về người tải lên/người trong ảnh; app chỉ lưu trên thiết bị của người học, không thu thập hay phân phối |

## Thành phần dự kiến ở giai đoạn sau (đã kiểm tra giấy phép thương mại)
- Kokoro-82M TTS — Apache 2.0
- Piper TTS — MIT/GPL tùy bản dựng (sẽ ghi rõ khi tích hợp)
- faster-whisper / Whisper — MIT
- MuseTalk — MIT
- SadTalker — Apache 2.0
- FFmpeg — chỉ dùng bản dựng LGPL (không bật --enable-gpl / --enable-nonfree)

## Thành phần bị cấm trong bản phát hành của dự án
- Wav2Lip (chỉ phi thương mại), XTTS v2 (Coqui Public Model License — phi thương mại), F5-TTS weights (CC-BY-NC).
- Mọi nội dung sao chép từ sách giáo khoa/nhà xuất bản, hình ảnh hoặc nhạc không rõ giấy phép.
