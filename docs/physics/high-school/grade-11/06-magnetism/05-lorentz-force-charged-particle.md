---
title: "Bài 5 — Lực Lorentz và chuyển động của hạt mang điện"
description: "Lực từ lên điện tích chuyển động, quỹ đạo tròn và xoắn ốc trong từ trường đều."
order: 5
difficulty: "standard-advanced"
prerequisites:
  - magnetic-field
  - circular-motion
tags:
  - physics
  - grade-11
  - lorentz-force
---

# Bài 5 — Lực Lorentz và chuyển động của hạt mang điện

## Mục tiêu

Bạn cần:

- dùng được $F=|q|vB\sin\alpha$;
- xác định chiều lực với điện tích dương và âm;
- giải chuyển động tròn khi $\vec v\perp\vec B$;
- hiểu trường hợp $\vec v\parallel\vec B$ và vận tốc xiên;
- biết giới hạn của mô hình không tương đối tính.

## 1. Lực từ lên điện tích chuyển động

Một điện tích q chuyển động với vận tốc $\vec v$ trong từ trường $\vec B$ chịu lực từ:

$$
\boxed{\vec F=q\vec v\times\vec B}.
$$

Độ lớn:

$$
\boxed{F=|q|vB\sin\alpha}
$$

với $\alpha$ là góc giữa $\vec v$ và $\vec B$.

## 2. Chiều lực

### Với q > 0

Dùng quy tắc bàn tay trái hoặc tích có hướng $\vec v\times\vec B$.

### Với q < 0

Chiều lực **ngược** chiều kết quả tìm cho điện tích dương có cùng $\vec v$.

!!! danger "Đây là lỗi dấu kinh điển"
    Nhiều bạn tìm đúng chiều $\vec v\times\vec B$ rồi quên electron có q âm. Không có định luật nào thương lượng với việc quên dấu điện tích.

## 3. Lực từ không sinh công trực tiếp lên hạt

Vì $\vec F\perp\vec v$:

$$
P=\vec F\cdot\vec v=0.
$$

Do đó từ trường thuần túy không làm thay đổi độ lớn vận tốc và động năng của hạt; nó chỉ đổi **hướng** vận tốc.

Điều này rất quan trọng: nếu đề chỉ có từ trường và vận tốc ban đầu, tốc độ v không đổi.

## 4. Trường hợp v song song B

Nếu $\alpha=0$ hoặc 180°:

$$
F=0.
$$

Hạt tiếp tục chuyển động thẳng đều theo phương ban đầu, nếu không có lực khác.

## 5. Trường hợp v vuông góc B

Khi $\vec v\perp\vec B$, lực luôn vuông góc vận tốc và có độ lớn không đổi:

$$
F=|q|vB.
$$

Lực đóng vai trò lực hướng tâm:

$$
|q|vB=\frac{mv^2}{r}.
$$

Suy ra bán kính quỹ đạo:

$$
\boxed{r=\frac{mv}{|q|B}}.
$$

Tốc độ góc:

$$
\omega_c=\frac{v}{r}=\frac{|q|B}{m}.
$$

Chu kì:

$$
\boxed{T=\frac{2\pi m}{|q|B}}.
$$

Tần số:

$$
f=\frac{|q|B}{2\pi m}.
$$

### Điểm đáng chú ý

Trong mô hình cổ điển không tương đối tính, T không phụ thuộc v. Đây là cơ sở ý tưởng của cyclotron ở mức đơn giản.

## 6. Trường hợp vận tốc xiên

Phân tích:

$$
\vec v=\vec v_{\parallel}+\vec v_{\perp}.
$$

- $v_{\parallel}$ không chịu lực từ → chuyển động thẳng đều dọc B;
- $v_{\perp}$ gây chuyển động tròn quanh đường sức.

Kết hợp thành **đường xoắn ốc**.

Bán kính:

$$
r=\frac{mv_{\perp}}{|q|B}.
$$

Bước xoắn, tức quãng đường tiến dọc B sau một chu kì:

$$
h=v_{\parallel}T=\frac{2\pi m v_{\parallel}}{|q|B}.
$$

