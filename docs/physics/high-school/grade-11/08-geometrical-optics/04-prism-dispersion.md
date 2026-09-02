---
title: "Bài 4 — Lăng kính và tán sắc"
description: "Đường truyền qua lăng kính, góc lệch, lệch cực tiểu, phản xạ toàn phần trong lăng kính và tán sắc."
order: 4
difficulty: "standard-advanced"
prerequisites:
  - refraction
  - total-internal-reflection
tags:
  - physics
  - grade-11
  - prism
  - dispersion
---

# Bài 4 — Lăng kính và tán sắc

## Mục tiêu

Bạn cần:

- dùng các quan hệ hình học của lăng kính;
- tính góc lệch qua hai lần khúc xạ;
- hiểu điều kiện lệch cực tiểu;
- giải thích tán sắc ánh sáng trắng;
- liên hệ lăng kính với phản xạ toàn phần.

## 1. Lăng kính

Lăng kính quang học thường là khối trong suốt giới hạn bởi hai mặt phẳng không song song. Góc giữa hai mặt khúc xạ gọi là **góc chiết quang A**.

Tia sáng qua lăng kính trải qua hai lần khúc xạ:

1. môi trường ngoài → lăng kính;
2. lăng kính → môi trường ngoài.

Gọi:

- $i_1$: góc tới mặt 1;
- $r_1$: góc khúc xạ trong lăng kính tại mặt 1;
- $r_2$: góc tới trong lăng kính tại mặt 2;
- $i_2$: góc ló;
- D: góc lệch tổng giữa tia tới kéo dài và tia ló.

## 2. Quan hệ hình học

Trong lăng kính:

$$
\boxed{r_1+r_2=A}.
$$

Góc lệch:

$$
\boxed{D=i_1+i_2-A}.
$$

Nếu lăng kính đặt trong không khí:

$$
\begin{gathered}
\sin i_1=n\sin r_1,\\
n\sin r_2=\sin i_2.
\end{gathered}
$$

Với môi trường ngoài có chiết suất khác 1, dùng Snell đầy đủ.

## 3. Góc lệch cực tiểu

Khi đường truyền đối xứng trong lăng kính:

$$
\begin{gathered}
i_1=i_2=i,\\
r_1=r_2=\frac A2.
\end{gathered}
$$

Khi đó D đạt giá trị cực tiểu $D_{min}$:

$$
D_{min}=2i-A.
$$

Suy ra:

$$
i=\frac{A+D_{min}}2.
$$

Với lăng kính trong không khí:

$$
\boxed{n=\frac{\sin\left(\frac{A+D_{min}}2\right)}{\sin(A/2)}}.
$$

Công thức này được dùng để đo chiết suất bằng lăng kính.

## 4. Ví dụ lệch cực tiểu

Lăng kính A=60°, $D_{min}=40°$:

$$
n=\frac{\sin50^\circ}{\sin30^\circ}
\approx1,532.
$$

## 5. Lăng kính phản xạ toàn phần

Lăng kính vuông cân 45°–45°–90° có thể cho tia tới vuông góc một mặt cạnh. Tia trong lăng kính tới mặt huyền ở góc 45°.

Nếu góc giới hạn của vật liệu nhỏ hơn 45°, xảy ra phản xạ toàn phần. Tia có thể bị đổi hướng 90°.

Đây là lí do lăng kính được dùng trong ống nhòm và một số hệ quang để bẻ/chuyển hướng tia với hiệu suất cao.

## 6. Tán sắc ánh sáng

Chiết suất của vật liệu **phụ thuộc bước sóng**. Với nhiều thủy tinh thông thường trong vùng nhìn thấy:

$$
n_{tím}>n_{đỏ}.
$$

Vì thế ánh sáng tím bị lệch nhiều hơn ánh sáng đỏ khi qua lăng kính.

Ánh sáng trắng gồm nhiều thành phần bước sóng; sau lăng kính, các thành phần đi theo hướng khác nhau, tạo dải màu. Đây là **tán sắc ánh sáng**.

## 7. Tán sắc và khúc xạ khác nhau thế nào?

- **Khúc xạ:** một tia thay đổi hướng vì tốc độ truyền đổi giữa hai môi trường.
- **Tán sắc:** các bước sóng khác nhau khúc xạ khác nhau vì n phụ thuộc $\lambda$.

Một tia đơn sắc vẫn khúc xạ nhưng không tách thành nhiều màu.

## 8. Góc lệch nhỏ — mở rộng

Với lăng kính mỏng A nhỏ và góc tới nhỏ, trong không khí có gần đúng:

$$
\boxed{D\approx(n-1)A}.
$$

Với hai màu:

$$
\Delta D\approx(n_1-n_2)A.
$$

Gần đúng này hữu ích để hiểu độ tán sắc nhưng không thay công thức đầy đủ khi góc lớn.

## 9. Liên hệ với quang phổ

Lăng kính có thể tách ánh sáng thành các thành phần phổ. Trong Chương 2, ta đã học bản chất sóng và quang phổ ở mức mở rộng. Ở đây, lăng kính được nhìn dưới góc độ **quang hình**: mỗi bước sóng có chiết suất khác và do đó có đường tia khác.

## 10. Sai lầm thường gặp

!!! warning "Dùng r1+r2=i1+i2"
    Quan hệ đúng trong lăng kính là $r_1+r_2=A$.

!!! warning "Cực tiểu nghĩa là D=0"
    Góc lệch cực tiểu thường vẫn khác 0; đó là giá trị nhỏ nhất khi thay đổi góc tới.

!!! warning "Màu đỏ lệch nhiều hơn tím"
    Với tán sắc bình thường của thủy tinh, tím có n lớn hơn và lệch nhiều hơn đỏ.

## 11. Phương pháp giải

1. Vẽ hai mặt và pháp tuyến.
2. Ghi $i_1,r_1,r_2,i_2$.
3. Dùng $r_1+r_2=A$.
4. Áp dụng Snell ở từng mặt.
5. Dùng $D=i_1+i_2-A$.
6. Nếu “lệch cực tiểu”, dùng đối xứng ngay.
7. Nếu có nhiều màu, dùng n riêng cho từng màu.

## Tóm tắt

Lăng kính cho hai lần khúc xạ với $r_1+r_2=A$, $D=i_1+i_2-A$. Ở lệch cực tiểu, đường truyền đối xứng. Vì chiết suất phụ thuộc bước sóng, lăng kính tách ánh sáng trắng thành các màu.

## 5 điều cần nhớ

1. $r_1+r_2=A$.
2. $D=i_1+i_2-A$.
3. Lệch cực tiểu: $i_1=i_2$, $r_1=r_2=A/2$.
4. Thủy tinh thường: $n_{tím}>n_{đỏ}$.
5. Tím lệch nhiều hơn đỏ trong tán sắc bình thường.

---

[← Bài 3](03-total-internal-reflection.md) | [↑ Chương](index.md) | [Bài 5 →](05-thin-lenses-image-construction.md)
