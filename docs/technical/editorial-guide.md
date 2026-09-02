---
title: "Quy chuẩn nội dung"
description: "Quy tắc cấu trúc, thuật ngữ, công thức và mức độ chi tiết."
---

# Quy chuẩn nội dung

## 1. Mục tiêu

Mỗi bài phải trả lời được:

1. Khái niệm là gì?
2. Vì sao cần khái niệm đó?
3. Điều kiện áp dụng là gì?
4. Công thức có ý nghĩa gì?
5. Khi nào dùng?
6. Khi nào không được dùng?
7. Sai lầm thường gặp là gì?
8. Kiến thức này nối với phần nào tiếp theo?

## 2. Không rút gọn theo kiểu làm mất ý

Khi nhiều tài liệu cùng trình bày một chủ đề:

- gộp phần trùng;
- giữ lại mọi ý **khác nhau và có giá trị học tập**;
- không xóa điều kiện áp dụng;
- không xóa trường hợp đặc biệt;
- không xóa cách giải có bản chất khác;
- không nhân bản cùng một nội dung ở nhiều file.

## 3. Cấu trúc ưu tiên cho bài Vật lí

Một bài có thể gồm:

- Mục tiêu
- Kiến thức tiên quyết
- Đặt vấn đề
- Hiện tượng
- Khái niệm
- Mô hình và giả thiết
- Đại lượng và đơn vị
- Công thức
- Suy luận hoặc chứng minh
- Trực giác
- Ví dụ
- Phản ví dụ
- Phân dạng
- Phương pháp giải
- Bẫy thường gặp
- Trường hợp đặc biệt
- Bài tập
- Gợi ý
- Đáp án và lời giải
- Tóm tắt
- 5 điều cần nhớ

Không ép bài nào cũng phải có đủ mọi mục nếu không phù hợp.

## 4. Công thức

Mỗi công thức quan trọng phải có:

- công thức;
- ý nghĩa từng kí hiệu;
- đơn vị;
- điều kiện;
- cách dùng;
- ít nhất một ví dụ nếu công thức dễ bị dùng sai.

## 5. Đơn vị

- Ưu tiên SI trong phần lí thuyết.
- Nếu đề bài dùng cm, mm, mA... có thể giữ nguyên khi phép tính không cần đổi.
- Phải đổi đơn vị trước những phép tính yêu cầu hệ đơn vị thống nhất.
- Không đổi đơn vị máy móc nếu làm bài khó đọc hơn mà không cần thiết.

## 6. Mức kiến thức

- Level 1 — Foundation
- Level 2 — Standard
- Level 3 — Applied
- Level 4 — Advanced
- Level 5 — Enrichment

Nội dung Level 4–5 phải tách khỏi luồng nền tảng.

## 7. Cách viết

Ưu tiên câu ngắn, trực tiếp.

Không thêm những cụm từ làm đề bài khó hiểu hơn.

Không biến một câu hỏi đơn giản thành một đoạn văn dài nếu dữ kiện không cần bối cảnh.

## 8. Thuật ngữ

Một khái niệm phải dùng nhất quán tên gọi trong toàn môn.

Nếu có hai cách gọi phổ biến, giải thích ở lần xuất hiện đầu tiên rồi chọn một cách dùng chính.

## 9. Cross-reference

Khi kiến thức đã được giải thích đầy đủ ở bài trước:

- tóm tắt tối thiểu phần cần nhớ;
- liên kết về bài cũ;
- không sao chép nguyên một mục dài.

## 10. Chuẩn LaTeX và khoảng trắng

Để công thức hiển thị ổn định với MkDocs Material + Arithmatex + MathJax:

- công thức trong câu dùng `$...$`;
- công thức cần tách dòng dùng `$$...$$`;
- không viết trực tiếp delimiter `\\(...\\)` hoặc `\\[...\\]` trong Markdown;
- không đặt `$...$` trong tiêu đề Markdown; dùng kí hiệu Unicode hoặc chữ thường trong tiêu đề, rồi trình bày công thức bằng MathJax ở phần thân bài;
- không tách một kí hiệu đơn thành một khối công thức lớn;
- công thức ngắn nên nằm ngay trong câu nếu cách đó dễ đọc hơn;
- chỉ dùng display math khi công thức cần nhấn mạnh, có phân số lớn hoặc có nhiều bước biến đổi.

Ví dụ nên dùng:

```text
**Kí hiệu:** $x$.
```

thay vì tạo một khối chỉ chứa `x`.

## 11. Trình bày trên điện thoại

Nội dung phải được kiểm tra ở màn hình hẹp trước khi xuất bản.

- tiêu đề không được chiếm gần toàn bộ màn hình;
- bảng nhiều cột phải cuộn ngang thay vì ép mỗi từ xuống một dòng;
- công thức dài được phép cuộn ngang;
- hạn chế chuỗi nhiều display equation liên tiếp nếu có thể viết thành một phép biến đổi duy nhất;
- khoảng cách giữa tiêu đề, đoạn văn và công thức phải đủ rõ nhưng không tạo vùng trắng vô nghĩa.

Trước khi push, chạy:

```bash
python tools/check_site.py
```

## Quy tắc trình bày công thức trên màn hình nhỏ

Để tránh bài học bị kéo dài bởi các khoảng trắng lớn, công thức được chọn cách trình bày theo vai trò của nó:

- Công thức ngắn nằm trong một câu giải thích nên viết **inline**, ví dụ: `Chu kì là $T=2\pi/\omega$.`
- Chỉ dùng công thức **display** (`$$...$$`) khi công thức là trọng tâm, dài, có nhiều bước biến đổi hoặc cần căn chỉnh nhiều dòng.
- Không tách mỗi đại lượng của một lời giải thành một khối display riêng. Với các kết quả như $A$, $\omega$, $T$, $f$, nên dùng câu hoặc danh sách ngắn.
- Trong `admonition`, `details` và danh sách đánh số, ưu tiên công thức inline. Không đặt delimiter `$$` thụt lề nếu không thực sự cần thiết, vì Markdown có thể xuất nguyên kí hiệu `$$` ra trang.
- Khi một lời giải có nhiều bước biến đổi liên tiếp, dùng **một** khối `aligned` thay vì nhiều khối công thức rời nhau.

Ví dụ nên dùng:

```markdown
- Biên độ: $A=8$ cm.
- Chu kì: $T=0,5$ s.
- Tần số: $f=2$ Hz.
```

Thay vì ba khối `$$...$$` riêng biệt.
