# Làm Education Hub hoàn toàn trên điện thoại Android

Repository này có thể duy trì mà không cần GitHub Codespaces.

## 1. Sửa nhanh bằng github.dev

Trên trình duyệt điện thoại, mở repository rồi đổi `github.com` thành `github.dev` trong thanh địa chỉ.

Ví dụ:

```text
https://github.dev/runover90s-arch/EducationHub
```

`github.dev` phù hợp để:

- sửa Markdown, YAML, Python và các file cấu hình;
- tìm kiếm toàn repository;
- xem diff;
- commit và push lên GitHub;
- tạo/switch branch.

`github.dev` không có terminal và không chạy `mkdocs serve` trực tiếp. Việc kiểm tra/build được GitHub Actions thực hiện tự động sau khi push.

## 2. Cách làm an toàn nhất trên điện thoại

Khi sửa nội dung đáng kể, nên tạo branch riêng trong github.dev, ví dụ `edit-mobile`, rồi commit/push. Workflow **Validate Education Hub** sẽ tự chạy checker và `mkdocs build --strict` trên branch đó. Khi tất cả đều xanh, tạo Pull Request và merge vào `main`.

Nếu chỉ sửa rất nhỏ và commit trực tiếp vào `main`, workflow deploy vẫn chạy toàn bộ checker trước khi publish GitHub Pages. Nếu checker thất bại, bản website mới sẽ không được deploy.

## 3. Chạy local bằng Termux khi thật sự cần terminal

Cài Termux từ F-Droid hoặc GitHub Releases của Termux. Sau đó chạy:

```bash
pkg update && pkg upgrade -y
pkg install -y git python
python -m pip install --upgrade pip
```

Clone repository lần đầu:

```bash
git clone https://github.com/runover90s-arch/EducationHub.git
cd EducationHub
python -m pip install -r requirements.txt
```

Những lần sau chỉ cần:

```bash
cd EducationHub
git pull --rebase
python tools/check_practice_bank.py
python tools/check_pdf_import.py
python tools/check_solution_quality.py
python tools/check_site.py
mkdocs build --strict
```

Muốn xem website local:

```bash
mkdocs serve -a 0.0.0.0:8000
```

Sau đó mở trình duyệt trên chính điện thoại và truy cập `http://127.0.0.1:8000/`.

## 4. Workflow GitHub Actions trong repository

- **Validate Education Hub**: chạy khi push lên branch khác `main`, khi mở/cập nhật Pull Request, hoặc chạy thủ công. Workflow này chỉ kiểm tra và build, không deploy.
- **Deploy Education Hub to GitHub Pages**: chạy khi push vào `main`. Chỉ deploy sau khi toàn bộ checker và build nghiêm ngặt thành công.

Các checker bắt buộc:

```bash
python tools/check_practice_bank.py
python tools/check_pdf_import.py
python tools/check_solution_quality.py
python tools/check_site.py
mkdocs build --strict
```

## 5. Khi Codespaces hết quota

Không cần xóa hoặc tạo Codespace mới để tiếp tục chỉnh repository. Dùng `github.dev` cho phần lớn công việc; chỉ dùng Termux khi cần terminal, chạy checker hoặc preview local. Cách này không sử dụng Codespaces compute hours.
