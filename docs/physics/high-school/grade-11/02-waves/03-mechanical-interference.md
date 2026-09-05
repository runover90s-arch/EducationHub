---
title: "Bài 3 — Giao thoa sóng cơ"
description: "Điều kiện nguồn kết hợp, tổng hợp hai sóng, cực đại–cực tiểu và phương pháp đếm điểm giao thoa."
order: 3
difficulty: "standard-applied"
prerequisites:
  - wave-equation-phase-graphs
tags:
  - physics
  - grade-11
  - waves
  - interference
---

# Bài 3 — Giao thoa sóng cơ

## Mục tiêu

Bạn cần:

- hiểu nguồn kết hợp và giao thoa;
- lập độ lệch pha tại một điểm từ hiệu đường đi;
- xác định điều kiện cực đại, cực tiểu cho nguồn cùng pha và có lệch pha;
- tính biên độ tổng hợp;
- đếm số điểm cực đại/cực tiểu trên đoạn, đường hoặc miền đơn giản;
- tránh sai dấu khi dùng hiệu đường đi.

## 1. Hiện tượng giao thoa

Khi hai sóng kết hợp gặp nhau, tại mỗi điểm li độ tổng bằng tổng đại số các li độ thành phần. Vì độ lệch pha thay đổi theo vị trí, có nơi dao động được tăng cường, có nơi bị giảm mạnh hoặc triệt tiêu.

### Nguồn kết hợp

Trong mô hình phổ thông, hai nguồn được gọi là kết hợp khi chúng:

- dao động cùng phương;
- cùng tần số;
- có độ lệch pha không đổi theo thời gian.

Biên độ hai nguồn không bắt buộc bằng nhau để có giao thoa, nhưng nhiều bài cơ bản giả sử bằng nhau.

## 2. Phương trình tại điểm M

Hai nguồn $S_1,S_2$ tạo sóng đến $M$, có khoảng cách $d_1,d_2$.

Giả sử:

$$
\begin{aligned}
&u_1=A_1\cos(\omega t+\varphi_1-kd_1)\\
&u_2=A_2\cos(\omega t+\varphi_2-kd_2).
\end{aligned}
$$

Độ lệch pha tại M:

$$
\Delta\Phi=\Phi_2-\Phi_1
=(\varphi_2-\varphi_1)-k(d_2-d_1).
$$

Đặt $\Delta\varphi_0=\varphi_2-\varphi_1$ và hiệu đường đi $\Delta d=d_2-d_1$:

$$
\boxed{\Delta\Phi=\Delta\varphi_0-\frac{2\pi\Delta d}{\lambda}}.
$$

## 3. Biên độ tổng hợp

Biên độ tại M thỏa:

$$
\boxed{
A_M^2=A_1^2+A_2^2+2A_1A_2\cos\Delta\Phi
}.
$$

Nếu $A_1=A_2=a$:

$$
A_M=2a\left|\cos\frac{\Delta\Phi}{2}\right|.
$$

### Cực đại và cực tiểu

- cực đại khi $\Delta\Phi=2k\pi$;
- cực tiểu hoàn toàn khi $A_1=A_2$ và $\Delta\Phi=(2k+1)\pi$.

Nếu hai biên độ không bằng nhau, “cực tiểu” có biên độ nhỏ nhất $|A_1-A_2|$, không nhất thiết bằng 0.

## 4. Hai nguồn cùng pha

Với $\Delta\varphi_0=0$:

### Cực đại

$$
\boxed{\Delta d=k\lambda}.
$$

### Cực tiểu

$$
\boxed{\Delta d=\left(k+\frac12\right)\lambda}.
$$

Ở đây $k$ là số nguyên.

## 5. Hai nguồn ngược pha

Nếu $\Delta\varphi_0=\pi$ thì điều kiện đổi vai:

- cực đại: $\Delta d=(k+\tfrac12)\lambda$;
- cực tiểu: $\Delta d=k\lambda$.

Đây là lý do không nên học thuộc điều kiện cực đại mà bỏ qua pha nguồn.

## 6. Hai nguồn có độ lệch pha bất kì

Từ điều kiện $\Delta\Phi=2k\pi$:

$$
\Delta\varphi_0-\frac{2\pi\Delta d}{\lambda}=2k\pi.
$$

Suy ra một cách viết:

$$
\Delta d=\left(\frac{\Delta\varphi_0}{2\pi}-k\right)\lambda.
$$

Vì $k$ chạy qua mọi số nguyên, có thể đổi tên chỉ số để được dạng tương đương. Quan trọng là **lập từ phương trình pha**, không phụ thuộc thuộc lòng một công thức dấu.

## 7. Hình học của hiệu đường đi

Với hai nguồn cách nhau $S_1S_2=a$, mọi điểm M thỏa:

$$
|\Delta d|=|d_2-d_1|\le a.
$$

Do đó khi đếm vân trên đoạn nối hai nguồn, chỉ cần tìm các số nguyên $k$ sao cho điều kiện cực đại/cực tiểu đồng thời thỏa miền hiệu đường đi.

### Quy trình đếm

1. Viết điều kiện cực đại hoặc cực tiểu.
2. Xác định miền của $\Delta d$ trên đoạn/miền cần xét.
3. Biến thành bất phương trình đối với $k$.
4. Đếm số nguyên thỏa.
5. Kiểm tra đầu mút có được tính hay không.

## 8. Khoảng cách giữa các cực trị trên đoạn nối hai nguồn

Trên đoạn $S_1S_2$, nếu đặt trục có gốc tại trung điểm, hiệu đường đi biến thiên tuyến tính theo tọa độ. Với hai nguồn cùng pha, các cực đại liên tiếp thường cách nhau $\lambda/2$ trên đoạn nối nguồn; cực đại và cực tiểu gần nhau cách $\lambda/4$.

