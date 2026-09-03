---
title: "Bài 4 — Hai dòng điện song song, khung dây và mômen từ"
description: "Lực giữa hai dòng điện song song, mômen lực lên khung dây và nguyên lí động cơ điện."
order: 4
difficulty: "standard-enrichment"
prerequisites:
  - magnetic-force-current-wire
  - fields-of-currents-superposition
tags:
  - physics
  - grade-11
  - parallel-currents
  - current-loop
---

# Bài 4 — Hai dòng điện song song, khung dây và mômen từ

## Mục tiêu

Bạn cần:

- xác định lực hút/đẩy giữa hai dây song song;
- dùng được lực trên một đơn vị chiều dài;
- hiểu vì sao khung dây trong từ trường có thể quay;
- dùng mômen $\tau=NIBS\sin\theta$ trong bài chuẩn;
- liên hệ với mômen từ và nguyên lí động cơ điện.

## 1. Lực giữa hai dây dẫn song song

Hai dây thẳng dài song song, cách nhau d, mang dòng $I_1$ và $I_2$.

Dây 1 tạo từ trường tại dây 2:

$$
B_1=\frac{\mu_0I_1}{2\pi d}.
$$

Nếu hai dây song song nên dòng trên dây 2 vuông góc với $\vec B_1$, lực từ trên đoạn dài l của dây 2:

$$
F=B_1I_2l.
$$

Suy ra:

$$
\boxed{\frac{F}{l}=\frac{\mu_0I_1I_2}{2\pi d}}.
$$

## 2. Hút hay đẩy?

- Hai dòng **cùng chiều** → hai dây **hút nhau**.
- Hai dòng **ngược chiều** → hai dây **đẩy nhau**.

### Vì sao?

Không cần học như khẩu hiệu. Chọn dây 1 tạo $\vec B$ tại vị trí dây 2, rồi dùng $\vec F=I\vec l\times\vec B$. Làm một lần đúng, quy tắc hút/đẩy tự xuất hiện.

## 3. Ví dụ lực giữa hai dây

Hai dây cách 5 cm, $I_1=10$ A, $I_2=4$ A cùng chiều. Lực trên 1 m dây:

$$
\frac{F}{l}=2\times10^{-7}\frac{I_1I_2}{d}
=2\times10^{-7}\frac{10\cdot4}{0,05}
=1,6\times10^{-4}\,\text{N/m}.
$$

Hai dây hút nhau.

## 4. Khung dây trong từ trường đều

Xét khung dây phẳng diện tích S, N vòng, dòng I đặt trong từ trường đều B.

Các lực từ trên các cạnh có thể tạo thành một **ngẫu lực**, làm khung có xu hướng quay.

Mômen lực:

$$
\boxed{\tau=NIBS\sin\theta}
$$

trong đó $\theta$ là góc giữa **pháp tuyến của mặt khung** và $\vec B$.

!!! warning "Góc theta không phải góc giữa mặt phẳng khung và B"
    Nếu mặt phẳng khung tạo với $\vec B$ góc $\beta$, thì pháp tuyến tạo với $\vec B$ góc $\theta=90^\circ-\beta$. Vì vậy $\tau=NIBS\cos\beta$.

## 5. Mômen từ

Đặt

$$
\boxed{\mu=NIS}
$$

với $\mu$ là độ lớn mômen từ của khung dây.

Vectơ $\vec\mu$ vuông góc mặt khung, chiều theo quy tắc bàn tay phải đối với chiều dòng điện.

Khi đó:

$$
\vec\tau=\vec\mu\times\vec B,
$$

và

$$
\tau=\mu B\sin\theta.
$$

## 6. Vị trí cân bằng

Mômen bằng 0 khi $\theta=0$ hoặc $180^\circ$. Nhưng hai vị trí không có tính ổn định giống nhau.

- $\vec\mu$ cùng chiều $\vec B$: trạng thái năng lượng thấp, cân bằng bền trong mô hình;
- $\vec\mu$ ngược chiều $\vec B$: cân bằng không bền.

