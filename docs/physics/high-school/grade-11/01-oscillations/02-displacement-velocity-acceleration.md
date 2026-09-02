---
title: "Bài 2 — Li độ, vận tốc và gia tốc"
description: "Quan hệ giữa li độ, vận tốc, gia tốc; pha; cực trị; đồ thị và các hệ thức độc lập thời gian trong dao động điều hòa."
order: 2
difficulty: "foundation-standard"
prerequisites:
  - harmonic-oscillation
  - basic-derivatives
tags:
  - physics
  - grade-11
  - oscillations
  - velocity
  - acceleration
---

# Bài 2 — Li độ, vận tốc và gia tốc

## Mục tiêu

Sau bài này, bạn cần có thể:

1. Từ phương trình li độ suy ra phương trình vận tốc và gia tốc.
2. Xác định hướng của vectơ vận tốc và vectơ gia tốc tại mọi vị trí.
3. Nhận ra vị trí có tốc độ cực đại, cực tiểu; gia tốc cực đại, cực tiểu.
4. Sử dụng đúng các hệ thức liên hệ giữa $x$, $v$, $a$ mà không cần biết thời gian.
5. Đọc và liên hệ được đồ thị $x-t$, $v-t$, $a-t$.
6. Xử lí các bài cho hai trạng thái khác nhau của cùng một dao động.
7. Tránh nhầm **vận tốc** với **tốc độ**, và tránh nhầm dấu của gia tốc với độ lớn của gia tốc.

## Kiến thức tiên quyết

Bạn cần đọc được phương trình chuẩn

$$
x=A\cos(\omega t+\varphi),\qquad A>0,\ \omega>0.
$$

Trong đó $x$ là li độ, $A$ là biên độ, $\omega$ là tần số góc và $\varphi$ là pha ban đầu.

## 1. Từ li độ đến vận tốc

Vận tốc tức thời là đạo hàm của li độ theo thời gian:

$$
v=x'.
$$

Với $x=A\cos(\omega t+\varphi)$, ta có

$$
v=-\omega A\sin(\omega t+\varphi).
$$

Có thể viết dưới dạng cos:

$$
v=\omega A\cos\left(\omega t+\varphi+\frac{\pi}{2}\right).
$$

### Ý nghĩa về pha

So với li độ, vận tốc **sớm pha $\pi/2$**. Điều này không có nghĩa vận tốc luôn dương trước li độ; đây là quan hệ pha giữa hai hàm dao động cùng tần số góc.

### Giá trị cực đại của tốc độ

Từ $|\sin|\le 1$:

$$
|v|\le \omega A.
$$

Do đó:

- vận tốc cực đại: $v_{\max}=+\omega A$;
- vận tốc cực tiểu: $v_{\min}=-\omega A$;
- tốc độ cực đại: $|v|_{\max}=\omega A$;
- tốc độ nhỏ nhất: $|v|_{\min}=0$.

!!! note "Vận tốc và tốc độ"
    Vận tốc $v$ có dấu. Tốc độ là $|v|$ nên không âm. Khi đề hỏi "tốc độ cực đại", đáp án là $\omega A$, không phải $\pm\omega A$.

## 2. Hướng chuyển động qua dấu của vận tốc

Trên trục $Ox$:

- $v>0$: vật chuyển động theo chiều dương;
- $v<0$: vật chuyển động theo chiều âm;
- $v=0$: vật đang ở một trong hai vị trí biên.

Tại vị trí cân bằng $x=0$, tốc độ đạt cực đại. Tại hai biên $x=\pm A$, tốc độ bằng $0$.

### Trực giác

Vật phải dừng lại trong một khoảnh khắc ở biên để đổi chiều, nên $v=0$ tại biên. Khi đi qua vị trí cân bằng, vật đã được lực kéo về gia tốc trong nửa quãng trước đó nên có tốc độ lớn nhất.

## 3. Gia tốc trong dao động điều hòa

Gia tốc là đạo hàm của vận tốc:

$$
a=v'=x''.
$$

Từ phương trình vận tốc:

$$
a=-\omega^2A\cos(\omega t+\varphi).
$$

Do $x=A\cos(\omega t+\varphi)$ nên có hệ thức đặc biệt quan trọng:

$$
\boxed{a=-\omega^2x}.
$$

