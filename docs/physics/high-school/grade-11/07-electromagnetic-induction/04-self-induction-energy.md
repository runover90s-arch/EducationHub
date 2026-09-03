---
title: "Bài 4 — Tự cảm và năng lượng từ trường"
description: "Hiện tượng tự cảm, hệ số tự cảm của ống dây, suất điện động tự cảm và năng lượng từ trường."
order: 4
difficulty: "standard-advanced"
prerequisites:
  - faraday-law
  - fields-of-currents-superposition
tags:
  - physics
  - grade-11
  - self-induction
---

# Bài 4 — Tự cảm và năng lượng từ trường

## Mục tiêu

Bạn cần:

- hiểu tự cảm là cảm ứng do chính dòng điện trong mạch gây ra;
- dùng được $\mathcal E_{tc}=-L\Delta I/\Delta t$;
- tính L của ống dây dài lõi không khí;
- tính năng lượng từ trường $W=LI^2/2$;
- hiểu vì sao dòng qua cuộn cảm không thể thay đổi tức thời trong mô hình lí tưởng.

## 1. Tự cảm là gì?

Dòng điện qua một cuộn dây tạo từ trường. Nếu chính dòng điện đó thay đổi, từ trường do nó tạo ra thay đổi, kéo theo từ thông qua cuộn thay đổi. Theo Faraday, cuộn sinh ra suất điện động cảm ứng.

Vì nguyên nhân nằm trong **chính mạch đó**, hiện tượng gọi là **tự cảm**.

## 2. Hệ số tự cảm L

Trong môi trường tuyến tính và hình học cố định, từ thông móc vòng tỉ lệ dòng điện:

$$
N\Phi=LI.
$$

L là **hệ số tự cảm** hay độ tự cảm, đơn vị henry (H).

Một cuộn có L lớn nghĩa là cùng mức biến thiên dòng điện, hiệu ứng tự cảm mạnh hơn.

## 3. Suất điện động tự cảm

Từ Faraday:

$$
\boxed{\mathcal E_{tc}=-L\frac{\Delta I}{\Delta t}}
$$

hoặc tức thời:

$$
\mathcal E_{tc}=-L\frac{dI}{dt}.
$$

Độ lớn:

$$
|\mathcal E_{tc}|=L\frac{|\Delta I|}{\Delta t}.
$$

Dấu trừ là biểu hiện Lenz: suất điện động tự cảm chống lại **sự thay đổi dòng điện**.

- I đang tăng → tự cảm chống tăng;
- I đang giảm → tự cảm có xu hướng duy trì dòng theo chiều cũ.

## 4. Độ tự cảm của ống dây dài

Ống dây lõi không khí/chân không, chiều dài l, tiết diện S, N vòng:

$$
\boxed{L=\mu_0\frac{N^2S}{l}}.
$$

### Xu hướng

- N tăng → L tăng theo $N^2$;
- S tăng → L tăng;
- l tăng với N, S cố định → L giảm.

Nếu có lõi vật liệu từ, L có thể tăng mạnh và phụ thuộc từ thẩm; công thức trên không còn đầy đủ.

## 5. Ví dụ tính L

Ống dây dài 0,50 m, N=1000, S=$4,0\times10^{-4}$ m²:

$$
L=4\pi\times10^{-7}\frac{1000^2\cdot4,0\times10^{-4}}{0,50}
\approx1,01\times10^{-3}\,\text H.
$$

Tức khoảng 1,0 mH.

## 6. Ví dụ suất điện động tự cảm

Cuộn L=0,20 H, dòng giảm từ 3 A xuống 1 A trong 0,05 s.

Độ lớn:

$$
|\mathcal E|=0,20\frac{2}{0,05}=8,0\,\text V.
$$

Chiều của suất điện động có xu hướng duy trì dòng theo chiều ban đầu vì I đang giảm.

## 7. Năng lượng từ trường

Khi dòng tăng qua cuộn cảm, nguồn phải làm công để thiết lập từ trường. Năng lượng tích trong từ trường của cuộn cảm lí tưởng:

$$
\boxed{W=\frac12LI^2}.
$$

Đơn vị J.

### So sánh với tụ điện

- tụ: $W_C=\frac12CU^2$ — năng lượng điện trường;
- cuộn cảm: $W_L=\frac12LI^2$ — năng lượng từ trường.

Sự đối xứng này sẽ xuất hiện rõ hơn trong mạch dao động điện từ ở chương trình sau.

## 8. Tại sao dòng qua cuộn cảm không đổi tức thời?

Nếu I thay đổi hữu hạn trong thời gian gần bằng 0:

$$
\left|\frac{dI}{dt}\right|\to\infty,
$$

thì mô hình $|\mathcal E_L|=L|dI/dt|$ đòi hỏi điện áp vô hạn. Trong mạch vật lí với điện áp hữu hạn, dòng qua cuộn cảm lí tưởng không thể nhảy tức thời.

Điều này tương tự tụ điện lí tưởng: điện áp trên tụ không thể nhảy tức thời nếu dòng hữu hạn.

## 9. Đóng/ngắt mạch có cuộn cảm

### Khi đóng mạch

Dòng có xu hướng tăng; suất tự cảm chống tăng, nên dòng không đạt ngay giá trị xác lập.

### Khi ngắt mạch

Dòng có xu hướng giảm nhanh; suất tự cảm có thể lớn để cố duy trì dòng. Vì vậy công tắc cuộn dây có thể phát tia lửa nếu không có mạch bảo vệ.

Trong mạch điện tử người ta dùng diode dập xung hoặc mạch snubber để tạo đường cho dòng cuộn cảm giảm an toàn.

## 10. Mạch RL — mở rộng

Với nguồn DC E, điện trở R và cuộn L nối tiếp, dòng tăng theo:

$$
I(t)=\frac ER\left(1-e^{-tR/L}\right)
$$

trong mô hình lí tưởng.

Hằng số thời gian:

$$
\tau=\frac LR.
$$

Đây là nội dung mở rộng; mục tiêu chính của bài vẫn là tự cảm, L và năng lượng.

## 11. Sai lầm thường gặp

!!! warning "Tự cảm không luôn chống dòng điện"
    Nó chống **sự biến thiên của dòng**. Khi I giảm, tự cảm có thể tạo suất điện động cùng chiều dòng cũ để giữ nó.

!!! warning "L không phải điện trở"
    L đo bằng H, không phải Ω. Cuộn dây thực còn có điện trở dây quấn, nhưng đó là đại lượng khác.

!!! warning "Quên bình phương N"
    Với ống dây dài lõi không khí, $L\propto N^2$.

## 12. Phương pháp bài tập

1. Nếu hỏi L: đổi S, l sang SI rồi dùng $L=\mu_0N^2S/l$.
2. Nếu hỏi suất tự cảm: tìm $|\Delta I|/\Delta t$.
3. Nếu hỏi chiều: xem I đang tăng hay giảm.
4. Nếu hỏi năng lượng: $W=LI^2/2$.
5. Kiểm tra đơn vị H, V, J.

## Tóm tắt

Tự cảm là cảm ứng điện từ do biến thiên dòng trong chính mạch tạo ra. Suất tự cảm $\mathcal E=-L\,dI/dt$, ống dây dài lõi không khí có $L=\mu_0N^2S/l$, năng lượng từ trường $W=LI^2/2$.

## 5 điều cần nhớ

1. Tự cảm chống sự thay đổi I.
2. $|\mathcal E|=L|\Delta I|/\Delta t$.
3. $L=\mu_0N^2S/l$ cho ống dây dài lõi không khí.
4. $W=LI^2/2$.
5. Dòng qua cuộn cảm lí tưởng không nhảy tức thời.


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/04-self-induction-energy/exercises.md)
- [Đáp án và lời giải](practice/04-self-induction-energy/solutions.md)

---

[← Bài 3](03-motional-emf.md) | [↑ Chương](index.md) | [Bài tập →](exercises.md)