Năng lượng thế từ của một lưỡng cực từ có thể viết ở mức mở rộng:

$$
U=-\vec\mu\cdot\vec B=-\mu B\cos\theta.
$$

## 7. Nguyên lí động cơ điện

Một khung dây có dòng trong từ trường chịu mômen quay. Nếu muốn quay liên tục, cần cơ chế đổi chiều dòng điện trong khung vào đúng thời điểm hoặc dùng từ trường quay/điều khiển điện tử.

Trong động cơ một chiều đơn giản:

1. dòng điện chạy qua cuộn dây;
2. hai cạnh đối diện chịu lực từ ngược chiều;
3. hai lực tạo mômen;
4. bộ góp đổi chiều dòng sau mỗi nửa vòng để mômen tiếp tục cùng chiều quay.

### Điều đáng hiểu

Động cơ không “tạo năng lượng từ nam châm”. Nguồn điện cung cấp năng lượng; từ trường là mắt xích biến đổi năng lượng điện thành cơ năng.

## 8. Ví dụ mômen

Khung N=50 vòng, diện tích $S=20\,\text{cm}^2=2,0\times10^{-3}\,\text{m}^2$, I=0,5 A, B=0,2 T. Pháp tuyến khung tạo với B góc 30°.

$$
\tau=50\cdot0,5\cdot0,2\cdot2,0\times10^{-3}\cdot\sin30^\circ
=5,0\times10^{-3}\,\text{N m}.
$$

## 9. Dạng bài thường gặp

### Dạng 1 — Lực giữa dây

Dùng trực tiếp $F/l=\mu_0I_1I_2/(2\pi d)$, rồi xét cùng/ngược chiều.

### Dạng 2 — Cân bằng cơ học của dây

Nếu lực từ cân bằng trọng lực theo một đoạn dài l:

$$
\frac{\mu_0I_1I_2}{2\pi d}l=mg.
$$

### Dạng 3 — Mômen cực đại

Mômen cực đại khi $\theta=90^\circ$:

$$
\tau_{\max}=NIBS.
$$

### Dạng 4 — Tìm góc từ mômen

$$
\sin\theta=\frac{\tau}{NIBS}.
$$

Phải kiểm tra vế phải nằm trong [0,1].

## 10. Sai lầm thường gặp

!!! warning "Nhầm lực lên mỗi dây với tổng lực cả hệ"
    Hai dây tác dụng lên nhau hai lực cùng độ lớn, ngược chiều. Tổng lực nội của hệ hai dây bằng 0 nếu không xét tương tác với nguồn/giá đỡ, nhưng mỗi dây vẫn chịu lực.

!!! warning "Dùng khoảng cách d sai"
    d là khoảng cách vuông góc giữa hai trục dây song song.

!!! warning "Mômen bằng 0 không có nghĩa lực bằng 0"
    Trên khung dây, các lực có thể khác 0 nhưng đường tác dụng khiến tổng mômen bằng 0 ở một số tư thế.

## Tóm tắt

Hai dòng song song cùng chiều hút, ngược chiều đẩy với $F/l=\mu_0I_1I_2/(2\pi d)$. Khung dây có dòng trong từ trường có mômen $\tau=NIBS\sin\theta$, nơi $\theta$ là góc giữa pháp tuyến khung và B.

## 5 điều cần nhớ

1. Cùng chiều hút, ngược chiều đẩy.
2. $F/l\propto I_1I_2/d$.
3. $\tau=NIBS\sin\theta$.
4. $\theta$ đo từ pháp tuyến mặt khung đến B.
5. Động cơ biến điện năng thành cơ năng thông qua mômen từ.


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/04-parallel-currents-current-loop/exercises.md)
- [Đáp án và lời giải](practice/04-parallel-currents-current-loop/solutions.md)

---

[← Bài 3](03-fields-of-currents-superposition.md) | [↑ Chương](index.md) | [Bài 5 →](05-lorentz-force-charged-particle.md)
