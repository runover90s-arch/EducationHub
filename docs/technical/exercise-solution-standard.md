---
title: "Chuẩn bài tập và lời giải"
description: "Quy tắc biên soạn, rà soát và giải bài tập."
---

# Chuẩn bài tập và lời giải

## 1. Mục tiêu của hệ bài tập

Bài tập phải kiểm tra một hoặc nhiều năng lực rõ ràng:

- nhớ đúng khái niệm;
- hiểu bản chất;
- đọc công thức;
- biến đổi đại lượng;
- đọc đồ thị;
- chọn mô hình;
- kết hợp nhiều hệ thức;
- phát hiện sai lầm.

Không tạo số lượng bằng cách chỉ thay số.

## 2. Dạng câu hỏi

Có thể dùng:

- trắc nghiệm bốn lựa chọn;
- đúng/sai theo từng ý;
- trả lời ngắn;
- bài tự luận;
- bài đọc đồ thị;
- bài tổng hợp nhiều bước.

## 3. Giữ câu chữ tự nhiên

Đề bài phải:

- nói thẳng dữ kiện;
- dùng thuật ngữ đã học;
- không thêm bối cảnh giả tạo;
- không dùng câu dài chỉ để làm bài trông khó.

## 4. Mức độ

### Mức 1 — Nhận biết

Một khái niệm hoặc một công thức trực tiếp.

### Mức 2 — Thông hiểu

Cần hiểu quan hệ giữa các đại lượng, không chỉ đọc số.

### Mức 3 — Vận dụng

Cần từ hai bước suy luận trở lên hoặc phải chọn công thức phù hợp.

### Mức 4 — Vận dụng cao

Kết hợp nhiều ý, có điều kiện ẩn hoặc cần chọn chiến lược.

### Mức 5 — Thử thách

Dành cho mở rộng; không được dùng để đánh giá phần nền nếu kiến thức vượt chương trình lõi.

## 5. Quy trình kiểm đáp án

Mỗi câu phải được kiểm tra theo thứ tự:

1. ghi lại dữ kiện;
2. xác định đại lượng cần tìm;
3. kiểm tra đơn vị;
4. chọn mô hình;
5. tính độc lập;
6. kiểm tra dấu;
7. kiểm tra thứ nguyên;
8. kiểm tra độ lớn có hợp lí không;
9. đối chiếu lựa chọn nếu là trắc nghiệm.

Không lấy đáp án có sẵn làm bằng chứng duy nhất.

## 6. Mức độ chi tiết của lời giải

### Câu dễ

- nêu công thức;
- thay số;
- kết luận.

### Câu trung bình

- giải thích vì sao chọn công thức;
- biến đổi từng bước;
- kết luận.

### Câu khó

Phải có:

- phân tích dữ kiện;
- nhận dạng ý tưởng;
- lí do chọn phương pháp;
- sơ đồ hoặc phân trường hợp nếu cần;
- phép biến đổi rõ;
- kiểm tra kết quả;
- chỉ ra bẫy nếu có.

## 7. Đúng/Sai

Mỗi ý phải được giải thích riêng.

Không chỉ ghi:

```text
a Đ; b S; c Đ; d S
```

mà không nêu lí do.

## 8. Trả lời ngắn

Nếu đáp án là số:

- ghi đơn vị khi đề yêu cầu;
- nêu quy tắc làm tròn;
- chỉ làm tròn ở cuối nếu không có chỉ dẫn khác.

## 9. Đồ thị

Khi bài có đồ thị:

- chỉ rõ trục;
- đơn vị;
- các mốc đọc;
- vì sao khoảng thời gian chọn được là $T$, $T/2$, $T/4$...;
- tránh suy luận từ hình vẽ không đúng tỉ lệ nếu đề không cho phép.

## 10. Cấu trúc ngân hàng theo từng bài

Mỗi bài học Vật lí 11 phải có hai trang riêng:

- **Bài tập:** trắc nghiệm, đúng/sai, trả lời ngắn, vận dụng;
- **Đáp án và lời giải:** đánh số khớp 1–1 với trang bài tập.

Mỗi bài lý thuyết phải đặt liên kết **Luyện tập sau bài** dẫn đến đúng hai trang này. Cuối chương vẫn giữ **Bài tập tổng hợp chương** để kiểm tra khả năng phối hợp kiến thức giữa nhiều bài.

Trước khi phát hành chạy:

```bash
python tools/check_practice_bank.py
python tools/check_pdf_import.py
python tools/check_solution_quality.py
python tools/check_site.py --lint-only
```

Bộ kiểm tra cấu trúc không thay thế việc kiểm chứng học thuật: người biên soạn vẫn phải tính lại đáp án và xem xét điều kiện vật lí của từng câu.
## 11. Văn phong lời giải Vật lí 11 theo corpus PDF

Khi bài được nhập hoặc đối chiếu từ corpus PDF Vật lí 11, phần lời giải ưu tiên nhịp trình bày quen thuộc của tài liệu nguồn nhưng phải được chuẩn hóa để học trên web:

- mở bằng **Đáp án** hoặc **Kết luận** khi cần;
- dùng nhãn **Hướng dẫn giải**;
- diễn đạt theo mạch: **Ta có → Suy ra → Thay số → Vậy**;
- câu nhận biết chỉ cần nêu đúng căn cứ, không kéo dài giả tạo;
- câu thông hiểu/vận dụng phải chỉ rõ quan hệ hoặc công thức quyết định;
- câu khó phải chia bước, nói vì sao chọn mô hình/phương pháp, kiểm tra điều kiện và chốt kết quả;
- câu Đúng/Sai phải giải thích từng ý, đặc biệt chỉ ra vì sao một phát biểu sai;
- không giữ nguyên các dòng OCR vỡ công thức nếu có thể viết lại bằng Markdown/LaTeX sạch.

Không sao chép máy móc lỗi trình bày của PDF. Mục tiêu là giữ **văn phong và cách lập luận** của nguồn, đồng thời làm cho lời giải mạch lạc, tự đủ thông tin và dễ theo dõi hơn.

## 12. Khi đáp án hoặc lời giải nguồn có mâu thuẫn

Không được sửa âm thầm. Quy trình bắt buộc:

1. đọc lại câu hỏi và hình gốc;
2. tính/biện luận độc lập từ dữ kiện;
3. đối chiếu phần đáp án và phần hướng dẫn trong PDF;
4. nếu nguồn tự mâu thuẫn nhưng kết quả đúng xác định được chắc chắn, hiệu chỉnh tối thiểu và thêm admonition `Đối chiếu nguồn`;
5. nếu thiếu dữ kiện để quyết định duy nhất, giữ nguyên vấn đề và ghi rõ điều kiện còn thiếu thay vì đoán.

Checker `tools/check_solution_quality.py` kiểm tra cả hai lớp ngân hàng — bài biên soạn trước và bài nhập từ PDF — về tính toàn vẹn, sự đồng nhất giữa lời giải inline/`solutions.md`, mức độ giải thích theo độ khó và cấu trúc Đúng/Sai. Checker này **không thay thế** bước kiểm chứng vật lí độc lập ở trên.

