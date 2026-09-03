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
python tools/check_site.py --lint-only
```

Bộ kiểm tra cấu trúc không thay thế việc kiểm chứng học thuật: người biên soạn vẫn phải tính lại đáp án và xem xét điều kiện vật lí của từng câu.
