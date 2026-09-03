---
title: "Bài 7 — Giao thoa ánh sáng"
description: "Thí nghiệm Young, hiệu đường đi, khoảng vân, vị trí vân sáng–tối và bài toán nhiều bức xạ."
order: 7
difficulty: "standard-applied"
prerequisites:
  - mechanical-interference
  - electromagnetic-waves
tags:
  - physics
  - grade-11
  - waves
  - light-interference
---

# Bài 7 — Giao thoa ánh sáng

## Mục tiêu

Bạn cần:

- hiểu giao thoa ánh sáng là bằng chứng của tính chất sóng;
- sử dụng mô hình hai khe Young;
- tính hiệu đường đi và khoảng vân;
- xác định vị trí vân sáng, vân tối;
- đếm số vân trong một đoạn;
- xử lí hai bức xạ đơn sắc và ánh sáng trắng ở mức phù hợp;
- nhận biết điều kiện gần đúng của công thức.

## 1. Mô hình thí nghiệm Young

Hai khe hẹp $S_1,S_2$ cách nhau $a$ được chiếu bởi ánh sáng kết hợp. Màn quan sát cách mặt phẳng hai khe một khoảng $D$, với $D\gg a$.

Điểm M trên màn có tọa độ ngang $x$ so với vân trung tâm.

Trong gần đúng góc nhỏ:

$$
\boxed{\delta=d_2-d_1\approx\frac{ax}{D}}.
$$

Trong đó $\delta$ là hiệu đường đi từ hai khe đến M.

## 2. Vân sáng

Hai sóng tới M cùng pha khi:

$$
\delta=k\lambda.
$$

Suy ra:

$$
\boxed{x_k=k\frac{\lambda D}{a}=ki}.
$$

Trong đó:

$$
\boxed{i=\frac{\lambda D}{a}}
$$

là **khoảng vân**, tức khoảng cách giữa hai vân sáng liên tiếp hoặc hai vân tối liên tiếp.

## 3. Vân tối

Điều kiện:

$$
\delta=\left(k+\frac12\right)\lambda.
$$

Vị trí:

$$
\boxed{x_{t}=\left(k+\frac12\right)i}.
$$

Vân tối gần vân trung tâm nhất nằm cách $i/2$ về hai phía.

## 4. Ý nghĩa của vân trung tâm

Tại $x=0$, $\delta=0$. Nếu hai khe nhận ánh sáng cùng pha, đây là vân sáng bậc 0.

Vân trung tâm là mốc thuận tiện để đánh số vân.

## 5. Tính bước sóng từ khoảng vân

Nếu biết $i,a,D$:

$$
\boxed{\lambda=\frac{ia}{D}}.
$$

Phải đổi tất cả về đơn vị thống nhất. Với thí nghiệm quang học, $a$ thường ở mm, $D$ ở m, $i$ ở mm; nếu thay trực tiếp không đổi đơn vị rất dễ sai bậc $10^3$.

## 6. Đếm vân trên đoạn đối xứng

Nếu miền quan sát là $[-L,L]$:

### Vân sáng
Tìm số nguyên $k$ thỏa:

$$
|ki|\le L.
$$

### Vân tối
Tìm số nguyên $k$ thỏa:

$$
\left|\left(k+\frac12\right)i\right|\le L.
$$

Không dùng công thức đếm máy móc nếu biên đi qua đúng một vân; hãy xử lí bất phương trình.

## 7. Hai bức xạ đơn sắc

Với $\lambda_1,\lambda_2$, khoảng vân:

$$
i_1=\frac{\lambda_1D}{a},\qquad
i_2=\frac{\lambda_2D}{a}.
$$

Vân sáng của hai bức xạ trùng nhau khi:

$$
k_1\lambda_1=k_2\lambda_2.
$$

Hay:

$$
k_1i_1=k_2i_2.
$$

Bài toán trở thành tìm cặp số nguyên dương nhỏ nhất thỏa tỉ lệ.

### Ví dụ
Nếu $\lambda_2/\lambda_1=3/2$, lần trùng sáng gần nhất ngoài trung tâm có $k_1=3$, $k_2=2$.

## 8. Ánh sáng trắng

Ánh sáng trắng gồm nhiều bước sóng. Tại trung tâm, $\delta=0$ cho mọi $\lambda$, nên vân trung tâm sáng trắng.

Ra xa trung tâm, vị trí cực đại phụ thuộc $\lambda$, nên các màu tách dần. Miền tím có bước sóng ngắn hơn nên khoảng vân nhỏ hơn miền đỏ.

## 9. Khoảng cách giữa hai vân

Nếu hai vân sáng có bậc $k_1,k_2$:

$$
\Delta x=|k_2-k_1|i.
$$

Nếu một sáng, một tối, hãy viết từng tọa độ rồi lấy trị tuyệt đối; cách này an toàn hơn học nhiều công thức phụ.

## 10. Ví dụ

### Ví dụ 1 — Khoảng vân

$a=1$ mm, $D=2$ m, $\lambda=600$ nm.

Đổi về SI:

$$
i=\frac{600\times10^{-9}\cdot2}{10^{-3}}
=1,2\times10^{-3}\ \text{m}=1,2\ \text{mm}.
$$

### Ví dụ 2 — Vị trí vân tối

Với $i=1,2$ mm, vân tối thứ nhất bên phải trung tâm ở $x=i/2=0,6$ mm; vân tối tiếp theo ở $1,8$ mm.

### Ví dụ 3 — Tìm bước sóng

Khoảng cách giữa 6 vân sáng liên tiếp là 5 khoảng vân. Nếu độ dài đo được là 5 mm thì $i=1$ mm, không phải $5/6$ mm.

## 11. Điều kiện áp dụng

Các công thức chuẩn $\delta\approx ax/D$ và $i=\lambda D/a$ dùng trong mô hình Young với:

- hai khe hẹp;
- khoảng cách màn lớn so với khoảng cách hai khe;
- góc quan sát nhỏ;
- ánh sáng kết hợp và điều kiện hình học ổn định.

## 12. Bẫy thường gặp

!!! warning "Số vân và số khoảng"
    $N$ vân liên tiếp tạo $N-1$ khoảng vân.

!!! warning "Bậc vân tối"
    Có nhiều quy ước gọi “vân tối thứ nhất”. Tốt nhất dùng tọa độ $(k+1/2)i$ với $k$ nguyên thay vì phụ thuộc tên gọi.

## Tóm tắt

- Hiệu đường đi $\delta\approx ax/D$.
- Vân sáng: $x=ki$.
- Vân tối: $x=(k+1/2)i$.
- Khoảng vân $i=\lambda D/a$.
- Hai bức xạ trùng vân sáng khi $k_1\lambda_1=k_2\lambda_2$.

## 5 điều cần nhớ

1. Vân trung tâm là sáng nếu hai khe cùng pha.
2. Khoảng vân tỉ lệ $\lambda$ và $D$, nghịch với $a$.
3. Đếm vân bằng bất phương trình là chắc nhất.
4. Đỏ có khoảng vân lớn hơn tím trong cùng bố trí.
5. Giao thoa ánh sáng thể hiện tính chất sóng của ánh sáng.


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/07-light-interference/exercises.md)
- [Đáp án và lời giải](practice/07-light-interference/solutions.md)

---

[← Bài 6](06-electromagnetic-waves.md) | [↑ Chương](index.md) | [Bài 8 →](08-practical-sound-frequency.md)
