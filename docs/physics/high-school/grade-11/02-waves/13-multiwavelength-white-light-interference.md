---
title: "Bài 13 — Giao thoa nhiều bức xạ và ánh sáng trắng"
description: "Vân trùng của hai–ba bức xạ, đếm vân, giao thoa ánh sáng trắng và chiến lược giải bài."
order: 13
difficulty: "applied-advanced"
prerequisites:
  - light-interference
  - light-wave-diffraction-dispersion
tags:
  - physics
  - grade-11
  - interference
  - white-light
---

# Bài 13 — Giao thoa nhiều bức xạ và ánh sáng trắng

## Mục tiêu

Bạn cần:

- xác định vị trí vân sáng của từng bức xạ;
- tìm vị trí hai hoặc ba hệ vân sáng trùng nhau;
- đếm số vân quan sát được trên một đoạn màn;
- hiểu hình ảnh giao thoa ánh sáng trắng;
- tránh dùng một "khoảng vân chung" khi tỉ số bước sóng không hữu tỉ theo mô hình số liệu.

## 1. Ôn lại Young với một bức xạ

Khoảng vân:

$$
i=\frac{\lambda D}{a}.
$$

Vị trí vân sáng:

$$
x_s=ki,\qquad k\in\mathbb Z.
$$

Vị trí vân tối:

$$
x_t=\left(k+\frac12\right)i.
$$

## 2. Hai bức xạ đơn sắc

Với $\lambda_1,\lambda_2$:

$$
i_1=\frac{\lambda_1D}{a},
\qquad
i_2=\frac{\lambda_2D}{a}.
$$

Một vị trí là vân sáng của cả hai khi:

$$
k_1i_1=k_2i_2.
$$

Do $D/a$ chung:

$$
\boxed{k_1\lambda_1=k_2\lambda_2}.
$$

Đây là phương trình quan trọng nhất của bài vân trùng.

## 3. Tìm cặp bậc nhỏ nhất

Ví dụ $\lambda_1=500$ nm, $\lambda_2=600$ nm.

Điều kiện:

$$
500k_1=600k_2
$$

hay:

$$
5k_1=6k_2.
$$

Cặp số nguyên dương nhỏ nhất là $k_1=6$, $k_2=5$.

Vì vậy khoảng cách giữa hai vị trí sáng trùng liên tiếp cùng phía là:

$$
i_{\text{trùng}}=6i_1=5i_2.
$$

## 4. Ba bức xạ

Vị trí sáng trùng của ba hệ thỏa:

$$
k_1\lambda_1=k_2\lambda_2=k_3\lambda_3.
$$

### Phương pháp

1. Đưa các bước sóng về cùng đơn vị.
2. Rút gọn tỉ số.
3. Tìm bộ số nguyên dương nhỏ nhất thỏa đẳng thức.
4. Tính vị trí hoặc khoảng lặp tương ứng.

Không nên đổi sang số thập phân quá sớm nếu bước sóng có tỉ số đẹp; giữ dạng nguyên giúp tránh sai số.

## 5. Đếm vân sáng trên đoạn đối xứng

Với một hệ vân, màn xét từ $-L/2$ đến $+L/2$.

Cần tìm số nguyên $k$ thỏa:

$$
-\frac L2\le ki\le\frac L2.
$$

Cách an toàn nhất là giải bất đẳng thức nguyên. Không cần thuộc hàng loạt công thức đếm trường hợp nếu dễ nhầm biên.

### Tại sao nên giải bất đẳng thức?

Vì các bài có thể hỏi:

- đoạn kín hay đoạn mở;
- hai điểm cùng phía hoặc khác phía;
- có tính hai đầu đoạn không;
- đếm riêng từng màu hay đếm vị trí sáng phân biệt.

Một công thức thuộc lòng thường chỉ đúng cho một cấu hình.

## 6. Đếm vị trí sáng phân biệt với hai bức xạ

Giả sử trên một đoạn màn:

- hệ 1 có $N_1$ vân sáng;
- hệ 2 có $N_2$ vân sáng;
- có $N_{12}$ vị trí sáng trùng.

Số vị trí sáng phân biệt:

$$
\boxed{N=N_1+N_2-N_{12}}.
$$

Đây là nguyên lí cộng–trừ tập hợp, không phải công thức riêng của quang học.

## 7. Vân sáng của một màu trùng vân tối của màu khác

Điều kiện tổng quát:

$$
k_1i_1=\left(k_2+\frac12\right)i_2.
$$

Tương đương:

$$
2k_1\lambda_1=(2k_2+1)\lambda_2.
$$

Bài kiểu này là bài số nguyên. Hãy tìm nghiệm theo điều kiện bậc vân và miền màn.

## 8. Giao thoa ánh sáng trắng

Ánh sáng trắng chứa dải bước sóng nhìn thấy. Mỗi bước sóng tạo hệ vân riêng.

### Vân trung tâm

