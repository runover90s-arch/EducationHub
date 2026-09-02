---
title: "Bài 3 — Từ trường của dòng điện và nguyên lí chồng chất"
description: "Dây thẳng dài, vòng dây tròn, ống dây dài và tổng hợp cảm ứng từ."
order: 3
difficulty: "standard-applied"
prerequisites:
  - magnetic-field
  - current-intensity
tags:
  - physics
  - grade-11
  - magnetic-field-current
---

# Bài 3 — Từ trường của dòng điện và nguyên lí chồng chất

## Mục tiêu

Bạn cần:

- tính được B của dây thẳng dài, vòng dây tròn và ống dây dài;
- xác định chiều bằng quy tắc nắm tay phải;
- tổng hợp nhiều $\vec B$;
- tìm vị trí $B=0$ hoặc hai từ trường có độ lớn bằng nhau;
- nhận ra điều kiện mô hình của từng công thức.

## 1. Dây dẫn thẳng dài

Trong chân không, từ trường của dây thẳng rất dài mang dòng I tại điểm cách dây khoảng r:

$$
\boxed{B=\frac{\mu_0 I}{2\pi r}=2\times10^{-7}\frac{I}{r}}
$$

với

$$
\mu_0=4\pi\times10^{-7}\,\text{T}\cdot\text{m/A}.
$$

### Điều kiện mô hình

Công thức dùng tốt khi chiều dài dây rất lớn so với khoảng cách r và điểm xét không gần đầu dây.

### Xu hướng

- I tăng 2 lần → B tăng 2 lần;
- r tăng 2 lần → B giảm 2 lần.

Không có bình phương khoảng cách như điện trường của điện tích điểm. Hai mô hình hình học khác nhau, nên luật khoảng cách cũng khác.

## 2. Vòng dây tròn

Tại tâm vòng dây bán kính R, N vòng sát nhau, dòng I:

$$
\boxed{B=\frac{\mu_0NI}{2R}}.
$$

Với một vòng, N=1.

### Chiều

Khum các ngón tay phải theo chiều dòng điện trên vòng; ngón cái choãi ra chỉ chiều $\vec B$ tại tâm.

Nếu nhìn thấy dòng điện chạy ngược chiều kim đồng hồ, $\vec B$ tại tâm hướng ra khỏi mặt phẳng vòng.

## 3. Ống dây dài

Ống dây dài l, gồm N vòng quấn đều, dòng I. Bên trong, xa hai đầu, từ trường gần đều:

$$
\boxed{B=\mu_0\frac{N}{l}I=\mu_0nI}
$$

với $n=N/l$ là số vòng trên một mét.

### Ý nghĩa

- nhiều vòng hơn trên cùng chiều dài → trường mạnh hơn;
- tăng I → B tăng tuyến tính;
- công thức trên là mô hình ống dây dài lõi không khí/chân không.

Nếu có lõi vật liệu từ, B còn phụ thuộc tính từ của lõi; không tự động dùng đúng công thức không khí.

## 4. So sánh ba công thức

| Nguồn | Độ lớn B trong mô hình chuẩn | Tham số khoảng cách |
|---|---|---|
| Dây thẳng dài | $\mu_0I/(2\pi r)$ | giảm theo $1/r$ |
| N vòng tròn tại tâm | $\mu_0NI/(2R)$ | giảm theo $1/R$ |
| Ống dây dài bên trong | $\mu_0NI/l$ | phụ thuộc mật độ vòng N/l |

Không nên “nhớ hình dạng công thức” rồi tráo r và R. Hãy gắn công thức với hình học nguồn.

## 5. Nguyên lí chồng chất từ trường

Nếu nhiều nguồn tạo từ trường tại cùng điểm M:

$$
\boxed{\vec B=\vec B_1+\vec B_2+\cdots+\vec B_n}.
$$

Đây là tổng vectơ.

### Hai vectơ cùng phương

- cùng chiều: $B=B_1+B_2$;
- ngược chiều: $B=|B_1-B_2|$.

### Hai vectơ vuông góc

$$
B=\sqrt{B_1^2+B_2^2}.
$$

### Góc bất kì θ

$$
B=\sqrt{B_1^2+B_2^2+2B_1B_2\cos\theta}.
$$

## 6. Hai dây thẳng song song — tìm điểm B bằng 0

