# Education Hub

Kho giáo trình học tập đa ngành được tổ chức bằng Markdown và xuất bản với MkDocs Material.

Nội dung học tập nằm trong `docs/`. Cấu trúc hiện tại:

`Education Hub -> Lĩnh vực -> Vật lí -> Trung học phổ thông -> Vật lí 11`

Vật lí 11 là giáo trình hoàn chỉnh đầu tiên của hệ thống; các lĩnh vực và giáo trình khác có thể được bổ sung tiếp mà không thay đổi kiến trúc gốc.

## Chạy tại Codespaces hoặc máy cá nhân

```bash
pip install -r requirements.txt
python tools/check_site.py
mkdocs serve
```

## Kiểm tra trước khi push

```bash
python tools/check_site.py
```

Trình kiểm tra rà Markdown, LaTeX, liên kết, navigation, asset và — khi MkDocs đã được cài — build strict rồi kiểm tra HTML render.
