---
title: "Bài 7 — Đọc và biến đổi mạch; ampe kế, vôn kế lí tưởng"
description: "Nhận diện nút, nối tiếp–song song, dây nối lí tưởng, đo dòng–áp và chiến lược mạch phức tạp."
order: 7
difficulty: "applied-advanced"
prerequisites:
  - resistance-ohm-law
  - full-circuit-ohm-law
tags:
  - physics
  - grade-11
  - circuits
  - circuit-reading
---

# Bài 7 — Đọc và biến đổi mạch; ampe kế, vôn kế lí tưởng

## Mục tiêu

Bạn cần:

- đánh dấu đúng nút điện;
- vẽ lại mạch không làm đổi liên kết;
- nhận diện nối tiếp/song song thật;
- dùng mô hình ampe kế và vôn kế lí tưởng;
- xử lí dây nối tắt;
- khai thác đối xứng/equipotential;
- tránh phụ thuộc vào hình dáng bản vẽ.

## 1. Nút điện

Mọi điểm nối với nhau bằng dây dẫn lí tưởng không có phần tử xen giữa được xem là **cùng một nút**, cùng điện thế.

Đây là nguyên tắc quan trọng nhất khi đọc mạch.

### Quy trình
Dùng kí hiệu A,B,C... tô cùng nhãn cho mọi đoạn dây liên thông.

Sau khi làm vậy, mạch “rối” thường trở thành sơ đồ đơn giản.

## 2. Nối tiếp thật

Hai phần tử nối tiếp khi nút chung giữa chúng **không nối thêm nhánh nào khác**, nên dòng qua chúng bắt buộc bằng nhau.

Nếu tại nút giữa có nhánh rẽ, không được gọi hai phần tử đó nối tiếp.

## 3. Song song thật

Hai phần tử song song khi hai đầu của chúng nối vào cùng hai nút.

Khi đó chúng có cùng hiệu điện thế.

Hình vẽ hai điện trở cạnh nhau không đủ để kết luận song song.

## 4. Dây nối lí tưởng và nối tắt

Dây lí tưởng có R=0 nên mọi điểm trên cùng dây có cùng điện thế.

Nếu một điện trở R bị mắc song song với một dây lí tưởng:

- hiệu điện thế trên R bằng 0;
- dòng qua R bằng 0 trong mô hình;
- R bị “nối tắt”.

!!! warning "Không xóa phần tử tùy ý"
    Chỉ loại R khi chứng minh hai đầu R cùng nút/equipotential, không vì đường dây nhìn như đi vòng qua nó.

## 5. Ampe kế lí tưởng

Ampe kế lí tưởng có điện trở:

$$
R_A=0.
$$

Mắc ampe kế **nối tiếp** với nhánh cần đo dòng.

Trong bài biến đổi mạch, ampe kế lí tưởng có thể được thay bằng dây nối khi chỉ quan tâm cấu trúc, nhưng số chỉ chính là dòng qua nhánh đó.

## 6. Vôn kế lí tưởng

Vôn kế lí tưởng có:

$$
R_V\to\infty.
$$

Mắc song song giữa hai điểm cần đo hiệu điện thế.

Nhánh chỉ chứa vôn kế lí tưởng không có dòng. Tuy nhiên vôn kế vẫn đo chênh lệch điện thế giữa hai nút.

## 7. Khi đồng hồ không lí tưởng

Nếu đề cho điện trở ampe kế $R_A$ hoặc vôn kế $R_V$ hữu hạn, phải coi đồng hồ như điện trở thật:

- ampe kế gây sụt áp;
- vôn kế hút dòng.

Không dùng mô hình lí tưởng nữa.

## 8. Vẽ lại mạch

### Bước 1
Bỏ bớt hình học: chỉ giữ các nút và phần tử nối giữa nút.

### Bước 2
Đặt mỗi nút thành một “thanh” hoặc cột.

### Bước 3
Vẽ phần tử giữa đúng cặp nút.

### Bước 4
Nhận ra nhóm song song/nối tiếp.

Cách này đặc biệt hiệu quả với mạch hình hộp, cầu, dây chéo.

## 9. Đối xứng và điểm cùng điện thế

Nếu mạch và nguồn đối xứng qua một trục, hai điểm đối xứng có thể cùng điện thế. Khi đó nhánh nối giữa chúng không có dòng.

Ví dụ cầu Wheatstone cân bằng:

$$
\frac{R_1}{R_2}=\frac{R_3}{R_4}.
$$

Hai nút giữa có cùng điện thế, dòng qua nhánh cầu bằng 0.

Đây là trường hợp đặc biệt hữu ích.

## 10. Phương pháp nút đơn giản

Ngay cả trước khi học Kirchhoff đầy đủ, có thể dùng bảo toàn dòng tại nút:

**tổng dòng vào = tổng dòng ra**.

Ví dụ dòng chính I tách thành $I_1,I_2$:

$$
I=I_1+I_2.
$$

Kết hợp U=IR giúp giải mạch nhánh.

## 11. Ví dụ

### Ví dụ 1 — Vôn kế
R1=R2 nối tiếp nguồn U. Vôn kế lí tưởng mắc qua R2. Vì không làm tải mạch, điện áp R2 bằng U/2.

### Ví dụ 2 — Ampe kế nối tắt
Nếu ampe kế lí tưởng mắc song song trực tiếp với R, nhánh ampe kế có R=0 làm hai đầu R cùng điện thế. Dòng qua R bằng 0 và dòng có thể rất lớn tùy phần còn lại — cấu hình thực tế nguy hiểm.

### Ví dụ 3 — Cầu cân bằng
Nếu R1/R2=R3/R4, dòng nhánh giữa bằng 0; có thể bỏ nhánh đó khi tính mạch ngoài.

## 12. Bẫy

!!! danger "Mắc đồng hồ sai"
    Ampe kế thực tế không được mắc trực tiếp song song nguồn; vôn kế không được mắc nối tiếp để đo dòng.

!!! warning "Đọc mạch"
    Đừng bắt đầu bấm công thức trước khi xác định các nút. Sai topology thì mọi phép tính sau đều vô nghĩa.

## Tóm tắt

- Dây lí tưởng tạo nút cùng điện thế.
- Nối tiếp dựa trên dòng bắt buộc chung.
- Song song dựa trên cùng hai nút.
- Ampe kế lí tưởng: R=0.
- Vôn kế lí tưởng: R→∞.
- Đối xứng có thể tạo điểm cùng điện thế.

## 5 điều cần nhớ

1. Đánh dấu nút trước.
2. Vẽ lại được phép kéo dây nhưng không đổi cặp nút của phần tử.
3. R song song dây lí tưởng bị nối tắt.
4. Đồng hồ hữu hạn phải tính như điện trở.
5. Cầu cân bằng có thể triệt dòng nhánh giữa.

---

[← Bài 6](06-source-combinations.md) | [↑ Chương](index.md) | [Bài 8 →](08-advanced-circuit-methods.md)
