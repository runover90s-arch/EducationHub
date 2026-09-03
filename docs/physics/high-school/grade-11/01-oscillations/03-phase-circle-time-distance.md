---
title: "Bài 3 — Đường tròn lượng giác, thời gian và quãng đường"
description: "Biểu diễn dao động điều hòa bằng chuyển động tròn đều; bài toán thời gian, số lần qua vị trí, quãng đường và tốc độ trung bình."
order: 3
difficulty: "standard-applied"
prerequisites:
  - harmonic-oscillation
  - displacement-velocity-acceleration
tags:
  - physics
  - grade-11
  - oscillations
  - phase
  - unit-circle
---

# Bài 3 — Đường tròn lượng giác, thời gian và quãng đường

## Mục tiêu

Sau bài này, bạn có thể:

- chuyển một dao động điều hòa thành bài toán góc quay;
- xác định thời điểm trong quá khứ hoặc tương lai vật đạt một trạng thái;
- tìm thời gian ngắn nhất giữa hai vị trí;
- đếm số lần vật đi qua một vị trí;
- tính quãng đường trong khoảng thời gian bất kì;
- xác định quãng đường lớn nhất, nhỏ nhất trong một khoảng thời gian ngắn;
- tính tốc độ trung bình đúng theo định nghĩa.

## 1. Mô hình đường tròn lượng giác

Xét một điểm $M$ chuyển động tròn đều trên đường tròn bán kính $A$ với tốc độ góc $\omega$. Hình chiếu của $M$ lên một đường kính thực hiện dao động điều hòa:

$$
x=A\cos\Phi,
$$

trong đó $\Phi$ là góc pha.

Nếu tại $t=0$ điểm quay có góc $\varphi$, thì sau thời gian $t$:

$$
\Phi=\omega t+\varphi.
$$

Do đó dao động điều hòa có thể được xử lí bằng một chuyển động tròn đều tương ứng.

## 2. Quy ước chiều quay và dấu vận tốc

Ta chọn điểm quay tăng pha theo chiều dương lượng giác. Vì

$$
v=-\omega A\sin\Phi,
$$

nên:

- $\sin\Phi>0$ → $v<0$ → vật đi theo chiều âm;
- $\sin\Phi<0$ → $v>0$ → vật đi theo chiều dương.

Điều này đặc biệt hữu ích khi cùng một li độ $x$ ứng với hai góc trên đường tròn nhưng vật có hai chiều chuyển động khác nhau.

## 3. Từ trạng thái sang pha

Một trạng thái của vật thường gồm:

- li độ $x$;
- dấu của vận tốc $v$.

Bước đầu xác định

$$
\cos\Phi=\frac{x}{A}.
$$

Sau đó dùng dấu của $v=-\omega A\sin\Phi$ để chọn đúng góc.

### Ví dụ

Nếu $x=A/2$ thì $\cos\Phi=1/2$, có hai họ góc cơ bản $\Phi=\pm\pi/3+2k\pi$.

- Nếu $v<0$ thì $\sin\Phi>0$ → chọn $\Phi=\pi/3+2k\pi$.
- Nếu $v>0$ thì $\sin\Phi<0$ → chọn $\Phi=-\pi/3+2k\pi$.

## 4. Góc quay và thời gian

Điểm quay quét góc $\Delta\Phi$ trong thời gian $\Delta t$:

$$
\boxed{\Delta t=\frac{\Delta\Phi}{\omega}}.
$$

Nếu dùng độ:

$$
\Delta t=\frac{\alpha}{360^\circ}T.
$$

Đây là công thức nền của mọi bài toán thời gian trong dao động điều hòa.

## 5. Thời gian ngắn nhất giữa hai trạng thái

### Quy trình

1. Xác định pha của trạng thái đầu.
2. Xác định pha của trạng thái cuối.
3. Chọn góc quay dương nhỏ nhất phù hợp với chiều tăng pha.
4. Tính $\Delta t=\Delta\Phi/\omega$.

!!! tip "Mẹo"
    Khi đề nói **thời gian ngắn nhất**, không tự động lấy hiệu hai góc theo trị tuyệt đối. Phải xét đúng chiều quay của pha.

## 6. Những mốc thời gian đặc biệt

Trong một dao động:

- từ vị trí cân bằng đến biên gần nhất: $T/4$;
- từ biên này đến biên kia: $T/2$;
- từ một trạng thái đến trạng thái cùng pha gần nhất: $T$;
- đến trạng thái ngược pha: $T/2$.

Với các vị trí đặc biệt $|x|=A/2$, $A/\sqrt2$, $A\sqrt3/2$, có thể dùng các góc lượng giác quen thuộc để tính nhanh.

## 7. Hai thời điểm vuông pha

Hai thời điểm có độ lệch pha

