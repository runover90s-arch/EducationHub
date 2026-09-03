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
- Nếu một đề có lỗi logic, thiếu dữ kiện, công thức sai hoặc đáp án nguồn sai/chưa được kiểm chứng, được phép hiệu chỉnh **sau khi tự kiểm tra chắc chắn**. Phiên bản sửa vẫn phải giữ phong cách và độ khó gần với nguồn.
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
- Không giữ watermark/text thừa nếu có thể crop bỏ mà không làm mất thông tin của hình.
- Không tạo ảnh AI để thay đồ thị/hình nguồn, trừ khi người dùng chủ động yêu cầu.
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

## 8. Trạng thái bàn giao hiện tại — Bài 1 Dao động điều hòa

Trong bản source ngay trước file hướng dẫn này:

- `Bài 1 — Đại cương về dao động điều hòa` đã được rà soát lại phần bài tập.
- Các bài đang hiển thị **liên tục từ Bài 1 đến Bài 119**.
- Không còn nhãn hiển thị kiểu **`Bài PDF ...`** trong bộ này.
- Các bài có phần **`Đáp án và lời giải`** dạng mở rộng.
- Ảnh minh họa đã được làm lại theo hướng chỉ giữ phần hình/đồ thị có ích, không dùng nguyên ảnh đề + lời giải.
- Một số lỗi nguồn đã được hiệu chỉnh sau khi kiểm tra (ví dụ sai chu kì, li độ, pha hoặc đáp án ở một số câu).

**Không được quay lại format cũ khi bổ sung bài mới.**

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

## 11. Nguyên tắc học thuật cốt lõi

Thứ tự ưu tiên:

**Chính xác → Mạch lạc → Đầy đủ → Dependency đúng → Dễ học → Dễ bảo trì**

Không được:

- bịa định nghĩa, công thức, định lý hoặc thuật ngữ;
- bịa tài liệu tham khảo;
- bịa đáp án;
- tự tạo "dạng bài chuẩn" rồi trình bày như phân loại chính thức;
- thêm kiến thức nâng cao vào phần nền mà không phân tầng;
- rút gọn quá mức làm mất bản chất hoặc mất cách suy luận mà nguồn muốn dạy.

---

**Handoff rule:** Khi repository này được gửi lại trong một phiên ChatGPT mới, hãy coi `tools/AI-INSTRUCTIONS.md` là tài liệu điều phối dự án và đọc nó trước khi đề xuất hoặc thực hiện thay đổi.
