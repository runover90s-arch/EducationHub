---
title: "Bài 6 — Ghép nguồn thành bộ"
description: "Ghép nối tiếp, song song, hỗn hợp đối xứng và lựa chọn cách ghép nguồn."
order: 6
difficulty: "applied"
prerequisites:
  - full-circuit-ohm-law
tags:
  - physics
  - grade-11
  - circuits
  - source-combination
---

# Bài 6 — Ghép nguồn thành bộ

## Mục tiêu

Bạn cần:

- tìm suất điện động và điện trở trong của bộ nguồn;
- ghép nối tiếp, song song các nguồn giống nhau;
- xử lí bộ hỗn hợp đối xứng;
- xác định dòng mạch ngoài;
- chọn số hàng–số nguồn mỗi hàng phù hợp với tải;
- tránh ghép song song nguồn khác suất điện động theo công thức nguồn giống nhau.

## 1. Ghép nối tiếp

Các nguồn nối tiếp cùng chiều:

$$
\begin{aligned}
&\boxed{\mathcal E_b=\mathcal E_1+\mathcal E_2+\cdots}\\
&\boxed{r_b=r_1+r_2+\cdots}.
\end{aligned}
$$

Nếu n nguồn giống nhau:

$$
\mathcal E_b=n\mathcal E,\qquad r_b=nr.
$$

### Nguồn mắc ngược
Suất điện động tổng phải cộng **đại số** theo chiều vòng mạch; điện trở trong vẫn cộng dương.

## 2. Ghép song song các nguồn giống nhau

n nguồn giống nhau $(\mathcal E,r)$ mắc song song đúng cực:

$$
\begin{aligned}
&\boxed{\mathcal E_b=\mathcal E}\\
&\boxed{r_b=\frac{r}{n}}.
\end{aligned}
$$

Ghép song song giúp giảm điện trở trong và tăng khả năng cung cấp dòng.

## 3. Vì sao nguồn khác E không nên dùng công thức trên?

Nếu các nguồn có suất điện động khác nhau mắc song song trực tiếp, ngay cả khi không có tải có thể xuất hiện dòng tuần hoàn giữa các nguồn. Bài toán cần mô hình tổng quát hơn.

Trong phần cơ bản, công thức song song đơn giản chỉ dùng cho các nguồn giống nhau hoặc khi đề cho điều kiện phù hợp.

## 4. Bộ hỗn hợp đối xứng

Có N nguồn giống nhau, ghép thành:

- m nhánh song song;
- mỗi nhánh có n nguồn nối tiếp,

với:

$$
N=mn.
$$

Khi các nhánh giống nhau:

$$
\begin{aligned}
&\boxed{\mathcal E_b=n\mathcal E}\\
&\boxed{r_b=\frac{nr}{m}}.
\end{aligned}
$$

Nối với tải R:

$$
I=\frac{n\mathcal E}{R+nr/m}.
$$

## 5. Viết theo tổng N

Vì $m=N/n$:

$$
r_b=\frac{n^2r}{N}.
$$

Do đó:

$$
I=\frac{n\mathcal E}{R+n^2r/N}.
$$

Biểu thức giúp chọn n để dòng lớn trong các bài tối ưu số hàng.

## 6. Điều kiện tối ưu liên tục

Xem n là biến liên tục tạm thời, dòng đạt cực đại khi điện trở trong bộ gần bằng tải:

$$
r_b\approx R.
$$

Tức:

$$
\frac{n^2r}{N}\approx R.
$$

Suy ra:

$$
n\approx\sqrt{\frac{NR}{r}}.
$$

Sau đó phải kiểm tra n là số nguyên và chia hết N theo cấu hình thực tế.

Đây là cách chọn ứng viên, không thay cho kiểm tra ràng buộc nguyên.

## 7. Giới hạn số nguồn/hàng

