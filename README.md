# Education Hub

Kho giáo trình học tập đa ngành được tổ chức bằng Markdown và xuất bản với MkDocs Material.

Nội dung học tập nằm trong `docs/`. Cấu trúc hiện tại:

`Education Hub -> Lĩnh vực -> Vật lí -> Trung học phổ thông -> Vật lí 11`

Vật lí 11 là giáo trình hoàn chỉnh đầu tiên của hệ thống; các lĩnh vực và giáo trình khác có thể được bổ sung tiếp mà không thay đổi kiến trúc gốc.

Bản hiện tại có ngân hàng luyện tập Vật lí 11 tách theo từng bài: mỗi bài có **Bài tập** và **Đáp án/Lời giải** riêng, đồng thời vẫn giữ bài tập tổng hợp cuối chương.

## Chạy tại Codespaces hoặc máy cá nhân

```bash
pip install -r requirements.txt
python tools/check_practice_bank.py
python tools/check_pdf_import.py
python tools/check_site.py
mkdocs serve
```

## Kiểm tra trước khi push

```bash
python tools/check_practice_bank.py
python tools/check_pdf_import.py
python tools/check_site.py
```

`check_practice_bank.py` kiểm tra cấu trúc ngân hàng bài tập đã biên soạn. `check_pdf_import.py` kiểm tra toàn vẹn ngân hàng nhập từ PDF: cặp đề–lời giải, source-id, câu trùng, ảnh công thức/hình vẽ và ngưỡng số lượng. `check_site.py` rà Markdown, LaTeX, liên kết, điều hướng, tài nguyên; khi MkDocs đã được cài, nó còn dựng website ở chế độ nghiêm ngặt và kiểm tra HTML đã kết xuất.
