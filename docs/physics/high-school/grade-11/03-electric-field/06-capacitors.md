---
title: "Bài 6 — Tụ điện, điện dung và năng lượng"
description: "Cấu tạo tụ điện, điện dung, tụ phẳng, năng lượng tích trữ và điện môi."
order: 6
difficulty: "standard-applied"
prerequisites:
  - work-potential-voltage
tags:
  - physics
  - grade-11
  - electric-field
  - capacitor
---

# Bài 6 — Tụ điện, điện dung và năng lượng

## Mục tiêu

Bạn cần:

- hiểu cấu tạo và chức năng cơ bản của tụ;
- dùng $C=Q/U$ đúng ý nghĩa;
- tính điện dung tụ phẳng;
- phân biệt Q, U, C;
- tính năng lượng của tụ;
- dự đoán đại lượng nào giữ nguyên khi thay điện môi/khoảng cách trong các điều kiện khác nhau;
- đọc thông số tụ.

## 1. Tụ điện

Tụ điện gồm hai vật dẫn đặt gần nhau, ngăn cách bởi lớp cách điện (điện môi).

Khi nối hai bản với nguồn, một bản tích $+Q$, bản kia tích $-Q$. Khi nói “điện tích của tụ”, thường dùng độ lớn Q trên một bản.

## 2. Điện dung

Điện dung:

$$
\boxed{C=\frac{Q}{U}}.
$$

Đơn vị: farad (F).

Các bội thường dùng:

- $\mu$F = $10^{-6}$ F;
- nF = $10^{-9}$ F;
- pF = $10^{-12}$ F.

### Ý nghĩa

C đặc trưng cho khả năng tích điện của cấu tạo tụ. Với tụ tuyến tính lí tưởng, C không phụ thuộc Q hoặc U; thay U chỉ làm Q thay đổi theo $Q=CU$.

!!! warning "Sai lầm"
    Không kết luận “Q tăng nên C tăng” từ $C=Q/U$. Với một tụ có cấu tạo không đổi trong miền tuyến tính, C là thông số cố định.

## 3. Tụ điện phẳng

Hai bản song song diện tích hữu hiệu S, khoảng cách d, điện môi đồng nhất có hằng số điện môi tương đối $\varepsilon_r$:

$$
\boxed{C=\frac{\varepsilon_0\varepsilon_r S}{d}}.
$$

Hệ quả:

- S tăng → C tăng;
- d tăng → C giảm;
- đưa điện môi có $\varepsilon_r>1$ lấp đầy khe → C tăng $\varepsilon_r$ lần.

## 4. Liên hệ Q, U và E

Với tụ phẳng bỏ qua hiệu ứng mép:

$$
U=Ed.
$$

Và $Q=CU$.

Từ đó trong chân không:

$$
E=\frac{Q}{\varepsilon_0S}
$$

khi Q cố định và mô hình bản lớn.

## 5. Năng lượng của tụ

Năng lượng tích trong tụ:

$$
\boxed{
W=\frac12QU=\frac12CU^2=\frac{Q^2}{2C}
}.
$$

Chọn biểu thức phù hợp với các đại lượng được giữ không đổi.

### Nếu U không đổi
$W=\tfrac12CU^2$ → C tăng thì W tăng.

### Nếu Q không đổi
$W=Q^2/(2C)$ → C tăng thì W giảm.

Sự khác nhau là do khi nối nguồn, nguồn có thể trao đổi năng lượng và điện tích với tụ.

## 6. Mật độ năng lượng điện trường

Trong điện trường đều tuyến tính, năng lượng trên một đơn vị thể tích có dạng:

$$
w=\frac12\varepsilon E^2,
$$

với $\varepsilon=\varepsilon_0\varepsilon_r$.

Đây là cách nhìn sâu hơn: năng lượng được gắn với điện trường trong không gian giữa các bản.

## 7. Tụ nối nguồn và tụ cô lập

### Tụ vẫn nối nguồn lí tưởng
U được nguồn giữ không đổi. Khi C đổi:

$$
Q=CU
$$

nên Q thay đổi do có điện tích đi qua mạch.

### Tụ đã ngắt khỏi nguồn, cô lập
Nếu không có đường rò và không nối với mạch khác, điện tích Q giữ không đổi. Khi C đổi, U thay đổi theo $U=Q/C$.

