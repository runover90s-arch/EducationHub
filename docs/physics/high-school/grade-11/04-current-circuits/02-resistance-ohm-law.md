---
title: "Bài 2 — Điện trở và định luật Ohm cho đoạn mạch"
description: "Điện trở, điện trở suất, phụ thuộc nhiệt độ, đặc tuyến V–A và ghép điện trở."
order: 2
difficulty: "standard-applied"
prerequisites:
  - current-intensity
tags:
  - physics
  - grade-11
  - circuits
  - resistance
---

# Bài 2 — Điện trở và định luật Ohm cho đoạn mạch

## Mục tiêu

Bạn cần:

- hiểu điện trở biểu thị mức cản trở dòng điện;
- dùng $R=\rho\ell/S$;
- dùng định luật Ohm $U=IR$ cho phần tử ohmic;
- đọc đặc tuyến V–A;
- ghép nối tiếp, song song;
- xử lí mạch điện trở hỗn hợp;
- hiểu giới hạn của định luật Ohm tuyến tính.

## 1. Điện trở

Điện trở R đặc trưng cho mức cản trở dòng điện của phần tử.

Đơn vị: ohm ($\Omega$).

Với vật dẫn ohmic ở điều kiện không đổi:

$$
\boxed{R=\frac{U}{I}}.
$$

Đây đồng thời là hệ quả của định luật Ohm tuyến tính.

## 2. Định luật Ohm cho đoạn mạch chỉ chứa điện trở

$$
\boxed{I=\frac{U}{R}},
$$

hay $U=IR$.

Điều kiện: phần tử được mô hình là điện trở ohmic và các điều kiện vật lí như nhiệt độ không làm R biến đổi đáng kể trong quá trình xét.

## 3. Điện trở suất

Dây dẫn đồng chất dài $\ell$, tiết diện S:

$$
\boxed{R=\rho\frac{\ell}{S}}.
$$

Trong đó $\rho$ là điện trở suất, đơn vị $\Omega\cdot$m.

Hệ quả:

- dây dài hơn → R lớn hơn;
- tiết diện lớn hơn → R nhỏ hơn;
- vật liệu khác → $\rho$ khác.

## 4. Phụ thuộc nhiệt độ của kim loại

Trong khoảng nhiệt độ phù hợp có thể dùng gần đúng tuyến tính:

$$
\boxed{R=R_0[1+\alpha(T-T_0)]}.
$$

$\alpha$ là hệ số nhiệt điện trở.

Không coi biểu thức tuyến tính là chính xác ở mọi nhiệt độ.

## 5. Đặc tuyến V–A

Nếu vẽ I theo U cho điện trở ohmic R không đổi:

$$
I=\frac{1}{R}U.
$$

Đường thẳng qua gốc, hệ số góc bằng $1/R$ nếu trục tung là I và trục hoành là U.

Nếu vẽ U theo I, hệ số góc là R.

!!! warning "Đọc đúng trục"
    Không được nhìn độ dốc rồi luôn kết luận bằng R. Phải xem trục nào là U, trục nào là I.

## 6. Mắc nối tiếp

Các điện trở nối tiếp có cùng dòng điện.

$$
\boxed{R_{\text{nt}}=R_1+R_2+\cdots}.
$$

Hiệu điện thế chia:

$$
U_i=IR_i.
$$

Do đó trong chuỗi cùng dòng:

$$
\frac{U_1}{U_2}=\frac{R_1}{R_2}.
$$

## 7. Mắc song song

Các điện trở song song có cùng hiệu điện thế.

$$
\boxed{
\frac1{R_{\text{ss}}}
=
\frac1{R_1}+\frac1{R_2}+\cdots
}.
$$

Hai điện trở:

$$
R_{\text{ss}}=\frac{R_1R_2}{R_1+R_2}.
$$

Dòng chia nghịch với điện trở:

$$
\frac{I_1}{I_2}=\frac{R_2}{R_1}.
$$

Điện trở tương đương song song nhỏ hơn điện trở nhánh nhỏ nhất.

## 8. N điện trở giống nhau