Đây là dấu hiệu động học cốt lõi của dao động điều hòa.

### Ý nghĩa của dấu âm

Gia tốc luôn hướng về vị trí cân bằng:

- nếu $x>0$ thì $a<0$;
- nếu $x<0$ thì $a>0$;
- nếu $x=0$ thì $a=0$.

Nói cách khác, vectơ gia tốc luôn ngược hướng với vectơ li độ.

## 4. Cực trị của gia tốc

Từ $a=-\omega^2x$ và $|x|\le A$:

$$
|a|\le \omega^2A.
$$

Vì vậy:

- $a_{\max}=+\omega^2A$ tại $x=-A$;
- $a_{\min}=-\omega^2A$ tại $x=+A$;
- $|a|_{\max}=\omega^2A$ tại hai biên;
- $|a|_{\min}=0$ tại vị trí cân bằng.

## 5. Quan hệ pha giữa $x$, $v$, $a$

Ba đại lượng cùng dao động với tần số góc $\omega$ nhưng lệch pha nhau:

- $v$ sớm pha $\pi/2$ so với $x$;
- $a$ sớm pha $\pi/2$ so với $v$;
- $a$ ngược pha với $x$.

Một cách ghi nhớ:

$$
x\ \xrightarrow{+\pi/2}\ v\ \xrightarrow{+\pi/2}\ a.
$$

!!! warning "Bẫy thường gặp"
    Không được suy ra rằng $v$ và $a$ luôn cùng dấu vì $a$ "sớm pha" so với $v$. Dấu tức thời còn phụ thuộc vị trí và chiều chuyển động.

## 6. Khi nào vật nhanh dần, chậm dần?

Xét dấu của $v$ và $a$:

- $va>0$: vận tốc và gia tốc cùng dấu → tốc độ tăng → vật **nhanh dần**;
- $va<0$: vận tốc và gia tốc trái dấu → tốc độ giảm → vật **chậm dần**.

Do gia tốc luôn hướng về vị trí cân bằng:

- vật đi **từ biên về vị trí cân bằng**: nhanh dần;
- vật đi **từ vị trí cân bằng ra biên**: chậm dần.

## 7. Hệ thức độc lập thời gian giữa $x$ và $v$

Từ

$$
x=A\cos\Phi,\qquad v=-\omega A\sin\Phi,
$$

với $\Phi=\omega t+\varphi$, bình phương rồi cộng cho ta:

$$
\boxed{\frac{x^2}{A^2}+\frac{v^2}{\omega^2A^2}=1}.
$$

Các dạng tương đương:

$$
\begin{aligned}
&v^2=\omega^2(A^2-x^2)\\
&|v|=\omega\sqrt{A^2-x^2},
\end{aligned}
$$

$$
A^2=x^2+\frac{v^2}{\omega^2}.
$$

### Khi nào dùng?

Dùng khi đề cho trạng thái tại một thời điểm bằng $x$ và $v$ nhưng không cho $t$, hoặc khi cần loại bỏ pha.

### Điều gì còn thiếu?

Công thức $v^2=\omega^2(A^2-x^2)$ chỉ cho **độ lớn** của vận tốc. Muốn xác định dấu của $v$, cần thêm thông tin về chiều chuyển động.

## 8. Hệ thức giữa $x$ và $a$

Do $a=-\omega^2x$:

$$
\omega^2=-\frac{a}{x}\qquad (x\ne0).
$$

Nếu biết hai trạng thái $(x_1,a_1)$ và $(x_2,a_2)$ của cùng một dao động, về lí thuyết phải có:

$$
\frac{a_1}{x_1}=\frac{a_2}{x_2}=-\omega^2.
$$

Đây cũng là cách kiểm tra nhanh dữ kiện có nhất quán hay không.

## 9. Hệ thức giữa $v$ và $a$

Thay $x=-a/\omega^2$ vào hệ thức $x-v$:

$$
\boxed{\frac{v^2}{\omega^2A^2}+\frac{a^2}{\omega^4A^2}=1}.
$$

Hay:

$$
A^2=\frac{v^2}{\omega^2}+\frac{a^2}{\omega^4}.
$$

## 10. Xác định $\omega$ từ hai trạng thái

### Trường hợp biết $(x_1,v_1)$ và $(x_2,v_2)$

Từ

