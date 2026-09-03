---
title: "Bài 3 — Nguồn điện, suất điện động và điện trở trong"
description: "Vai trò của nguồn, lực lạ, suất điện động, điện trở trong và hiệu điện thế hai cực."
order: 3
difficulty: "standard"
prerequisites:
  - resistance-ohm-law
tags:
  - physics
  - grade-11
  - circuits
  - source
---

# Bài 3 — Nguồn điện, suất điện động và điện trở trong

## Mục tiêu

Bạn cần:

- hiểu nguồn điện duy trì chênh lệch điện thế;
- định nghĩa suất điện động;
- phân biệt suất điện động và hiệu điện thế cực;
- hiểu điện trở trong;
- viết $U=\mathcal E-Ir$ khi nguồn phát điện;
- nhận biết trường hợp nạp nguồn;
- tính công của nguồn.

## 1. Vai trò của nguồn

Trong mạch kín có điện trở, năng lượng điện chuyển thành các dạng khác. Nếu không có nguồn, chênh lệch điện thế không được duy trì lâu dài.

Nguồn điện dùng các quá trình không thuần tĩnh điện để đưa điện tích “ngược chiều tự nhiên” bên trong nguồn, duy trì hai cực có điện thế khác nhau.

Các lực thực hiện công đó thường được gọi chung là **lực lạ**.

## 2. Suất điện động

Suất điện động $\mathcal E$ của nguồn:

$$
\boxed{\mathcal E=\frac{A_{\text{nguồn}}}{q}}.
$$

Trong đó $A_{\text{nguồn}}$ là công của lực lạ khi dịch chuyển điện tích q bên trong nguồn.

Đơn vị: volt (V).

### Ý nghĩa năng lượng

Mỗi coulomb điện tích đi qua nguồn nhận năng lượng $\mathcal E$ joule từ quá trình chuyển hóa bên trong nguồn, trong mô hình lí tưởng.

## 3. Điện trở trong

Nguồn thực có điện trở trong r. Khi dòng chạy qua nguồn, một phần năng lượng bị tiêu hao bên trong:

$$
P_{\text{trong}}=I^2r.
$$

Do đó hiệu điện thế hai cực có thể khác suất điện động.

## 4. Nguồn đang phát điện

Mạch ngoài R nối với nguồn $(\mathcal E,r)$, dòng đi ra cực dương ở mạch ngoài.

Định luật toàn mạch sẽ cho:

$$
I=\frac{\mathcal E}{R+r}.
$$

Hiệu điện thế hai cực:

$$
\boxed{U=\mathcal E-Ir}.
$$

Cũng bằng $IR$ nếu mạch ngoài chỉ có R.

Khi I=0 (mạch hở), U=$\mathcal E$ trong mô hình lí tưởng đo bằng vôn kế có điện trở rất lớn.

## 5. Nguồn đang được nạp

Nếu dòng điện bị ép đi vào cực dương của nguồn, nguồn nhận năng lượng. Với quy ước U theo hai cực phù hợp:

$$
U=\mathcal E+Ir.
$$

Không nên học thuộc dấu tách rời chiều dòng; hãy dùng quy tắc tăng/giảm điện thế khi đi qua nguồn và điện trở.

## 6. Công và công suất nguồn

Trong thời gian t, điện lượng q=It qua nguồn.

Công của nguồn:

$$
\boxed{A_{\text{nguồn}}=\mathcal E It}.
$$

Công suất nguồn:

$$
\boxed{P_{\text{nguồn}}=\mathcal E I}.
$$

Phần hao phí trong nguồn:

$$
P_{\text{hp}}=I^2r.
$$

Công suất mạch ngoài trong trường hợp R:

$$
P_R=I^2R=UI.
$$

## 7. Hiệu suất nguồn trong mạch R

$$
H=\frac{P_R}{P_{\text{nguồn}}}
=\frac{UI}{\mathcal EI}
=\frac{U}{\mathcal E}.
$$

