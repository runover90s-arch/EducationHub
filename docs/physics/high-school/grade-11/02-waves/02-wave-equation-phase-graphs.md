---
title: "Bài 2 — Phương trình sóng, độ lệch pha và đồ thị"
description: "Lập phương trình truyền sóng, xác định pha theo không gian–thời gian và khai thác đồ thị sóng."
order: 2
difficulty: "standard-applied"
prerequisites:
  - mechanical-wave-basics
  - harmonic-oscillation
tags:
  - physics
  - grade-11
  - waves
  - wave-equation
---

# Bài 2 — Phương trình sóng, độ lệch pha và đồ thị

## Mục tiêu

Bạn cần:

- lập phương trình sóng từ phương trình tại nguồn;
- hiểu dấu trước phần $kx$;
- tính pha tại một điểm, độ lệch pha giữa hai điểm;
- suy ra chiều truyền sóng từ hai phương trình;
- đọc đồ thị $u-x$ và $u-t$;
- xử lí bài “sau bao lâu trạng thái tại A truyền tới B”.

## 1. Mô hình cơ bản

Giả sử tại nguồn $O$:

$$
u_O=A\cos(\omega t+\varphi_0).
$$

Sóng truyền theo chiều dương $Ox$ với tốc độ $v$. Điểm $M$ cách $O$ một đoạn $x$ nhận trạng thái của nguồn trễ một thời gian $x/v$:

$$
u_M=A\cos\left[\omega\left(t-\frac{x}{v}\right)+\varphi_0\right].
$$

Vì $\omega/v=2\pi/\lambda$, ta được:

$$
\boxed{u(x,t)=A\cos\left(\omega t-\frac{2\pi x}{\lambda}+\varphi_0\right)}.
$$

Đặt số sóng $k=2\pi/\lambda$:

$$
u=A\cos(\omega t-kx+\varphi_0).
$$

## 2. Sóng truyền theo chiều âm

Nếu sóng truyền theo chiều âm $Ox$, điểm có tọa độ $x$ tương ứng với dạng:

$$
\boxed{u=A\cos(\omega t+kx+\varphi_0)}.
$$

### Quy tắc dấu

- dạng $\omega t-kx$ → truyền theo chiều $+x$;
- dạng $\omega t+kx$ → truyền theo chiều $-x$.

Quy tắc đúng khi biểu thức được viết theo dạng pha chuẩn với hệ số $\omega>0$, $k>0$.

## 3. Pha tại một điểm

Với sóng theo $+x$:

$$
\Phi(x,t)=\omega t-kx+\varphi_0.
$$

Tại cùng thời điểm, điểm xa hơn theo chiều truyền có pha **trễ hơn**.

Giữa hai điểm $M,N$ với $x_N-x_M=d$:

$$
\Delta\varphi=\Phi_N-\Phi_M=-kd=-\frac{2\pi d}{\lambda}.
$$

Nếu đề chỉ hỏi độ lệch pha, thường dùng độ lớn $2\pi d/\lambda$ rồi xét modulo $2\pi$.

## 4. Thời gian trễ

Trạng thái dao động truyền từ $M$ đến $N$ cách nhau $d$ theo phương truyền trong thời gian:

$$
\boxed{\Delta t=\frac{d}{v}}.
$$

Cũng có thể suy từ pha:

$$
\frac{\Delta t}{T}=\frac{d}{\lambda}.
$$

## 5. Từ phương trình tìm các đại lượng

Với:

$$
u=A\cos(\omega t-kx+\varphi),
$$

đọc được:

- biên độ $A$;
- $\omega$ → $T=2\pi/\omega$, $f=\omega/(2\pi)$;
- $k$ → $\lambda=2\pi/k$;
- $v=\omega/k=\lambda f$;
- dấu của $kx$ → chiều truyền.

### Ví dụ

Cho $u=3\cos(20\pi t-4\pi x+\pi/6)$ cm, $x$ tính bằng m.

Ta có:

- $A=3$ cm;
- $f=10$ Hz;
- $\lambda=0,5$ m;
- $v=5$ m/s;
- sóng truyền theo $+x$.

## 6. Từ phương trình tại hai điểm tìm khoảng cách

Nếu:

$$
u_M=A\cos(\omega t+\varphi_M),\qquad
u_N=A\cos(\omega t+\varphi_N),
$$

thì độ lệch pha đo được cho ta:

$$
|\varphi_N-\varphi_M|=\frac{2\pi d}{\lambda}
$$