Trong bài đèn hoặc tải có giới hạn, ngoài tối đa dòng/công suất còn phải kiểm tra:

- điện áp trên tải;
- dòng định mức;
- công suất từng nguồn;
- số nguồn nguyên;
- các nhánh đối xứng.

Không tối ưu một đại lượng rồi bỏ điều kiện an toàn.

## 8. Ví dụ

### Ví dụ 1 — Nối tiếp
3 pin 1,5 V, r=0,2 Ω nối tiếp:

$\mathcal E_b=4,5$ V, $r_b=0,6$ Ω.

### Ví dụ 2 — Song song
4 pin giống nhau song song:

$\mathcal E_b=1,5$ V, $r_b=0,05$ Ω.

### Ví dụ 3 — Hỗn hợp
12 nguồn, mỗi nguồn E,r. Ghép 3 nhánh, mỗi nhánh 4 nguồn nối tiếp:

$\mathcal E_b=4E$, $r_b=4r/3$.

## 9. Bẫy

!!! danger "Sai cực"
    Khi ghép nối tiếp, phải xác định cực nguồn. Một nguồn ngược chiều làm suất điện động đại số bị trừ.

!!! warning "Song song"
    Không áp dụng $\mathcal E_b=\mathcal E$ cho các nguồn tùy ý khác nhau.

## Tóm tắt

- Nối tiếp: E cộng, r cộng.
- Song song nguồn giống: E giữ, r giảm n lần.
- Hỗn hợp đối xứng: $E_b=nE$, $r_b=nr/m$.
- Tối ưu tải thường gắn với $r_b\approx R$.
- Luôn kiểm tra cấu hình nguyên và định mức.

## 5 điều cần nhớ

1. Gắn dấu cho E khi nguồn có thể ngược.
2. r luôn là đại lượng dương.
3. Nhánh song song phải đối xứng trong công thức cơ bản.
4. N=mn.
5. Tối ưu không bỏ qua giới hạn thiết bị.

## Các dạng bài trọng tâm

Các nhóm bài dưới đây được tổ chức theo dấu hiệu nhận biết và công cụ giải để người học chọn phương pháp phù hợp và tự kiểm tra kết quả.

### Dạng 1 — Nguồn điện ghép nối tiếp

Với các nguồn mắc nối tiếp cùng chiều, suất điện động bộ bằng tổng các suất điện động và điện trở trong bộ bằng tổng điện trở trong. Nếu các nguồn giống nhau, $\mathcal E_b=n\mathcal E$, $r_b=nr$. Sau đó coi cả bộ như một nguồn duy nhất.

### Dạng 2 — Nguồn điện ghép song song

Chỉ áp dụng công thức đơn giản khi các nguồn giống nhau và mắc đúng cực tương ứng: $\mathcal E_b=\mathcal E$, $r_b=r/n$. Với nguồn không giống nhau, cần phương pháp mạch tổng quát thay vì dùng công thức này máy móc.

### Dạng 3 — Nguồn điện ghép xung đối

Chọn chiều vòng mạch trước, gán dấu suất điện động theo chiều đi qua nguồn. Suất điện động tương đương là tổng đại số, còn điện trở trong luôn cộng dương. Sau khi tính dòng, nếu kết quả âm thì dòng thực tế ngược chiều đã giả thiết.

### Dạng 4 — Nguồn điện ghép hỗn hợp đối xứng

Xác định số nguồn trong mỗi nhánh nối tiếp và số nhánh song song. Tính suất điện động và điện trở trong của một nhánh trước, rồi ghép các nhánh giống nhau song song. Kiểm tra tổng số nguồn bằng tích hai con số này.

<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/06-source-combinations/exercises.md)
- [Đáp án và lời giải](practice/06-source-combinations/solutions.md)

---

[← Bài 5](05-full-circuit-ohm-law.md) | [↑ Chương](index.md) | [Bài 7 →](07-circuit-reading-meters.md)
