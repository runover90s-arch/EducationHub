---
title: "Kiểm soát độ bao phủ"
description: "Cách đảm bảo nội dung không bị bỏ sót hoặc trùng lặp."
---

# Kiểm soát độ bao phủ

## 1. Nguyên tắc

Mục tiêu không phải tạo nhiều file. Mục tiêu là:

- không bỏ sót ý quan trọng;
- không lặp một ý ở nhiều nơi;
- không đưa kiến thức nâng cao vào quá sớm;
- bài tập phủ đủ các kĩ năng;
- lời giải tương xứng độ khó;
- mọi công thức đều có ngữ cảnh và điều kiện.

## 2. Ledger theo chương

Mỗi chương theo dõi bốn lớp:

### A. Lý thuyết
Khái niệm, định luật, công thức, điều kiện, đồ thị, trường hợp đặc biệt, bẫy.

### B. Phương pháp
Nhận dạng, quy trình, lí do chọn phương pháp, biến thể và cách kiểm tra.

### C. Bài tập
Nhận biết, thông hiểu, vận dụng, vận dụng cao, đúng/sai, trả lời ngắn, đồ thị và bài tổng hợp.

### D. Lời giải
Có đáp án; giải thích; câu khó có chiến lược; không mâu thuẫn đề–đáp án.

## 3. Trạng thái Vật lí 11

| Chương | Lý thuyết | Bài tập | Lời giải | Kiểm tra | Trạng thái |
| --- | --- | --- | --- | --- | --- |
| 1. Dao động cơ học | đầy đủ bản hiện tại | có | có | có | `đã kiểm tra` |
| 2. Sóng | lõi + thực hành + Doppler/nhiễu xạ/tán sắc/quang phổ/nhiều bức xạ | có | có | có | `đã kiểm tra` |
| 3. Điện trường | lõi + cân bằng điện tích/con lắc điện | có | có | có | `đã kiểm tra` |
| 4. Dòng điện và mạch điện | lõi + thực hành + nguồn/máy thu/nhánh tụ | có | có | có | `đã kiểm tra` |
| 5. Dòng điện trong các môi trường | phần mở rộng | có | có | có | `đã kiểm tra` |
| 6. Từ trường và cảm ứng từ | phần mở rộng | có | có | có | `đã kiểm tra` |
| 7. Cảm ứng điện từ | phần mở rộng | có | có | có | `đã kiểm tra` |
| 8. Khúc xạ ánh sáng và quang hình | phần mở rộng | có | có | có | `đã kiểm tra` |

`đã kiểm tra` ở đây nghĩa là đã qua kiểm tra cấu trúc, link, LaTeX và rà logic nội bộ của bản biên soạn. Khi có phản hồi học thuật hoặc thêm corpus mới, mục có thể quay lại `bản nháp` để sửa.


## 3.1. Ngân hàng bài tập theo từng bài

Bên cạnh bài tập tổng hợp cuối chương, Vật lí 11 có **61 bộ luyện tập theo bài** với **540 câu/bài mới**, mỗi bộ có trang **Bài tập** và trang **Đáp án và lời giải** tách riêng. Bộ kiểm tra `tools/check_practice_bank.py` bảo vệ các yêu cầu cấu trúc: đủ cặp đề–giải, số câu khớp, trắc nghiệm đủ phương án, không trùng nguyên văn và không để mất liên kết từ bài học.

## 4. Kiểm tra trùng lặp

Trước khi tạo file mới:

1. tìm bài có khái niệm gần nhất;
2. xác định đây là kiến thức mới hay biến thể;
3. nếu là kiến thức cũ, liên kết;
4. nếu là mở rộng thực sự, bổ sung đúng vị trí.

## 5. Kiểm tra kiến thức tiên quyết

Một bài không dùng công cụ chưa học mà không báo trước.

Nếu buộc dùng kiến thức ngoài luồng:
- ghi rõ kiến thức tiên quyết;
- hoặc cung cấp hộp nhắc nhanh đủ dùng.

## 6. Kiểm tra bài tập

Trước khi phát hành:
- tính lại đáp án độc lập;
- kiểm tra đơn vị;
- kiểm tra dấu;
- kiểm tra điều kiện vật lí;
- kiểm tra nghiệm có nằm trong miền cho phép;
- với bài đếm, kiểm tra đầu mút;
- với mạch, kiểm tra cấu trúc liên kết mạch;
- với điện trường, kiểm tra vectơ;
- với dao động/sóng, kiểm tra pha theo modulo $2\pi$.

## 7. Kiểm tra trình bày

Chạy:

```bash
python tools/check_site.py --lint-only
```

Trước khi triển khai, GitHub Actions chạy bản đầy đủ gồm dựng website bằng MkDocs và kiểm tra HTML đã kết xuất để phát hiện LaTeX lọt ra dạng chữ thô.
