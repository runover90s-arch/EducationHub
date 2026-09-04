# AI Project Instructions — Education Hub

> **Đọc file này trước khi chỉnh sửa repository.**
>
> Đây là ghi chú bàn giao dành cho AI/maintainer để những lần làm việc sau giữ đúng cách tổ chức, cách biên soạn và các quyết định đã thống nhất với chủ repository.

## 1. Nguyên tắc chung

- Repository **Education Hub đã tồn tại** và đang dùng **MkDocs Material + GitHub Pages**.
- Không tạo repository mới khi người dùng gửi lại source.
- Trước khi thay đổi, phải đọc cấu trúc hiện tại, `mkdocs.yml`, các file liên quan và xác định đúng phạm vi cần sửa.
- Chỉ sửa/thêm phần người dùng yêu cầu. Không tự ý viết lại các phần đã ổn.
- Không làm mất nội dung cũ, không tạo link chết, không phá navigation hoặc naming convention hiện có.
- Khi thêm nội dung mới phải kiểm tra trùng lặp và ưu tiên tích hợp vào cấu trúc đang có.
- Nếu người dùng nói **"tiếp tục"**, tiếp tục đúng trạng thái hiện tại; không tạo lại phần đã hoàn thành.

## 2. Chính sách đối với nguồn PDF Vật lí 11

Các PDF do người dùng cung cấp là **nguồn chính** để bổ sung lý thuyết, dạng bài, ví dụ, bài tập và lời giải Vật lí 11.

Khi dùng các nguồn này:

- Không tự ý rút ngắn nội dung chỉ để làm trang gọn hơn.
- Không làm mất bước suy luận, điều kiện áp dụng, dữ kiện hoặc độ khó của bài.
- Không tự ý đổi văn phong ra đề nếu không cần thiết.
- Giữ cách dùng thuật ngữ, mức độ kiến thức, cấu trúc bài và phong cách ra đề gần với tài liệu nguồn.
- Có thể chuẩn hóa Markdown, LaTeX, đơn vị, dấu câu và cách trình bày để người học đọc dễ hơn, **nhưng không được làm thay đổi nội dung học thuật**.
- Nếu nhiều nguồn nói về cùng một nội dung, cần đối chiếu để tránh đưa đáp án hoặc công thức mâu thuẫn.
- Nếu một đề có lỗi logic, thiếu dữ kiện, công thức sai hoặc đáp án nguồn sai/chưa được kiểm chứng, chỉ được hiệu chỉnh **mức tối thiểu cần thiết** sau khi đối chiếu chắc chắn với chính PDF/ảnh trang nguồn. Phiên bản sửa phải giữ cùng ý tưởng kiểm tra, dữ kiện cốt lõi, độ khó và văn phong ra đề gần với nguồn.
- **Không được âm thầm sửa hoặc thay đáp án nguồn.** Nếu đề/đáp án/lời giải trong chính PDF tự mâu thuẫn, phải ghi rõ điểm mâu thuẫn trong phần đáp án/lời giải hoặc đánh dấu cần kiểm tra; không giả vờ nguồn nhất quán.
- Không bịa thêm đáp án chỉ để hoàn thiện trang.
- Nếu không đủ cơ sở để xác minh, phải đánh dấu vấn đề thay vì đoán.

### Không tạo mục tài liệu tham khảo công khai

- **Không thêm `references.md`, mục "Nguồn", "Tài liệu tham khảo" hoặc danh sách tên PDF lên website/repository public-facing nếu người dùng chưa yêu cầu.**
- Tên nguồn trong file này chỉ phục vụ bàn giao nội bộ cho AI/maintainer.

## 3. Danh sách nguồn Vật lí 11 đã được người dùng cung cấp

Các file nguồn đã dùng/được chỉ định làm corpus tham khảo trong phiên làm việc trước:

1. `EBOOK BẢN ĐỒ KIẾN THỨC VẬT LÝ 11, MAPSTUDY-compressed.pdf`
2. `EBOOK CHUYÊN ĐỀ VẬT LÝ 11 TẬP 1 DAO ĐỘNG VÀ SÓNG, THẦY VŨ HOÀNG QUÂN-compressed.pdf`
3. `EBOOK CHUYÊN ĐỀ VẬT LÝ 11 TẬP 2 ĐIỆN TRƯỜNG VÀ DÒNG ĐIỆN, THẦY VŨ HOÀNG QUÂN-compressed.pdf`
4. `EBOOK LÀM CHỦ VÀ NÂNG CAO VẬT LÝ 11 TẬP 1 DAO ĐỘNG VÀ SÓNG, THẦY VŨ TUẤN ANH-compressed.pdf`
5. `EBOOK LÀM CHỦ VÀ NÂNG CAO VẬT LÝ 11 TẬP 2 ĐIỆN TRƯỜNG, DÒNG ĐIỆN MẠCH ĐIỆN, THẦY VŨ TUẤN ANH-compressed.pdf`
6. `EBOOK PHONG TOẢ VẬT LÝ 11 TẬP 1 DAO ĐỘNG, SÓNG, MAPSTUDY-compressed.pdf`
7. `EBOOK PHONG TOẢ VẬT LÝ 11 TẬP 2 ĐIỆN TRƯỜNG, DÒNG ĐIỆN, MẠCH ĐIỆN, MAPSTUDY-compressed.pdf`
8. `EBOOK SỔ TAY CÔNG THỨC VẬT LÝ 11, THẦY VŨ HOÀNG QUÂN-compressed.pdf`
9. `EBOOK SỔ TAY LÝ THUYẾT VẬT LÝ 10 11 12, IPCLASS-compressed.pdf`
10. `BT-Chương I_1.pdf`
11. `BT-Chương II_1.pdf`
12. `BT-Chương III_1.pdf`
13. `BT-Chương IV_1.pdf`

**Quan trọng:** Các PDF trên không nhất thiết nằm trong repository. Nếu một phiên làm việc mới chỉ có source GitHub nhưng không có PDF, không được giả vờ đã đọc PDF; cần yêu cầu người dùng cung cấp lại file nguồn cần thiết trước khi trích nội dung mới từ chúng.

## 4. Quy tắc tích hợp bài tập từ PDF

### 4.1. Đánh số bài liên tục

- **Không dùng tên kiểu `Bài PDF 11`, `Bài PDF 12`, ...**
- Số bài lấy từ PDF gốc chỉ là thông tin nguồn, không phải số hiển thị trên website.
- Bài mới phải nối tiếp số bài đang có trong đúng bộ bài tập.
- Ví dụ: bộ hiện tại có Bài 1–10 thì bài mới bắt đầu từ **Bài 11**, tiếp theo Bài 12, Bài 13,...
- Sau khi nhập hàng loạt, kiểm tra không thiếu số, không trùng số và không còn chuỗi `Bài PDF`.

### 4.2. Đề bài phải là nội dung Markdown

- Trích đề từ PDF và **gõ lại thành Markdown/LaTeX sạch**.
- Không dùng ảnh chụp nguyên đề thay cho phần văn bản nếu đề có thể biểu diễn tốt bằng Markdown.
- Nếu trong ảnh có số câu gốc như `Câu 6`, không để số đó khiến người học nhầm với số bài trên website.
- Phương án A/B/C/D, bảng Đúng/Sai, dữ kiện và đơn vị phải được trình bày rõ ràng, logic.

## 5. Quy tắc trích hình/đồ thị

Ảnh chỉ được giữ khi nó mang thông tin trực quan cần thiết cho bài, ví dụ:

- đồ thị li độ–thời gian;
- đồ thị vận tốc/gia tốc;
- sơ đồ mạch;
- hình thí nghiệm;
- hình học/vectơ cần quan sát;
- bảng/biểu đồ không thể tái tạo hợp lý bằng Markdown.

Khi crop ảnh từ PDF:

- **Chỉ cắt đúng đồ thị/hình minh họa cần thiết.**
- Không cắt luôn phần đề bài nếu đề đã được gõ ở Markdown.
- Không cắt luôn đáp án, hướng dẫn giải hoặc lời giải vào ảnh.
- **Ưu tiên crop tránh logo, watermark và dòng chữ nguồn.** Nếu chúng nằm ngoài phần hình cần thiết thì phải loại khỏi crop.
- Nếu watermark nằm chồng trực tiếp lên hình gốc và không thể cắt bỏ mà không làm mất dữ kiện, chỉ giữ **vùng tối thiểu cần thiết**; không xóa, vẽ đè hoặc tái tạo giả hình để che watermark.
- **Không tự tạo/redraw ảnh, đồ thị hoặc sơ đồ mới.** Chỉ dùng hình được crop từ chính PDF nguồn, trừ khi người dùng chủ động yêu cầu tạo hình mới.
- Ảnh phải đủ rõ để đọc trục, ký hiệu, số liệu và chú thích quan trọng.