$$
v_1^2=\omega^2(A^2-x_1^2),\qquad v_2^2=\omega^2(A^2-x_2^2),
$$

lấy hai phương trình trừ nhau:

$$
\boxed{\omega^2=\frac{v_1^2-v_2^2}{x_2^2-x_1^2}}.
$$

Điều kiện: $x_1^2\ne x_2^2$.

### Trường hợp biết $(v_1,a_1)$ và $(v_2,a_2)$

Từ hệ thức $v-a$:

$$
\boxed{\omega^2=\frac{a_1^2-a_2^2}{v_2^2-v_1^2}}.
$$

Cần kiểm tra dấu và đơn vị trước khi lấy căn.

## 11. Đồ thị $x-t$, $v-t$, $a-t$

Ba đồ thị đều là các đường hình sin/cos có cùng chu kì $T$.

Nếu chọn $x=A\cos\omega t$ thì:

- $x$ bắt đầu tại $+A$;
- $v=-\omega A\sin\omega t$ bắt đầu tại $0$ và đi theo chiều âm;
- $a=-\omega^2A\cos\omega t$ bắt đầu tại $-\omega^2A$.

### Đọc đồ thị li độ

Từ đồ thị $x-t$, có thể xác định:

- $A$: tung độ cực đại theo trị tuyệt đối;
- $T$: khoảng thời gian giữa hai trạng thái lặp lại gần nhất;
- dấu $v$: dựa vào độ dốc của đồ thị $x-t$;
- dấu $a$: ngược dấu với $x$.

### Đọc đồ thị vận tốc

Từ đồ thị $v-t$:

- biên độ vận tốc là $\omega A$;
- lúc $v=0$, vật ở biên;
- lúc $|v|$ cực đại, vật qua vị trí cân bằng.

## 12. Đồ thị quan hệ $v-x$

Hệ thức

$$
\frac{x^2}{A^2}+\frac{v^2}{\omega^2A^2}=1
$$

là phương trình một elip trong mặt phẳng $(x,v)$.

Các giao điểm với trục:

- trục $x$: $x=\pm A$;
- trục $v$: $v=\pm\omega A$.

Đường elip này mô tả toàn bộ trạng thái động học có thể có của vật trong một dao động điều hòa.

## 13. Đồ thị quan hệ $a-x$

Từ $a=-\omega^2x$, đồ thị $a$ theo $x$ là đường thẳng đi qua gốc tọa độ có hệ số góc $-\omega^2$.

Đây là một dấu hiệu rất mạnh: nếu thí nghiệm cho đồ thị $a-x$ là đường thẳng qua gốc có hệ số góc âm, chuyển động phù hợp với mô hình dao động điều hòa.

## Ví dụ 1 — Tính trạng thái từ phương trình

Một vật dao động theo

$$
x=5\cos\left(4\pi t-\frac{\pi}{3}\right)\text{ cm}.
$$

Tại $t=\frac{1}{12}$ s, xác định $x$, $v$, $a$.

### Giải

Pha tại thời điểm xét là $\Phi=4\pi\cdot\frac{1}{12}-\frac{\pi}{3}=0$.

Do đó $x=5$ cm, $v=0$ và $a=-\omega^2x=-(4\pi)^2\cdot5$ cm/s².

Vật đang ở biên dương và chuẩn bị chuyển động theo chiều âm.

## Ví dụ 2 — Tìm tốc độ từ li độ

Vật dao động với $A=8$ cm, $\omega=5$ rad/s. Khi $x=4$ cm, tốc độ là

$$
|v|=\omega\sqrt{A^2-x^2}=5\sqrt{64-16}=20\sqrt3\text{ cm/s}.
$$

Nếu đề nói vật đang đi theo chiều âm thì $v=-20\sqrt3$ cm/s.

## Ví dụ 3 — Tìm tần số góc từ hai trạng thái

Tại hai thời điểm, vật có $(x_1,v_1)=(3\text{ cm},40\text{ cm/s})$ và $(x_2,v_2)=(4\text{ cm},30\text{ cm/s})$.

Ta có

$$
\omega^2=\frac{40^2-30^2}{4^2-3^2}=100,
$$

nên $\omega=10$ rad/s.

Biên độ được suy ra từ $A^2=x_1^2+v_1^2/\omega^2=25$, do đó $A=5$ cm.

