---
title: "Bài 2 — Bản mặt song song và độ sâu biểu kiến"
description: "Tia qua bản hai mặt song song, độ dời ngang, độ sâu biểu kiến và bài quang hình."
order: 2
difficulty: "standard-applied"
prerequisites:
  - refraction
tags:
  - physics
  - grade-11
  - parallel-slab
---

# Bài 2 — Bản mặt song song và độ sâu biểu kiến

## Mục tiêu

Bạn cần:

- chứng minh tia ló qua bản mặt song song song song tia tới;
- tính độ dời ngang;
- hiểu vật dưới nước nhìn nông hơn;
- dùng gần đúng độ sâu biểu kiến khi quan sát gần vuông góc;
- xử lí hình học nhiều lớp cơ bản.

## 1. Bản mặt song song

Bản mặt song song là một lớp môi trường trong suốt có hai mặt phẳng biên song song, ví dụ tấm kính phẳng có bề dày e.

Một tia từ môi trường 1 đi vào bản n rồi đi ra lại môi trường 1. Ở mặt thứ nhất:

$$
n_1\sin i=n\sin r.
$$

Ở mặt thứ hai, vì hai pháp tuyến song song, góc tới bên trong bằng r:

$$
n\sin r=n_1\sin i'.
$$

Suy ra $i'=i$. Tia ló **song song tia tới**.

Nhưng hai tia thường không trùng nhau: có một độ dời ngang.

## 2. Độ dời ngang

Với bản dày e, góc tới i, góc khúc xạ r:

$$
\boxed{x=e\frac{\sin(i-r)}{\cos r}}.
$$

### Kiểm tra giới hạn

- i=0 → r=0 → x=0;
- e tăng → x tăng;
- khi n gần n1, i gần r → x nhỏ.

## 3. Ví dụ độ dời

Tấm kính dày 4 cm, n=1,5, tia từ không khí tới i=45°.

Đầu tiên:

$$
\sin r=\frac{\sin45^\circ}{1,5}\Rightarrow r\approx28,1^\circ.
$$

Độ dời:

$$
x=4\frac{\sin(45^\circ-28,1^\circ)}{\cos28,1^\circ}
\approx1,32\,\text{cm}.
$$

## 4. Độ sâu biểu kiến

Một vật ở độ sâu h trong môi trường chiết suất $n_1$, quan sát từ môi trường $n_2$ qua mặt phẳng và theo góc nhỏ gần pháp tuyến.

Độ sâu biểu kiến gần đúng:

$$
\boxed{h'=h\frac{n_2}{n_1}}.
$$

Với vật trong nước nhìn từ không khí:

$$
h'=\frac{h}{n_{nước}}
$$

nếu lấy $n_{không\ khí}\approx1$.

Vì $n_{nước}>1$, $h'<h$: đáy bể trông nông hơn.

!!! note "Đây là gần đúng góc nhỏ"
    Công thức h' đơn giản xuất phát từ $\tan i\approx\sin i\approx i$. Nếu quan sát góc lớn, nên dùng hình học và Snell đầy đủ.

## 5. Suy ra công thức độ sâu gần đúng

Với một tia gần pháp tuyến:

$$
\tan i\approx\frac{x}{h'},\qquad \tan r\approx\frac{x}{h}.
$$

Snell:

$$
n_2\sin i=n_1\sin r.
$$

Ở góc nhỏ:

$$
n_2\frac{x}{h'}\approx n_1\frac{x}{h}.
$$

Suy ra:

$$
h'\approx h\frac{n_2}{n_1}.
$$

## 6. Ví dụ — bể nước

Đáy bể sâu 1,20 m, nước n=4/3, nhìn gần vuông góc từ không khí:

$$
h'=1,20\frac{1}{4/3}=0,90\,\text m.
$$

Đáy có vẻ gần mặt nước hơn 0,30 m.

## 7. Nhiều lớp song song

Nếu quan sát gần vuông góc qua nhiều lớp, mỗi lớp dày $h_i$ và chiết suất $n_i$ nhìn từ không khí, độ dày biểu kiến tổng gần đúng:

$$
h'\approx\sum_i\frac{h_i}{n_i}.
$$

Nếu môi trường quan sát có chiết suất $n_0$:

$$
h'\approx\sum_i h_i\frac{n_0}{n_i}.
$$

Đây là cách gọn để xử lí lớp nước + kính khi các góc nhỏ.

## 8. Bài tia qua bể và điểm nhìn

Với góc không nhỏ, không nên dùng h'. Hãy:

1. vẽ tia thật từ vật tới mặt;
2. dùng Snell tìm r/i;
3. dùng tam giác lượng giác để liên hệ khoảng ngang và độ sâu;
4. kéo dài tia ló ngược để xác định vị trí ảnh ảo nếu cần.

## 9. Sai lầm thường gặp

!!! warning "Ảnh biểu kiến không phải vật nổi lên thật"
    Đường truyền ánh sáng bị gãy; não kéo dài tia ló theo đường thẳng và suy ra vị trí biểu kiến.

!!! warning "Bản song song không làm tia ló trùng tia tới"
    Tia ló song song nhưng thường bị dời ngang.

!!! warning "Dùng h'=h/n cho mọi góc"
    Công thức đơn giản là gần đúng quan sát gần pháp tuyến.

## 10. Liên hệ

- Bản mặt song song là ứng dụng trực tiếp của Snell hai lần.
- Độ sâu biểu kiến giải thích nhiều hiện tượng nhìn vật dưới nước.
- Khi góc bên trong tăng đủ lớn trong môi trường chiết suất cao, ta gặp phản xạ toàn phần ở bài sau.

## Tóm tắt

Tia qua bản hai mặt song song ló ra song song tia tới nhưng bị dời ngang. Độ dời $x=e\sin(i-r)/\cos r$. Khi nhìn gần vuông góc qua mặt phẳng, vật trong môi trường chiết suất lớn thường có độ sâu biểu kiến nhỏ hơn độ sâu thật.

## 5 điều cần nhớ

1. Hai mặt song song → tia ló song song tia tới.
2. Có thể có độ dời ngang.
3. $x=e\sin(i-r)/\cos r$.
4. Gần pháp tuyến: $h'=h n_2/n_1$.
5. Góc lớn → dùng Snell + hình học đầy đủ.


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/02-parallel-slab-apparent-depth/exercises.md)
- [Đáp án và lời giải](practice/02-parallel-slab-apparent-depth/solutions.md)

---

[← Bài 1](01-refraction-refractive-index.md) | [↑ Chương](index.md) | [Bài 3 →](03-total-internal-reflection.md)