## 6. Quy tắc đáp án và lời giải

Mỗi bài nên có phần mở rộng bằng MkDocs Material, theo mẫu đang dùng:

```markdown
??? success "Đáp án và lời giải"
    Nội dung lời giải...
```

Yêu cầu:

- Không để đáp án/lời giải nằm sẵn trong ảnh đề.
- Người học bấm **"Đáp án và lời giải"** mới thấy phần giải.
- Độ chi tiết phải phụ thuộc độ khó:
  - bài nhận biết: ngắn nhưng phải nêu căn cứ;
  - bài thông hiểu/vận dụng: chỉ rõ công thức, thay số, lập luận;
  - bài khó/vận dụng cao: giải theo từng bước, giải thích vì sao chọn phương pháp, kiểm tra điều kiện và kết luận;
  - bài có nhiều hướng giải đáng giá: có thể trình bày thêm cách khác nếu giúp học bản chất.
- "Dễ hiểu" nghĩa là **trình bày logic, mạch lạc và có sư phạm**, không phải hạ độ khó hoặc biến đổi đề thành bài dễ hơn.
- Công thức phải có đơn vị và điều kiện áp dụng khi cần.
- Kết quả cuối phải được kiểm tra lại với dữ kiện và với đáp án nguồn nếu nguồn có đáp án.

## 7. Kiểm tra chất lượng bài tập

Trước khi hoàn tất một đợt nhập/sửa bài tập:

- rà lại toàn bộ số bài;
- kiểm tra câu bị trùng;
- kiểm tra đề có đủ dữ kiện;
- kiểm tra công thức, đại lượng, dấu, pha, đơn vị;
- kiểm tra đáp án lựa chọn khớp kết quả tính;
- kiểm tra lời giải không tự mâu thuẫn;
- kiểm tra ảnh đúng bài và không chứa phần đáp án ngoài ý muốn;
- kiểm tra ảnh không bị crop mất trục/ký hiệu quan trọng;
- kiểm tra các khối `??? success` render hợp lệ;
- chạy các checker có sẵn trong `tools/` nếu phù hợp.

## 8. Trạng thái bàn giao hiện tại — chuẩn Vật lí 11 v16

Từ bản v16, **toàn bộ 61 bộ luyện tập theo từng bài của Vật lí 11** tiếp tục giữ chuẩn hiển thị đã thống nhất, đồng thời áp dụng quality gate cho đáp án/lời giải:

- câu/bài hiển thị bằng nhãn **`Bài N`** theo thứ tự liên tục trong từng bộ;
- **không còn nhãn `Bài PDF N`** hoặc dùng số câu PDF làm nhãn hiển thị;
- đề bài được gõ bằng Markdown/LaTeX; các lựa chọn A/B/C/D phải tách dòng/đoạn rõ ràng, không dính thành một khối khó đọc;
- mỗi bài phải có nút **`Đáp án và lời giải`** riêng ngay sau đề; đáp án/hướng dẫn không được lẫn vào phần đề;
- không dùng ảnh chụp nguyên câu hỏi có sẵn đáp án được tô/chọn; nếu cần hình thì chỉ crop đồ thị, sơ đồ, bảng hoặc hình minh họa thật sự cần thiết từ PDF;
- ảnh crop phải đủ dữ kiện nhưng càng chặt càng tốt, ưu tiên loại logo/watermark/text nguồn khi có thể mà không làm mất thông tin;
- không tự tạo ảnh thay thế;
- các câu trùng nội dung phải được loại để không lặp bài;
- sau mỗi đợt sửa phải chạy `check_practice_bank.py`, `check_pdf_import.py`, `check_solution_quality.py`, `check_site.py` và kiểm tra `mkdocs build --strict` khi môi trường có MkDocs.
- `check_solution_quality.py` phải bao phủ **cả bài biên soạn trước lẫn bài nhập từ PDF**, kiểm tra sự đồng nhất lời giải, cấu trúc Đúng/Sai và yêu cầu bài Mức 4 có đường suy luận đủ rõ.
- với câu Đúng/Sai nhập từ PDF, lời giải phải có kết luận rõ và giải thích đủ từng ý; không chấp nhận các dòng `a.`, `b.`, `c.`, `d.` trống.
- khi PDF tự mâu thuẫn giữa đề, bảng đáp án và hướng dẫn, được phép hiệu chỉnh sau khi tính lại chắc chắn nhưng phải ghi `Đối chiếu nguồn`, không sửa âm thầm.
- văn phong lời giải ưu tiên nhịp của corpus PDF: **Đáp án/Kết luận → Hướng dẫn giải → Ta có/Suy ra/Thay số → Vậy**; độ dài tăng theo độ khó thực của bài, không theo nhãn mức độ một cách máy móc.

