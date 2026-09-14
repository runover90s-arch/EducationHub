# AI Project Instructions — Education Hub

> **Đọc file này trước khi chỉnh sửa repository.**
>
> Đây là ghi chú bàn giao dành cho AI/maintainer để những lần làm việc sau giữ đúng cách tổ chức, cách biên soạn và các quyết định đã thống nhất với chủ repository.

## 0. Trạng thái môi trường hiện tại — ưu tiên cao nhất

- Chủ repository hiện làm việc **100% trên điện thoại Android**.
- **GitHub Codespaces hiện không sử dụng được do quota/budget đã hết và KHÔNG phải workflow hiện hành.** Không hướng dẫn tạo/mở/xóa Codespace, không yêu cầu chạy lệnh trong Codespaces và không coi Codespaces là bước mặc định.
- **Termux là terminal chính** để clone/pull source, giải nén bản `education-hub-vN.zip`, chạy Git, checker, build và push.
- `github.dev` chỉ là lựa chọn phụ cho chỉnh sửa nhanh; GitHub Actions là quality gate/build/deploy từ xa.
- Nếu các mục cũ trong file này có nhắc đến Codespaces, coi chúng là **legacy/fallback không hoạt động**. Chỉ được quay lại Codespaces khi người dùng nói rõ rằng Codespaces đã dùng được trở lại và muốn sử dụng nó.
- Khi bàn giao một ZIP mới, hướng dẫn tiếp theo phải ưu tiên **một khối lệnh Termux copy-paste**, không phải khối lệnh Codespaces.
- Quy tắc ở mục 0 này **ghi đè mọi hướng dẫn Codespaces cũ** nếu có xung đột.

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
- **Không được lấy đáp án nguồn làm bằng chứng duy nhất.** Mọi đáp án phải được kiểm chứng độc lập từ dữ kiện, mô hình, đơn vị, dấu/pha/vectơ và điều kiện áp dụng. Nếu PDF tự mâu thuẫn, chỉ hiệu chỉnh sau khi đã xác minh chắc chắn và bảo toàn dấu vết bằng comment/metadata/report nội bộ; không đưa lịch sử sai lệch nguồn lên trang người học.
- Không bịa thêm đáp án chỉ để hoàn thiện trang.
- Nếu không đủ cơ sở để xác minh, phải đánh dấu vấn đề thay vì đoán.

### Không tạo mục tài liệu tham khảo công khai

- **Không thêm `references.md`, mục "Nguồn", "Tài liệu tham khảo" hoặc danh sách tên PDF lên website/repository public-facing nếu người dùng chưa yêu cầu.**
- Tên nguồn trong file này chỉ phục vụ bàn giao nội bộ cho AI/maintainer.

### Kiểm chứng web bắt buộc cho Chương V–VIII Vật lí 11

- Với `05-current-media/` đến `08-.../` của Vật lí 11, **bắt buộc kiểm chứng bằng nguồn web bên ngoài uy tín** khi audit, cập nhật hoặc mở rộng nội dung học thuật; không chỉ dựa vào trí nhớ mô hình hay corpus PDF hiện có.
- Ưu tiên theo thứ tự: nguồn chính thức/cơ quan đo lường hoặc giáo dục, giáo trình/trường đại học và tài liệu chuyên môn uy tín; các website Vật lí phổ thông có chất lượng như `vatlypt.com` được dùng để đối chiếu thuật ngữ, phạm vi và cách trình bày THPT nhưng **không được là bằng chứng duy nhất cho điểm học thuật quan trọng**.
- Mọi công thức, điều kiện áp dụng, chiều chuyển động hạt tải, dấu điện tích, đáp án và dữ kiện định lượng quan trọng phải được kiểm chéo với nguồn mạnh hơn hoặc tự kiểm chứng vật lí độc lập.
- **Nội dung learner-facing hiện có nếu đúng thì giữ nguyên.** Không tự rút gọn, viết lại hoặc đổi văn phong chỉ vì nguồn web diễn đạt khác. Chỉ patch tối thiểu phần sai, thiếu điều kiện, sai đơn vị hoặc gây hiểu nhầm.
- Khi tích hợp kiến thức mới từ web, chỉ lấy ý/dữ kiện cần thiết sau khi xác minh và diễn đạt lại phù hợp repository; không sao chép nguyên văn dài.
- Không tự tạo mục nguồn/reference learner-facing nếu người dùng chưa yêu cầu. URL/tên nguồn dùng cho kiểm chứng có thể ghi trong report/status nội bộ của `tools/`.

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

