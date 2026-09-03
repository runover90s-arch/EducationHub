---
title: "Bài 1 — Đại cương về dao động điều hòa"
description: "Dao động cơ, dao động tuần hoàn, dao động điều hòa, phương trình dao động, biên độ, pha, chu kì và tần số."
order: 1
difficulty: "foundation"
prerequisites:
  - basic-trigonometry
  - graph-reading
tags:
  - physics
  - grade-11
  - oscillations
  - harmonic-motion
---

# Bài 1 — Đại cương về dao động điều hòa

## Mục tiêu

Sau bài này, bạn cần làm được các việc sau:

1. Nhận biết dao động cơ.
2. Xác định vị trí cân bằng.
3. Phân biệt dao động tuần hoàn, dao động tự do và dao động điều hòa.
4. Đọc đúng phương trình $x=A\cos(\omega t+\varphi)$.
5. Hiểu ý nghĩa của $x,A,\omega,\varphi,\omega t+\varphi$.
6. Tính được chu kì, tần số, tần số góc.
7. Xác định quỹ đạo và miền giá trị của li độ.
8. Đọc các thông tin cơ bản từ đồ thị li độ – thời gian.
9. Tránh các lỗi về đơn vị, dấu của biên độ và pha.

---

## Kiến thức tiên quyết

Bạn cần biết:

- hàm $\sin$, $\cos$;
- đơn vị thời gian;
- khái niệm đồ thị;
- đổi độ sang radian khi cần;
- biến đổi đại số cơ bản.

---

## 1. Đặt vấn đề

Một vật gắn vào lò xo, một quả nặng treo trên dây, một cành cây rung sau khi bị lệch khỏi trạng thái ban đầu... đều có thể chuyển động qua lại quanh một vị trí đặc biệt.

Điểm chung quan trọng là:

- vật không đi mãi theo một chiều;
- vật thường quay lại gần hoặc đi qua một vị trí trung tâm;
- trạng thái chuyển động có thể lặp lại.

Từ đó ta xây dựng khái niệm **dao động cơ**.

---

## 2. Dao động cơ

### Định nghĩa

**Dao động cơ** là chuyển động qua lại của một vật quanh một vị trí xác định gọi là **vị trí cân bằng**.

### Hiểu đơn giản

Hãy tưởng tượng một vật có một vị trí "ở giữa". Khi bị kéo lệch khỏi vị trí đó rồi thả ra, vật đi sang một phía, quay lại, đi qua vị trí giữa, sang phía còn lại rồi tiếp tục lặp lại.

### Vị trí cân bằng

Vị trí cân bằng, viết tắt **VTCB**, là vị trí quanh đó vật dao động.

Trong nhiều mô hình cơ học cơ bản, khi vật đứng yên tại VTCB thì hợp lực theo phương dao động bằng không.

!!! note "Không nhầm"
    "Vị trí cân bằng" không có nghĩa là vật luôn đứng yên ở đó. Khi đang dao động, vật có thể đi qua VTCB với tốc độ lớn.

### Ví dụ

- Vật gắn với lò xo nằm ngang dao động qua lại quanh vị trí lò xo cân bằng dưới tác dụng tổng hợp của các lực.
- Quả nặng của con lắc đơn dao động qua lại quanh vị trí thấp nhất.
- Một điểm trên dây có sóng truyền qua dao động quanh vị trí cân bằng của nó.

### Phản ví dụ

Một xe chạy thẳng đều trên đường không phải là dao động cơ vì xe không chuyển động qua lại quanh một vị trí cân bằng cố định.

---

## 3. Dao động tuần hoàn

### Định nghĩa

**Dao động tuần hoàn** là dao động mà trạng thái chuyển động của vật được lặp lại như cũ sau những khoảng thời gian bằng nhau xác định.

Khoảng thời gian ngắn nhất để trạng thái lặp lại như cũ là **chu kì**.

### Điều cần lưu ý

Không chỉ vị trí phải lặp lại. Để trạng thái dao động lặp lại như cũ, chiều chuyển động cũng phải phù hợp.