Đây là chìa khóa của nhiều bài thay khoảng cách hoặc đưa điện môi.

## 8. Thay khoảng cách bản

Tụ phẳng: $C\propto1/d$.

### Nối nguồn
U không đổi → Q tỉ lệ C → d tăng làm Q giảm.

### Cô lập
Q không đổi → U=Q/C → d tăng làm U tăng.

Vì $E=U/d$, trong mô hình cô lập chân không, E có thể giữ không đổi khi chỉ thay d vì $E=Q/(\varepsilon_0S)$.

## 9. Đưa điện môi

Nếu điện môi lấp đầy:

$C'=\varepsilon_r C$.

- nối nguồn: $U$ không đổi → $Q'=\varepsilon_r Q$;
- cô lập: $Q$ không đổi → $U'=U/\varepsilon_r$.

Năng lượng thay đổi khác nhau theo hai điều kiện.

## 10. Thông số định mức

Tụ thường ghi:

- điện dung danh định;
- điện áp làm việc tối đa.

Không nên đặt hiệu điện thế vượt định mức vì điện môi có thể bị đánh thủng.

Thông số định mức là giới hạn kĩ thuật, không phải công thức vật lí để suy ngược mọi trạng thái.

## 11. Ví dụ

### Ví dụ 1
$C=5\,\mu$F, $U=12$ V:

$Q=CU=60\,\mu$C.

Năng lượng:

$$
W=\frac12CU^2=3,6\times10^{-4}\ \text{J}.
$$

### Ví dụ 2 — Tụ cô lập thay khoảng cách
Tăng d gấp đôi → C giảm nửa. Q không đổi nên U tăng gấp đôi; W=Q²/(2C) tăng gấp đôi.

### Ví dụ 3 — Nối nguồn, đưa điện môi
$\varepsilon_r=4$. C tăng 4 lần, U không đổi → Q và W đều tăng 4 lần.

## 12. Bẫy thường gặp

!!! danger "Phải xác định điều kiện mạch"
    Câu “tăng khoảng cách hai bản” chưa đủ để kết luận Q hay U thay đổi. Trước hết hỏi: **tụ còn nối nguồn hay đã cô lập?**

## Tóm tắt

- $C=Q/U$.
- Tụ phẳng: $C=\varepsilon_0\varepsilon_rS/d$.
- Năng lượng: $W=QU/2=CU^2/2=Q^2/(2C)$.
- Nối nguồn → U thường cố định.
- Cô lập → Q thường cố định.

## 5 điều cần nhớ

1. C do cấu tạo và điện môi quyết định.
2. Q ở hai bản bằng độ lớn và trái dấu.
3. Chọn dạng năng lượng theo đại lượng cố định.
4. Điện môi làm tăng C.
5. Luôn kiểm tra điện áp định mức trong ứng dụng thực tế.

<!-- V9_SOURCE_TYPES -->

## Các dạng bài được hệ thống hóa từ ngân hàng PDF

Các dạng dưới đây chỉ sử dụng những nhóm bài đã được gọi tên rõ trong các tài liệu bài tập. Phần trình bày được tổ chức lại để người học nhận diện đề, chọn công cụ và tự kiểm tra kết quả; không tạo thêm tên dạng mới.

### Dạng 1 — Tính điện dung, điện tích, hiệu điện thế và năng lượng của tụ điện

Ba đại lượng cơ bản liên hệ bởi $Q=CU$. Năng lượng tụ có thể viết dưới các dạng $W=\tfrac12CU^2=Q^2/(2C)=\tfrac12QU$. Chọn dạng phù hợp với các đại lượng đề cho để giảm biến đổi.

Khi tụ vẫn nối với nguồn, hiệu điện thế được giữ không đổi; khi tụ bị ngắt khỏi nguồn và cô lập, điện tích toàn phần trên tụ được giữ không đổi. Đây là điều kiện quyết định trong các bài thay đổi điện môi hoặc khoảng cách bản.

<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/06-capacitors/exercises.md)
- [Đáp án và lời giải](practice/06-capacitors/solutions.md)

---

[← Bài 5](05-work-potential-voltage.md) | [↑ Chương](index.md) | [Bài 7 →](07-charged-particle-motion.md)
