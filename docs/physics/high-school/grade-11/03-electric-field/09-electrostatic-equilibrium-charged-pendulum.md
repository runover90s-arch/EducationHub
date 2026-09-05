---
title: "Bài 9 — Cân bằng điện tích và con lắc trong điện trường"
description: "Hệ điện tích cân bằng, điểm điện trường bằng không, vật tích điện treo dây và các bài lực điện–trọng lực."
order: 9
difficulty: "applied-advanced"
prerequisites:
  - coulomb-law
  - field-superposition-equilibrium
tags:
  - physics
  - grade-11
  - electrostatics
  - equilibrium
---

# Bài 9 — Cân bằng điện tích và con lắc trong điện trường

## Mục tiêu

Bạn cần:

- phân biệt bài tìm $\vec E=0$ với bài tổng lực lên một điện tích bằng 0;
- giải hệ ba điện tích thẳng hàng ở trạng thái cân bằng;
- xử lí vật tích điện treo bằng dây trong điện trường đều;
- kết hợp lực điện với trọng lực và lực căng;
- nhận biết khi nào dấu điện tích quyết định hướng lực nhưng không đổi độ lớn biểu thức.

## 1. Hai bài toán thường bị trộn lẫn

### Tìm điểm có điện trường tổng hợp bằng 0

Ta xét **điện trường do các điện tích nguồn** tại điểm M:

$$
\vec E(M)=\vec E_1+\vec E_2+\cdots=\vec0.
$$

Không cần đặt điện tích thử thật tại M.

### Tìm vị trí để một điện tích q cân bằng

Ta xét tổng lực lên q:

$$
\vec F_{\text{tổng}}=\vec0.
$$

Nếu chỉ có lực điện thì $\vec F=q\vec E$, nên với $q\ne0$ điều kiện tương đương $\vec E=0$ do các điện tích khác tạo ra.

Nhưng nếu còn trọng lực, lực căng, lực đàn hồi..., điều kiện cân bằng không còn đơn giản là $\vec E=0$.

## 2. Điểm điện trường bằng 0 trên đường nối hai điện tích

Với hai điện tích điểm $q_1,q_2$ cố định, trước hết xét hướng của $\vec E_1,\vec E_2$ ở từng miền.

### Hai điện tích cùng dấu

Giữa hai điện tích, hai vectơ điện trường ngược chiều nên có khả năng triệt tiêu.

Điều kiện độ lớn:

$$
\frac{k|q_1|}{r_1^2}=\frac{k|q_2|}{r_2^2}.
$$

Suy ra:

$$
\frac{r_1}{r_2}=\sqrt{\frac{|q_1|}{|q_2|}}.
$$

Điểm cân bằng nằm gần điện tích có độ lớn nhỏ hơn.

### Hai điện tích trái dấu

Trong đoạn giữa hai điện tích, hai vectơ điện trường cùng chiều nên không thể triệt tiêu. Điểm $E=0$ nếu tồn tại phải nằm ngoài đoạn nối hai điện tích và ở phía điện tích có độ lớn nhỏ hơn.

!!! tip "Luôn xét hướng trước khi lập phương trình độ lớn"
    Nếu chỉ giải phương trình bình phương khoảng cách mà không xét hướng, bạn rất dễ nhận một nghiệm hình học không hợp lệ.

## 3. Ba điện tích thẳng hàng cân bằng

Giả sử $q_1,q_2$ cố định, cần đặt $q_3$ để cả hệ cân bằng.

Một quy trình hợp lí:

1. Tìm vị trí mà điện trường do $q_1,q_2$ bằng 0; đó là ứng viên đặt $q_3$ để lực lên $q_3$ bằng 0.
2. Sau đó dùng điều kiện lực lên $q_1$ hoặc $q_2$ bằng 0 để xác định dấu và độ lớn $q_3$.
3. Kiểm tra điều kiện còn lại.

Không phải cứ đặt $q_3$ tại điểm $E_{12}=0$ là toàn hệ tự động cân bằng; $q_3$ còn tác dụng ngược trở lại lên $q_1,q_2$.

## 4. Vật tích điện treo dây trong điện trường ngang

Một vật khối lượng $m$, điện tích $q$, treo bằng dây nhẹ trong điện trường đều nằm ngang $\vec E$.

Các lực:

- trọng lực $\vec P=m\vec g$ hướng xuống;
- lực điện $\vec F_e=q\vec E$;
- lực căng $\vec T$ dọc dây.

Nếu dây lệch góc $\alpha$ so với phương thẳng đứng:

$$
\begin{gathered}
T\cos\alpha=mg,\\
T\sin\alpha=|q|E.
\end{gathered}
$$

Suy ra:

$$
\boxed{\tan\alpha=\frac{|q|E}{mg}}.
$$

Dấu của q quyết định vật lệch **cùng chiều hay ngược chiều** $\vec E$.

## 5. Điện trường thẳng đứng

Nếu $\vec E$ thẳng đứng, lực điện cùng phương với trọng lực.

Ta có thể dùng "gia tốc hiệu dụng" theo độ lớn:

$$
g_{\text{eff}}=\left|g\pm\frac{qE}{m}\right|
$$

với dấu đại số phải xác định theo chiều trục đã chọn.