**Bài 1 là mẫu trực quan để đối chiếu, nhưng chuẩn này áp dụng cho toàn bộ Vật lí 11. Không được quay lại format cũ khi bổ sung bài mới.**

## 9. Cách xử lý khi người dùng yêu cầu sửa repository

1. Xác định MODE: CREATE / EXPAND / CONTINUE / UPDATE / AUDIT.
2. Nếu repo đã tồn tại, không thiết kế repo mới.
3. Đọc file này trước.
4. Đọc cây thư mục và đúng file liên quan.
5. Với nội dung dựa vào PDF, tìm đúng phần trong PDF trước khi viết.
6. Thực hiện patch nhỏ nhất đáp ứng yêu cầu.
7. Rà soát logic học thuật + Markdown + navigation + links.
8. Chỉ sau khi kiểm tra mới đóng gói bản mới.

## 10. Quy tắc đóng gói ZIP

File ZIP bàn giao cho người dùng phải đặt theo mẫu:

```text
education-hub-vN.zip
```

Trong đó `N` là số phiên bản tăng dần.

Ví dụ:

```text
education-hub-v10.zip
education-hub-v11.zip
education-hub-v12.zip
```

- Không dùng hậu tố dài kiểu `-bai-1-fixed`, `-final`, `-new`, `-fixed2` nếu người dùng không yêu cầu.
- Bản tiếp theo phải tăng số version, không ghi đè tên version cũ.
- ZIP phải chứa nội dung repository ở root của archive, không bọc thêm một thư mục cha không cần thiết.

## 11. Quy trình GitHub Codespaces khi bàn giao bản ZIP mới

Mỗi lần AI/maintainer bàn giao một bản `education-hub-vN.zip`, phải gửi kèm cho người dùng **một khối lệnh duy nhất** để copy-paste trong GitHub Codespaces. Không chia quy trình thành nhiều code block nếu người dùng không yêu cầu.

**Không được bắt người dùng sửa tên ZIP/version thủ công trong lệnh.** Khối lệnh phải tự xác định file `education-hub-vN.zip` có version lớn nhất đang có trên `origin/main`, đồng bộ file đó về Codespaces, giải nén vào repository hiện tại, rồi **xóa chính file ZIP vừa giải nén** trước khi commit/push.

Quy trình bắt buộc:

1. kiểm tra repository và trạng thái working tree;
2. `git fetch origin`;
3. chuyển về nhánh `main`;
4. `git pull --rebase origin main` để nhận các file người dùng vừa upload trực tiếp lên GitHub;
5. tự tìm ZIP mới nhất theo mẫu `education-hub-v[0-9]+.zip` bằng version sort, không hard-code `vN`;
6. nếu ZIP tồn tại trên `origin/main` nhưng chưa xuất hiện trong working tree, lấy đúng file đó từ `origin/main`;
7. kiểm tra tính toàn vẹn ZIP và chặn archive có đường dẫn nguy hiểm hoặc chứa `.git/`;
8. giải nén ZIP vào root repository bằng `unzip -o`;
9. xóa file ZIP vừa giải nén bằng `rm -f -- "$ZIP"` để ZIP không lưu lại trên nhánh `main` sau lần push kế tiếp;
10. cài/đồng bộ dependency;
11. chạy các checker và `mkdocs build --strict`;
12. `git add -A`, commit nếu có thay đổi và `git push origin main`.

### 11.1. Lỗi thường gặp: đã upload ZIP lên `main` nhưng Codespaces báo không tìm thấy file

