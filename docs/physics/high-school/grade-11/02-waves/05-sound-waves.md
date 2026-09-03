---
title: "Bài 5 — Sóng âm"
description: "Bản chất âm, tần số, độ cao, độ to, mức cường độ âm, âm sắc và cộng hưởng âm."
order: 5
difficulty: "standard"
prerequisites:
  - mechanical-wave-basics
  - standing-waves
tags:
  - physics
  - grade-11
  - waves
  - sound
---

# Bài 5 — Sóng âm

## Mục tiêu

Bạn cần:

- hiểu âm là sóng cơ;
- liên hệ tần số với độ cao;
- phân biệt cường độ âm và mức cường độ âm;
- dùng quan hệ nghịch đảo bình phương cho nguồn điểm đẳng hướng trong điều kiện thích hợp;
- hiểu âm sắc gắn với phổ và dạng dao động;
- nhận biết hạ âm, âm nghe được, siêu âm theo quy ước phổ thông.

## 1. Bản chất của âm

Âm là sóng cơ có thể gây cảm giác âm khi tác động lên tai người trong miền tần số thích hợp. Vì là sóng cơ, âm cần môi trường vật chất để truyền.

Trong không khí, âm thường được mô hình là sóng dọc gồm các vùng nén và dãn.

## 2. Nguồn âm

Nguồn âm là vật dao động phát ra sóng âm. Ví dụ:

- dây đàn;
- màng loa;
- cột không khí trong ống;
- âm thoa;
- dây thanh quản.

Tần số của âm cơ bản liên hệ trực tiếp với tần số dao động của nguồn.

## 3. Miền tần số

Theo quy ước phổ biến trong giáo dục:

- hạ âm: tần số dưới khoảng 20 Hz;
- âm nghe được: xấp xỉ 20 Hz đến 20 kHz;
- siêu âm: trên khoảng 20 kHz.

Khả năng nghe thực tế phụ thuộc từng người, tuổi và cường độ âm, nên các mốc trên là mốc quy ước gần đúng.

## 4. Độ cao của âm

Độ cao chủ yếu gắn với **tần số**:

- tần số lớn → âm cao;
- tần số nhỏ → âm trầm.

Không được đồng nhất “cao” với “to”. Một âm có thể rất cao nhưng nhỏ, hoặc trầm nhưng rất to.

## 5. Cường độ âm

Cường độ âm $I$ tại một điểm là công suất âm truyền qua một đơn vị diện tích đặt vuông góc với phương truyền:

$$
\boxed{I=\frac{P}{S}}.
$$

Đơn vị: W/m².

### Nguồn điểm đẳng hướng

Nếu nguồn điểm phát công suất $P$ đều theo mọi hướng trong môi trường không hấp thụ đáng kể, ở khoảng cách $r$:

$$
\boxed{I=\frac{P}{4\pi r^2}}.
$$

Do đó $I\propto1/r^2$.

Nếu khoảng cách tăng 2 lần, cường độ giảm 4 lần.

## 6. Mức cường độ âm

Tai cảm nhận âm trên một dải cường độ rất rộng, nên dùng thang logarit.

Mức cường độ âm:

$$
\boxed{L=10\log_{10}\frac{I}{I_0}\ \text{dB}},
$$

với $I_0=10^{-12}$ W/m² là cường độ chuẩn thường dùng.

### So sánh hai mức

$$
L_2-L_1=10\log_{10}\frac{I_2}{I_1}.
$$

Hệ quả:

- $I$ tăng 10 lần → $L$ tăng 10 dB;
- $I$ tăng 100 lần → $L$ tăng 20 dB;
- $I$ tăng 2 lần → $L$ tăng khoảng 3,01 dB.

## 7. Độ to

Độ to là cảm giác sinh lí, phụ thuộc:

- cường độ/mức cường độ;
- tần số;
- đặc điểm tai người.

Vì vậy không thể nói độ to chỉ là một cách gọi khác của cường độ âm.

## 8. Âm sắc

Âm sắc giúp phân biệt hai nguồn phát cùng độ cao và có thể cùng độ to nhưng nghe khác nhau.

Về vật lí, âm sắc liên quan đến:

- thành phần các họa âm;
- biên độ tương đối của các thành phần;
- dạng sóng và quá trình phát âm.

## 9. Âm cơ bản và họa âm

Một hệ dao động như dây đàn hoặc cột khí có nhiều tần số riêng. Tần số thấp nhất thường gọi là tần số cơ bản. Các thành phần ở tần số cao hơn có quan hệ với mode riêng và góp phần tạo âm sắc.

Phần này liên hệ trực tiếp với sóng dừng.

## 10. Ví dụ

### Ví dụ 1 — Cường độ theo khoảng cách

Ở khoảng cách $r$, cường độ là $I$. Ở $3r$, nếu nguồn đẳng hướng và bỏ qua hấp thụ:

