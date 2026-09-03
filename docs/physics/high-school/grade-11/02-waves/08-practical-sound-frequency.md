---
title: "Bài 8 — Thực hành đo tần số của sóng âm"
description: "Đo tần số âm từ dạng sóng theo thời gian bằng micro, dao động kí hoặc phần mềm ghi âm; cách đọc chu kì và giảm sai số."
order: 8
difficulty: "foundation-standard"
prerequisites:
  - sound-waves
  - wave-equation-phase-graphs
tags:
  - physics
  - grade-11
  - waves
  - sound
  - experiment
---

# Bài 8 — Thực hành đo tần số của sóng âm

## Mục tiêu

Sau bài thực hành này, bạn cần:

- hiểu vì sao có thể suy ra tần số âm từ đồ thị dao động theo thời gian;
- xác định được chu kì từ một tín hiệu tuần hoàn tương đối ổn định;
- biết đo trên nhiều chu kì để giảm ảnh hưởng của sai số đọc;
- biết cách tổ chức bảng số liệu và kiểm tra kết quả;
- nhận ra các trường hợp tín hiệu không đủ sạch để đọc trực tiếp một chu kì.

## 1. Ý tưởng của phép đo

Âm do một nguồn tuần hoàn phát ra làm áp suất không khí tại micro biến thiên theo thời gian. Micro biến đổi sự biến thiên đó thành tín hiệu điện. Phần mềm hoặc dao động kí hiển thị tín hiệu dưới dạng đồ thị theo thời gian.

Nếu nguồn âm có chu kì $T$, thì tần số:

$$
\boxed{f=\frac{1}{T}}.
$$

Vấn đề thực hành không nằm ở công thức, mà nằm ở việc **đọc đúng chu kì từ tín hiệu thật**.

## 2. Dụng cụ có thể dùng

Một cấu hình đơn giản gồm:

- nguồn âm có tần số tương đối ổn định: âm thoa, máy phát âm hoặc loa phát một tần số xác định;
- micro của điện thoại hoặc micro ngoài;
- phần mềm hiển thị dạng sóng theo thời gian, hoặc dao động kí nếu phòng học có thiết bị;
- thước thời gian trên màn hình.

Không nhất thiết phải có thiết bị phòng thí nghiệm đắt tiền. Điều quan trọng là tín hiệu phải đủ rõ và trục thời gian phải đọc được.

## 3. Cách nhận biết một chu kì trên đồ thị

Hai điểm được chọn phải có **cùng trạng thái dao động**. Cách dễ nhất là chọn:

- hai đỉnh liên tiếp;
- hai đáy liên tiếp;
- hoặc hai lần tín hiệu đi qua cùng một mức theo cùng chiều.

Khoảng thời gian giữa hai trạng thái lặp lại liên tiếp là một chu kì $T$.

!!! warning "Không chọn hai lần cắt trục bất kì"
    Một dao động gần hình sin cắt trục hai lần trong mỗi chu kì. Nếu chọn hai lần cắt liên tiếp mà không xét chiều chuyển động, rất dễ lấy nhầm $T/2$.

## 4. Vì sao nên đo nhiều chu kì?

Giả sử ta đọc trực tiếp một chu kì rất ngắn. Chỉ cần lệch một vài pixel trên màn hình, sai số tương đối có thể khá lớn.

Thay vào đó, chọn hai điểm cùng pha cách nhau $N$ chu kì. Nếu khoảng thời gian đo được là $\Delta t$ thì:

$$
\boxed{T=\frac{\Delta t}{N}},
\qquad
\boxed{f=\frac{N}{\Delta t}}.
$$

Đo 10 hoặc 20 chu kì thường dễ ổn định hơn đo đúng một chu kì.

## 5. Quy trình thực hành

### Bước 1 — Tạo nguồn âm ổn định

Đặt nguồn âm ở vị trí cố định. Nếu dùng loa, không nên đặt âm lượng quá lớn làm micro bị bão hòa.

### Bước 2 — Ghi tín hiệu

Đặt micro cách nguồn một khoảng vừa phải. Ghi một đoạn âm ngắn, tránh chạm điện thoại hoặc gây tiếng động phụ.

### Bước 3 — Chọn đoạn tín hiệu ổn định

Không nên đo ngay lúc nguồn vừa bắt đầu phát nếu biên độ còn thay đổi mạnh. Chọn đoạn giữa bản ghi có dạng lặp đều.

### Bước 4 — Chọn hai điểm cùng pha

Ví dụ chọn đỉnh thứ nhất và đỉnh thứ 11. Khi đó giữa chúng có 10 chu kì, tức $N=10$.

### Bước 5 — Đọc khoảng thời gian

Đọc $\Delta t$ giữa hai điểm đã chọn, rồi tính:

$$
f=\frac{N}{\Delta t}.
$$

### Bước 6 — Lặp lại

