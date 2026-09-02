---
title: "Bài 2 — Định luật Coulomb"
description: "Lực tương tác giữa các điện tích điểm trong chân không và điện môi, phương–chiều và bài toán tổng hợp lực."
order: 2
difficulty: "standard"
prerequisites:
  - electron-theory-charge-conservation
tags:
  - physics
  - grade-11
  - electric-field
  - coulomb
---

# Bài 2 — Định luật Coulomb

## Mục tiêu

Bạn cần:

- nhận biết khi nào có thể dùng mô hình điện tích điểm;
- tính lực Coulomb trong chân không và điện môi;
- xác định phương, chiều lực;
- dùng nguyên lí chồng chất để tổng hợp lực;
- xử lí bài cân bằng điện tích trên đường thẳng và hình học đơn giản;
- hiểu giới hạn của mô hình.

## 1. Điện tích điểm

Điện tích điểm là mô hình trong đó kích thước vật mang điện nhỏ so với khoảng cách đang xét hoặc phân bố điện có thể được thay thế bằng điện tích tập trung tại một điểm trong điều kiện đối xứng phù hợp.

Không phải mọi vật tích điện đều có thể tùy ý xem là điện tích điểm.

## 2. Định luật Coulomb trong chân không

Hai điện tích điểm $q_1,q_2$ cách nhau $r$ trong chân không tương tác bằng lực có độ lớn:

$$
\boxed{F=k\frac{|q_1q_2|}{r^2}},
$$

với:

$$
k=\frac{1}{4\pi\varepsilon_0}\approx8,99\times10^9\ \text{N·m}^2/\text{C}^2.
$$

Trong bài phổ thông thường dùng $k\approx9\times10^9$.

## 3. Phương và chiều

Lực Coulomb nằm trên đường thẳng nối hai điện tích.

- cùng dấu → đẩy;
- trái dấu → hút.

Hai lực $\vec F_{12}$ và $\vec F_{21}$ là cặp lực trực đối theo định luật III Newton:

$$
\vec F_{12}=-\vec F_{21}.
$$

!!! warning "Không gọi là hai lực cân bằng"
    Hai lực này tác dụng lên **hai vật khác nhau**, nên không phải hai lực cân bằng tác dụng lên cùng một vật.

## 4. Trong điện môi đồng tính

Nếu môi trường được mô hình bởi hằng số điện môi tương đối $\varepsilon_r$:

$$
\boxed{F=\frac{k|q_1q_2|}{\varepsilon_r r^2}}.
$$

Trong chân không $\varepsilon_r=1$. Với không khí ở điều kiện thường, nhiều bài phổ thông lấy gần bằng 1.

## 5. Quy luật tỉ lệ

Từ $F\propto|q_1q_2|/r^2$:

- một điện tích tăng 2 lần → lực tăng 2 lần;
- cả hai tăng 2 lần → lực tăng 4 lần;
- khoảng cách tăng 2 lần → lực giảm 4 lần;
- khoảng cách giảm 3 lần → lực tăng 9 lần.

Nếu đồng thời đổi nhiều yếu tố, nên viết tỉ số:

$$
\frac{F_2}{F_1}
=
\frac{|q_1'q_2'|}{|q_1q_2|}
\frac{r_1^2}{r_2^2}
\frac{\varepsilon_{r1}}{\varepsilon_{r2}}.
$$

## 6. Nguyên lí chồng chất lực điện

Nếu điện tích $q$ chịu tác dụng của nhiều điện tích khác:

$$
\boxed{\vec F=\vec F_1+\vec F_2+\cdots}.
$$

Quy trình:

1. xác định từng lực riêng;
2. vẽ phương và chiều;
3. tính độ lớn;
4. cộng vectơ.

### Hai lực vuông góc
$F=\sqrt{F_1^2+F_2^2}$.

### Hai lực cùng phương
Phải xét chiều rồi cộng đại số.

### Hai lực hợp góc α
$$
F=\sqrt{F_1^2+F_2^2+2F_1F_2\cos\alpha}.
$$

## 7. Cân bằng của một điện tích

Điện tích $q_0$ cân bằng khi:

$$
\vec F_1+\vec F_2+\cdots=\vec0.
$$

Với chỉ hai lực, chúng phải:

- cùng giá;
- ngược chiều;
- bằng độ lớn.

Đây là điều kiện hình học rất mạnh để xác định vị trí.

## 8. Cân bằng trên đường nối hai điện tích

Cho $q_1,q_2$ cố định và tìm vị trí đặt $q_0$ để lực tổng bằng 0.

Vì $\vec F=q_0\vec E$, vị trí cân bằng không phụ thuộc độ lớn $q_0$ nếu $q_0\ne0$; có thể giải trực tiếp bằng cân bằng cường độ điện trường.

### Hai điện tích cùng dấu
Điểm triệt tiêu nằm **giữa** hai điện tích, gần điện tích có độ lớn nhỏ hơn.

### Hai điện tích trái dấu
Trong đoạn giữa, hai vectơ điện trường cùng chiều nên không triệt tiêu. Điểm triệt tiêu nếu tồn tại nằm ngoài đoạn, về phía điện tích có độ lớn nhỏ hơn.

## 9. Ví dụ

### Ví dụ 1
$q_1=2\,\mu$C, $q_2=-3\,\mu$C, $r=0,10$ m trong chân không.

$$
F=9\times10^9\frac{2\times10^{-6}\cdot3\times10^{-6}}{0,10^2}
=5,4\ \text{N}.
$$

Hai điện tích trái dấu nên hút nhau.

### Ví dụ 2 — Thay đổi khoảng cách
Giữ điện tích không đổi, $r$ giảm từ $r$ xuống $r/3$. Lực tăng 9 lần.

### Ví dụ 3 — Hai lực vuông góc
Điện tích q chịu hai lực 3 N và 4 N vuông góc. Hợp lực 5 N.

## 10. Đơn vị và kiểm tra kết quả

- điện tích phải đổi về C;
- khoảng cách đổi về m;
- lực ra N.

Nếu dùng $\mu$C và cm mà không đổi, sai thường rất lớn.

## 11. Giới hạn mô hình

Định luật Coulomb dạng đơn giản trên dùng cho điện tích điểm đứng yên trong mô hình tĩnh điện và môi trường đồng nhất phù hợp. Với vật dẫn lớn, phân bố điện tích biến đổi do cảm ứng, việc lấy điện tích tập trung tại tâm có thể không đúng.

## Tóm tắt

- $F=k|q_1q_2|/(\varepsilon_r r^2)$.
- Lực nằm trên đường nối hai điện tích.
- Cùng dấu đẩy, trái dấu hút.
- Nhiều điện tích: cộng vectơ lực.
- Cân bằng: tổng vectơ lực bằng 0.

## 5 điều cần nhớ

1. Dùng trị tuyệt đối trong công thức độ lớn.
2. Dấu điện tích dùng để xác định chiều.
3. $r$ phải là khoảng cách giữa hai điện tích.
4. Lực Coulomb tỉ lệ nghịch bình phương khoảng cách.
5. Vẽ vectơ trước khi bấm máy.

---

[← Bài 1](01-electron-theory-charge-conservation.md) | [↑ Chương](index.md) | [Bài 3 →](03-electric-field-intensity.md)