$$
\Delta\Phi=\frac{\pi}{2}+k\pi
$$

thì các giá trị li độ thỏa một số hệ thức đặc biệt. Nếu hai trạng thái cách nhau $T/4$ hoặc $3T/4$, ta có thể dùng quan hệ hình học của hai bán kính vuông góc trên đường tròn.

Trường hợp thường gặp:

$$
\left(\frac{x_1}{A}\right)^2+\left(\frac{x_2}{A}\right)^2=1
$$

khi hai thời điểm lệch pha đúng $\pi/2$.

## 8. Hai thời điểm ngược pha

Nếu

$$
\Delta t=\frac{T}{2},
$$

thì $\Delta\Phi=\pi$ và:

$$
x_2=-x_1,\qquad v_2=-v_1,\qquad a_2=-a_1.
$$

Độ lớn của ba đại lượng không đổi.

## 9. Đếm số lần đi qua một vị trí

Một vị trí $x=x_0$ với $|x_0|<A$ thường được đi qua **hai lần trong một chu kì**: một lần theo chiều dương và một lần theo chiều âm.

Riêng hai biên $x=\pm A$, mỗi biên chỉ được chạm **một lần trong một chu kì**.

Nếu đề quy định thêm chiều chuyển động thì số lần thỏa điều kiện thường giảm một nửa.

### Phương pháp chắc chắn

1. Xác định tất cả pha thỏa vị trí và chiều trong một chu kì.
2. Chuyển các pha thành thời điểm mẫu.
3. Lập dãy thời điểm bằng cách cộng $kT$.
4. Đếm số phần tử thuộc khoảng thời gian đề cho.

Cách này an toàn hơn việc dùng công thức đếm máy móc khi khoảng thời gian bắt đầu ở trạng thái đặc biệt.

## 10. Quãng đường trong một chu kì và nửa chu kì

Vật đi từ biên này sang biên kia rồi trở lại:

$$
S_T=4A.
$$

Trong mọi nửa chu kì:

$$
S_{T/2}=2A.
$$

Nếu vật bắt đầu hoặc kết thúc tại vị trí cân bằng, quãng đường trong một phần tư chu kì là $A$.

## 11. Quãng đường trong khoảng thời gian bất kì

Giả sử cần tính quãng đường từ $t_1$ đến $t_2$.

### Bước 1 — Tách số chu kì trọn vẹn

Đặt $\Delta t=t_2-t_1$ và viết

$$
\Delta t=nT+\Delta t_r,
$$

với $0\le\Delta t_r<T$.

Phần $nT$ cho quãng đường $4nA$.

### Bước 2 — Xử lí phần thời gian dư

Xác định trạng thái tại $t_1$, quay thêm góc

$$
\Delta\Phi_r=\omega\Delta t_r,
$$

rồi chia quãng đường theo các mốc vị trí cân bằng hoặc biên mà vật đi qua.

### Tại sao không dùng |x₂ − x₁|?

Vì quãng đường là tổng chiều dài quỹ đạo vật đã đi. Nếu giữa hai thời điểm vật đổi chiều, $|x_2-x_1|$ chỉ là độ lớn độ dời, nhỏ hơn quãng đường thực tế.

## 12. Quãng đường lớn nhất và nhỏ nhất trong khoảng thời gian ngắn

Với khoảng thời gian tương ứng góc quét $0\le\alpha\le\pi$, quãng đường phụ thuộc vị trí bắt đầu.

### Quãng đường lớn nhất

Đạt được khi khoảng chuyển động đặt cân đối quanh vị trí cân bằng, nơi tốc độ lớn.

$$
\boxed{S_{\max}=2A\sin\frac{\alpha}{2}}.
$$

### Quãng đường nhỏ nhất

Đạt được khi khoảng chuyển động đặt gần một vị trí biên, nơi tốc độ nhỏ.

$$
\boxed{S_{\min}=2A\left(1-\cos\frac{\alpha}{2}\right)}.
$$

Các công thức này dùng cho một đoạn thời gian không vượt quá nửa chu kì; với khoảng dài hơn cần tách phần nguyên $T/2$ hoặc $T$ trước.

## 13. Tốc độ trung bình

Tốc độ trung bình luôn được tính từ **quãng đường**:

$$
\boxed{v_{\mathrm{tb}}=\frac{S}{\Delta t}}.
$$

Trong một chu kì:

$$
v_{\mathrm{tb},T}=\frac{4A}{T}=\frac{2\omega A}{\pi}.
$$

Đừng nhầm với vận tốc trung bình, vốn dùng độ dời.

## 14. Thời gian lò xo dãn hoặc nén — ý tưởng chung

Trong con lắc lò xo thẳng đứng, điều kiện lò xo dãn/nén có thể chuyển thành điều kiện đối với li độ $x$ so với độ dãn cân bằng $\Delta\ell_0$. Sau khi tìm được miền li độ, bài toán thời gian lại trở về bài toán góc trên đường tròn.