Thực hiện ít nhất 3 lần trên các đoạn tín hiệu khác nhau. Nếu các kết quả gần nhau, lấy giá trị trung bình.

## 6. Bảng ghi số liệu gợi ý

| Lần đo | Số chu kì $N$ | Khoảng thời gian $\Delta t$ (s) | $f=N/\Delta t$ (Hz) |
|---:|---:|---:|---:|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

Sau cùng:

$$
\bar f=\frac{f_1+f_2+f_3}{3}.
$$

Ở mức phổ thông, điều quan trọng nhất là biết kết quả các lần đo có nhất quán hay không; không cần biến bài thực hành thành một bài thống kê dài dòng.

## 7. Ví dụ mẫu

Trên đồ thị, từ đỉnh thứ nhất đến đỉnh thứ 21 có khoảng thời gian $0,040$ s.

Giữa hai đỉnh đó có:

$N=20$ chu kì.

Do đó:

$$
f=\frac{20}{0,040}=500\ \text{Hz}.
$$

Tần số nguồn âm xấp xỉ **500 Hz**.

## 8. Nếu tín hiệu không phải hình sin đẹp

Âm của nhạc cụ hoặc giọng nói thường không phải hình sin đơn giản vì có nhiều họa âm. Tuy vậy, nếu dạng tín hiệu lặp lại đều, chu kì cơ bản vẫn có thể xác định từ khoảng lặp.

Nếu tín hiệu quá phức tạp, có thể dùng phổ tần số của phần mềm và tìm thành phần cơ bản nổi bật. Tuy nhiên, khi học phép đo cơ bản, nên ưu tiên cách đọc chu kì trên miền thời gian vì nó giúp hiểu trực tiếp ý nghĩa của $T$ và $f$.

## 9. Sai số thường gặp

### Chọn nhầm số chu kì

Từ đỉnh thứ 1 đến đỉnh thứ 11 là **10 chu kì**, không phải 11 chu kì.

### Đọc nhầm đơn vị thời gian

Nếu phần mềm hiển thị ms:

$$
1\ \text{ms}=10^{-3}\ \text{s}.
$$

### Micro bị bão hòa

Nếu tín hiệu bị bẹt ở đỉnh hoặc đáy, giảm âm lượng hoặc tăng khoảng cách tới nguồn.

### Nhiễu nền

Tiếng nói, quạt, va chạm bàn hoặc tiếng xe có thể làm đồ thị khó đọc. Chọn đoạn tín hiệu sạch hơn thay vì cố ép một kết quả từ dữ liệu xấu.

## 10. Bài tập thực hành nhanh

### Câu 1
Trên đồ thị, 15 chu kì chiếm $30$ ms. Tính tần số âm.

### Câu 2
Từ đỉnh thứ 3 đến đỉnh thứ 13 của tín hiệu có khoảng thời gian $25$ ms. Tính tần số.

### Câu 3
Ba lần đo cho $f_1=498$ Hz, $f_2=502$ Hz, $f_3=500$ Hz. Tính giá trị trung bình.

### Câu 4
Một học sinh lấy khoảng thời gian giữa hai lần tín hiệu hình sin liên tiếp cắt trục thời gian rồi gọi đó là chu kì. Vì sao cách làm này có thể sai?

## Đáp án và hướng dẫn

1. $f=15/(30\times10^{-3})=500$ Hz.
2. Từ đỉnh thứ 3 đến đỉnh thứ 13 có 10 chu kì, nên $f=10/(25\times10^{-3})=400$ Hz.
3. $\bar f=(498+502+500)/3=500$ Hz.
4. Hai lần cắt trục liên tiếp của tín hiệu hình sin thường cách nhau $T/2$. Muốn lấy đúng $T$, phải chọn hai trạng thái cùng pha, chẳng hạn hai đỉnh liên tiếp hoặc hai lần cắt cùng chiều.

## Tóm tắt

- Đo chu kì rồi dùng $f=1/T$.
- Đo trên nhiều chu kì thường ổn định hơn.
- Với $N$ chu kì trong thời gian $\Delta t$: $f=N/\Delta t$.
- Chọn hai điểm cùng pha.
- Lặp lại phép đo để kiểm tra tính nhất quán.

## 5 điều cần nhớ

1. Đỉnh thứ 1 đến đỉnh thứ 11 là 10 chu kì.
2. ms phải đổi sang s khi tính Hz.
3. Hai lần cắt trục liên tiếp chưa chắc cách nhau một chu kì.
4. Tín hiệu sạch quan trọng hơn cố đọc thật nhiều chữ số.
5. Tần số là số chu kì trong một giây.


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/08-practical-sound-frequency/exercises.md)
- [Đáp án và lời giải](practice/08-practical-sound-frequency/solutions.md)

---

[← Bài 7](07-light-interference.md) | [↑ Chương](index.md) | [Bài 9 →](09-practical-sound-speed.md)
