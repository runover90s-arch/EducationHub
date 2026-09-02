---
title: "Kiểm tra website và LaTeX"
description: "Quy trình kiểm tra công thức, liên kết và build trước khi xuất bản."
---

# Kiểm tra website và LaTeX

Education Hub có trình kiểm tra tự động tại:

`tools/check_site.py`

## Chạy kiểm tra đầy đủ

```bash
python tools/check_site.py
```

Lệnh này thực hiện ba lớp kiểm tra:

1. rà Markdown và cú pháp LaTeX thường gây lỗi hiển thị;
2. kiểm tra liên kết Markdown nội bộ;
3. chạy `mkdocs build --strict` để phát hiện lỗi cấu hình hoặc cảnh báo build.

## Chuẩn viết công thức

Trong file Markdown, dùng:

- công thức trong dòng: `$x=A\cos(\omega t+\varphi)$`;
- công thức tách dòng: mở và đóng bằng `$$`.

Không viết trực tiếp `\(...\)` hoặc `\[...\]` trong file Markdown. Với cấu hình hiện tại, `pymdownx.arithmatex` chịu trách nhiệm nhận diện công thức và chuyển sang dạng MathJax cần xử lí.

## Các lỗi trình kiểm tra phát hiện

- delimiter LaTeX thô `\(`, `\)`, `\[`, `\]`;
- lệnh như `\omega`, `\frac`, `\cos` nằm ngoài vùng toán;
- dấu `$` hoặc khối `$$` không cân bằng;
- khối công thức chỉ chứa một kí hiệu đơn, thường gây khoảng trắng lớn không cần thiết;
- liên kết `.md` nội bộ trỏ tới file không tồn tại;
- lỗi hoặc warning từ `mkdocs build --strict`.

## Quy tắc trình bày công thức

Công thức tách dòng chỉ dùng khi nó thực sự cần được nhấn mạnh hoặc có nhiều bước biến đổi.

Ví dụ, không nên viết một kí hiệu đơn như sau:

```text
$$
x
$$
```

Nên viết gọn trong câu:

```text
**Kí hiệu:** $x$.
```

Cách này tránh tạo khoảng trống lớn trên màn hình điện thoại.