Ví dụ, vật đi qua cùng một vị trí hai lần trong một chu kì nhưng hai lần đó có thể chuyển động theo hai chiều ngược nhau. Hai thời điểm đó chưa chắc cách nhau một chu kì.

---

## 4. Dao động tự do

### Khái niệm

Trong mô hình lí tưởng, **dao động tự do** là dao động của hệ sau khi được kích thích ban đầu rồi để hệ tự dao động dưới tác dụng của các lực nội tại hoặc lực đặc trưng của hệ.

### Ý nghĩa

Chu kì hoặc tần số riêng của dao động tự do phụ thuộc vào các đặc trưng của hệ.

Ví dụ:

- con lắc lò xo lí tưởng có tần số riêng phụ thuộc vào khối lượng và độ cứng lò xo;
- con lắc đơn góc nhỏ có chu kì phụ thuộc vào chiều dài dây và gia tốc trọng trường.

Phần này sẽ được học kĩ ở các bài sau.

---

## 5. Dao động điều hòa

### Định nghĩa

Một dao động được gọi là **dao động điều hòa** nếu li độ của vật là một hàm cos hoặc sin của thời gian.

Dạng chuẩn thường dùng:

$$
\boxed{x=A\cos(\omega t+\varphi)}
$$

Trong đó:

- $x$: li độ tại thời điểm $t$;
- $A$: biên độ dao động;
- $\omega$: tần số góc;
- $\varphi$: pha ban đầu;
- $\omega t+\varphi$: pha dao động tại thời điểm $t$.

### Tại sao dùng dạng cos?

Dùng cos hay sin đều được vì hai hàm chỉ lệch pha nhau:

$$
\sin\alpha=\cos\left(\alpha-\frac{\pi}{2}\right).
$$

Trong giáo trình này, khi viết phương trình chuẩn, ta ưu tiên dạng cos.

---

## 6. Li độ

### Định nghĩa

**Li độ** là tọa độ của vật tính từ vị trí cân bằng trên trục dao động đã chọn.

**Kí hiệu:** $x$.

### Miền giá trị

Vì $-1\le \cos(\omega t+\varphi)\le 1$, nên li độ luôn thỏa **$-A\le x\le A$**.

Hai vị trí $x=+A$ và $x=-A$ là hai vị trí biên.

### Dấu của li độ

- $x>0$: vật nằm phía dương của VTCB.
- $x<0$: vật nằm phía âm.
- $x=0$: vật ở VTCB.

!!! warning "Bẫy thường gặp"
    Dấu của $x$ cho biết vị trí so với VTCB, **không tự động cho biết chiều chuyển động**.

---

## 7. Biên độ

### Định nghĩa

**Biên độ** là độ lớn li độ cực đại của vật: $A=x_{\max}=|x|_{\max}$. Theo quy ước, **$A>0$**.

### Ý nghĩa hình học

Vật dao động trên đoạn thẳng từ $-A$ đến $+A$.

Vì vậy chiều dài quỹ đạo là:

$$
\boxed{L=2A}.
$$

### Ví dụ

Với:

$$
x=6\cos(4\pi t-\frac{\pi}{3})\;(\text{cm}),
$$

ta có:

- $A=6$ cm;
- $x\in[-6;6]$ cm;
- chiều dài quỹ đạo $L=12$ cm.

!!! danger "Sai lầm nghiêm trọng"
    Không viết biên độ âm. Nếu gặp $x=-5\cos(\omega t+\alpha)$, phải đưa về dạng có biên độ dương $x=5\cos(\omega t+\alpha+\pi)$.

---

## 8. Pha dao động

### Định nghĩa

Pha dao động tại thời điểm $t$ là:

$$
\boxed{\Phi=\omega t+\varphi}.
$$

### Pha ban đầu

Tại $t=0$:

$$
\Phi_0=\varphi.
$$

Vì vậy $\varphi$ được gọi là **pha ban đầu**.

### Vai trò của pha

Pha giúp xác định trạng thái dao động của vật tại một thời điểm.

Từ:

$$
x=A\cos\Phi,
$$