### 7.1. Re-audit trạng thái VERIFIED

- Khi người dùng yêu cầu audit/re-audit một practice file, GROUP hoặc chương, **không được dùng trạng thái `VERIFIED` từ lượt trước làm lý do để bỏ qua bài đó**. Nếu bài nằm trong phạm vi audit hiện tại thì phải đọc lại đầy đủ đề/hình/phương án/answer/solution và tự giải kiểm chứng độc lập như một bài mới.
- `FIXED` cũ cũng không phải bằng chứng học thuật; nếu người dùng yêu cầu rà lại toàn phạm vi thì phải kiểm lại sau sửa.
- Chỉ được bỏ qua phần đã hoàn tất khi người dùng nói rõ **chỉ tiếp tục từ một `NEXT` cụ thể và không rà lại phần trước**.
- Nếu re-audit một bài từng `VERIFIED` mà phát hiện lỗi, coi đó là tín hiệu chất lượng: kiểm tra các occurrence cùng công thức/template/OCR trong file hoặc phạm vi liên quan, không chỉ sửa riêng một câu.

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

## 8. Chuẩn hiển thị Vật lí 11 — áp dụng từ v16

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
- khi PDF tự mâu thuẫn giữa đề, bảng đáp án và hướng dẫn, được phép hiệu chỉnh tối thiểu sau khi tính lại chắc chắn; provenance của hiệu chỉnh phải nằm ở comment/metadata/report nội bộ, không hiển thị `Đối chiếu nguồn` trên trang người học.
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

File ZIP bàn giao cho người dùng tiếp tục dùng mẫu:

```text
education-hub-vN.zip
```

### 10.1. Reset version đã được người dùng xác nhận

- Chuỗi checkpoint lịch sử kết thúc tại `education-hub-v60.zip`.
- Theo quyết định của chủ repository ngày 2026-09-12, **chuỗi version hoạt động được reset về `v1` sau checkpoint v60**.
- Checkpoint đầu tiên của chuỗi mới là `education-hub-v1.zip`; các lượt sau tăng `v2`, `v3`, ... **trong chuỗi mới**, không quay lại `v61`.
- Các ZIP lịch sử `v42`–`v60` (và các checkpoint cũ hơn nếu còn) được giữ làm lịch sử nhưng **không được dùng số N của chúng để chọn version kế tiếp**.
- Không ghi đè một checkpoint đã tồn tại trong cùng chuỗi hoạt động.

### 10.2. Marker chuỗi checkpoint

- Mỗi checkpoint thuộc chuỗi reset phải có `tools/checkpoint-series.json`.
- Marker hiện hành dùng schema tối thiểu:

```json
{
  "series": 2,
  "version": 1,
  "reset_after": "education-hub-v60.zip"
}
```

- `series=1` được hiểu là chuỗi legacy trước reset; ZIP legacy không có marker cũng được coi là series 1.
- Khi tạo checkpoint mới, giữ nguyên `series=2` và tăng trường `version` đồng bộ với tên file.
- Khi recovery có đồng thời ZIP legacy `v60` và ZIP reset `v1`, **ZIP có `series` lớn hơn là source of truth**; trong cùng `series`, chọn `version` lớn nhất.
- Không dùng riêng `sort -V | tail -n 1` trên tên file sau reset, vì cách đó sẽ chọn nhầm `v60` legacy thay vì `v1` của series mới.