Tại hiệu đường đi bằng 0, mọi bước sóng đều cực đại cùng lúc, vì vậy vân trung tâm có màu gần trắng.

### Ra xa trung tâm

Khoảng vân tăng theo $\lambda$, nên vị trí cực đại của đỏ và tím tách dần. Các dải màu chồng lấp phức tạp và độ tương phản giảm khi ra xa.

Trong bài tính, người ta thường hỏi miền chồng của một bậc màu đỏ và một bậc màu tím hoặc khoảng mà quang phổ bậc này không chồng quang phổ bậc khác.

## 9. Dạng bài thay đổi điều kiện giao thoa

Vì:

$$
i=\frac{\lambda D}{a},
$$

nên:

- tăng $D$ → khoảng vân tăng;
- tăng $a$ → khoảng vân giảm;
- tăng $\lambda$ → khoảng vân tăng.

Nếu toàn bộ thí nghiệm đặt trong môi trường chiết suất $n$ mà hình học không đổi, bước sóng giảm còn $\lambda/n$, nên:

$$
i'=\frac{i}{n}.
$$

## 10. Ví dụ — Hai màu trùng nhau

$\lambda_1=450$ nm, $\lambda_2=600$ nm.

Điều kiện:

$$
450k_1=600k_2
$$

rút gọn:

$$
3k_1=4k_2.
$$

Cặp nhỏ nhất $k_1=4$, $k_2=3$.

Nếu $i_1=0,90$ mm thì khoảng sáng trùng:

$$
i_{\text{trùng}}=4i_1=3,60\text{ mm}.
$$

## 11. Ví dụ — Đếm vân bằng bất đẳng thức

Khoảng vân $i=1,2$ mm. Xét đoạn $x\in[-5;7]$ mm.

Vân sáng thỏa:

$$
-5\le1,2k\le7.
$$

Suy ra:

$$
-4,166\ldots\le k\le5,833\ldots
$$

Nên $k=-4,-3,\ldots,5$: có 10 vân sáng.

Cách này rõ ràng hơn việc cố nhớ công thức cho đoạn không đối xứng.

## 12. Bẫy thường gặp

!!! warning "Nhầm bậc với vị trí"
    Hai vân trùng nhau không có nghĩa chúng có cùng bậc. Thường $k_1\ne k_2$.

!!! warning "Quên trừ vân trùng khi đếm vị trí phân biệt"
    Nếu cộng $N_1+N_2$ thì các vị trí trùng đã bị đếm hai lần.

!!! warning "Làm tròn bước sóng sớm"
    Bài vân trùng phụ thuộc tỉ số số nguyên. Làm tròn có thể phá mất quan hệ chính xác.

## 13. Phương pháp tổng quát

1. Viết $i_j=\lambda_jD/a$.
2. Dịch câu hỏi thành phương trình vị trí.
3. Rút $D/a$ nếu có thể.
4. Giải bài số nguyên.
5. Áp miền hình học của màn.
6. Cuối cùng mới đếm hoặc tính khoảng cách.

## Tóm tắt

Giao thoa nhiều bức xạ thực chất là chồng nhiều hệ vân có khoảng vân khác nhau. Cốt lõi không nằm ở việc thuộc nhiều công thức, mà ở điều kiện vị trí và bài toán số nguyên.

## 5 điều cần nhớ

1. Vân sáng: $x=k\lambda D/a$.
2. Hai sáng trùng: $k_1\lambda_1=k_2\lambda_2$.
3. Ba sáng trùng: mở rộng cùng nguyên tắc.
4. Đếm vân an toàn nhất bằng bất đẳng thức nguyên.
5. Vân trung tâm của ánh sáng trắng là vị trí các bước sóng cùng cực đại.

## Các dạng bài trọng tâm

Các nhóm bài dưới đây được tổ chức theo dấu hiệu nhận biết và công cụ giải để người học chọn phương pháp phù hợp và tự kiểm tra kết quả.

### Dạng 12 — Giao thoa với ánh sáng trắng

Ánh sáng trắng gồm nhiều bước sóng nên mỗi màu tạo một hệ vân có khoảng vân khác nhau. Vân trung tâm của mọi màu trùng nhau và có màu trắng; ra xa trung tâm các hệ vân tách dần.

Khi tìm màu xuất hiện tại một vị trí, dùng $x=k\lambda D/a$ để suy các bước sóng khả dĩ trong miền khả kiến và điều kiện $k$ nguyên. Khi tìm vùng chồng lấn hay bậc vân, phải xét giới hạn bước sóng đỏ–tím thay vì chọn một bước sóng đại diện.

<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/13-multiwavelength-white-light-interference/exercises.md)
- [Đáp án và lời giải](practice/13-multiwavelength-white-light-interference/solutions.md)

---

[← Bài 12](12-spectra-electromagnetic-spectrum.md) | [↑ Chương](index.md) | [Bài tập →](exercises.md)