ta thấy cùng một biên độ nhưng pha khác nhau có thể cho vị trí khác nhau.

### Tính tuần hoàn của pha

Do hàm cos có chu kì $2\pi$:

$$
\cos(\Phi+2k\pi)=\cos\Phi,\qquad k\in\mathbb Z.
$$

Vì vậy hai pha hơn kém nhau $2k\pi$ cho cùng giá trị cos.

---

## 9. Chu kì, tần số và tần số góc

### 9.1. Chu kì

**Chu kì $T$** là khoảng thời gian để vật thực hiện một dao động toàn phần.

**Đơn vị SI:** $[T]=\text{s}$.

Nếu trong thời gian $\Delta t$ vật thực hiện $N$ dao động toàn phần:

$$
\boxed{T=\frac{\Delta t}{N}}.
$$

---

### 9.2. Tần số

**Tần số $f$** là số dao động toàn phần vật thực hiện trong một giây.

**Đơn vị:** $[f]=\text{Hz}$.

Ta có $f=\dfrac{1}{T}$. Nếu vật thực hiện $N$ dao động trong thời gian $\Delta t$ thì $f=\dfrac{N}{\Delta t}$.

---

### 9.3. Tần số góc

Với phương trình $x=A\cos(\omega t+\varphi)$, hệ số của $t$ trong pha là tần số góc $\omega$. Quan hệ cơ bản là:

$$
\boxed{\omega=2\pi f=\frac{2\pi}{T}}.
$$

**Đơn vị thường dùng:** $[\omega]=\text{rad/s}$.

Suy ra:

$$
\boxed{T=\frac{2\pi}{\omega}},\qquad
\boxed{f=\frac{\omega}{2\pi}}.
$$

---

## 10. Vì sao ωT = 2π?

Sau đúng một chu kì, trạng thái dao động lặp lại.

Sau một chu kì, pha tăng $\Delta\Phi=\omega T$. Để hàm cos trở lại đúng trạng thái ban đầu sau khoảng thời gian ngắn nhất, độ tăng pha phải bằng $2\pi$. Vì vậy:

$$
\omega T=2\pi\quad\Rightarrow\quad T=\frac{2\pi}{\omega}.
$$

Đây là nguồn gốc của hệ thức giữa chu kì và tần số góc.

---

## 11. Số dao động trong một khoảng thời gian

Nếu chu kì là $T$, số dao động toàn phần trong thời gian $\Delta t$ là:

$$
\boxed{N=\frac{\Delta t}{T}=f\Delta t=\frac{\omega\Delta t}{2\pi}}.
$$

### Lưu ý

Công thức trên cho số chu kì tương ứng với khoảng thời gian. Nếu đề hỏi **số lần vật đi qua một vị trí**, **số lần đạt biên**, hoặc **số lần có một giá trị li độ**, không được lấy ngay $N$ làm đáp án. Các bài đó cần phân tích trạng thái dao động.

---

## 12. Đồ thị li độ – thời gian

Với:

$$
x=A\cos(\omega t+\varphi),
$$

đồ thị $x$ theo $t$ là một đường hình sin.

### Đọc biên độ

Biên độ là giá trị lớn nhất của $|x|$:

$$
A=|x|_{\max}.
$$

### Đọc chu kì

Chu kì là khoảng thời gian ngắn nhất giữa hai trạng thái lặp lại.

Trên đồ thị, có thể đo khoảng thời gian giữa:

- hai đỉnh liên tiếp;
- hai đáy liên tiếp;
- hai lần qua VTCB theo cùng một chiều.

### Đọc tần số

Sau khi có $T$:

$$
f=\frac{1}{T}.
$$

---

## 13. Chuẩn hóa phương trình dao động

Phương trình chuẩn có dạng $x=A\cos(\omega t+\varphi)$ với **$A>0$** và **$\omega>0$**.

### Trường hợp hệ số cos âm

Ví dụ $x=-4\cos\left(5t-\dfrac{\pi}{6}\right)$. Dùng $-\cos\alpha=\cos(\alpha+\pi)$, ta được:

