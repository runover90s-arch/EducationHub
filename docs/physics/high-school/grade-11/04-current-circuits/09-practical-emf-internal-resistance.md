---
title: "Bài 9 — Thực hành đo suất điện động và điện trở trong của pin"
description: "Đo nhiều cặp U–I của pin điện hóa, dùng đồ thị U theo I để xác định suất điện động và điện trở trong."
order: 9
difficulty: "standard-applied"
prerequisites:
  - emf-internal-resistance
  - full-circuit-ohm-law
  - circuit-reading-meters
tags:
  - physics
  - grade-11
  - circuits
  - source
  - experiment
---

# Bài 9 — Thực hành đo suất điện động và điện trở trong của pin

## Mục tiêu

Sau bài thực hành, bạn cần:

- mắc đúng ampe kế và vôn kế;
- đo nhiều cặp $(I,U)$ khi thay đổi tải;
- dùng quan hệ $U=\mathcal E-rI$;
- xác định $\mathcal E$ từ tung độ gốc và $r$ từ độ dốc của đồ thị;
- biết cách tính bằng hai điểm khi chưa vẽ đồ thị;
- nhận ra những sai lầm có thể làm nóng pin hoặc sai số liệu.

## 1. Mô hình nguồn thực

Pin thật được mô hình bằng:

- một nguồn lí tưởng có suất điện động $\mathcal E$;
- điện trở trong $r$ nối tiếp với nguồn.

Khi pin đang phát điện, điện áp hai cực là:

$$
\boxed{U=\mathcal E-rI}.
$$

Đây là cơ sở của phép đo.

## 2. Ý nghĩa của đồ thị U–I

Viết theo dạng đường thẳng:

$$
U=\mathcal E+(-r)I.
$$

So với $y=b+ax$:

- tung độ gốc là $\mathcal E$;
- hệ số góc là $-r$.

Vì vậy nếu vẽ $U$ theo $I$, ta không chỉ thấy xu hướng mà còn đọc được hai đại lượng của nguồn.

## 3. Dụng cụ

Một bộ cơ bản gồm:

- pin điện hóa cần đo;
- ampe kế;
- vôn kế;
- biến trở hoặc một số điện trở tải khác nhau;
- công tắc;
- dây nối.

Nếu dùng đồng hồ số, phải chọn đúng chế độ đo và giới hạn đo phù hợp.

## 4. Cách mắc mạch

- Ampe kế mắc **nối tiếp** với tải để đo dòng qua mạch.
- Vôn kế mắc **song song** với hai cực nguồn để đo $U$.
- Biến trở dùng để thay đổi dòng điện.
- Công tắc giúp chỉ đóng mạch trong lúc đọc số liệu.

!!! danger "Không nối tắt hai cực pin"
    Không được nối trực tiếp hai cực pin bằng dây dẫn có điện trở rất nhỏ để "xem dòng cực đại". Dòng lớn có thể làm nóng dây, nóng pin, hỏng thiết bị và làm kết quả đo mất ý nghĩa.

## 5. Quy trình đo

### Bước 1 — Kiểm tra mạch khi công tắc đang mở

Kiểm tra cực của ampe kế, vôn kế và nguồn. Với đồng hồ số, kiểm tra cổng cắm dây đo.

### Bước 2 — Đặt biến trở ở trạng thái dòng nhỏ

Mục đích là tránh dòng quá lớn ngay khi đóng công tắc.

### Bước 3 — Đóng công tắc và đọc số

Ghi một cặp:

$(I_1,U_1)$.

Sau khi đọc xong, mở công tắc nếu cần điều chỉnh mạch.

### Bước 4 — Thay đổi tải

Thay đổi biến trở để thu thêm nhiều cặp $(I,U)$.

Nên có ít nhất 4–5 điểm trải trên một khoảng dòng hợp lí thay vì đo nhiều điểm gần như trùng nhau.

### Bước 5 — Vẽ đồ thị

- trục ngang: $I$ (A);
- trục dọc: $U$ (V).

Nếu mô hình nguồn gần tuyến tính trong vùng đo, các điểm nằm gần một đường thẳng giảm.

### Bước 6 — Suy ra suất điện động và r

Kéo đường thẳng phù hợp qua xu hướng chung của các điểm.

- Giao với trục $U$ tại $I=0$ cho $\mathcal E$.
- Độ lớn hệ số góc cho $r$.

## 6. Tính bằng hai điểm

Nếu chỉ dùng hai điểm đo khác nhau:

$$
\begin{aligned}
U_1&=\mathcal E-rI_1,\\
U_2&=\mathcal E-rI_2.
\end{aligned}
$$

Lấy phương trình thứ nhất trừ phương trình thứ hai:

$$
U_1-U_2=r(I_2-I_1).
$$

Do đó:

$$
\boxed{r=\frac{U_1-U_2}{I_2-I_1}}.
$$

Sau đó:

$$
\boxed{\mathcal E=U_1+rI_1}.
$$

Dùng nhiều điểm và đồ thị vẫn đáng tin hơn vì không phụ thuộc quá mạnh vào một cặp số đo duy nhất.

## 7. Ví dụ mẫu

Đo được:

- khi $I_1=0,10$ A thì $U_1=1,44$ V;
- khi $I_2=0,30$ A thì $U_2=1,32$ V.

Điện trở trong:

$$
r=\frac{1,44-1,32}{0,30-0,10}=0,60\ \Omega.
$$

Suất điện động:

$$
\mathcal E=1,44+0,60\cdot0,10=1,50\ \text{V}.
$$

Kiểm tra bằng điểm thứ hai:

$1,32+0,60\cdot0,30=1,50$ V.

Hai cách cho cùng kết quả, nên phép tính tự nhất quán.

## 8. Bảng số liệu gợi ý

| Lần đo | $I$ (A) | $U$ (V) | $U+rI$ sau khi tìm $r$ (V) |
|---:|---:|---:|---:|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

Cột cuối dùng để kiểm tra: nếu mô hình tốt, các giá trị $U+rI$ phải gần nhau và gần $\mathcal E$.

## 9. Mạch hở có đo được suất điện động không?

Khi vôn kế có điện trở rất lớn và mạch ngoài gần như hở, dòng qua nguồn rất nhỏ:

$I\approx0$.

Khi đó:

$$
U\approx\mathcal E.
$$

Vì vậy số chỉ vôn kế ở mạch hở cho một ước lượng tốt của suất điện động. Tuy nhiên, để xác định cả $r$, vẫn cần các số đo khi nguồn có tải.

## 10. Sai số và cách làm kết quả dễ tin hơn

### Không giữ mạch đóng quá lâu

Khi pin phát dòng liên tục, nhiệt độ và trạng thái hóa học của pin có thể thay đổi, làm số liệu trôi.

### Không đo ở dòng quá lớn

Dòng lớn vừa không an toàn vừa làm mô hình tuyến tính đơn giản kém chính xác hơn.

### Đọc nhiều điểm

Một điểm bất thường do tiếp xúc kém sẽ dễ nhận ra nếu có cả một dãy dữ liệu.

### Kiểm tra đơn vị

Độ dốc có đơn vị:

$$
\frac{\text{V}}{\text{A}}=\Omega,
$$

đúng với đơn vị của điện trở trong.

## 11. Bài tập thực hành nhanh

### Câu 1
Nguồn cho $U=1,46$ V khi $I=0,10$ A và $U=1,34$ V khi $I=0,30$ A. Tính $r$ và $\mathcal E$.

### Câu 2
Đồ thị $U-I$ cắt trục $U$ tại 1,60 V và khi $I$ tăng 0,50 A thì $U$ giảm 0,20 V. Tìm $\mathcal E$ và $r$.

### Câu 3
Một pin có $\mathcal E=1,50$ V, $r=0,50\ \Omega$. Khi dòng là 0,40 A, điện áp hai cực bằng bao nhiêu?

### Câu 4
Vì sao không nên xác định $r$ bằng cách nối tắt pin rồi lấy $r=\mathcal E/I_{sc}$ trong bài thực hành thông thường ở trường học?

## Đáp án và hướng dẫn

1. $r=(1,46-1,34)/(0,30-0,10)=0,60\ \Omega$. $\mathcal E=1,46+0,60\cdot0,10=1,52$ V.
2. $\mathcal E=1,60$ V; $r=0,20/0,50=0,40\ \Omega$.
3. $U=1,50-0,50\cdot0,40=1,30$ V.
4. Nối tắt làm dòng rất lớn, dễ gây nóng và hỏng nguồn hoặc đồng hồ. Ngoài ra trạng thái của pin có thể thay đổi nên phép đo không còn đại diện tốt cho mô hình tuyến tính ở vùng làm việc thông thường.

## Tóm tắt

- Nguồn phát điện: $U=\mathcal E-rI$.
- Đồ thị $U-I$ có tung độ gốc $\mathcal E$ và độ dốc $-r$.
- Hai điểm cho $r=(U_1-U_2)/(I_2-I_1)$.
- Mạch hở cho $U\approx\mathcal E$.
- Đo nhiều điểm và tránh dòng lớn giúp kết quả ổn định hơn.

## 5 điều cần nhớ

1. Ampe kế nối tiếp, vôn kế song song.
2. Đường $U-I$ phải dốc xuống khi nguồn đang phát điện theo mô hình đơn giản.
3. Độ lớn độ dốc chính là $r$.
4. Tung độ gốc chính là $\mathcal E$.
5. Không nối tắt pin để tạo dòng cực lớn trong bài thực hành thông thường.

---

[← Bài 8](08-advanced-circuit-methods.md) | [↑ Chương](index.md) | [Bài 10 →](10-source-receiver-capacitor-branches.md)