### 10.3. Cấu trúc archive

- ZIP phải chứa nội dung repository ở root của archive, không bọc thêm thư mục cha.
- Không dùng hậu tố dài kiểu `-final`, `-fixed`, `-new` nếu người dùng không yêu cầu.
- Không chứa `.git/`, `site/`, virtualenv, cache, `__pycache__`, file tạm/render/log hoặc checkpoint ZIP cũ.
- Phải kiểm path traversal/absolute path và chạy `unzip -t` trước khi bàn giao.

## 11. Quy trình Termux khi bàn giao bản ZIP mới

Mỗi lần AI/maintainer bàn giao một bản `education-hub-vN.zip`, phải hướng dẫn người dùng xử lý bằng **Termux trên Android**. Codespaces không phải môi trường hiện hành.

Nguyên tắc:

1. ZIP người dùng tải từ ChatGPT thường nằm trong `~/storage/downloads/` sau khi đã cấp quyền bằng `termux-setup-storage`.
2. Repository làm việc mặc định là `~/EducationHub`.
3. Trước khi ghi đè source, kiểm tra working tree; nếu có thay đổi chưa commit thì dừng, không dùng `git reset --hard`.
4. `git fetch` + `git pull --rebase origin main` trước khi áp dụng ZIP mới.
5. Tự tìm checkpoint thuộc **series mới nhất** bằng `tools/checkpoint-series.json`; trong cùng series chọn version lớn nhất. Không bắt người dùng sửa version thủ công.
6. Kiểm tra ZIP bằng `unzip -t` và chặn archive có path traversal, absolute path hoặc `.git/`.
7. Giải nén vào thư mục tạm rồi copy vào repository; không commit chính file ZIP.
8. Xóa `tools/__pycache__` và không commit `*.pyc`.
9. Chạy checker/build khi dependency trên Termux cho phép; GitHub Actions vẫn là quality gate cuối cùng.
10. Commit và push lên `main`; sau đó kiểm tra tab Actions.
11. Nếu Git báo `Author identity unknown`, cấu hình repo-local `user.name`/`user.email` trước khi commit.

### 11.1. Mẫu khối lệnh Termux mặc định

Khi phù hợp, ưu tiên đưa người dùng **một code block duy nhất** có thể copy-paste. Mẫu hiện hành:

```bash
set -euo pipefail

cd "$HOME/EducationHub"

printf '\n== Kiểm tra repository ==\n'
git status --short
if ! git diff --quiet || ! git diff --cached --quiet || [ -n "$(git ls-files --others --exclude-standard)" ]; then
  echo "ERROR: Repository đang có thay đổi chưa commit. Dừng để tránh ghi đè dữ liệu."
  git status
  exit 1
fi

printf '\n== Đồng bộ main ==\n'
git fetch origin
git switch main
git pull --rebase origin main

printf '\n== Tìm checkpoint thuộc series mới nhất ==\n'
ZIP="$(python - <<'PY_SELECT_ZIP'
from pathlib import Path
import json, re, zipfile

roots = [Path.home() / "storage/downloads", Path.home() / "EducationHub"]
candidates = []
for root in roots:
    if root.exists():
        candidates.extend(root.glob("education-hub-v*.zip"))

best = None
for path in candidates:
    m = re.fullmatch(r"education-hub-v(\d+)\.zip", path.name)
    if not m:
        continue
    legacy_version = int(m.group(1))
    series = 1
    version = legacy_version
    try:
        with zipfile.ZipFile(path) as zf:
            marker = "tools/checkpoint-series.json"
            if marker in zf.namelist():
                meta = json.loads(zf.read(marker).decode("utf-8"))
                series = int(meta["series"])
                version = int(meta["version"])
    except Exception:
        continue
    key = (series, version, path.stat().st_mtime_ns)
    if best is None or key > best[0]:
        best = (key, path)

if best:
    print(best[1])
PY_SELECT_ZIP
)"

if [ -z "${ZIP:-}" ] || [ ! -f "$ZIP" ]; then
  echo "ERROR: Không tìm thấy checkpoint Education Hub hợp lệ."
  exit 1
fi

echo "ZIP: $ZIP"
unzip -t "$ZIP"
if unzip -Z1 "$ZIP" | grep -Eq '(^/|(^|/)\.\.(/|$)|^\.git(/|$))'; then
  echo "ERROR: ZIP chứa đường dẫn không an toàn hoặc chứa .git/."
  exit 1
fi

printf '\n== Áp dụng source mới ==\n'
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
unzip -q "$ZIP" -d "$TMP"
rsync -a --exclude='.git/' "$TMP"/ "$HOME/EducationHub"/
rm -rf tools/__pycache__

touch .gitignore
grep -qxF '__pycache__/' .gitignore || echo '__pycache__/' >> .gitignore
grep -qxF '*.py[cod]' .gitignore || echo '*.py[cod]' >> .gitignore

printf '\n== Git identity ==\n'
git config user.name "runover90s-arch"
git config user.email "266472043+runover90s-arch@users.noreply.github.com"

printf '\n== Thay đổi sẽ commit ==\n'
git add -A
git status --short

if git diff --cached --quiet; then
  echo "Không có thay đổi mới để commit."
else
  VERSION="$(basename "$ZIP" .zip)"
  git commit -m "Update ${VERSION}"
  git push origin main
fi

printf '\n== Hoàn tất ==\n'
git status
```

Nếu lệnh dừng vì working tree có thay đổi, phải xem `git status` và bảo toàn thay đổi đó trước. Không dùng `git reset --hard`, `git push --force` hoặc `git push -f` làm hướng dẫn mặc định.

### 11.2. Codespaces là legacy/fallback, không dùng mặc định

Các workflow Codespaces từ phiên bản cũ chỉ được giữ như lịch sử/fallback. **Không đưa lệnh Codespaces cho người dùng trong trạng thái hiện tại.** Chỉ kích hoạt lại nếu chính người dùng xác nhận Codespaces đã khả dụng trở lại và yêu cầu dùng nó.


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
- Trang learner-facing không hiển thị các đoạn giải thích chung về quy trình import, project/repository, corpus/source hay cách nội bộ tổ chức dữ liệu nếu chúng không phải nội dung học tập. Provenance cần bảo toàn bằng comment/metadata ẩn theo schema hiện hành.
- Nhãn hiển thị phải là `Bài N`, đánh số liên tục trong từng bộ; tuyệt đối không quay lại `Bài PDF N` hoặc số câu PDF làm nhãn chính.
- Với trắc nghiệm bốn lựa chọn, `A.`, `B.`, `C.`, `D.` phải xếp theo hàng dọc; mỗi phương án là một paragraph riêng, có dòng trống giữa các phương án; không dùng bảng hoặc multi-column cho đáp án trên mobile.
- Với câu Đúng/Sai, `a)`, `b)`, `c)`, `d)` phải xếp theo hàng dọc và mỗi ý là một paragraph riêng. Trong lời giải, từng ý cũng phải là paragraph riêng và nêu rõ kết luận Đúng/Sai.
- Thứ tự learner-facing chuẩn là **đề dẫn → hình/đồ thị/sơ đồ dùng chung (nếu có) → phương án hoặc mệnh đề → `Đáp án và lời giải`**. Không đặt hình dữ kiện dùng chung sau các mệnh đề.
- Trong `??? success "Đáp án và lời giải"`, phần **Đáp án/Kết luận** và **Hướng dẫn giải** phải là các paragraph riêng; phải có dòng trống Markdown thực sự giữa chúng và giữa nhãn `Hướng dẫn giải` với nội dung giải tiếp theo.
- Không hiển thị trên trang người học các ghi chú provenance/nội bộ như `Đối chiếu nguồn`, `Đối chiếu nguồn PDF`, `PDF chọn...`, lịch sử source sai, ghi chú repository/corpus/import. Nếu cần bảo toàn provenance, dùng comment HTML ẩn hoặc metadata/report nội bộ theo schema hiện hành.
- Các quy tắc về A/B/C/D, a/b/c/d, thứ tự đề → hình → lựa chọn/mệnh đề → lời giải và paragraph của `Đáp án`/`Hướng dẫn giải` áp dụng cho toàn bộ nội dung Vật lí 11 có cấu trúc tương ứng, không chỉ các trang practice hoặc Bài 1.
- Quality gate phải **fail** các lỗi deterministic tương ứng: ghép A/B/C/D hoặc a/b/c/d trong cùng paragraph, thiếu một marker bắt buộc, lời giải Đúng/Sai thiếu verdict/giải thích theo từng ý, `Đáp án` và `Hướng dẫn giải` dính cùng paragraph, hình local không tồn tại, hoặc hình dữ kiện đứng sau choices/statements. Không hạ threshold cũ, không dùng allowlist hàng loạt và không vô hiệu duplicate/source checker để làm gate xanh.
- Các nghi vấn ngữ nghĩa như câu hỏi quá ngắn, không thấy dữ kiện/hình nhưng có đáp án số chỉ được báo **WARNING** khi checker chưa thể chứng minh lỗi; phải đối chiếu nguồn trước khi sửa dữ kiện.
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