$$
x=4\cos\left(5t-\frac{\pi}{6}+\pi\right)
=4\cos\left(5t+\frac{5\pi}{6}\right).
$$

### Trường hợp dùng sin

Ví dụ $x=3\sin\left(2\pi t+\dfrac{\pi}{3}\right)$. Dùng $\sin\alpha=\cos\left(\alpha-\dfrac{\pi}{2}\right)$, ta được:

$$
x=3\cos\left(2\pi t+\frac{\pi}{3}-\frac{\pi}{2}\right)
=3\cos\left(2\pi t-\frac{\pi}{6}\right).
$$

---

## 14. Trực giác về pha

Có thể xem pha như một "đồng hồ trạng thái" của dao động.

Mỗi khi pha tăng thêm:

$$
2\pi,
$$

vật hoàn thành một chu kì.

Mỗi khi thời gian tăng thêm một chu kì $T$, pha tăng thêm $\omega T=2\pi$.

Điều này giải thích vì sao phương pháp đường tròn lượng giác rất hữu ích. Ta sẽ học riêng phương pháp đó ở Bài 3.

---

## 15. Phân dạng cơ bản

!!! note "Về tên các dạng"
    Cách chia dưới đây phục vụ mục đích sư phạm, không phải một hệ phân loại học thuật chính thức.

### Dạng 1 — Đọc các đại lượng từ phương trình

#### Dấu hiệu

Đề cho trực tiếp:

$$
x=A\cos(\omega t+\varphi).
$$

#### Cần tìm

Thường là:

- biên độ;
- tần số góc;
- chu kì;
- tần số;
- pha ban đầu;
- pha tại thời điểm $t$;
- li độ tại thời điểm $t$.

#### Phương pháp

1. Đưa phương trình về dạng chuẩn nếu cần.
2. Đọc $A,\omega,\varphi$.
3. Tính $T=\dfrac{2\pi}{\omega}$ và $f=\dfrac{\omega}{2\pi}$.
4. Nếu hỏi tại thời điểm $t$, thay $t$ vào pha hoặc phương trình.

---

### Dạng 2 — Tính từ số dao động trong một khoảng thời gian

Dùng:

$$
T=\frac{\Delta t}{N},
\qquad
f=\frac{N}{\Delta t},
\qquad
\omega=2\pi f.
$$

---

### Dạng 3 — Đọc biên độ và chu kì từ đồ thị

1. Tìm $|x|_{\max}\Rightarrow A$.
2. Chọn hai trạng thái lặp lại gần nhau nhất.
3. Lấy hiệu thời gian để có $T$.
4. Từ đó tính $f,\omega$.

---

## 16. Bẫy thường gặp

!!! warning "Bẫy 1 — Nhầm $\omega$ với $f$"
    Trong $x=A\cos(\omega t+\varphi)$, hệ số của $t$ là $\omega$, **không phải** $f$.

!!! warning "Bẫy 2 — Quên $2\pi$"
    Công thức đúng là $\omega=2\pi f$, **không phải** $\omega=f$.

!!! warning "Bẫy 3 — Biên độ âm"
    Biên độ theo quy ước phải dương.

!!! warning "Bẫy 4 — Li độ và quãng đường"
    Li độ là tọa độ có dấu. Quãng đường là đại lượng không âm.

!!! warning "Bẫy 5 — Cùng vị trí chưa chắc cùng trạng thái"
    Vật có thể đi qua cùng một vị trí theo hai chiều khác nhau.

!!! warning "Bẫy 6 — Đơn vị"
    Nếu $x$ ghi bằng cm thì biên độ đọc ra từ phương trình cũng đang ở cm. Khi tính những đại lượng cần SI, phải đổi đơn vị đúng lúc.

---

# Ví dụ

## Ví dụ 1 — Đọc phương trình

Cho:

$$
x=8\cos\left(4\pi t-\frac{\pi}{3}\right)\;(\text{cm}).
$$

Xác định $A,\omega,T,f,\varphi$.

### Giải

So sánh với dạng chuẩn $x=A\cos(\omega t+\varphi)$, ta đọc trực tiếp được:

