---
title: "Bài 3 — Phản xạ toàn phần"
description: "Điều kiện phản xạ toàn phần, góc giới hạn, sợi quang và bài nhiều mặt phân cách."
order: 3
difficulty: "standard-applied"
prerequisites:
  - refraction
tags:
  - physics
  - grade-11
  - total-internal-reflection
---

# Bài 3 — Phản xạ toàn phần

## Mục tiêu

Bạn cần:

- nêu đủ hai điều kiện phản xạ toàn phần;
- tính góc giới hạn;
- phân biệt phản xạ toàn phần với phản xạ thông thường;
- xử lí lăng kính phản xạ và sợi quang ở mức phổ thông.

## 1. Từ khúc xạ đến phản xạ toàn phần

Xét ánh sáng đi từ môi trường chiết suất lớn $n_1$ sang nhỏ $n_2$.

Snell:

$$
n_1\sin i=n_2\sin r.
$$

Vì $n_1>n_2$, ta có r>i. Khi i tăng, r tăng nhanh hơn. Đến một giá trị i, tia khúc xạ lướt theo mặt phân cách: $r=90^\circ$.

Góc tới đó gọi là **góc giới hạn** $i_c$.

## 2. Góc giới hạn

Đặt $r=90^\circ$:

$$
n_1\sin i_c=n_2.
$$

Do đó:

$$
\boxed{\sin i_c=\frac{n_2}{n_1}},\qquad n_1>n_2.
$$

## 3. Hai điều kiện phản xạ toàn phần

Phải đồng thời có:

1. ánh sáng truyền từ môi trường có chiết suất **lớn sang nhỏ**, $n_1>n_2$;
2. góc tới **lớn hơn góc giới hạn**, $i>i_c$.

Khi $i=i_c$, tia khúc xạ đi sát mặt, chưa gọi là phản xạ toàn phần theo định nghĩa chuẩn.

## 4. Ví dụ — thủy tinh ra không khí

$n_1=1,50$, $n_2=1$:

$$
\begin{gathered}
\sin i_c=\frac1{1,5}=\frac23.\\
i_c\approx41,8^\circ.
\end{gathered}
$$

Nếu góc tới trong thủy tinh là 50°, phản xạ toàn phần xảy ra. Nếu là 30°, vẫn có tia khúc xạ ra không khí.

## 5. Sợi quang

Sợi quang gồm lõi có chiết suất $n_{core}$ lớn hơn lớp vỏ $n_{clad}$. Tia sáng được dẫn trong lõi nhờ nhiều lần phản xạ toàn phần tại biên lõi–vỏ, nếu góc tới đáp ứng điều kiện.

### Ý nghĩa

- truyền tín hiệu với suy hao thấp;
- cách điện tốt;
- băng thông cao trong hệ thông tin quang;
- nội soi y học dùng bó sợi để truyền ánh sáng/hình ảnh trong một số thiết kế.

## 6. Khẩu độ số — mở rộng

Với sợi bậc thang đơn giản trong không khí, khẩu độ số:

$$
NA=\sqrt{n_1^2-n_2^2}
$$

nếu môi trường ngoài gần n=1.

Góc thu nhận cực đại $\theta_{max}$ thỏa:

$$
\sin\theta_{max}=NA.
$$

Phần này là mở rộng; bài nền chỉ cần điều kiện phản xạ toàn phần.

## 7. Lăng kính phản xạ toàn phần

Một lăng kính vuông cân có thể bẻ tia 90° hoặc 180° nhờ phản xạ toàn phần tại mặt nghiêng, nếu góc tới nội bộ lớn hơn góc giới hạn.

Ưu điểm so với gương kim loại trong một số hệ:

- phản xạ cao trong điều kiện toàn phần;
- không cần lớp phủ phản xạ trên mặt đó;
- hình học ổn định.

## 8. Ví dụ nhiều bước

Tia đi từ không khí vào mặt bên của khối thủy tinh n=1,6 rồi tới mặt thủy tinh–không khí bên trong với góc 45°.

Góc giới hạn:

$$
i_c=\arcsin\frac1{1,6}\approx38,7^\circ.
$$

Vì 45° > 38,7°, tại mặt thứ hai xảy ra phản xạ toàn phần.

Điểm quan trọng: góc 45° phải là **góc tới tại chính mặt thứ hai**, không phải góc ngoài ban đầu nếu hình chưa chứng minh chúng bằng nhau.

## 9. Sai lầm thường gặp

!!! danger "Chỉ kiểm tra i>ic"
    Nếu tia đi từ n nhỏ sang n lớn thì không có phản xạ toàn phần, dù bạn cố gán một góc giới hạn tưởng tượng.

!!! warning "Nhầm i=ic với phản xạ toàn phần"
    Tại i=ic, tia khúc xạ vẫn tồn tại theo phương sát mặt phân cách.

!!! warning "Dùng n tuyệt đối sai phía"
    $\sin i_c=n_{nhỏ}/n_{lớn}$, tỉ số phải <1.

## 10. Phương pháp giải

1. Xác định hướng truyền ở mặt đang xét.
2. Gọi môi trường tới n1, môi trường kia n2.
3. Kiểm tra n1>n2.
4. Tính $i_c=\arcsin(n_2/n_1)$.
5. Tìm góc tới i từ hình học.
6. So sánh i với $i_c$.

## Tóm tắt

Phản xạ toàn phần xảy ra khi ánh sáng đi từ môi trường chiết suất lớn sang nhỏ và góc tới lớn hơn góc giới hạn. Góc giới hạn thỏa $\sin i_c=n_2/n_1$. Hiện tượng là nền của dẫn sáng bằng sợi quang và lăng kính phản xạ.

## 5 điều cần nhớ

1. Phải đi từ n lớn sang n nhỏ.
2. $\sin i_c=n_2/n_1$.
3. i>ic mới phản xạ toàn phần.
4. i=ic → tia khúc xạ sát mặt.
5. Sợi quang dựa trên phản xạ toàn phần.


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/03-total-internal-reflection/exercises.md)
- [Đáp án và lời giải](practice/03-total-internal-reflection/solutions.md)

---

[← Bài 2](02-parallel-slab-apparent-depth.md) | [↑ Chương](index.md) | [Bài 4 →](04-prism-dispersion.md)