- **Dễ/nhận biết:** căn cứ hoặc công thức chính → áp dụng/thay số → kết luận.
- **Trung bình/thông hiểu:** nêu lí do chọn quan hệ → biến đổi rõ → kết luận.
- **Vận dụng:** dữ kiện → công thức/phương pháp → thay số → đơn vị/điều kiện → kết luận.
- **Khó/vận dụng cao:** phân tích dữ kiện → chiến lược → các bước trung gian → điều kiện/dấu/pha/vectơ → kiểm tra → kết luận và bẫy nếu có.

Phong cách lời giải sau khi chỉnh phải **giữ văn phong của các PDF nguồn**: trực tiếp, theo bước, ưu tiên công thức và lập luận vật lí; chỉ làm rõ hơn cho người học, không biến thành một văn phong hoàn toàn khác.

Nếu phát hiện đáp án hoặc lời giải trong PDF nguồn sai:

- được phép sửa khi đã có đủ căn cứ kiểm chứng độc lập;
- phải sửa cả đáp án và lời giải cho nhất quán;
- không đổi đề nếu không cần; ưu tiên sửa đúng điểm sai nhỏ nhất;
- provenance của hiệu chỉnh phải được giữ bằng comment/metadata/report nội bộ, không bằng ghi chú learner-facing;
- nếu chưa đủ chắc chắn, đánh dấu cần kiểm tra trong lớp nội bộ thay vì đoán.

Với câu trắc nghiệm **một đáp án A–D**:

- sau khi kiểm chứng chắc chắn mà không có phương án đúng, được sửa **tối thiểu một phương án** để có đúng một đáp án;
- không thêm phương án `E`;
- không để lựa chọn kiểu `Không có phương án phù hợp` nếu kết quả vật lí xác định được chắc chắn.

### 13.4. Không làm mất dấu vết quyết định dự án

- Các quyết định ổn định do chủ repository nhắc lại nhiều lần phải được ghi vào `tools/AI-INSTRUCTIONS.md` để phiên AI/maintainer sau đọc được.
- Khi có một quy tắc lâu dài mới được người dùng xác nhận, hãy cập nhật file này trong bản source kế tiếp thay vì chỉ ghi nhớ trong hội thoại.
- Khi bàn giao source mới, không xóa các quy tắc cũ trừ khi người dùng yêu cầu rõ ràng thay đổi chúng.
- Nếu người dùng nói `tiếp tục`, tiếp tục đúng phần đang làm dở và trạng thái `Next`; không quay lại khởi tạo hoặc làm lại từ đầu.


