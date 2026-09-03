---
title: "Bài 1 — Dòng điện trong kim loại"
description: "Electron dẫn, điện trở kim loại, phụ thuộc nhiệt độ, cặp nhiệt điện và siêu dẫn."
order: 1
difficulty: "foundation-applied"
prerequisites:
  - current-intensity
  - resistance-ohm-law
tags:
  - physics
  - grade-11
  - metals
  - current
---

# Bài 1 — Dòng điện trong kim loại

## Mục tiêu

Bạn cần:

- mô tả được hạt tải điện trong kim loại;
- hiểu vì sao kim loại có điện trở;
- dùng quan hệ gần tuyến tính của điện trở theo nhiệt độ trong miền thích hợp;
- hiểu cặp nhiệt điện và suất điện động nhiệt điện;
- nhận biết khái niệm siêu dẫn và giới hạn của mô hình đơn giản.

## 1. Cấu trúc và electron dẫn

Trong kim loại, các nguyên tử liên kết thành mạng tinh thể. Một số electron hóa trị không còn gắn chặt với một nguyên tử riêng lẻ mà có thể chuyển động trong toàn khối kim loại. Ta thường gọi chúng là **electron dẫn** hay electron tự do theo mô hình phổ thông.

Khi chưa có điện trường, chuyển động vi mô của electron hỗn loạn theo nhiều hướng nên không tạo dòng điện vĩ mô có hướng.

Khi có điện trường, chuyển động hỗn loạn vẫn còn nhưng chồng thêm một vận tốc trôi trung bình ngược chiều $\vec E$.

## 2. Bản chất dòng điện trong kim loại

Dòng điện trong kim loại là dòng chuyển dời có hướng của các electron dẫn.

Vì electron mang điện âm:

- electron trôi **ngược chiều điện trường**;
- chiều dòng điện quy ước **cùng chiều điện trường** trong dây dẫn thuần trở.

Liên hệ vi mô đơn giản:

$$
I=neSv_d.
$$

Trong đó n là mật độ electron dẫn, e là độ lớn điện tích electron, S là tiết diện dây và $v_d$ là tốc độ trôi.

## 3. Vì sao kim loại có điện trở?

Electron dẫn tương tác với mạng tinh thể, khuyết tật và dao động nhiệt của mạng. Các tương tác này cản trở chuyển động trôi có hướng.

Khi nhiệt độ kim loại tăng, dao động nhiệt của mạng thường mạnh hơn nên điện trở của kim loại thông thường tăng.

## 4. Điện trở suất và nhiệt độ

Trong một khoảng nhiệt độ không quá rộng, có thể dùng gần đúng:

$$
\rho=\rho_0[1+\alpha(T-T_0)].
$$

Nếu hình học dây không đổi:

$$
R=R_0[1+\alpha(T-T_0)].
$$

Với nhiệt độ Celsius, hiệu nhiệt độ có cùng giá trị số như Kelvin nên có thể dùng $t-t_0$.

### Điều kiện áp dụng

Quan hệ tuyến tính là xấp xỉ. Không được coi $\alpha$ là hằng số chính xác trên mọi khoảng nhiệt độ rất rộng hoặc qua các chuyển pha.

## 5. Ví dụ — Dây tóc bóng đèn

Một dây có $R_0=50\,\Omega$ ở 20°C, hệ số $\alpha=4,5\times10^{-3}\,\text{K}^{-1}$. Nếu nhiệt độ làm việc là 2000°C, theo mô hình tuyến tính:

$$
R=50[1+4,5\times10^{-3}(2000-20)]\approx495,5\,\Omega.
$$

Kết quả giải thích vì sao điện trở dây tóc nóng có thể lớn hơn rất nhiều điện trở khi nguội.

## 6. Hiện tượng nhiệt điện

Nếu hai kim loại khác nhau tạo thành một mạch có hai mối nối ở hai nhiệt độ khác nhau, có thể xuất hiện suất điện động nhiệt điện.