Nếu vật treo cân bằng thẳng đứng, lực căng:

$$
T=|mg\pm qE|.
$$

Trong bài con lắc đơn dao động nhỏ trong điện trường đều thẳng đứng, nếu mô hình cho phép gộp các lực không đổi theo phương thẳng đứng, chu kì có thể viết:

$$
T_{\text{dao động}}=2\pi\sqrt{\frac{\ell}{g_{\text{eff}}}}.
$$

## 6. Điện trường ngang và con lắc đơn

Khi trọng lực $m\vec g$ và lực điện $q\vec E$ vuông góc, hợp lực không đổi có độ lớn:

$$
F_0=\sqrt{(mg)^2+(qE)^2}.
$$

Ta định nghĩa:

$$
g_{\text{eff}}=\frac{F_0}{m}=\sqrt{g^2+\left(\frac{qE}{m}\right)^2}.
$$

Vị trí cân bằng mới nằm theo hướng ngược hợp lực tác dụng ngoài. Dao động nhỏ quanh vị trí này có chu kì:

$$
T=2\pi\sqrt{\frac{\ell}{g_{\text{eff}}}}.
$$

Đây là bài mở rộng; chỉ dùng khi điện trường đều và lực điện không đổi theo vị trí trong miền dao động.

## 7. Ví dụ — Tìm điểm E = 0

$q_1=+4q$, $q_2=+q$, cách nhau d.

Điểm E=0 nằm giữa hai điện tích. Gọi khoảng cách đến $q_1$ là x, đến $q_2$ là $d-x$:

$$
\frac{4}{x^2}=\frac{1}{(d-x)^2}.
$$

Lấy căn dương theo khoảng cách:

$$
\frac{2}{x}=\frac{1}{d-x}.
$$

Suy ra $x=2d/3$. Điểm này cách điện tích nhỏ $q_2$ một đoạn $d/3$, đúng với trực giác "gần điện tích yếu hơn".

## 8. Ví dụ — Hạt tích điện treo dây

$m=20$ g, $q=2\,\mu$C, $E=5\times10^4$ V/m, $g=10$ m/s².

Lực điện:

$$
F_e=qE=0,10\text{ N}.
$$

Trọng lực:

$$
P=mg=0,20\text{ N}.
$$

Vậy:

$$
\tan\alpha=0,5.
$$

Suy ra $\alpha\approx26,6^\circ$.

## 9. Bẫy thường gặp

!!! danger "Quên lực của điện tích cần cân bằng lên các điện tích khác"
    Trong hệ ba điện tích cùng cân bằng, không được chỉ kiểm tra lực lên điện tích thứ ba.

!!! warning "Lấy căn mất điều kiện hình học"
    Phương trình $q_1/r_1^2=q_2/r_2^2$ chỉ là độ lớn. Vị trí còn phải thỏa hướng hai vectơ ngược nhau.

!!! warning "Dấu q trong lực điện"
    $\vec F=q\vec E$. Nếu q âm, lực ngược chiều điện trường.

## 10. Phương pháp chung

1. Vẽ hình và chia miền nếu cần.
2. Xác định hướng từng lực/vectơ trường.
3. Chọn trục.
4. Chỉ sau đó mới viết phương trình độ lớn.
5. Giải nghiệm hình học.
6. Kiểm tra dấu điện tích và điều kiện cân bằng.

## Tóm tắt

Bài cân bằng điện tích là bài **vectơ và điều kiện hình học** trước khi là bài đại số. Khi thêm dây treo và trọng lực, hãy trở lại sơ đồ lực thay vì cố ghép công thức điện trường một cách máy móc.

## 5 điều cần nhớ

1. $E=0$ và $F_{tổng}=0$ không luôn là cùng một câu hỏi.
2. Cùng dấu: điểm E=0 thường nằm giữa hai nguồn.
3. Trái dấu: điểm E=0 nếu có nằm ngoài đoạn nối hai nguồn.
4. Vật treo trong điện trường ngang: $\tan\alpha=|q|E/(mg)$.
5. Luôn kiểm tra hướng trước khi lấy độ lớn.

## Các dạng bài trọng tâm

Các nhóm bài dưới đây được tổ chức theo dấu hiệu nhận biết và công cụ giải để người học chọn phương pháp phù hợp và tự kiểm tra kết quả.

### Dạng 3 — Điều kiện cân bằng của điện tích điểm

Điều kiện nền tảng là tổng vectơ lực điện và các lực cơ học tác dụng lên vật bằng 0. Với ba điện tích thẳng hàng, vị trí cân bằng phải làm hai lực điện ngược chiều và bằng độ lớn; điều này quyết định miền đặt điểm trước khi lập phương trình.

Với vật treo hoặc hạt lơ lửng, vẽ đầy đủ trọng lực, lực căng, lực đẩy Ác-si-mét nếu có và lực điện. Chỉ sau khi xác định chiều lực điện mới suy dấu của điện tích.

<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/09-electrostatic-equilibrium-charged-pendulum/exercises.md)
- [Đáp án và lời giải](practice/09-electrostatic-equilibrium-charged-pendulum/solutions.md)

---

[← Bài 8](08-advanced-capacitors.md) | [↑ Chương](index.md) | [Bài tập →](exercises.md)