Mỗi điện trở R:

- nối tiếp n cái → $R_{eq}=nR$;
- song song n cái → $R_{eq}=R/n$.

## 9. Kĩ thuật nhận dạng mạch

Hai phần tử nối tiếp khi:

- chúng chia sẻ một nút giữa không có nhánh rẽ khác;
- cùng dòng bắt buộc đi qua cả hai.

Hai phần tử song song khi:

- hai đầu của chúng nối vào cùng hai nút.

Hình vẽ thẳng hay cong không quyết định quan hệ điện.

## 10. Mạch đối xứng

Trong một số mạch cầu đối xứng, hai điểm có cùng điện thế. Khi đó nhánh nối giữa chúng có thể không có dòng.

Chỉ được dùng khi chứng minh được đối xứng điện thế, không vì hình vẽ “trông cân”.

## 11. Ví dụ

### Ví dụ 1
Dây cùng vật liệu, chiều dài tăng 2 lần, bán kính giảm 2 lần.

S tỉ lệ $r^2$ nên S giảm 4 lần. R tăng $2/(1/4)=8$ lần.

### Ví dụ 2
$R_1=6\Omega$, $R_2=3\Omega$ song song:

$R_{eq}=2\Omega$.

Nếu U=12 V, tổng I=6 A; $I_1=2$ A, $I_2=4$ A.

## 12. Bẫy

!!! danger "Nối tiếp hình học"
    Hai điện trở nằm cạnh nhau trên hình chưa chắc nối tiếp nếu nút giữa có nhánh rẽ.

!!! warning "Điện trở không phải lúc nào hằng số"
    Bóng đèn sợi đốt thay đổi nhiệt độ mạnh nên đặc tuyến không hoàn toàn tuyến tính; không áp dụng R cố định một cách mù quáng.

## Tóm tắt

- $R=\rho\ell/S$.
- Ohm: $I=U/R$ cho phần tử ohmic.
- Nối tiếp: cùng I, R cộng.
- Song song: cùng U, nghịch đảo R cộng.
- Đọc nút để nhận mạch.

## 5 điều cần nhớ

1. Đổi tiết diện theo bình phương kích thước ngang.
2. Hệ số góc đặc tuyến phụ thuộc cách chọn trục.
3. Song song làm R tương đương giảm.
4. Nối tiếp làm R tương đương tăng.
5. Luôn đánh dấu nút trước khi rút gọn mạch phức tạp.

## Các dạng bài trọng tâm

Các nhóm bài dưới đây được tổ chức theo dấu hiệu nhận biết và công cụ giải để người học chọn phương pháp phù hợp và tự kiểm tra kết quả.

### Dạng 1 — Áp dụng định luật Ohm, xác định điện trở suất

Dùng $U=IR$ và $R=\rho l/S$. Khi thay đổi hình học dây, xét đồng thời chiều dài và tiết diện; nếu dây bị kéo mà thể tích không đổi thì $lS$ không đổi. Với phụ thuộc nhiệt độ, dùng đúng mô hình tuyến tính và mốc nhiệt độ được cho.

Kiểm tra đơn vị điện trở suất và tiết diện trước khi thay số.

### Dạng 2 — Đoạn mạch gồm các điện trở ghép nối tiếp, song song

Nhận dạng các nút điện thế trước, không dựa vào hình vẽ “trông giống” nối tiếp/song song. Nối tiếp: cùng dòng điện và $R_{tđ}=\sum R$; song song: cùng hiệu điện thế và $1/R_{tđ}=\sum1/R$.

Sau khi rút gọn điện trở tương đương, dùng định luật Ohm để tìm dòng tổng rồi quay ngược từng nhánh. Có thể kiểm tra bằng định luật nút: tổng dòng vào bằng tổng dòng ra.

<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/02-resistance-ohm-law/exercises.md)
- [Đáp án và lời giải](practice/02-resistance-ohm-law/solutions.md)

---

[← Bài 1](01-current-intensity.md) | [↑ Chương](index.md) | [Bài 3 →](03-emf-internal-resistance.md)