**chỉ khi** biết hai điểm nằm trên cùng phương truyền và độ lệch pha chưa bị mất thông tin do modulo $2\pi$.

Trong bài thực tế, nếu chỉ biết hai phương trình theo cos, ta thường có họ nghiệm:

$$
d=\left(k+\frac{\Delta\varphi_{\text{rút gọn}}}{2\pi}\right)\lambda
$$

hoặc dạng tương đương tùy chiều truyền.

!!! warning "Modulo pha"
    Hai pha chênh nhau $2\pi$, $4\pi$, ... mô tả cùng trạng thái. Vì vậy từ pha rút gọn không luôn suy ra duy nhất khoảng cách nếu đề chưa bổ sung miền của $d$.

## 7. Đồ thị u–t

Đồ thị $u-t$ tại một vị trí cố định là dao động điều hòa của **một phần tử**.

Có thể đọc:

- $A$ từ giá trị cực đại;
- $T$ từ khoảng thời gian lặp lại cùng trạng thái;
- pha ban đầu từ $u(0)$ và chiều chuyển động.

## 8. Đồ thị u–x

Đồ thị $u-x$ tại một thời điểm cố định là ảnh không gian.

Có thể đọc:

- $A$;
- $\lambda$;
- quan hệ pha giữa các điểm;
- kết hợp chiều truyền để suy chiều chuyển động của phần tử.

### Liên hệ hai đồ thị

Một đoạn dài $\lambda$ trên trục $x$ tương ứng với một chu kì $T$ trên trục $t$:

$$
\frac{x}{\lambda}\longleftrightarrow\frac{t}{T}.
$$

Đây là ý tưởng cốt lõi để chuyển bài hình học trên đồ thị thành bài pha.

## 9. Xác định chiều truyền từ trạng thái tức thời

Nếu biết một điểm $M$ đang có $u>0$ và đang chuyển động lên ($v_M>0$), quan sát độ dốc của đường cong tại $M$:

- nếu độ dốc $\partial u/\partial x<0$, phù hợp sóng đi theo $+x$;
- nếu độ dốc $\partial u/\partial x>0$, phù hợp sóng đi theo $-x$.

Không cần thuộc hình mẫu; hãy dùng quan hệ dấu giữa vận tốc dao động và độ dốc.

## 10. Ví dụ tổng hợp

### Ví dụ 1 — Viết phương trình tại điểm M

Nguồn $O$: $u_O=4\cos(10\pi t)$ mm. Sóng truyền theo $+x$ với $v=2$ m/s. Điểm $M$ cách O $30$ cm.

$f=5$ Hz nên $\lambda=v/f=0,4$ m. Độ trễ pha từ O đến M:

$$
\frac{2\pi x}{\lambda}=2\pi\frac{0,30}{0,40}=\frac{3\pi}{2}.
$$

Vậy:

$$
u_M=4\cos(10\pi t-3\pi/2)\ \text{mm}.
$$

### Ví dụ 2 — Tìm chiều truyền

Cho $u=2\cos(50t+5x)$ cm. Hệ số $x$ mang dấu cộng nên sóng truyền theo chiều âm $Ox$.

### Ví dụ 3 — Tìm trạng thái trễ

Hai điểm cách nhau $12$ cm, tốc độ truyền $0,6$ m/s. Thời gian truyền từ điểm trước đến điểm sau là $0,12/0,6=0,20$ s.

## 11. Lỗi thường gặp

!!! warning "Nhầm pha không gian"
    Trong $\omega t-kx+\varphi_0$, hệ số $k$ có đơn vị rad/m. Không được đọc $k$ trực tiếp thành bước sóng.

!!! warning "Nhầm dấu chiều truyền"
    Phải đưa phương trình về dạng có $\omega>0$. Nếu bạn nhân cả pha với $-1$ rồi dùng tính chẵn của cos, dấu trước $kx$ có thể đổi cùng dấu trước $\omega$; hãy chuẩn hóa trước khi kết luận.

## Tóm tắt

- Sóng theo $+x$: $u=A\cos(\omega t-kx+\varphi_0)$.
- Sóng theo $-x$: $u=A\cos(\omega t+kx+\varphi_0)$.
- $k=2\pi/\lambda$; $v=\omega/k$.
- Độ lệch pha theo khoảng cách: $kd$.
- Thời gian trễ: $d/v$.
- $u-t$ mô tả một điểm theo thời gian; $u-x$ mô tả nhiều điểm tại cùng thời điểm.

