---
title: "Bài 6 — Phương pháp bài toán thấu kính"
description: "Khoảng cách vật–ảnh, hai vị trí thấu kính, dịch chuyển, tiêu cự, ghép thấu kính và công thức chế tạo."
order: 6
difficulty: "standard-advanced"
prerequisites:
  - thin-lens
tags:
  - physics
  - grade-11
  - lens-problems
---

# Bài 6 — Phương pháp bài toán thấu kính

## Mục tiêu

Bạn cần:

- giải hệ công thức thấu kính và phóng đại một cách có kiểm tra;
- xử lí bài vật–màn cố định;
- hiểu điều kiện có hai vị trí thấu kính cho ảnh rõ;
- dùng phương pháp Bessel;
- giải bài dịch vật/dịch kính bằng quan hệ đại số;
- biết công thức chế tạo thấu kính ở mức mở rộng.

## 1. Bộ công thức lõi

$$
\begin{gathered}
\frac1f=\frac1d+\frac1{d'},\\
k=-\frac{d'}d.
\end{gathered}
$$

Có thể biến đổi:

$$
\begin{gathered}
d'=\frac{fd}{d-f},\\
d=\frac{fd'}{d'-f}.
\end{gathered}
$$

Các dạng biến đổi chỉ nên dùng sau khi đã xác định quy ước dấu.

## 2. Biết k và khoảng cách vật–ảnh

Nếu ảnh thật, vật và ảnh ở hai phía thấu kính:

$$
L=d+d'.
$$

Nếu biết $|k|=d'/d=m$ với ảnh thật:

$$
\begin{gathered}
d'=md,\\
d=\frac{L}{1+m},\qquad d'=\frac{mL}{1+m}.
\end{gathered}
$$

Sau đó:

$$
f=\frac{dd'}{d+d'}.
$$

### Ví dụ

Vật và màn cách nhau L=100 cm, ảnh rõ lớn gấp 4 lần vật.

$d'=4d$, nên 5d=100 → d=20 cm, d'=80 cm.

$$
f=\frac{20\cdot80}{100}=16\,\text{cm}.
$$

## 3. Vật–màn cố định: điều kiện có ảnh thật

Với vật và màn cách nhau L, thấu kính hội tụ đặt giữa chúng:

$$
\begin{gathered}
d+d'=L,\\
dd'=fL.
\end{gathered}
$$

d và d' là nghiệm của:

$$
x^2-Lx+fL=0.
$$

Có nghiệm thực khi:

$$
\Delta=L^2-4fL\ge0.
$$

Vì L>0:

$$
\boxed{L\ge4f}.
$$

- L<4f: không thể có ảnh thật rõ trên màn;
- L=4f: một vị trí duy nhất d=d'=2f;
- L>4f: có hai vị trí thấu kính.

## 4. Hai vị trí thấu kính — phương pháp Bessel

Với L>4f, hai nghiệm d và d' hoán đổi cho nhau. Khoảng cách giữa hai vị trí thấu kính là a:

$$
a=|d'-d|.
$$

Từ

$$
\begin{gathered}
d+d'=L,\\
d'-d=a,
\end{gathered}
$$

suy ra:

$$
d=\frac{L-a}{2},\qquad d'=\frac{L+a}{2}.
$$

Tiêu cự:

$$
\boxed{f=\frac{L^2-a^2}{4L}}.
$$

Đây là phương pháp đo f thực nghiệm khá đẹp vì không cần biết chính xác vị trí quang tâm tuyệt đối ở từng phép đo nhỏ.

## 5. Hai ảnh có độ phóng đại nghịch đảo

Ở hai vị trí Bessel:

$$
\begin{gathered}
|k_1|=\frac{d'}d,\\
|k_2|=\frac d{d'}.
\end{gathered}
$$

Do đó:

$$
|k_1k_2|=1.
$$

Một ảnh phóng đại, ảnh kia thu nhỏ.

## 6. Bài dịch vật hoặc dịch thấu kính

Không cần săn một “công thức thần chú” cho mọi bài. Cách ổn định hơn:

1. viết trạng thái 1: $1/f=1/d_1+1/d_1'$;
2. viết trạng thái 2: $1/f=1/d_2+1/d_2'$;
3. dùng quan hệ dịch chuyển đề cho, ví dụ $d_2=d_1+\Delta$;
4. nếu màn cố định, thêm quan hệ hình học cho d';
5. giải hệ và kiểm tra dấu.

Cách này dài hơn vài dòng nhưng ít tạo ra công thức nhớ nhầm. Bộ não người đã đủ việc phải nhớ rồi.

## 7. Ghép hai thấu kính mỏng sát nhau — mở rộng

Hai thấu kính mỏng sát nhau trong không khí có độ tụ tổng:

$$
\boxed{D=D_1+D_2}.
$$

Do đó:

$$
\frac1f=\frac1{f_1}+\frac1{f_2}.
$$

Nếu cách nhau một khoảng đáng kể, không dùng công thức này trực tiếp; cần truyền ảnh của kính 1 thành vật cho kính 2 hoặc dùng ma trận quang học ở mức cao hơn.

## 8. Công thức chế tạo thấu kính — mở rộng

Với thấu kính mỏng có chiết suất $n_l$ đặt trong môi trường chiết suất $n_m$, dùng bán kính cong có dấu $R_1,R_2$ theo quy ước hình học nhất quán:

$$
\boxed{\frac1f=\left(\frac{n_l}{n_m}-1\right)\left(\frac1{R_1}-\frac1{R_2}\right)}.
$$

Nếu thấu kính trong không khí, $n_m\approx1$.

### Cảnh báo quy ước

Một số tài liệu phổ thông dùng độ lớn bán kính và thay dấu theo hình từng loại thấu kính. Giáo trình này dùng **bán kính đại số** trong công thức trên. Không trộn hai quy ước giữa chừng.

## 9. Bài ảnh qua hai thấu kính cách nhau

Quy trình:

1. kính 1 tạo ảnh A1B1;
2. xác định vị trí A1 so với kính 2;
3. coi A1B1 là vật của kính 2; vật có thể thật hoặc ảo;
4. áp dụng công thức kính 2;
5. số phóng đại tổng:

$$
k=k_1k_2.
$$

Dạng này thuộc Level 4–5 vì yêu cầu kiểm soát dấu tốt.

## 10. Ví dụ Bessel

Vật–màn cách L=90 cm. Có hai vị trí kính cách nhau a=30 cm.

$$
f=\frac{90^2-30^2}{4\cdot90}
=\frac{7200}{360}=20\,\text{cm}.
$$

Hai khoảng:

$$
d=30\,\text{cm},\qquad d'=60\,\text{cm}
$$

hoặc ngược lại.

## 11. Kiểm tra nghiệm vật lí

Sau khi giải, luôn kiểm tra:

- thấu kính hội tụ cho ảnh thật trên màn phải có d>f và d'>0;
- ảnh ảo không thể hứng trực tiếp trên màn;
- nếu L<4f mà vẫn ra hai vị trí thật, đại số hoặc dấu đã sai;
- k phải phù hợp hình dựng.

## 12. Bẫy thường gặp

!!! danger "Dùng L=d+d' cho ảnh ảo"
    Quan hệ đó chỉ là khoảng cách hình học đơn giản cho vật thật–ảnh thật ở hai phía. Ảnh ảo cần xét vị trí có dấu.

!!! warning "Dịch thấu kính bao nhiêu thì ảnh dịch bấy nhiêu"
    Không đúng nói chung. d' phụ thuộc phi tuyến vào d.

!!! warning "Ghép kính cách xa vẫn cộng độ tụ"
    $D=D_1+D_2$ chỉ đúng cho hai thấu kính mỏng sát nhau trong mô hình cơ bản.

## Tóm tắt

Bài thấu kính khó chủ yếu là bài quan hệ hình học và dấu. Với vật–màn cố định, $L\ge4f$ là điều kiện có ảnh thật và phương pháp Bessel cho $f=(L^2-a^2)/(4L)$. Bài dịch chuyển nên lập hai trạng thái thay vì học thuộc hàng loạt công thức rời.

## 5 điều cần nhớ

1. Luôn bắt đầu từ công thức thấu kính và quy ước dấu.
2. Vật–màn ảnh thật: L=d+d'.
3. Có ảnh rõ khi L≥4f.
4. Bessel: $f=(L^2-a^2)/(4L)$.
5. Ghép kính sát: độ tụ cộng.

---

[← Bài 5](05-thin-lenses-image-construction.md) | [↑ Chương](index.md) | [Bài 7 →](07-eye-and-defects.md)