Nguyên nhân phổ biến là workspace Codespaces chưa đồng bộ với remote. **Không kết luận file không tồn tại trước khi chạy `git fetch`, `git pull` và kiểm tra trực tiếp cây file của `origin/main`.**

Khối lệnh chuẩn bên dưới lấy tên ZIP trực tiếp từ `origin/main`, nên không phụ thuộc việc người dùng nhớ tên version mới nhất. Nếu file có trên remote nhưng chưa có ở working tree, lệnh sẽ dùng `git checkout origin/main -- "$ZIP"` để lấy riêng đúng file đó.

Không dùng `git reset --hard`, `git push --force` hoặc `git push -f` làm quy trình mặc định. Nếu working tree đang có thay đổi chưa commit, quy trình phải dừng để tránh ghi đè dữ liệu cục bộ.

### 11.2. Mẫu khối lệnh bắt buộc khi bàn giao

Đây là mẫu mặc định. **Không thay `vN` bằng tay và không yêu cầu người dùng tự sửa tên ZIP.**

```bash
set -euo pipefail

printf '\n== Repository ==\n'
pwd
git branch --show-current
git status --short

# Không tự ghi đè thay đổi local chưa commit.
if ! git diff --quiet || ! git diff --cached --quiet || [ -n "$(git ls-files --others --exclude-standard)" ]; then
  echo "ERROR: Working tree đang có thay đổi chưa commit. Hãy commit/stash các thay đổi này trước rồi chạy lại."
  git status
  exit 1
fi

printf '\n== Đồng bộ nhánh main với GitHub ==\n'
git fetch origin
git switch main
git pull --rebase origin main

printf '\n== Xác định ZIP Education Hub mới nhất ==\n'
ZIP="$(git ls-tree -r --name-only origin/main \
  | grep -E '^education-hub-v[0-9]+\.zip$' \
  | sort -V \
  | tail -n 1 || true)"

# Fallback: nếu ZIP chưa được track trên origin/main nhưng đang có ở root working tree.
if [ -z "$ZIP" ]; then
  ZIP="$(find . -maxdepth 1 -type f -name 'education-hub-v*.zip' -printf '%f\n' \
    | grep -E '^education-hub-v[0-9]+\.zip$' \
    | sort -V \
    | tail -n 1 || true)"
fi

if [ -z "$ZIP" ]; then
  echo "ERROR: Không tìm thấy education-hub-vN.zip trên origin/main hoặc ở root repository."
  echo "Các ZIP đang có trên origin/main:"
  git ls-tree -r --name-only origin/main | grep -Ei '\.zip$' || true
  exit 1
fi

echo "ZIP mới nhất: $ZIP"

# Nếu remote có ZIP nhưng working tree chưa có thì lấy riêng file đó.
if [ ! -f "$ZIP" ]; then
  git checkout origin/main -- "$ZIP"
fi

printf '\n== Kiểm tra và giải nén ==\n'
ls -lh "$ZIP"
unzip -t "$ZIP"

# Chặn path traversal/absolute path và không cho archive ghi vào .git.
if unzip -Z1 "$ZIP" | grep -Eq '(^/|(^|/)\.\.(/|$)|^\.git(/|$))'; then
  echo "ERROR: ZIP chứa đường dẫn không an toàn hoặc chứa .git/."
  exit 1
fi

unzip -o "$ZIP" -d .

printf '\n== Xóa ZIP sau khi giải nén ==\n'
rm -f -- "$ZIP"
echo "Đã xóa: $ZIP"

printf '\n== Cài dependency và kiểm tra repository ==\n'
python -m pip install -r requirements.txt
python tools/check_practice_bank.py
python tools/check_pdf_import.py
python tools/check_solution_quality.py
python tools/check_site.py
mkdocs build --strict

printf '\n== Commit và push ==\n'
git status
git add -A

if git diff --cached --quiet; then
  echo "Không có thay đổi mới để commit."
else
  VERSION="${ZIP%.zip}"
  git commit -m "Update ${VERSION}"
fi

git push origin main

printf '\n== Hoàn tất ==\n'
git status
```

Nếu lệnh dừng vì working tree đang có thay đổi, **không được hướng dẫn người dùng xóa chúng bằng `reset --hard`**. Hãy kiểm tra `git status`; sau đó commit hoặc `git stash -u` nếu người dùng muốn giữ thay đổi, rồi mới chạy lại khối lệnh.