Với $I=\mathcal E/(R+r)$:

$$
\boxed{H=\frac{R}{R+r}}.
$$

Đây là hiệu suất theo mô hình chỉ có R ngoài và r trong.

## 8. Đo suất điện động và điện trở trong

Nếu đo nhiều cặp (I,U) khi thay tải:

$$
U=\mathcal E-rI.
$$

Đồ thị U theo I là đường thẳng:

- tung độ gốc: $\mathcal E$;
- độ dốc: $-r$.

Đây là cách thực nghiệm rất hữu ích.

## 9. Ví dụ

### Ví dụ 1
Nguồn $\mathcal E=12$ V, r=1 Ω, mạch ngoài R=5 Ω.

$I=12/6=2$ A.

$U=\mathcal E-Ir=10$ V.

### Ví dụ 2
Mạch hở: I≈0, U≈$\mathcal E$.

### Ví dụ 3
Nguồn 9 V, dòng 0,5 A. Công suất nguồn 4,5 W.

## 10. Bẫy

!!! warning "Suất điện động không phải lực"
    Dù tên lịch sử có chữ “động”, $\mathcal E$ có đơn vị volt, không phải newton.

!!! warning "U không luôn bằng E"
    Khi nguồn có dòng và r khác 0, điện áp cực thay đổi theo chế độ phát/nạp.

## Tóm tắt

- $\mathcal E=A/q$.
- Nguồn thực có r.
- Phát điện: $U=\mathcal E-Ir$.
- Công suất nguồn: $\mathcal EI$.
- Hao phí trong: $I^2r$.
- Đồ thị U–I có độ dốc -r.

## 5 điều cần nhớ

1. Nguồn chuyển hóa năng lượng khác thành điện năng.
2. $\mathcal E$ đặc trưng năng lượng trên một coulomb.
3. Điện trở trong gây sụt áp khi nguồn phát.
4. Mạch hở giúp đo gần đúng suất điện động.
5. Dấu công thức phải gắn với chiều dòng và quy ước hiệu điện thế.

<!-- V9_SOURCE_TYPES -->

## Các dạng bài được hệ thống hóa từ ngân hàng PDF

Các dạng dưới đây chỉ sử dụng những nhóm bài đã được gọi tên rõ trong các tài liệu bài tập. Phần trình bày được tổ chức lại để người học nhận diện đề, chọn công cụ và tự kiểm tra kết quả; không tạo thêm tên dạng mới.

### Dạng 1 — Tìm công của nguồn điện, thời gian sử dụng và dòng điện qua nguồn

Công của nguồn liên hệ với điện lượng qua nguồn bởi $A_{ng}=\mathcal E q=\mathcal E It$. Khi đề cho dung lượng hoặc thời gian sử dụng, đổi đúng đơn vị rồi dùng quan hệ điện lượng.

Phân biệt công của nguồn với điện năng hữu ích ở mạch ngoài; có điện trở trong thì một phần năng lượng tỏa nhiệt bên trong nguồn.

### Dạng 2 — Tìm suất điện động, điện trở trong và hiệu điện thế hai cực nguồn

Dùng phương trình cực nguồn khi phát điện $U=\mathcal E-Ir$ cùng định luật Ohm toàn mạch. Nếu có nhiều trạng thái tải khác nhau, lập một phương trình cho mỗi trạng thái rồi giải hệ để tìm $\mathcal E$ và $r$.

Đồ thị $U-I$ là đường thẳng có tung độ gốc $\mathcal E$ và độ dốc bằng $-r$, rất hữu ích cho bài thực nghiệm.

<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/03-emf-internal-resistance/exercises.md)
- [Đáp án và lời giải](practice/03-emf-internal-resistance/solutions.md)

---

[← Bài 2](02-resistance-ohm-law.md) | [↑ Chương](index.md) | [Bài 4 →](04-energy-power-joule.md)
