---
title: "Bài 4 — Dòng điện trong chất bán dẫn"
description: "Bán dẫn tinh khiết, electron–lỗ trống, bán dẫn n/p, tiếp giáp p–n và điốt ở mức phổ thông."
order: 4
difficulty: "standard-enrichment"
prerequisites:
  - current-intensity
tags:
  - physics
  - grade-11
  - semiconductor
  - diode
---

# Bài 4 — Dòng điện trong chất bán dẫn

## Mục tiêu

Bạn cần:

- hiểu bán dẫn khác kim loại ở điểm nào;
- mô tả electron và lỗ trống như hai loại hạt tải hiệu dụng;
- phân biệt bán dẫn tinh khiết, loại n và loại p;
- hiểu tiếp giáp p–n và tính chỉnh lưu của điốt ở mức định tính;
- tránh hiểu "lỗ trống" như một hạt vật chất thật bay trong tinh thể.

## 1. Bán dẫn là gì?

Bán dẫn là vật liệu có độ dẫn nằm giữa chất dẫn tốt và điện môi, đồng thời độ dẫn có thể thay đổi mạnh bởi:

- nhiệt độ;
- pha tạp;
- ánh sáng;
- điện trường và cấu trúc linh kiện.

Silic là ví dụ điển hình.

## 2. Bán dẫn tinh khiết

Trong mô hình liên kết cộng hóa trị, ở nhiệt độ đủ cao một số electron nhận năng lượng để rời trạng thái liên kết và trở thành electron dẫn.

Chỗ thiếu electron trong hệ liên kết được mô tả như một **lỗ trống** mang điện tích hiệu dụng dương.

Một quá trình kích thích tạo ra một cặp electron–lỗ trống.

## 3. Dòng điện trong bán dẫn

Trong điện trường:

- electron dẫn trôi ngược chiều $\vec E$;
- lỗ trống có chuyển động hiệu dụng cùng chiều $\vec E$.

Dòng điện tổng là đóng góp của cả hai loại hạt tải.

## 4. Bán dẫn loại n

Pha tạp donor làm tăng số electron dẫn. Trong bán dẫn n:

- electron là hạt tải đa số;
- lỗ trống là hạt tải thiểu số.

Chữ n gợi "negative" cho hạt tải đa số, nhưng cả miếng bán dẫn vẫn gần trung hòa điện về tổng thể.

## 5. Bán dẫn loại p

Pha tạp acceptor tạo nhiều lỗ trống hiệu dụng hơn.

Trong bán dẫn p:

- lỗ trống là hạt tải đa số;
- electron là hạt tải thiểu số.

## 6. Tiếp giáp p–n

Khi ghép vùng p và n:

- electron từ n khuếch tán sang p;
- lỗ trống từ p khuếch tán sang n;
- gần mặt tiếp giáp hình thành vùng nghèo hạt tải và điện trường nội.

Điện trường nội tạo một hàng rào thế cản sự khuếch tán tiếp tục.

## 7. Phân cực thuận

Nối cực dương nguồn với phía p và cực âm với phía n làm hàng rào thế giảm. Khi điện áp đủ, dòng qua tiếp giáp tăng mạnh.

## 8. Phân cực ngược

Nối ngược lại làm vùng nghèo rộng hơn và dòng rất nhỏ trong điều kiện bình thường, cho đến khi có cơ chế đánh thủng ở điện áp đủ lớn.

Tính chất dẫn mạnh một chiều và cản chiều kia là cơ sở của **điốt bán dẫn**.

## 9. Điốt và chỉnh lưu

Điốt có thể dùng để:

- chỉnh lưu AC thành dòng một chiều xung;
- bảo vệ cực tính;
- tách tín hiệu;
- tạo mạch logic/ghim áp trong cấu hình phù hợp.

Ở mức mạch đơn giản, điốt có thể được mô hình hóa:

- điốt lí tưởng: dẫn hoàn toàn khi thuận, khóa khi ngược;
- mô hình sụt áp gần cố định: ví dụ khoảng 0,7 V cho diode silic trong một miền dòng, nhưng đây chỉ là gần đúng.

## 10. Nhiệt độ và độ dẫn bán dẫn

Khác kim loại, khi nhiệt độ tăng, số hạt tải trong bán dẫn tinh khiết có thể tăng mạnh làm điện trở giảm.

Vì vậy không được áp dụng máy móc quy luật $R$ tăng theo nhiệt độ của kim loại cho bán dẫn.

## 11. Cảm biến và quang dẫn

Ánh sáng có thể tạo thêm cặp electron–lỗ trống, làm độ dẫn thay đổi. Đây là nền tảng của nhiều cảm biến quang và linh kiện bán dẫn.

## 12. Bẫy thường gặp

!!! warning "Bán dẫn n không mang điện âm toàn khối"
    Chữ n nói về loại hạt tải đa số, không có nghĩa vật mang điện âm đáng kể.

!!! warning "Lỗ trống không phải proton di chuyển"
    Lỗ trống là mô tả hiệu dụng của vị trí thiếu electron trong hệ liên kết.

!!! warning "Điốt không phải công tắc lí tưởng trong mọi bài"
    Chỉ dùng mô hình lí tưởng khi đề cho phép. Linh kiện thật có đặc tuyến phi tuyến, dòng rò và giới hạn công suất.

## 13. So sánh nhanh với kim loại

| Đặc điểm | Kim loại | Bán dẫn |
|---|---|---|
| Hạt tải chính | electron dẫn | electron và lỗ trống |
| Ảnh hưởng nhiệt độ điển hình | R tăng khi T tăng | độ dẫn có thể tăng mạnh khi T tăng |
| Điều khiển bằng pha tạp | không phải cơ chế chính | cực kì quan trọng |
| Ứng dụng | dây dẫn, điện trở | diode, transistor, cảm biến, IC |

## Tóm tắt

Bán dẫn đặc biệt vì mật độ và loại hạt tải có thể điều khiển. Pha tạp tạo bán dẫn n/p; tiếp giáp p–n tạo tính chỉnh lưu, nền tảng của điện tử học hiện đại.

## 5 điều cần nhớ

1. Bán dẫn tinh khiết có electron và lỗ trống.
2. n: electron đa số; p: lỗ trống đa số.
3. p–n tạo vùng nghèo và điện trường nội.
4. Phân cực thuận làm dòng tăng mạnh.
5. Quy luật nhiệt độ của bán dẫn khác kim loại.

---

[← Bài 3](03-current-in-gases.md) | [↑ Chương](index.md) | [Bài 5 →](05-vacuum-photoelectric-cell.md)