- biên độ: $A=8$ cm;
- tần số góc: $\omega=4\pi$ rad/s;
- pha ban đầu: $\varphi=-\dfrac{\pi}{3}$ rad.

Từ $\omega=4\pi$ rad/s:

- chu kì: $T=\dfrac{2\pi}{\omega}=\dfrac{2\pi}{4\pi}=0,5$ s;
- tần số: $f=\dfrac1T=2$ Hz.

**Kết quả:** $A=8$ cm, $\omega=4\pi$ rad/s, $T=0,5$ s, $f=2$ Hz, $\varphi=-\dfrac{\pi}{3}$ rad.

---

## Ví dụ 2 — Pha và li độ tại một thời điểm

Với $x=8\cos\left(4\pi t-\dfrac{\pi}{3}\right)$ cm, tính pha và li độ tại $t=0,25$ s.

### Giải

Tính pha rồi thay vào $x=A\cos\Phi$:

$$
\begin{aligned}
\Phi&=4\pi\cdot0,25-\frac{\pi}{3}=\frac{2\pi}{3},\\
x&=8\cos\frac{2\pi}{3}=8\left(-\frac12\right)=-4\text{ cm}.
\end{aligned}
$$

**Kết quả:** $\Phi=\dfrac{2\pi}{3}$ rad và $x=-4$ cm.

---

## Ví dụ 3 — Từ số dao động

Một vật thực hiện 30 dao động toàn phần trong 12 s. Tính $T,f,\omega$.

### Giải

Tần số là số dao động thực hiện trong một giây:

$$
f=\frac{N}{\Delta t}=\frac{30}{12}=2,5\text{ Hz}.
$$

Suy ra $T=\dfrac1f=0,4$ s và $\omega=2\pi f=5\pi$ rad/s.

**Kết quả:** $T=0,4$ s, $f=2,5$ Hz, $\omega=5\pi$ rad/s.

---

## Ví dụ 4 — Chuẩn hóa phương trình

Cho:

$$
x=-6\sin\left(2\pi t+\frac{\pi}{6}\right)\text{ cm}.
$$

Viết phương trình về dạng cos với biên độ dương.

### Giải

Trước hết đổi sin sang cos bằng $\sin\alpha=\cos\left(\alpha-\dfrac{\pi}{2}\right)$:

$$
\begin{aligned}
x
&=-6\cos\left(2\pi t+\frac{\pi}{6}-\frac{\pi}{2}\right)\\
&=-6\cos\left(2\pi t-\frac{\pi}{3}\right).
\end{aligned}
$$

Biên độ đang mang dấu âm, nên dùng $-\cos\beta=\cos(\beta+\pi)$:

$$
\begin{aligned}
x
&=6\cos\left(2\pi t-\frac{\pi}{3}+\pi\right)\\
&=6\cos\left(2\pi t+\frac{2\pi}{3}\right)\text{ cm}.
\end{aligned}
$$

**Kết quả:** $x=6\cos\left(2\pi t+\dfrac{2\pi}{3}\right)$ cm.

---

# Bài tập

## Mức 1 — Nhận biết

### Câu 1

Chuyển động nào dưới đây là dao động cơ?

A. Một ô tô chạy thẳng đều trên đường.  
B. Một vật gắn lò xo chuyển động qua lại quanh vị trí cân bằng.  
C. Một viên đá rơi tự do.  
D. Một vệ tinh chuyển động tròn đều quanh Trái Đất.

### Câu 2

Đại lượng cho biết số dao động toàn phần vật thực hiện trong một giây là:

A. biên độ.  
B. chu kì.  
C. tần số.  
D. pha ban đầu.

### Câu 3

Trong phương trình:

$$
x=5\cos(4\pi t-\frac{\pi}{3})\text{ cm},
$$

tần số góc là:

A. $4$ rad/s.  
B. $4\pi$ rad/s.  
C. $2$ Hz.  
D. $\pi/3$ rad.

### Câu 4

Một vật dao động điều hòa có biên độ $A=7$ cm. Chiều dài quỹ đạo là:

A. $7$ cm.  
B. $14$ cm.  
C. $3,5$ cm.  
D. $49$ cm.

### Câu 5

Với phương trình:

$$
x=4\cos(10\pi t+\frac{\pi}{6})\text{ cm},
$$

chu kì là:

A. $0,1$ s.  
B. $0,2$ s.  
C. $5$ s.  
D. $10$ s.

---

## Mức 2 — Thông hiểu

### Câu 6

Một vật thực hiện 18 dao động toàn phần trong 9 s. Tần số của dao động bằng bao nhiêu?

### Câu 7

Cho:

$$
x=6\cos(5\pi t-\frac{\pi}{2})\text{ cm}.
$$

Tính:

1. chu kì;
2. tần số;
3. pha tại $t=0,3$ s.

### Câu 8

Cho:

$$
x=3\cos(2\pi t+\frac{\pi}{3})\text{ cm}.
$$

Tính li độ tại:

1. $t=0$;
2. $t=\dfrac16$ s;
3. $t=\dfrac13$ s.

### Câu 9

Một dao động có chu kì $0,25$ s.

Tính:

1. tần số;
2. tần số góc;
3. số dao động toàn phần trong 5 s.

---

## Mức 2 — Đúng/Sai

### Câu 10

Cho:

$$
x=4\cos\left(5\pi t+\frac{\pi}{6}\right)\text{ cm}.
$$

Xét các phát biểu:

a) Biên độ của dao động là $4$ cm.  
b) Tần số là $5\pi$ Hz.  
c) Tại $t=0$, li độ là $2\sqrt3$ cm.  
d) Chiều dài quỹ đạo là $8$ cm.

Hãy xác định đúng hoặc sai cho từng ý.

### Câu 11

Xét dao động điều hòa.

a) Pha dao động biến thiên tuyến tính theo thời gian.  
b) Cùng một li độ thì vật luôn có cùng một trạng thái chuyển động.  
c) Sau mỗi chu kì, trạng thái dao động lặp lại như cũ.  
d) Biên độ có thể nhận giá trị âm nếu pha ban đầu phù hợp.

Hãy xác định đúng hoặc sai.

---

## Mức 3 — Vận dụng

### Câu 12

Một vật có phương trình:

$$
x=-5\cos\left(4\pi t-\frac{\pi}{6}\right)\text{ cm}.
$$

1. Viết phương trình về dạng chuẩn với biên độ dương.
2. Xác định $A,T,f,\varphi$ của phương trình chuẩn.

### Câu 13

Một vật dao động điều hòa. Trong 6 s vật thực hiện 15 dao động toàn phần. Biên độ là 4 cm.

Tính:

1. chu kì;
2. tần số;
3. tần số góc;
4. chiều dài quỹ đạo.

### Câu 14

Một đồ thị li độ – thời gian có giá trị cực đại $+5$ cm và cực tiểu $-5$ cm. Hai đỉnh liên tiếp của đồ thị xuất hiện tại $t=0,2$ s và $t=0,8$ s.

Tính:

1. biên độ;
2. chu kì;
3. tần số;
4. tần số góc.

### Câu 15

Cho:

$$
x=10\cos\left(2\pi t+\frac{\pi}{3}\right)\text{ mm}.
$$

Trong khoảng thời gian 3 s, vật thực hiện bao nhiêu dao động toàn phần?

---

# Gợi ý

??? hint "Câu 7"
    Từ hệ số của $t$, đọc $\omega=5\pi$. Sau đó dùng $T=\dfrac{2\pi}{\omega}$ và $f=\dfrac1T$.

??? hint "Câu 12"
    Dùng $-\cos\alpha=\cos(\alpha+\pi)$ để đưa biên độ về số dương.

??? hint "Câu 14"
    Khoảng thời gian giữa hai đỉnh liên tiếp chính là một chu kì.

---

# Đáp án và lời giải

## Câu 1

**Đáp án: B.** Dao động cơ là chuyển động qua lại quanh vị trí cân bằng. Vật gắn lò xo ở phương án B có đúng đặc điểm này.

---

## Câu 2