Giả sử hai dây rất dài song song, dòng $I_1,I_2$, cách nhau d.

### Dòng cùng chiều

Trong đoạn giữa hai dây, hai từ trường ngược chiều, nên điểm triệt tiêu có thể nằm giữa:

$$
\frac{I_1}{r_1}=\frac{I_2}{r_2},\qquad r_1+r_2=d.
$$

Điểm triệt tiêu gần dây có dòng **nhỏ hơn**, vì để trường yếu hơn của dòng nhỏ cân bằng trường của dòng lớn, ta phải đứng gần nguồn nhỏ hơn.

### Dòng ngược chiều

Trong đoạn giữa hai dây, từ trường thường cùng chiều nên không triệt tiêu. Điểm B=0, nếu tồn tại, nằm ngoài hai dây, về phía dây có dòng nhỏ hơn.

!!! tip "Kiểm tra vùng trước khi giải phương trình"
    Đừng giải đại số trước rồi phát hiện nghiệm nằm ở vùng mà hai vectơ lại cùng chiều. Hãy xét chiều $\vec B_1,\vec B_2$ theo từng miền trước.

## 7. Ví dụ — hai dây cùng chiều

Hai dây cách 12 cm, $I_1=2$ A, $I_2=4$ A cùng chiều. Điểm M giữa hai dây có B=0.

Đặt $r_1=x$, $r_2=0,12-x$:

$$
\frac{2}{x}=\frac{4}{0,12-x}.
$$

Suy ra

$$
2(0,12-x)=4x\Rightarrow x=0,04\,\text{m}=4\,\text{cm}.
$$

M cách dây 2 A 4 cm và cách dây 4 A 8 cm.

## 8. Ví dụ — vòng dây và dây thẳng

Một vòng tròn bán kính 10 cm, N=20, I=0,5 A. Tại tâm:

$$
B=\frac{4\pi\times10^{-7}\cdot20\cdot0,5}{2\cdot0,10}
=2\pi\times10^{-5}\,\text T.
$$

Nếu một trường ngoài ngược chiều có $B_0=2\pi\times10^{-5}$ T, tổng trường tại tâm bằng 0.

## 9. Dạng bài nâng cao vừa đủ

### Dạng 1 — Điểm B=0

1. chia không gian thành các miền;
2. xác định chiều từng $\vec B$;
3. chỉ giữ miền hai trường ngược chiều;
4. lập $B_1=B_2$;
5. kiểm tra nghiệm thuộc miền đã chọn.

### Dạng 2 — B tổng hợp vuông góc

Tính từng B riêng, dựng tam giác vectơ rồi dùng Pythagore.

### Dạng 3 — Nhiều dòng điện qua các đỉnh hình học

Dùng đối xứng. Nếu các độ lớn bằng nhau, nhiều thành phần có thể triệt tiêu từng cặp; đừng cộng độ lớn như cộng hóa đơn.

## 10. Sai lầm thường gặp

!!! danger "Sai đơn vị r, R, l"
    Tất cả độ dài trong công thức SI phải đổi sang mét.

!!! warning "Quên N ở cuộn nhiều vòng"
    Trường tại tâm N vòng lý tưởng bằng N lần một vòng nếu các vòng trùng gần nhau.

!!! warning "Lấy B=0 bằng cách đặt B1=B2 nhưng không xét chiều"
    Hai vectơ cùng độ lớn mà cùng chiều thì tổng là 2B, không phải 0.

## Tóm tắt

Ba công thức nền của chương là $B=\mu_0I/(2\pi r)$ cho dây thẳng dài, $B=\mu_0NI/(2R)$ tại tâm vòng dây và $B=\mu_0NI/l$ trong ống dây dài. Khi có nhiều nguồn, tổng hợp theo vectơ.

## 5 điều cần nhớ

1. Dây thẳng: B giảm theo $1/r$.
2. Vòng tròn: B tại tâm tăng theo N và I.
3. Ống dây dài: B tăng theo mật độ vòng N/l.
4. Chiều dùng quy tắc tay phải.
5. B tổng là tổng vectơ, không phải tổng số học trong mọi tình huống.

---

[← Bài 2](02-magnetic-force-current-wire.md) | [↑ Chương](index.md) | [Bài 4 →](04-parallel-currents-current-loop.md)
