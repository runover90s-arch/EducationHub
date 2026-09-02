---
title: "Bài 4 — Tổng hợp điện trường và cân bằng điện tích"
description: "Chồng chất vectơ điện trường, điểm triệt tiêu, cấu hình hình học và cân bằng điện tích."
order: 4
difficulty: "applied"
prerequisites:
  - electric-field-intensity
tags:
  - physics
  - grade-11
  - electric-field
  - superposition
---

# Bài 4 — Tổng hợp điện trường và cân bằng điện tích

## Mục tiêu

Bạn cần:

- dựng đúng vectơ điện trường của từng nguồn;
- tổng hợp trường trên đường thẳng và trong hình học 2D;
- tìm điểm $\vec E=0$;
- phân tích cân bằng của điện tích thử;
- dùng đối xứng để giảm tính toán;
- tránh cộng độ lớn khi các vectơ không cùng phương.

## 1. Nguyên lí chồng chất

Tại điểm M:

$$
\vec E_M=\sum_i\vec E_{iM}.
$$

Mỗi trường thành phần được xác định từ:

- vị trí nguồn;
- dấu nguồn;
- khoảng cách đến M;
- môi trường.

## 2. Quy trình chuẩn

1. Vẽ M và các điện tích nguồn.
2. Với từng nguồn, vẽ $\vec E_i$:
   - ra xa điện tích dương;
   - hướng vào điện tích âm.
3. Chọn trục tọa độ phù hợp.
4. Phân tích thành phần nếu cần.
5. Cộng vectơ.
6. Kiểm tra hướng kết quả có hợp lí không.

## 3. Hai điện trường cùng phương

### Cùng chiều
$E=E_1+E_2$.

### Ngược chiều
$E=|E_1-E_2|$, chiều theo vectơ lớn hơn.

Đây là trường hợp thường gặp trên đường nối hai điện tích.

## 4. Hai điện trường vuông góc

$$
E=\sqrt{E_1^2+E_2^2}.
$$

Góc có thể tìm bằng lượng giác:

$$
\tan\alpha=\frac{E_y}{E_x}.
$$

## 5. Hai điện trường hợp góc θ

$$
E=\sqrt{E_1^2+E_2^2+2E_1E_2\cos\theta}.
$$

Nếu $E_1=E_2=E_0$, hợp lực/trường nằm theo phân giác của góc nếu cấu hình đối xứng.

## 6. Điểm triệt tiêu trên đường nối hai điện tích

Điều kiện:

$$
\vec E_1+\vec E_2=\vec0.
$$

Với hai nguồn, cần hai vectơ ngược chiều và bằng độ lớn.

### Hai điện tích cùng dấu

Trong đoạn giữa hai điện tích, hai trường ngược chiều. Điểm triệt tiêu nằm giữa và gần điện tích nhỏ hơn về độ lớn.

Nếu khoảng cách hai nguồn là $a$, điểm cách $q_1$ một đoạn $x$:

$$
\frac{|q_1|}{x^2}=\frac{|q_2|}{(a-x)^2}.
$$

Lấy căn dương rồi giải.

### Hai điện tích trái dấu

Giữa hai điện tích, hai trường cùng chiều nên không triệt tiêu. Điểm triệt tiêu nếu có nằm ngoài đoạn, phía điện tích có độ lớn nhỏ hơn.

Nếu $|q_1|=|q_2|$ và trái dấu, không có điểm hữu hạn trên đường nối mà tổng trường bằng 0.

## 7. Cân bằng điện tích thử

Điện tích $q_0\ne0$ cân bằng tĩnh về lực điện khi:

$$
q_0\vec E=\vec0
\quad\Longleftrightarrow\quad
\vec E=\vec0.
$$

Vị trí cân bằng do trường quyết định, không phụ thuộc dấu hay độ lớn $q_0$.

Tuy nhiên **ổn định hay không ổn định** là vấn đề khác. Điều kiện $\vec E=0$ chỉ bảo đảm lực tức thời bằng 0.

## 8. Tam giác đều

Ba vị trí đỉnh tam giác đều thường dùng đối xứng.

Ví dụ hai điện tích bằng nhau ở A,B; xét điểm C:

- $E_A=E_B$;
- góc giữa hai vectơ có thể là $60^\circ$ hoặc $120^\circ$ tùy dấu;
- hợp trường theo trục đối xứng.

Thay vì nhớ công thức riêng, vẽ hướng và dùng định lí cos hoặc phân tích thành phần.

## 9. Hình vuông

Tại tâm hình vuông, các nguồn đối xứng có thể triệt tiêu từng cặp. Khi một điện tích khác dấu hoặc khác độ lớn, nên lấy cấu hình đối xứng làm “nền” rồi xét phần chênh.

Đây là kĩ thuật giảm số phép tính.

## 10. Điện trường đều và cân bằng với trọng lực

Hạt mang điện khối lượng m đứng yên trong điện trường đều khi lực điện cân bằng trọng lực:

$$
q\vec E+m\vec g=\vec0.
$$

Về độ lớn nếu hai lực thẳng đứng ngược chiều:

$$
|q|E=mg.
$$

Dấu q quyết định E phải hướng lên hay xuống để lực điện có hướng cần thiết.

## 11. Ví dụ

### Ví dụ 1 — Hai điện tích cùng dấu
$q_1=+Q$, $q_2=+4Q$, cách nhau a. Tìm điểm triệt tiêu giữa chúng, cách $q_1$ là x.

$$
\frac{Q}{x^2}=\frac{4Q}{(a-x)^2}.
$$

Suy ra $(a-x)=2x$, nên $x=a/3$.

Điểm gần điện tích nhỏ Q hơn, phù hợp kiểm tra trực giác.

### Ví dụ 2 — Trọng lực và điện trường
Hạt có $q>0$ cân bằng trong điện trường thẳng đứng. Trọng lực xuống nên lực điện phải lên; vì q dương, E phải hướng lên.

## 12. Bẫy thường gặp

!!! danger "Không cộng độ lớn tùy ý"
    Nếu $\vec E_1,\vec E_2$ không cùng phương, $E\ne E_1+E_2$ nói chung.

!!! warning "Hai điện tích trái dấu"
    Giữa hai điện tích trái dấu, điện trường của chúng cùng hướng từ dương sang âm. Vì vậy không tìm điểm triệt tiêu ở giữa.

## 🔬 Mở rộng

Một điểm $\vec E=0$ có thể không phải cân bằng bền. Phân tích ổn định cần xét điều gì xảy ra khi hạt lệch một lượng nhỏ khỏi vị trí đó và các lực khác có mặt hay không.

## Tóm tắt

- Cộng vectơ trường, không cộng vô hướng tùy tiện.
- Điểm triệt tiêu: các vectơ phải có thể đối nhau.
- Cùng dấu → điểm triệt tiêu giữa hai nguồn.
- Trái dấu → điểm triệt tiêu ngoài đoạn nếu độ lớn khác nhau.
- Cân bằng lực điện của q khác 0 tương đương E=0 nếu không có lực khác.

## 5 điều cần nhớ

1. Vẽ hướng từng E trước.
2. Dùng đối xứng khi có thể.
3. Kiểm tra vị trí nghiệm sau đại số.
4. Có trọng lực thì tổng tất cả lực bằng 0, không chỉ lực điện.
5. E=0 không đồng nghĩa điện thế V=0.

---

[← Bài 3](03-electric-field-intensity.md) | [↑ Chương](index.md) | [Bài 5 →](05-work-potential-voltage.md)
