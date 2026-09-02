---
title: "Bài 1 — Khúc xạ ánh sáng và chiết suất"
description: "Định luật khúc xạ, chiết suất, tính thuận nghịch của đường truyền và cách đọc hình tia sáng."
order: 1
difficulty: "foundation-standard"
tags:
  - physics
  - grade-11
  - refraction
---

# Bài 1 — Khúc xạ ánh sáng và chiết suất

## Mục tiêu

Bạn cần:

- mô tả đúng hiện tượng khúc xạ;
- dùng định luật Snell;
- hiểu chiết suất tuyệt đối và chiết suất tỉ đối;
- dự đoán tia lệch gần hay xa pháp tuyến;
- dùng tính thuận nghịch của đường truyền ánh sáng;
- biết giới hạn của mô hình tia.

## 1. Hiện tượng khúc xạ

Khi tia sáng truyền xiên qua mặt phân cách giữa hai môi trường trong suốt khác nhau, hướng truyền thường thay đổi. Hiện tượng này gọi là **khúc xạ ánh sáng**.

Tại điểm tới O:

- tia tới nằm trong môi trường 1;
- tia khúc xạ đi vào môi trường 2;
- pháp tuyến là đường vuông góc mặt phân cách tại O;
- góc tới i là góc giữa tia tới và pháp tuyến;
- góc khúc xạ r là góc giữa tia khúc xạ và pháp tuyến.

!!! warning "Góc quang học đo với pháp tuyến"
    i và r không đo từ mặt phân cách. Nếu đề cho góc với mặt, phải lấy góc phụ.

## 2. Chiết suất tuyệt đối

Chiết suất của một môi trường đối với chân không:

$$
\boxed{n=\frac cv}
$$

trong đó c là tốc độ ánh sáng trong chân không và v là tốc độ pha của ánh sáng trong môi trường.

Với môi trường vật chất thông thường ở vùng quang học:

$$
n\ge1.
$$

Ví dụ gần đúng:

- không khí: n xấp xỉ 1;
- nước: khoảng 1,33;
- nhiều loại thủy tinh: khoảng 1,5 nhưng phụ thuộc loại và bước sóng.

## 3. Định luật khúc xạ Snell

Với hai môi trường đẳng hướng:

$$
\boxed{n_1\sin i=n_2\sin r}.
$$

Hay:

$$
\frac{\sin i}{\sin r}=\frac{n_2}{n_1}=n_{21}.
$$

$n_{21}$ là chiết suất tỉ đối của môi trường 2 đối với môi trường 1.

## 4. Tia lệch về hay xa pháp tuyến?

Từ Snell:

### Nếu $n_2>n_1$

$$
\sin r<\sin i\Rightarrow r<i
$$

với góc trong miền 0–90°. Tia khúc xạ **lệch về phía pháp tuyến**.

### Nếu $n_2<n_1$

$r>i$: tia **lệch xa pháp tuyến**.

### Tới vuông góc

Nếu i=0 thì r=0. Tia không đổi phương, dù tốc độ và bước sóng trong môi trường có thể đổi.

## 5. Tần số và bước sóng khi khúc xạ

Khi ánh sáng đi qua mặt phân cách ổn định:

- tần số f do nguồn quyết định, **không đổi**;
- tốc độ thay đổi theo n;
- bước sóng thay đổi vì $v=\lambda f$.

Do đó:

$$
\lambda=\frac{v}{f}=\frac{c}{nf}.
$$

Nếu đi vào môi trường có n lớn hơn, v giảm và bước sóng giảm.

## 6. Tính thuận nghịch

Nếu ánh sáng có thể đi từ A qua các mặt quang học tới B theo một đường, thì khi truyền ngược từ B về A trong cùng hệ, nó đi ngược đúng đường đó trong quang hình lí tưởng.

Đây là công cụ rất hữu ích khi vẽ tia và kiểm tra kết quả.

## 7. Ví dụ cơ bản

Tia từ không khí $n_1=1$ tới thủy tinh $n_2=1,50$ với i=30°.

$$
\begin{gathered}
\sin r=\frac{n_1}{n_2}\sin i =\frac1{1,5}\cdot0,5=\frac13.\\
r\approx19,5^\circ.
\end{gathered}
$$

Vì đi vào môi trường chiết suất lớn hơn, r<i, phù hợp dự đoán.

## 8. Ví dụ tìm chiết suất

Từ không khí, i=45°, r=28°:

$$
n\approx\frac{\sin45^\circ}{\sin28^\circ}\approx1,51.
$$

Nếu bài thực nghiệm cho nhiều cặp i-r, nên tính nhiều lần hoặc vẽ quan hệ $\sin i$ theo $\sin r$ để giảm ảnh hưởng sai số ngẫu nhiên.

## 9. Góc lệch của tia tại một mặt

Độ lệch đơn giản giữa phương tia tới kéo dài và tia khúc xạ có độ lớn:

$$
\delta=|i-r|.
$$

Đây không phải góc lệch tổng qua lăng kính; lăng kính có hai lần khúc xạ.

## 10. Mô hình tia có giới hạn

Quang hình bỏ qua rõ rệt các hiệu ứng nhiễu xạ và giao thoa. Khi khe/vật cản có kích thước cỡ bước sóng, cần dùng mô hình sóng đã học ở Chương 2.

Điều này không làm quang hình “sai”; nó chỉ có miền áp dụng. Vật lí khá khoái việc mỗi mô hình có lãnh địa riêng, làm người học phải nghĩ trước khi cắm công thức.

## 11. Phương pháp bài tập

1. Vẽ mặt phân cách và pháp tuyến.
2. Ghi n1 ở phía tia tới, n2 ở phía tia khúc xạ.
3. Đổi góc với mặt thành góc với pháp tuyến nếu cần.
4. Dự đoán r<i hay r>i.
5. Dùng $n_1\sin i=n_2\sin r$.
6. Kiểm tra $0\le\sin r\le1$.

## 12. Bẫy thường gặp

!!! danger "Đổi n1 và n2"
    n1 luôn thuộc môi trường chứa tia tới ở bước đang xét. Khi tia truyền ngược, vai trò n1-n2 đổi.

!!! warning "Tần số đổi khi sang môi trường"
    Trong khúc xạ tại mặt phân cách đứng yên, tần số không đổi; tốc độ và bước sóng đổi.

!!! warning "Sin r lớn hơn 1"
    Nếu tính ra như vậy khi truyền từ n lớn sang n nhỏ, có thể tình huống đã đi vào miền phản xạ toàn phần. Đó là Bài 3.

## Tóm tắt

Khúc xạ tuân theo $n_1\sin i=n_2\sin r$, với $n=c/v$. Tia đi vào môi trường có n lớn hơn sẽ lệch về pháp tuyến. Tần số ánh sáng không đổi qua mặt phân cách; tốc độ và bước sóng thay đổi.

## 5 điều cần nhớ

1. Góc đo với pháp tuyến.
2. $n=c/v$.
3. $n_1\sin i=n_2\sin r$.
4. n tăng → tia gần pháp tuyến hơn.
5. f không đổi khi khúc xạ qua mặt đứng yên.

---

[← Chương](index.md) | [Bài 2 →](02-parallel-slab-apparent-depth.md)