### 13.5. Quy trình Termux là workflow bàn giao hiện hành

- Mỗi bản ZIP bàn giao phải ưu tiên **một code block Termux duy nhất** để người dùng copy-paste khi cần áp dụng source vào repository.
- Không yêu cầu người dùng quay lại Codespaces trong workflow hiện tại.
- Lệnh phải tự tìm checkpoint thuộc **series mới nhất** trong `~/storage/downloads/` hoặc root repo; trong cùng series chọn version lớn nhất, không bắt sửa `vN` bằng tay.
- Phải kiểm tra working tree, đồng bộ `origin/main`, kiểm tra archive, giải nén an toàn, bỏ `__pycache__`, commit và push.
- Phải xử lý trước lỗi Git identity thường gặp trên Termux bằng repo-local `git config user.name` và `git config user.email`.
- Không dùng `git reset --hard`, `git push --force` hoặc `git push -f` làm hướng dẫn mặc định.
- GitHub Actions là quality gate/build/deploy sau khi push.


### 13.6. Provenance khi khử trùng và tách source block PDF

Áp dụng cho Vật lí 11 khi đã đối chiếu trực tiếp PDF và xác minh chắc chắn source bị lặp hoặc một raw extraction block chứa nhiều câu độc lập:

- **Không xuất bản hai bài learner-facing giống nhau chỉ để giữ hai source-id.** Giữ một bài canonical và bảo toàn mỗi ID của lần lặp bằng comment ẩn `<!-- source-alias-id: ... -->` ngay trong block canonical.
- `source-alias-id` phải dùng đúng schema source-id hiện hành, phải unique toàn Grade 11, không được trùng với canonical source-id khác và phải được khai báo trong `tools/v9_import_report.json`.
- Không dùng alias để né duplicate checker: nội dung lặp phải thật sự bị gỡ khỏi learner-facing; `check_pdf_import.py` vẫn kiểm tra duplicate trên các block canonical và kiểm tra mapping alias riêng.
- Nếu **một raw extraction unit đã được xác minh chứa hai câu PDF độc lập**, được phép tách thành hai block canonical mà **không renumber các ID phía sau**. Giữ ID legacy cho câu đầu; với câu con bị dính, dùng đúng `page` + `q` nhìn thấy trên PDF và giữ cùng raw serial của unit bị dính. Ví dụ đã xác minh: `BT-Chuong-IV-p64-q21-213` tách thành `...-q21-213` và `...-q22-213`.
- Mọi split như trên phải được ghi deterministic trong `source_id_migrations` của import report và được checker xác nhận rằng toàn bộ child ID tồn tại.
- Số `Bài N` hiển thị có thể renumber cục bộ để liên tục; **không đổi source-id của các bài phía sau**.
- Khi một lần lặp có lỗi in riêng (ví dụ sai đơn vị) nhưng nội dung thực chất trùng canonical, giữ khác biệt đó trong metadata provenance/report thay vì xuất bản lại cả bài.

Quy tắc này là migration/provenance rule, không phải cơ chế nới quality gate. Không giảm threshold, không bỏ duplicate detection và không cho phép alias trùng/cô lập.

---

**Handoff rule:** Khi repository này được gửi lại trong một phiên ChatGPT mới, hãy coi `tools/AI-INSTRUCTIONS.md` là tài liệu điều phối dự án và đọc nó trước khi đề xuất hoặc thực hiện thay đổi.

## 14. Workflow Android hiện hành — Termux-first, không dùng Codespaces

Chủ repository hiện làm việc hoàn toàn trên Android và **Codespaces đang không khả dụng do quota/budget**. Trạng thái này là một ràng buộc thực tế, không chỉ là sở thích.