## 5 điều cần nhớ

1. Dấu của $kx$ cho chiều truyền sau khi chuẩn hóa phương trình.
2. Pha giảm theo $x$ khi sóng đi theo $+x$.
3. Pha chỉ xác định modulo $2\pi$.
4. Một bước sóng tương ứng một chu kì về pha.
5. Đừng dùng tốc độ dao động của phần tử thay cho tốc độ truyền sóng.

## Các dạng bài trọng tâm

Các nhóm bài dưới đây được tổ chức theo dấu hiệu nhận biết và công cụ giải để người học chọn phương pháp phù hợp và tự kiểm tra kết quả.

### Dạng 1 — Quan sát đồ thị sóng để xác định chu kì, tần số, biên độ và tốc độ truyền sóng

Trước hết xác định đồ thị là ảnh chụp theo không gian $u-x$ hay diễn biến theo thời gian $u-t$. Trên $u-x$, khoảng cách giữa hai điểm gần nhất cùng pha là bước sóng; trên $u-t$, khoảng thời gian giữa hai trạng thái lặp lại là chu kì.

Sau khi có $\lambda$ và $T$ hoặc $f$, suy ra tốc độ truyền $v=\lambda/T=\lambda f$. Khi xác định chiều truyền từ ảnh chụp sóng, cần kết hợp chiều vận tốc tức thời của một phần tử với độ dốc cục bộ của đường sóng.

### Dạng 2 — Độ lệch pha giữa hai phần tử

Hai điểm trên cùng phương truyền sóng cách nhau $\Delta x$ có độ lệch pha theo độ lớn $|\Delta\varphi|=2\pi\Delta x/\lambda$. Từ đó nhận ra cùng pha, ngược pha, vuông pha hoặc một độ lệch pha cụ thể.

Điểm dễ sai là bỏ qua tính tuần hoàn của pha. Khi tìm khoảng cách, nghiệm phải có thêm bội nguyên của bước sóng nếu đề hỏi tất cả vị trí; khi hỏi khoảng cách ngắn nhất thì chọn nghiệm dương nhỏ nhất.

### Dạng 3 — Bài toán khoảng cách giữa các phần tử

Dạng này đảo ngược quan hệ pha–khoảng cách. Hãy viết điều kiện pha trước, sau đó chuyển sang $\Delta x$. Ví dụ cùng pha cho $\Delta x=k\lambda$, ngược pha cho $\Delta x=(k+1/2)\lambda$.

Nếu hai điểm nằm trong một đoạn hữu hạn, sau khi lập công thức phải dùng điều kiện hình học của đoạn để giới hạn số nguyên $k$; không đếm bằng trực giác.

### Dạng 4 — Bài tập liên quan đến phương truyền sóng

**Dấu hiệu nhận biết.** Đề cho ảnh dạng sóng ở một thời điểm, trạng thái chuyển động của một phần tử, hoặc hỏi sóng đang truyền theo chiều nào.

**Kiến thức cần dùng.** Với sóng chạy, trạng thái theo không gian và theo thời gian liên hệ qua phương trình sóng. Một điểm ở phía trước theo chiều truyền nhận cùng trạng thái pha muộn hơn điểm phía sau.

**Phương pháp.**

1. Chọn một điểm trên hình có độ dốc không bằng 0 và xác định chiều vận tốc tức thời của phần tử nếu đề cho.
2. Dùng quy tắc dịch chuyển dạng sóng sau một khoảng thời gian rất nhỏ: hình dạng phải tịnh tiến theo chiều truyền.
3. Đối chiếu dấu độ dốc theo không gian với dấu vận tốc dao động để kết luận chiều truyền.
4. Nếu đề cho phương trình, kiểm tra dấu trước phần phụ thuộc tọa độ: dạng $\omega t-kx$ và $\omega t+kx$ tương ứng hai chiều truyền ngược nhau theo quy ước trục.

**Bẫy thường gặp.** Tốc độ truyền sóng không phải tốc độ dao động của phần tử môi trường. Phần tử chỉ dao động quanh vị trí cân bằng, không chạy theo ngọn sóng.

<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/02-wave-equation-phase-graphs/exercises.md)
- [Đáp án và lời giải](practice/02-wave-equation-phase-graphs/solutions.md)

---

[← Bài 1](01-mechanical-wave-basics.md) | [↑ Chương](index.md) | [Bài 3 →](03-mechanical-interference.md)