Khi gửi lệnh cho người dùng, ưu tiên nguyên khối lệnh trên. Chỉ thay đổi mẫu khi repository thực tế đã thay đổi workflow hoặc tên file chuẩn.


## 12. Nguyên tắc học thuật cốt lõi

Thứ tự ưu tiên:

**Chính xác → Mạch lạc → Đầy đủ → Dependency đúng → Dễ học → Dễ bảo trì**

Không được:

- bịa định nghĩa, công thức, định lý hoặc thuật ngữ;
- bịa tài liệu tham khảo;
- bịa đáp án;
- tự tạo "dạng bài chuẩn" rồi trình bày như phân loại chính thức;
- thêm kiến thức nâng cao vào phần nền mà không phân tầng;
- rút gọn quá mức làm mất bản chất hoặc mất cách suy luận mà nguồn muốn dạy.


## 13. Các lưu ý bắt buộc đã thống nhất với chủ repository

Phần này tổng hợp các yêu cầu làm việc mà chủ repository đã nhắc qua nhiều phiên. Đây là **quy tắc dự án**, không phải gợi ý tùy chọn. Nếu có xung đột với cách làm tự động cũ, ưu tiên các quy tắc dưới đây trừ khi người dùng yêu cầu khác trong phiên hiện tại.

### 13.1. Trung thành với PDF nguồn

- Khi người dùng yêu cầu thêm/mở rộng Vật lí 11 dựa trên PDF đã cung cấp, PDF là **nguồn nội dung chính**.
- Không rút gọn lý thuyết, ví dụ, đề bài, dữ kiện, phương án, lời giải hoặc các bước suy luận chỉ để trang ngắn hơn.
- Không tự ý đổi số liệu, điều kiện, đáp án, cấp độ khó, ý tưởng kiểm tra hoặc văn phong ra đề.
- Khi cần chuẩn hóa cách trình bày, chỉ sửa Markdown/LaTeX, xuống dòng, ký hiệu, đơn vị, dấu câu và bố cục để dễ đọc; không đổi bản chất nội dung.
- Nếu đề nguồn thật sự thiếu logic/thiếu dữ kiện, có thể biên soạn lại **tối thiểu** để bài có nghĩa, nhưng phải giữ cùng ý tưởng, mức độ khó, mô hình dữ kiện và văn phong của bộ PDF.
- Nếu text extract từ PDF bị lỗi, thiếu công thức, thiếu hình hoặc dính cột, phải kiểm tra **ảnh trang PDF gốc** trước khi kết luận. Không đoán từ text parse hỏng.
- Không dùng kiến thức ngoài PDF để âm thầm lấp chỗ trống. Nếu cần kiến thức ngoài nguồn để kiểm chứng, phải phân biệt rõ phần kiểm chứng với nội dung lấy từ PDF.

### 13.2. Chuẩn hiển thị toàn bộ bài tập Vật lí 11

- **Bài 1 là mẫu giao diện/structure trực quan; chuẩn này áp dụng cho tất cả 61 bộ bài tập theo từng bài.**
- Nhãn hiển thị phải là `Bài N`, đánh số liên tục trong từng bộ; tuyệt đối không quay lại `Bài PDF N` hoặc số câu PDF làm nhãn chính.
- Đề bài và phương án phải tách dòng rõ, không dính liền thành một đoạn dài.
- Mỗi bài phải có khối `??? success "Đáp án và lời giải"` riêng; đáp án/lời giải không được trộn vào phần đề.
- Không để ảnh đề chứa sẵn phương án được tô/chọn, đáp án, hướng dẫn giải hay lời giải nếu các phần đó có thể tách khỏi hình.
- Khi cần hình, chỉ crop đồ thị/sơ đồ/bảng/hình minh họa thật sự cần thiết; crop càng chặt càng tốt nhưng không được mất trục, số liệu, ký hiệu hoặc chú thích quan trọng.
- Hạn chế tối đa logo, watermark và dòng chữ nguồn trong crop. Nếu watermark nằm đè trực tiếp lên dữ kiện không thể tránh được, giữ vùng tối thiểu cần thiết; **không tạo ảnh mới, không redraw và không vẽ đè để che nguồn**.

### 13.3. Rà soát đáp án và lời giải — áp dụng từ v15 trở đi