Trong mô hình tuyến tính đơn giản:

$$
\boxed{\mathcal E=\alpha_T(T_2-T_1)}.
$$

$\alpha_T$ là hệ số nhiệt điện của cặp vật liệu.

### Ứng dụng

Cặp nhiệt điện dùng để đo nhiệt độ ở những nơi mà nhiệt kế thông thường không thuận tiện, ví dụ lò nung hoặc hệ đo công nghiệp.

## 7. Hiện tượng siêu dẫn

Một số vật liệu khi hạ dưới nhiệt độ tới hạn có điện trở điện một chiều giảm xuống mức cực nhỏ, về mô hình lí tưởng có thể xem bằng 0. Trạng thái này gọi là **siêu dẫn**.

Siêu dẫn không chỉ là "kim loại lạnh nên điện trở nhỏ". Đây là một pha vật chất có tính chất lượng tử tập thể. Nhiệt độ tới hạn phụ thuộc vật liệu, và từ trường/dòng điện quá lớn có thể phá trạng thái siêu dẫn.

### Hiệu ứng Meissner

Một chất siêu dẫn có thể đẩy từ trường ra khỏi phần thể tích bên trong ở trạng thái siêu dẫn trong điều kiện phù hợp. Đây là hiện tượng quan trọng để phân biệt siêu dẫn với một vật dẫn hoàn hảo đơn giản.

## 8. Bẫy thường gặp

!!! warning "Electron không chạy từ nguồn đến bóng đèn với tốc độ gần ánh sáng"
    Tốc độ trôi của electron có thể rất nhỏ. Tín hiệu điện và điện trường thiết lập trong mạch truyền nhanh hơn rất nhiều.

!!! warning "R tăng theo nhiệt độ không đúng cho mọi vật liệu"
    Đây là đặc trưng điển hình của kim loại trong miền thích hợp, không phải quy luật phổ quát cho bán dẫn hay mọi chất.

!!! warning "Siêu dẫn không có nghĩa mọi tổn hao đều biến mất trong mọi điều kiện"
    Trạng thái siêu dẫn có miền nhiệt độ, từ trường và mật độ dòng giới hạn.

## 9. Phương pháp bài tập

### Dạng 1 — Tìm điện trở ở nhiệt độ khác

1. xác định $R_0,T_0$;
2. đổi hiệu nhiệt độ;
3. dùng $R=R_0[1+\alpha\Delta T]$;
4. kiểm tra R có tăng đúng xu hướng đối với kim loại.

### Dạng 2 — Cặp nhiệt điện

1. xác định hai nhiệt độ;
2. dùng hiệu $T_2-T_1$;
3. đổi $\mu$V/K hoặc mV/K sang V/K nếu cần;
4. tính $\mathcal E$.

## Tóm tắt

Kim loại dẫn điện nhờ electron dẫn. Điện trở xuất hiện do tương tác giữa electron và mạng tinh thể. Nhiệt độ ảnh hưởng điện trở; chênh nhiệt độ giữa hai mối nối của hai vật liệu khác nhau có thể sinh suất nhiệt điện; ở nhiệt độ rất thấp một số vật liệu chuyển sang trạng thái siêu dẫn.

## 5 điều cần nhớ

1. Hạt tải điện trong kim loại: electron dẫn.
2. Electron trôi ngược chiều dòng quy ước.
3. Gần đúng: $R=R_0[1+\alpha\Delta T]$.
4. Cặp nhiệt điện biến chênh nhiệt độ thành suất điện động.
5. Siêu dẫn là trạng thái đặc biệt, không chỉ là "R giảm dần vì lạnh".


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/01-current-in-metals/exercises.md)
- [Đáp án và lời giải](practice/01-current-in-metals/solutions.md)

---

[↑ Chương](index.md) | [Bài 2 →](02-electrolytes-faraday.md)