Phần công thức hệ thống sẽ được trình bày ở [Bài 4 — Con lắc lò xo](04-spring-oscillator.md).

## Ví dụ 1 — Thời gian từ cân bằng đến x = A/2

Vật đi từ vị trí cân bằng theo chiều dương. Trạng thái đầu có pha $-\pi/2$; trạng thái $x=A/2$ theo chiều dương có pha $-\pi/3$.

Góc quay là $\pi/6$, nên

$$
\Delta t=\frac{\pi/6}{\omega}=\frac{T}{12}.
$$

## Ví dụ 2 — Quãng đường trong 3T/4

Bắt đầu tại biên dương. Trong $T/2$, vật đi từ $+A$ đến $-A$: quãng đường $2A$. Trong $T/4$ tiếp theo, vật đi từ $-A$ đến vị trí cân bằng: thêm $A$.

Vậy $S=3A$.

## Ví dụ 3 — Quãng đường cực đại trong T/6

Góc quét là

$$
\alpha=\omega\frac{T}{6}=\frac{\pi}{3}.
$$

Suy ra

$$
S_{\max}=2A\sin\frac{\pi}{6}=A.
$$

## Phân dạng

> Đây là cách phân loại phục vụ mục đích sư phạm, không phải phân loại học thuật chính thức.

### Dạng 1 — Xác định thời điểm

Lập pha mục tiêu → tạo họ nghiệm → chọn thời điểm theo yêu cầu "lần thứ", "sớm nhất", "sau thời điểm...".

### Dạng 2 — Thời gian ngắn nhất

Đưa hai trạng thái lên đường tròn → tìm góc quay ngắn nhất đúng chiều → chia cho $\omega$.

### Dạng 3 — Số lần đi qua vị trí

Xác định các pha thỏa điều kiện trong một chu kì → lập dãy thời điểm → đếm.

### Dạng 4 — Quãng đường

Tách chu kì hoặc nửa chu kì trọn vẹn → xử lí phần dư bằng đường tròn.

### Dạng 5 — Quãng đường cực trị

Tách phần thời gian dài; với đoạn dư không quá $T/2$, dùng $S_{\max}$ hoặc $S_{\min}$ theo góc quét.

## Bẫy thường gặp

!!! danger "Bẫy 1"
    Đếm mỗi vị trí bên trong quỹ đạo là một lần trong một chu kì. Thực tế vật thường đi qua vị trí đó hai lần với hai chiều khác nhau.

!!! danger "Bẫy 2"
    Dùng $|x_2-x_1|$ làm quãng đường khi vật đã đổi chiều giữa hai thời điểm.

!!! warning "Bẫy 3"
    Khi tìm "lần thứ $n$", không nên dùng ngay $nT/2$ nếu vị trí xét không phải vị trí cân bằng hoặc điều kiện còn kèm chiều chuyển động.

## Bài tập nhanh

1. Một vật có $T=1,2$ s. Thời gian ngắn nhất từ vị trí cân bằng đến biên là bao nhiêu?
2. Trong $2,5T$, quãng đường vật đi được là bao nhiêu theo $A$?
3. Trong một chu kì, vật đi qua $x=A/3$ bao nhiêu lần nếu không xét chiều?
4. Trong một chu kì, vật đi qua $x=A/3$ theo chiều dương bao nhiêu lần?
5. Với $A=6$ cm, khoảng thời gian ứng với góc quét $\pi/3$. Tính $S_{\max}$.

### Đáp án nhanh

1. $0,3$ s.
2. $10A$.
3. Hai lần.
4. Một lần.
5. $6$ cm.

## Tóm tắt

Cốt lõi của bài toán thời gian là biến thời gian thành góc:

$$
\Delta\Phi=\omega\Delta t.
$$

Cốt lõi của bài toán quãng đường là:

- $S_T=4A$;
- $S_{T/2}=2A$;
- phần dư phải xét các lần đổi chiều.

## 5 điều cần nhớ

1. Một li độ chưa xác định đầy đủ trạng thái; cần thêm chiều chuyển động.
2. Thời gian bằng góc quay chia tốc độ góc.
3. Một vị trí bên trong quỹ đạo thường được đi qua hai lần mỗi chu kì.
4. Quãng đường khác độ dời.
5. Tách chu kì trọn vẹn trước giúp bài quãng đường ngắn và ít sai.


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/03-phase-circle-time-distance/exercises.md)
- [Đáp án và lời giải](practice/03-phase-circle-time-distance/solutions.md)

---

[← Bài 2](02-displacement-velocity-acceleration.md) | [↑ Chương](index.md) | [Bài 4 →](04-spring-oscillator.md)
