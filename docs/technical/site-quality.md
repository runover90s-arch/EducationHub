---
title: "Kiểm tra website và LaTeX"
---

# Kiểm tra website và LaTeX

Education Hub có quality gate tại:

```bash
python tools/check_site.py
```

## Những lỗi được kiểm tra ở mã nguồn

Trình kiểm tra phát hiện:

- delimiter LaTeX thô `\\(...\\)` hoặc `\\[...\\]` trong Markdown;
- LaTeX trong tiêu đề Markdown (`#`, `##`, `###`); tiêu đề dùng kí hiệu Unicode/chữ thường, còn công thức đầy đủ đặt ở nội dung ngay bên dưới;
- lệnh LaTeX như `\\omega`, `\\frac`, `\\cos` nằm ngoài vùng toán;
- dấu `$` hoặc `$$` không cân bằng;
- `$$` bị thụt lề trong list/admonition, là trường hợp dễ hiện nguyên LaTeX trên web;
- display math chỉ chứa một kí hiệu và tạo khoảng trắng vô ích;
- nhiều display math ngắn xếp sát nhau, làm lời giải bị giãn quá mức trên mobile;
- link Markdown nội bộ bị chết;
- ảnh Markdown local bị thiếu hoặc resolve ra ngoài `docs/`;
- file được khai báo trong `nav`, CSS hoặc JavaScript nhưng không tồn tại;
- `mkdocs.yml` không hợp lệ.

## Kiểm tra sau khi kết xuất

Khi không dùng `--lint-only`, script còn chạy:

```bash
mkdocs build --strict
```

Sau đó nó quét **HTML đã dựng**. Những chuỗi như `$$`, `\\omega`, `\\frac`, `\\cos` còn xuất hiện dưới dạng văn bản nhìn thấy được bên ngoài vùng `arithmatex` sẽ làm kiểm tra thất bại.

Điểm này quan trọng vì một file Markdown có thể nhìn đúng về mặt cú pháp nhưng vẫn bị parser hiểu sai trong list hoặc admonition. Kiểm tra HTML giúp bắt đúng loại lỗi từng xuất hiện trên giao diện điện thoại.

## Cú pháp toán chuẩn

Công thức trong dòng:

```markdown
$x=A\cos(\omega t+\varphi)$
```

Công thức cần tách dòng:

```markdown
$$
\omega=2\pi f
$$
```

Không dùng display math chỉ để hiển thị một biến như `$x$`, `$T$` hoặc một kết quả rất ngắn. Những trường hợp đó nên để inline.

## Khi chỉ muốn lint nhanh

```bash
python tools/check_site.py --lint-only
```

Chế độ này không cần MkDocs nhưng cũng không thể phát hiện lỗi chỉ xuất hiện sau khi Markdown được kết xuất thành HTML.


## Lỗi và cảnh báo

`check_site.py` dùng **ERROR** cho lỗi deterministic có thể xác định từ source, gồm link/asset local không tồn tại, path asset thoát khỏi `docs/`, cấu hình MkDocs sai và các lỗi LaTeX/HTML chắc chắn. Các nghi vấn mang tính ngữ nghĩa của bài tập được để cho checker chuyên biệt báo **WARNING** thay vì làm build thất bại khi chưa đủ bằng chứng.

Với Vật lí 11, phân công gate tối thiểu là: `check_practice_bank.py` bắt layout phần biên soạn trước và ghi chú nội bộ learner-facing; `check_pdf_import.py` bắt layout/provenance/asset của khối nhập PDF; `check_solution_quality.py` bắt cấu trúc lời giải, Đúng/Sai, placeholder đã xác nhận và cảnh báo đề nghi thiếu dữ kiện; `check_site.py` tiếp tục là lớp bảo vệ link/asset toàn site. Các gate này bổ sung cho nhau, không thay thế duplicate/source checks hiện có.
