# Education Hub

Kho giáo trình học tập đa ngành được xuất bản bằng MkDocs Material.

Nội dung học tập nằm trong `docs/`. Vật lí 11 là giáo trình đầu tiên đang được xây dựng trong nhánh:

`Vật lí -> Trung học phổ thông -> Vật lí 11`.

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

Trình kiểm tra sẽ rà lỗi Markdown/LaTeX, liên kết nội bộ và chạy `mkdocs build --strict`.