Khi người dùng yêu cầu kiểm tra chất lượng đáp án/lời giải, phải rà soát học thuật chứ không chỉ chạy checker cú pháp.

Đối với từng bài cần kiểm tra tối thiểu:

1. đáp án cuối có khớp dữ kiện và đơn vị không;
2. công thức dùng có đúng điều kiện áp dụng không;
3. dấu, chiều vectơ, pha, quy ước, đổi đơn vị và làm tròn có đúng không;
4. các bước trong lời giải có tự mâu thuẫn không;
5. lời giải có đủ để người học hiểu vì sao chọn phương pháp không;
6. với trắc nghiệm, kết quả tính có đúng với phương án được chọn không;
7. với Đúng/Sai, từng mệnh đề phải được giải thích riêng nếu cần;
8. với bài dựa trên đồ thị/hình, phải đối chiếu trực tiếp hình PDF nếu text parse không đủ tin cậy.

Mức độ chi tiết của lời giải phải theo độ khó:

- **Nhận biết:** nêu căn cứ/công thức chính và kết luận; không cần kéo dài giả tạo.
- **Thông hiểu:** chỉ rõ quan hệ vật lí, công thức, thay số và kết luận.
- **Vận dụng:** chia bước hợp lý, giải thích lựa chọn công thức/phương pháp, theo dõi đơn vị và điều kiện.
- **Vận dụng cao/bài khó:** giải chi tiết theo từng bước; giải thích chiến lược, biến đổi trung gian quan trọng, điều kiện, kiểm tra kết quả và kết luận rõ ràng.

Phong cách lời giải sau khi chỉnh phải **giữ văn phong của các PDF nguồn**: trực tiếp, theo bước, ưu tiên công thức và lập luận vật lí; chỉ làm rõ hơn cho người học, không biến thành một văn phong hoàn toàn khác.

Nếu phát hiện đáp án hoặc lời giải trong PDF nguồn sai:

- được phép sửa khi đã có đủ căn cứ kiểm chứng;
- phải sửa cả đáp án và lời giải cho nhất quán;
- phải ghi rõ trong phần lời giải rằng **đáp án/lời giải nguồn có sai lệch và đã được hiệu chỉnh**, không âm thầm thay đổi;
- không đổi đề nếu không cần; ưu tiên sửa đúng điểm sai nhỏ nhất;
- nếu chưa đủ chắc chắn, đánh dấu cần kiểm tra thay vì đoán.

### 13.4. Không làm mất dấu vết quyết định dự án

- Các quyết định ổn định do chủ repository nhắc lại nhiều lần phải được ghi vào `tools/AI-INSTRUCTIONS.md` để phiên AI/maintainer sau đọc được.
- Khi có một quy tắc lâu dài mới được người dùng xác nhận, hãy cập nhật file này trong bản source kế tiếp thay vì chỉ ghi nhớ trong hội thoại.
- Khi bàn giao source mới, không xóa các quy tắc cũ trừ khi người dùng yêu cầu rõ ràng thay đổi chúng.
- Nếu người dùng nói `tiếp tục`, tiếp tục đúng phần đang làm dở và trạng thái `Next`; không quay lại khởi tạo hoặc làm lại từ đầu.

### 13.5. Quy trình Codespaces là một khối lệnh duy nhất

- Mỗi bản ZIP bàn giao phải kèm **một code block duy nhất** cho Codespaces.
- Khối lệnh phải tự tìm `education-hub-vN.zip` có version lớn nhất; không bắt người dùng sửa tên/version thủ công.
- Phải `git fetch` + `git pull --rebase origin main` trước khi tìm ZIP để xử lý trường hợp người dùng upload file trực tiếp lên nhánh `main` nhưng Codespaces chưa thấy.
- Sau khi kiểm tra archive, phải `unzip -o` vào root repo rồi **xóa chính ZIP vừa giải nén**.
- Sau đó chạy checker/build, `git add -A`, commit nếu có thay đổi và `git push origin main`.
- Không dùng `git reset --hard`, `git push --force` hoặc `git push -f` làm hướng dẫn mặc định.

---

**Handoff rule:** Khi repository này được gửi lại trong một phiên ChatGPT mới, hãy coi `tools/AI-INSTRUCTIONS.md` là tài liệu điều phối dự án và đọc nó trước khi đề xuất hoặc thực hiện thay đổi.