- **Termux là môi trường terminal chính** cho Git, giải nén source, checker, build và push.
- `github.dev` có thể dùng cho chỉnh sửa nhanh nhưng không thay thế Termux khi cần terminal.
- GitHub Actions làm quality gate/build/deploy từ xa.
- Không đề xuất mua thêm quota, tăng budget, tạo Codespace mới hoặc quay lại Codespaces trừ khi người dùng chủ động hỏi.
- Không tạo hướng dẫn phụ thuộc Codespaces trong bản source mới.
- Workflow `Validate Education Hub` phải kiểm tra branch/PR bằng đủ: `check_practice_bank.py`, `check_pdf_import.py`, `check_solution_quality.py`, `check_site.py`, và `mkdocs build --strict`.
- Workflow deploy trên `main` cũng phải chạy đủ các checker trên trước khi publish GitHub Pages.
- Khi bàn giao source, ưu tiên workflow: **tải ZIP về Android → Termux áp dụng ZIP vào `~/EducationHub` → commit/push → kiểm tra GitHub Actions**.
- Tài liệu hướng dẫn mobile chính thức nằm tại `MOBILE-DEVELOPMENT.md`; cập nhật file đó nếu workflow/lệnh thay đổi.
- Chỉ thay đổi trạng thái này khi người dùng xác nhận rõ rằng Codespaces đã dùng được trở lại và muốn chuyển về Codespaces.


## 15. Khi người dùng gửi lại source/ZIP trong một phiên ChatGPT mới

Mục tiêu của phần này là tránh trường hợp AI thấy file ZIP nhưng kết luận nhầm rằng "không đọc được" chỉ vì công cụ tìm kiếm nội dung không index archive.

- Khi người dùng đính kèm `education-hub-vN.zip`, phải coi đó là **source dự án có thể đọc và xử lý**, không yêu cầu người dùng tự giải nén trước.
- **Không dùng kết quả `files.search` rỗng hoặc thông báo ZIP không được index làm bằng chứng rằng file không đọc được.** ZIP/binary archive thường không có text index.
- Nếu phiên hiện tại cung cấp đường dẫn file đã mount/sandbox path, dùng **đúng đường dẫn đó** để kiểm tra archive bằng công cụ container (`unzip -l`, `unzip -p`, giải nén vào thư mục tạm khi cần).
- Nếu file chỉ có file reference mà chưa có bytes trong container, dùng Files để **materialize bản `raw_file`** rồi mới xử lý bằng container. Không đoán đường dẫn từ tên file.
- Bước đọc đầu tiên sau khi mở ZIP là tìm và đọc `tools/AI-INSTRUCTIONS.md`; sau đó mới đọc cây thư mục, `README.md`, `mkdocs.yml`, workflow và các file liên quan đến yêu cầu hiện tại.
- Chỉ yêu cầu người dùng upload lại khi file thật sự **không còn trong cuộc trò chuyện/thư viện, materialize thất bại, archive hỏng, hoặc thiếu file cần thiết**. Không yêu cầu upload lại chỉ vì một công cụ semantic search không đọc được ZIP.
- Khi người dùng gửi một source ZIP mới hơn, coi source đó là trạng thái dự án hiện hành để tiếp tục; không tự quay về bản cũ chỉ vì bản cũ từng được đọc ở phiên trước.
- Khi bàn giao lại source, tăng version theo mục 10 và giữ cấu trúc repository ở root archive.
- ZIP bàn giao là **gói trao đổi source**, không phải file nội dung cần giữ trong repository. Khi cập nhật GitHub, phải giải nén/merge nội dung vào repo; không chỉ upload ZIP rồi chờ GitHub tự giải nén.

**Quy tắc chốt:** nếu người dùng nói kiểu “mình gửi file rồi, đọc source này và làm tiếp”, hãy ưu tiên mở chính attachment/source ZIP đó trước; không trả lời rằng không thể đọc file cho đến khi đã thử đúng đường dẫn mount hoặc quy trình materialize `raw_file` nêu trên.