!!! note "Chỉ dùng đúng hình học"
    Quy tắc $\lambda/2$ này là kết quả riêng trên đoạn nối hai nguồn trong cấu hình chuẩn, không phải khoảng cách giữa mọi hai đường cực đại trong mặt phẳng.

## 9. Điểm trên trung trực

Trên trung trực $d_1=d_2$, nên $\Delta d=0$. Trạng thái tại đó chỉ còn phụ thuộc độ lệch pha ban đầu của hai nguồn:

- nguồn cùng pha → trung trực là cực đại;
- nguồn ngược pha → trung trực là cực tiểu nếu biên độ bằng nhau.

## 10. Ví dụ

### Ví dụ 1 — Cực đại cơ bản

Hai nguồn cùng pha, $\lambda=2$ cm. Điểm M có $d_2-d_1=6$ cm. Vì $\Delta d=3\lambda$, M thuộc cực đại.

### Ví dụ 2 — Biên độ tại M

Hai nguồn cùng biên độ $a=3$ mm. Tại M, hai sóng lệch pha $2\pi/3$:

$$
A_M=2a|\cos(\pi/3)|=3\ \text{mm}.
$$

### Ví dụ 3 — Đếm cực đại trên đoạn nối nguồn

Hai nguồn cùng pha cách nhau $a=10$ cm, $\lambda=2$ cm. Trên đoạn nối nguồn, $|\Delta d|\le10$ cm. Cực đại khi $\Delta d=2k$ cm, nên $|k|\le5$. Nếu tính cả hai nguồn theo mô hình toán học, có 11 giá trị $k$; trong bài thực nghiệm có thể loại đầu mút nếu đề quy định chỉ xét điểm trong khoảng.

## 11. Bẫy thường gặp

!!! warning "Hiệu đường đi có dấu"
    Khi chỉ đếm đối xứng có thể dùng $|\Delta d|$. Khi lập pha với nguồn lệch pha, nên giữ $\Delta d=d_2-d_1$ có dấu để tránh mất thông tin.

!!! warning "Nguồn không cùng biên độ"
    Điều kiện pha cho vị trí cực đại/cực tiểu vẫn có ý nghĩa, nhưng cực tiểu không triệt tiêu hoàn toàn nếu $A_1\ne A_2$.

## 🔬 Mở rộng và nâng cao

Đường $\Delta d=$ hằng số trong mặt phẳng là các nhánh hyperbol có hai tiêu điểm tại hai nguồn. Vì vậy hệ vân giao thoa cơ hai nguồn điểm có cấu trúc hyperbol.

Đây là liên hệ hình học quan trọng nhưng không cần dùng phương trình hyperbol cho phần nền.

## Tóm tắt

- Giao thoa là hệ quả của chồng chất sóng kết hợp.
- $\Delta\Phi=\Delta\varphi_0-2\pi\Delta d/\lambda$.
- $A_M^2=A_1^2+A_2^2+2A_1A_2\cos\Delta\Phi$.
- Nguồn cùng pha: cực đại $\Delta d=k\lambda$, cực tiểu $\Delta d=(k+1/2)\lambda$.
- Đếm điểm = điều kiện pha + miền hình học.

## 5 điều cần nhớ

1. Luôn xác định pha ban đầu của hai nguồn.
2. Hiệu đường đi quyết định phần pha do truyền.
3. Trung trực có $\Delta d=0$.
4. Cực tiểu bằng 0 chỉ khi hai biên độ tới bằng nhau và ngược pha.
5. Khi đếm, phải kiểm tra biên và đầu mút.

## Các dạng bài trọng tâm

Các nhóm bài dưới đây được tổ chức theo dấu hiệu nhận biết và công cụ giải để người học chọn phương pháp phù hợp và tự kiểm tra kết quả.

### Dạng 6 — Điều kiện cực đại, cực tiểu

Viết hiệu đường đi $\Delta d=|d_2-d_1|$, sau đó áp dụng điều kiện giao thoa tương ứng với quan hệ pha của hai nguồn. Với hai nguồn cùng pha: cực đại khi $\Delta d=k\lambda$, cực tiểu khi $\Delta d=(k+1/2)\lambda$.

Khi nguồn lệch pha, phải đưa độ lệch pha ban đầu vào điều kiện; không dùng máy móc công thức nguồn cùng pha.

### Dạng 7 — Phương trình giao thoa, biên độ giao thoa

Viết dao động do từng nguồn truyền tới điểm xét, bảo toàn đúng phần trễ pha do quãng đường rồi cộng hai dao động cùng tần số. Có thể dùng công thức tổng hai cos để rút biên độ tổng hợp.

Biên độ tại điểm phụ thuộc hiệu pha hai sóng tới, còn pha chung phụ thuộc cả tổng quãng đường; hai đại lượng này không được nhầm lẫn.

### Dạng 8 — Số điểm cực đại, cực tiểu

Lập điều kiện cực đại hoặc cực tiểu dưới dạng bất đẳng thức cho số nguyên $k$ từ miền giá trị của hiệu đường đi trên đoạn đang xét. Sau đó đếm số giá trị nguyên thỏa mãn.

Phải xem hai đầu đoạn có được tính hay không và chúng có đúng là điểm cực đại/cực tiểu theo điều kiện hay không; đây là nguồn sai số đếm phổ biến.

<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/03-mechanical-interference/exercises.md)
- [Đáp án và lời giải](practice/03-mechanical-interference/solutions.md)

---

[← Bài 2](02-wave-equation-phase-graphs.md) | [↑ Chương](index.md) | [Bài 4 →](04-standing-waves.md)