## 7. Ví dụ — proton chuyển động tròn

Proton có $m=1,67\times10^{-27}$ kg, $q=1,60\times10^{-19}$ C, vận tốc $2,0\times10^6$ m/s vuông góc với $B=0,20$ T.

$$
r=\frac{1,67\times10^{-27}\cdot2,0\times10^6}{1,60\times10^{-19}\cdot0,20}
\approx0,104\,\text m.
$$

Bán kính khoảng 10,4 cm.

## 8. Ví dụ — electron và proton cùng tốc độ

Cùng v và B, vì

$$
r\propto\frac{m}{|q|},
$$

proton có bán kính lớn hơn electron xấp xỉ tỉ số khối lượng $m_p/m_e\approx1836$ nếu cùng độ lớn điện tích. Hai hạt còn cong về **hai phía ngược nhau** vì dấu q trái nhau.

## 9. Hạt được tăng tốc qua hiệu điện thế rồi vào B

Nếu hạt xuất phát gần nghỉ và được tăng tốc qua hiệu điện thế U:

$$
|q|U=\frac12mv^2.
$$

Suy ra

$$
v=\sqrt{\frac{2|q|U}{m}}.
$$

Thay vào bán kính:

$$
\boxed{r=\frac1B\sqrt{\frac{2mU}{|q|}}}.
$$

Công thức này dùng nhiều trong bài xác định tỉ số q/m hoặc phân tích hạt.

## 10. Bộ chọn vận tốc — mở rộng

Nếu đồng thời có điện trường $\vec E$ và từ trường $\vec B$ vuông góc, có thể chọn vận tốc sao cho lực điện và lực từ cân bằng:

$$
|q|E=|q|vB.
$$

Do đó:

$$
\boxed{v=\frac EB}.
$$

Đây là ý tưởng nền của bộ chọn vận tốc. Không cần thuộc nếu chỉ học mức chuẩn, nhưng nó kết nối đẹp giữa Chương 3 và Chương 6.

## 11. Giới hạn mô hình

Các công thức $r=mv/(|q|B)$ và $T=2\pi m/(|q|B)$ dùng khối lượng cổ điển m. Khi v tiến gần tốc độ ánh sáng, phải dùng động lực học tương đối tính; chương này không xét trường hợp đó.

## 12. Sai lầm thường gặp

!!! warning "Dùng toàn bộ v khi vận tốc xiên"
    Bán kính chỉ phụ thuộc $v_\perp$, không phụ thuộc thành phần song song.

!!! warning "Cho rằng từ trường làm hạt nhanh dần"
    Từ trường thuần túy đổi hướng chứ không đổi tốc độ của hạt.

!!! warning "Dùng q có dấu trong công thức bán kính"
    Bán kính là độ dài dương nên dùng $|q|$. Dấu q dùng để xác định chiều cong.

## 13. Phương pháp giải

1. Xác định q dương hay âm.
2. Phân tích góc giữa v và B.
3. Nếu vuông góc: dùng chuyển động tròn.
4. Nếu xiên: tách $v_\parallel,v_\perp$.
5. Nếu hạt được tăng tốc qua U: dùng năng lượng để tìm v trước.
6. Xác định chiều cong riêng bằng quy tắc lực.

## Tóm tắt

Lực Lorentz từ có độ lớn $F=|q|vB\sin\alpha$ và vuông góc với vận tốc. Khi v vuông góc B, hạt chuyển động tròn với $r=mv/(|q|B)$, $T=2\pi m/(|q|B)$. Khi vận tốc xiên, quỹ đạo là xoắn ốc.

## 5 điều cần nhớ

1. $\vec F=q\vec v\times\vec B$.
2. Electron có chiều lực ngược điện tích dương.
3. Từ trường thuần không đổi động năng.
4. $r=mv_\perp/(|q|B)$.
5. $T=2\pi m/(|q|B)$ trong mô hình cổ điển.

---

[← Bài 4](04-parallel-currents-current-loop.md) | [↑ Chương](index.md) | [Bài tập →](exercises.md)