$$
I'=\frac{I}{9}.
$$

### Ví dụ 2 — Mức âm

Nếu $I=10^{-6}$ W/m²:

$$
L=10\log_{10}(10^6)=60\ \text{dB}.
$$

### Ví dụ 3 — Hai nguồn độc lập

Nếu hai nguồn không kết hợp tạo tại điểm M các cường độ $I_1,I_2$, tổng cường độ trung bình thường lấy $I=I_1+I_2$. Không cộng trực tiếp các mức dB.

## 11. Lỗi thường gặp

!!! warning "Không cộng dB trực tiếp"
    Hai âm 60 dB không tạo thành 120 dB. Phải đổi về cường độ, cộng cường độ rồi đổi lại mức.

!!! warning "Công thức $1/r^2$ có điều kiện"
    Quan hệ $I=P/(4\pi r^2)$ giả sử nguồn điểm đẳng hướng trong không gian tự do và bỏ qua hấp thụ/phản xạ đáng kể.

## 12. Tốc độ truyền âm và sự thay đổi môi trường

Tốc độ truyền âm không phải một hằng số chung cho mọi môi trường. Nó phụ thuộc vào tính đàn hồi, khối lượng riêng và trạng thái của môi trường; trong chất khí còn phụ thuộc đáng kể vào nhiệt độ.

Khi một sóng âm truyền từ môi trường này sang môi trường khác, **tần số do nguồn quyết định nên không đổi**. Từ

$$
v=\lambda f,
$$

nếu tốc độ truyền thay đổi thì bước sóng thay đổi theo.

Ví dụ, một âm 500 Hz truyền từ môi trường A có $v_A=300$ m/s sang môi trường B có $v_B=450$ m/s:

- trong A: $\lambda_A=300/500=0,60$ m;
- trong B: $\lambda_B=450/500=0,90$ m;
- tần số vẫn là 500 Hz.

!!! note "Đừng biến nhận xét định tính thành luật tuyệt đối"
    Trong điều kiện thông thường, âm thường truyền nhanh hơn trong chất rắn và chất lỏng so với trong chất khí. Tuy nhiên giá trị cụ thể phụ thuộc từng vật liệu và điều kiện, nên khi tính phải dùng dữ kiện của đề hoặc số liệu đo.

## 13. Cộng hưởng âm trong cột khí

Cột khí có thể tạo sóng dừng. Với ống lí tưởng một đầu kín, một đầu hở:

$$
L_k=\frac{(2k+1)\lambda}{4},\qquad k=0,1,2,\ldots
$$

Hai chiều dài cộng hưởng liên tiếp cách nhau:

$$
\Delta L=\frac{\lambda}{2}.
$$

Do đó nếu biết tần số nguồn âm $f$:

$$
\boxed{v=2f\Delta L}.
$$

Công thức này rất hữu ích trong thí nghiệm đo tốc độ truyền âm vì dùng hiệu hai vị trí cộng hưởng, thay vì phụ thuộc hoàn toàn vào một chiều dài duy nhất.

### Ví dụ

Hai vị trí cộng hưởng liên tiếp cách nhau 17 cm, nguồn âm có $f=1000$ Hz.

$\Delta L=0,17$ m nên:

$$
v=2\cdot1000\cdot0,17=340\ \text{m/s}.
$$

## 14. Ngưỡng nghe và ngưỡng đau

Tai người không có cùng độ nhạy ở mọi tần số. Vì vậy:

- **ngưỡng nghe** là cường độ nhỏ nhất có thể gây cảm giác âm ở một tần số nhất định;
- **ngưỡng đau** là mức âm rất lớn bắt đầu gây cảm giác đau và có nguy cơ làm tổn thương thính giác.

Các giá trị này phụ thuộc tần số và từng người. Khi làm bài phổ thông, chỉ dùng một giá trị số cụ thể nếu đề đã cho hoặc quy ước rõ.

## Tóm tắt

- Âm là sóng cơ.
- Độ cao chủ yếu do tần số.
- $I=P/S$; nguồn điểm đẳng hướng: $I=P/(4\pi r^2)$.
- $L=10\log_{10}(I/I_0)$ dB.
- Âm sắc liên hệ phổ họa âm.

## 5 điều cần nhớ

1. Âm không truyền trong chân không.
2. Cao/thấp khác to/nhỏ.
3. Mức dB là thang logarit.
4. Cường độ giảm theo $1/r^2$ chỉ trong mô hình phù hợp.
5. Sóng dừng giải thích nhiều tần số riêng của nhạc cụ.


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/05-sound-waves/exercises.md)
- [Đáp án và lời giải](practice/05-sound-waves/solutions.md)

---

[← Bài 4](04-standing-waves.md) | [↑ Chương](index.md) | [Bài 6 →](06-electromagnetic-waves.md)
