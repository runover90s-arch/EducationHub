# Làm Education Hub hoàn toàn trên điện thoại Android

> **Trạng thái hiện tại:** GitHub Codespaces đang không sử dụng được do quota/budget đã hết. Workflow chính của repository là **Termux-first** trên Android. Không cần Codespaces để tiếp tục phát triển. Chỉ quay lại Codespaces nếu sau này chủ repository xác nhận nó đã khả dụng và muốn dùng lại.

Termux là terminal chính; `github.dev` chỉ dùng khi muốn sửa nhanh; GitHub Actions chịu trách nhiệm quality gate/build/deploy từ xa.

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

## 3. Termux — môi trường terminal chính

Cài Termux từ F-Droid hoặc GitHub Releases của Termux. Sau đó chạy:

```bash
pkg update && pkg upgrade -y
pkg install -y git python gh unzip rsync
termux-setup-storage
python -m pip install --upgrade pip
```

Khi Android hỏi quyền truy cập file, chọn **Cho phép**. Repository mặc định làm việc tại `~/EducationHub`; các ZIP tải từ ChatGPT thường nằm ở `~/storage/downloads/`.

Để tránh lỗi `Author identity unknown` khi commit, cấu hình repo-local một lần:

```bash
cd ~/EducationHub
git config user.name "runover90s-arch"
git config user.email "266472043+runover90s-arch@users.noreply.github.com"
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

## 5. Codespaces hiện không dùng

Codespaces hiện đang không khả dụng vì quota/budget. **Không coi đây là bước tạm thời cần khắc phục trong workflow phát triển.** Tiếp tục làm việc bằng Termux + GitHub Actions; `github.dev` chỉ là công cụ sửa nhanh tùy chọn. Cách này không sử dụng Codespaces compute hours.

Nếu sau này Codespaces dùng được trở lại, chỉ chuyển workflow khi chủ repository nói rõ muốn dùng lại.