**Đáp án: C.** Tần số là số dao động toàn phần vật thực hiện trong một giây.

---

## Câu 3

**Đáp án: B.** So sánh $x=5\cos\left(4\pi t-\dfrac{\pi}{3}\right)$ với $x=A\cos(\omega t+\varphi)$, hệ số của $t$ trong pha là $\omega$. Vì vậy $\omega=4\pi$ rad/s.

---

## Câu 4

**Đáp án: B.** Với $A=7$ cm, chiều dài quỹ đạo là $L=2A=14$ cm.

---

## Câu 5

**Đáp án: B.** Ta có $\omega=10\pi$ rad/s, nên

$$
T=\frac{2\pi}{\omega}=\frac{2\pi}{10\pi}=0,2\text{ s}.
$$

---

## Câu 6

Vật thực hiện $N=18$ dao động trong $\Delta t=9$ s, do đó $f=\dfrac{N}{\Delta t}=\dfrac{18}{9}=2$ Hz.

**Đáp án:** $f=2$ Hz.

---

## Câu 7

Từ $x=6\cos\left(5\pi t-\dfrac{\pi}{2}\right)$ cm, ta đọc được $\omega=5\pi$ rad/s.

- **Chu kì:** $T=\dfrac{2\pi}{5\pi}=0,4$ s.
- **Tần số:** $f=\dfrac1T=2,5$ Hz.
- **Pha tại $t=0,3$ s:** $\Phi=5\pi\cdot0,3-\dfrac{\pi}{2}=\pi$ rad.

**Kết quả:** $T=0,4$ s, $f=2,5$ Hz, $\Phi=\pi$ rad.

---

## Câu 8

Với $x=3\cos\left(2\pi t+\dfrac{\pi}{3}\right)$ cm, thay lần lượt từng thời điểm vào phương trình:

1. Tại $t=0$: $x=3\cos\dfrac{\pi}{3}=1,5$ cm.
2. Tại $t=\dfrac16$ s: pha $\Phi=2\pi\cdot\dfrac16+\dfrac{\pi}{3}=\dfrac{2\pi}{3}$, nên $x=3\cos\dfrac{2\pi}{3}=-1,5$ cm.
3. Tại $t=\dfrac13$ s: pha $\Phi=2\pi\cdot\dfrac13+\dfrac{\pi}{3}=\pi$, nên $x=3\cos\pi=-3$ cm.

**Kết quả:** $x(0)=1,5$ cm; $x\left(\dfrac16\right)=-1,5$ cm; $x\left(\dfrac13\right)=-3$ cm.

---

## Câu 9

Cho $T=0,25$ s.

- Tần số: $f=\dfrac1T=4$ Hz.
- Tần số góc: $\omega=2\pi f=8\pi$ rad/s.
- Trong 5 s, số dao động là $N=f\Delta t=4\cdot5=20$.

**Kết quả:** $f=4$ Hz, $\omega=8\pi$ rad/s, $N=20$.

---

## Câu 10

Với $x=4\cos\left(5\pi t+\dfrac{\pi}{6}\right)$ cm:

- **a) Đúng.** Biên độ $A=4$ cm.
- **b) Sai.** $5\pi$ là tần số góc, không phải tần số. Ta có $f=\dfrac{\omega}{2\pi}=\dfrac{5\pi}{2\pi}=2,5$ Hz.
- **c) Đúng.** Tại $t=0$, $x=4\cos\dfrac{\pi}{6}=2\sqrt3$ cm.
- **d) Đúng.** Chiều dài quỹ đạo $L=2A=8$ cm.

**Kết luận:** a Đúng; b Sai; c Đúng; d Đúng.

---

## Câu 11

- **a) Đúng.** Pha $\Phi=\omega t+\varphi$ là hàm bậc nhất theo $t$.
- **b) Sai.** Vật có thể đi qua cùng một li độ theo hai chiều khác nhau; cùng li độ chưa đủ để khẳng định cùng trạng thái chuyển động.
- **c) Đúng.** Trạng thái lặp lại sau những khoảng thời gian bằng nhau là đặc trưng của dao động tuần hoàn.
- **d) Sai.** Biên độ theo quy ước luôn dương: $A>0$.