## Phản ví dụ

Một chuyển động có $a=-4x+2$ không thỏa trực tiếp dạng $a=-\omega^2x$ với gốc tọa độ đang chọn. Không được kết luận ngay đây là dao động điều hòa quanh $x=0$. Nếu đổi gốc tọa độ về vị trí cân bằng mới, bài toán có thể trở thành dao động điều hòa.

## Phân dạng

> Đây là cách phân loại phục vụ mục đích sư phạm, không phải phân loại học thuật chính thức.

### Dạng 1 — Từ phương trình li độ suy ra $v$, $a$

**Dấu hiệu:** đề cho $x(t)$ và hỏi vận tốc, gia tốc, cực trị hoặc trạng thái tại thời điểm.

**Phương pháp:** đọc $A,\omega,\varphi$ → viết $v(t)$ → dùng $a=-\omega^2x$ nếu tiện.

### Dạng 2 — Quan hệ trạng thái $x-v-a$

**Dấu hiệu:** đề không cho thời gian hoặc cho trạng thái ở một vài thời điểm.

**Phương pháp:** ưu tiên $v^2=\omega^2(A^2-x^2)$ và $a=-\omega^2x$.

### Dạng 3 — Đọc đồ thị

**Dấu hiệu:** đề cho đồ thị $x-t$, $v-t$, $a-t$, $v-x$ hoặc $a-x$.

**Phương pháp:** xác định biên độ và chu kì trước; sau đó dùng quan hệ pha và dấu.

## Bẫy thường gặp

!!! danger "Sai lầm 1"
    Từ $v^2=\omega^2(A^2-x^2)$ suy ra ngay $v=+\omega\sqrt{A^2-x^2}$. Đúng phải là $v=\pm\omega\sqrt{A^2-x^2}$; dấu phụ thuộc chiều chuyển động.

!!! danger "Sai lầm 2"
    Cho rằng gia tốc lớn nhất ở vị trí cân bằng. Thực tế tại vị trí cân bằng $a=0$; độ lớn gia tốc lớn nhất ở hai biên.

!!! warning "Sai lầm 3"
    Nhầm $a_{\max}$ với $|a|_{\max}$. $a_{\max}=+\omega^2A$, còn giá trị nhỏ nhất của gia tốc là $-\omega^2A$.

## Bài tập nhanh

1. Vật dao động với $A=6$ cm, $\omega=4$ rad/s. Tính tốc độ cực đại và độ lớn gia tốc cực đại.
2. Với $x=3$ cm, $A=5$ cm, $\omega=10$ rad/s, tính tốc độ.
3. Một vật có $a=-100x$ khi dùng cùng đơn vị SI. Xác định $\omega$ và $T$.
4. Tại một thời điểm $x>0$ và $v>0$. Vật đang nhanh dần hay chậm dần?
5. Một đồ thị $a-x$ có hệ số góc $-64$ s⁻². Tìm tần số góc.

### Đáp án nhanh

1. $24$ cm/s; $96$ cm/s².
2. $40$ cm/s.
3. $\omega=10$ rad/s; $T=\pi/5$ s.
4. Chậm dần vì $a<0$ và $v>0$.
5. $8$ rad/s.

## Tóm tắt

Ba phương trình quan trọng:

$$
x=A\cos\Phi,\qquad v=-\omega A\sin\Phi,\qquad a=-\omega^2A\cos\Phi,
$$

với $\Phi=\omega t+\varphi$.

Hai hệ thức cần thuộc bản chất:

$$
\begin{aligned}
&a=-\omega^2x\\
&v^2=\omega^2(A^2-x^2).
\end{aligned}
$$

## 5 điều cần nhớ

1. Vận tốc sớm pha $\pi/2$ so với li độ.
2. Gia tốc ngược pha với li độ và luôn hướng về vị trí cân bằng.
3. Tốc độ lớn nhất tại vị trí cân bằng; bằng $0$ tại biên.
4. Độ lớn gia tốc lớn nhất tại biên; bằng $0$ tại vị trí cân bằng.
5. Hệ thức $x-v-a$ giúp giải nhiều bài mà không cần tìm thời gian.

---

[← Bài 1](01-harmonic-oscillation-foundations.md) | [↑ Chương](index.md) | [Bài 3 →](03-phase-circle-time-distance.md)