**Kết luận:** a Đúng; b Sai; c Đúng; d Sai.

---

## Câu 12

Ban đầu:

$$
x=-5\cos\left(4\pi t-\frac{\pi}{6}\right)\text{ cm}.
$$

Dùng $-\cos\alpha=\cos(\alpha+\pi)$:

$$
\begin{aligned}
x
&=5\cos\left(4\pi t-\frac{\pi}{6}+\pi\right)\\
&=5\cos\left(4\pi t+\frac{5\pi}{6}\right)\text{ cm}.
\end{aligned}
$$

Sau khi chuẩn hóa, đọc được $A=5$ cm, $\omega=4\pi$ rad/s và $\varphi=\dfrac{5\pi}{6}$ rad. Do đó $T=\dfrac{2\pi}{4\pi}=0,5$ s và $f=\dfrac1T=2$ Hz.

**Kết quả:** $A=5$ cm, $T=0,5$ s, $f=2$ Hz, $\varphi=\dfrac{5\pi}{6}$ rad.

---

## Câu 13

Trong $\Delta t=6$ s, vật thực hiện $N=15$ dao động và có biên độ $A=4$ cm.

- Chu kì: $T=\dfrac{\Delta t}{N}=\dfrac6{15}=0,4$ s.
- Tần số: $f=\dfrac{N}{\Delta t}=\dfrac{15}{6}=2,5$ Hz.
- Tần số góc: $\omega=2\pi f=5\pi$ rad/s.
- Chiều dài quỹ đạo: $L=2A=8$ cm.

**Kết quả:** $T=0,4$ s, $f=2,5$ Hz, $\omega=5\pi$ rad/s, $L=8$ cm.

---

## Câu 14

Từ đồ thị, $x_{\max}=+5$ cm và $x_{\min}=-5$ cm nên $A=5$ cm. Hai đỉnh liên tiếp ở $0,2$ s và $0,8$ s, vì vậy $T=0,8-0,2=0,6$ s.

Suy ra $f=\dfrac1T=\dfrac53$ Hz và $\omega=2\pi f=\dfrac{10\pi}{3}$ rad/s.

**Kết quả:** $A=5$ cm, $T=0,6$ s, $f=\dfrac53$ Hz, $\omega=\dfrac{10\pi}{3}$ rad/s.

---

## Câu 15

Với $x=10\cos\left(2\pi t+\dfrac{\pi}{3}\right)$ mm, ta có $\omega=2\pi$ rad/s nên $f=\dfrac{\omega}{2\pi}=1$ Hz.

Trong $3$ s, số dao động toàn phần là $N=f\Delta t=1\cdot3=3$.

**Kết quả:** $N=3$ dao động toàn phần.

---

## Tóm tắt

1. Dao động cơ là chuyển động qua lại quanh vị trí cân bằng.
2. Dao động tuần hoàn có trạng thái lặp lại sau những khoảng thời gian bằng nhau.
3. Dao động điều hòa có phương trình $x=A\cos(\omega t+\varphi)$.
4. Biên độ thỏa $A>0$ và $-A\le x\le A$.
5. Chiều dài quỹ đạo là $L=2A$.
6. Chu kì và tần số liên hệ bởi $f=\frac1T$.
7. Tần số góc: $\omega=2\pi f=\frac{2\pi}{T}$.
8. Pha dao động: $\Phi=\omega t+\varphi$.

## 5 điều cần nhớ

1. Hệ số của $t$ trong phương trình chuẩn là $\omega$, không phải $f$.
2. Biên độ luôn lấy dương.
3. Li độ có thể âm; quãng đường không âm.
4. Cùng vị trí chưa chắc cùng trạng thái.
5. Muốn đọc chu kì từ đồ thị, phải chọn hai trạng thái lặp lại như cũ.


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/01-harmonic-oscillation-foundations/exercises.md)
- [Đáp án và lời giải](practice/01-harmonic-oscillation-foundations/solutions.md)

---

[↑ Chương 1](./index.md)
