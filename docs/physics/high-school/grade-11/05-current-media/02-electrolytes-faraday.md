---
title: "Bài 2 — Dòng điện trong chất điện phân và định luật Faraday"
description: "Ion trong dung dịch, điện phân, dương cực tan, các định luật Faraday và bài toán mạch chứa bình điện phân."
order: 2
difficulty: "standard-applied"
prerequisites:
  - current-intensity
  - full-circuit-ohm-law
tags:
  - physics
  - grade-11
  - electrolysis
  - faraday
---

# Bài 2 — Dòng điện trong chất điện phân và định luật Faraday

## Mục tiêu

Bạn cần:

- hiểu vì sao dung dịch điện phân dẫn điện;
- xác định chiều chuyển động của ion dương và ion âm;
- mô tả hiện tượng điện phân và dương cực tan;
- dùng định luật Faraday để tính khối lượng chất giải phóng;
- phối hợp bình điện phân với bài mạch điện.

## 1. Chất điện phân

Các dung dịch axit, bazơ, muối hoặc chất điện phân nóng chảy có thể chứa ion dương và ion âm chuyển động tương đối tự do.

Khi đặt điện trường:

- ion dương chuyển về catot;
- ion âm chuyển về anot.

Hai loại ion chuyển ngược hướng nhau nhưng, do mang điện tích trái dấu, phần đóng góp của chúng vào dòng điện quy ước **bên trong chất điện phân** có cùng chiều.

## 2. Bản chất dòng điện trong chất điện phân

Dòng điện trong chất điện phân là dòng chuyển dời có hướng của **ion dương và ion âm** dưới tác dụng của điện trường.

Khác kim loại, dòng điện trong chất điện phân thường đi kèm biến đổi hóa học tại điện cực.

## 3. Điện phân và phản ứng ở điện cực

Khi ion đến điện cực, chúng có thể nhận hoặc nhường electron. Kết quả có thể là:

- kim loại bám lên catot;
- khí thoát ra;
- điện cực bị hòa tan;
- thành phần dung dịch thay đổi.

Chi tiết phản ứng phụ thuộc bản chất chất điện phân và vật liệu điện cực.

## 4. Hiện tượng dương cực tan

Trong một số hệ, anot làm bằng chính kim loại có ion trong dung dịch có thể hòa tan dần khi dòng chạy. Đây là hiện tượng dương cực tan.

Ứng dụng liên quan gồm mạ điện, tinh luyện kim loại và một số quá trình điện hóa công nghiệp.

## 5. Định luật Faraday thứ nhất

Khối lượng chất giải phóng ở điện cực tỉ lệ với điện lượng đi qua bình:

$$
\boxed{m=kq}.
$$

Nếu dòng điện không đổi trong thời gian $t$ thì $q=It$, do đó:

$$
\boxed{m=kIt}.
$$

Nếu dòng thay đổi theo thời gian, phải dùng điện lượng tổng $q=\int I\,dt$ thay vì thay trực tiếp một giá trị $I$ bất kì. Trong các bài phổ thông, thường ngầm coi toàn bộ dòng điện tham gia phản ứng điện phân cần xét; nếu đề cho hiệu suất dòng điện nhỏ hơn 100% thì phải nhân thêm hệ số hiệu suất tương ứng. $k$ là đương lượng điện hóa của chất, có đơn vị khối lượng trên điện lượng, chẳng hạn $\mathrm{kg/C}$ hoặc $\mathrm{g/C}$.

## 6. Định luật Faraday thứ hai

Đương lượng điện hóa tỉ lệ với đương lượng hóa học $A/n$:

$$
\boxed{k=\frac{1}{F}\frac{A}{n}}.
$$

Với:

- $A$: khối lượng mol của chất được giải phóng; trong các bài kim loại đơn nguyên tử, đây thường là khối lượng mol nguyên tử;
- $n$: số mol electron trao đổi trên một mol chất được giải phóng; với ion kim loại đơn giản, $n$ trùng với độ lớn hóa trị của ion;
- $F\approx9,65\times10^4\,\mathrm{C/mol}$ là hằng số Faraday.

Nếu $A$ dùng theo $\mathrm{g/mol}$ thì $k$ nhận đơn vị $\mathrm{g/C}$ và $m$ tính ra gam; nếu $A$ dùng theo $\mathrm{kg/mol}$ thì $k$ có đơn vị $\mathrm{kg/C}$ và $m$ tính ra kilôgam.

Kết hợp:

$$
\boxed{m=\frac{AIt}{nF}}.
$$

## 7. Ý nghĩa vi mô của hằng số Faraday

Một mol electron mang điện lượng xấp xỉ:

$$
F=N_Ae.
$$

Vì vậy công thức Faraday nối điện lượng vĩ mô $q$ với số mol electron trao đổi trong phản ứng điện hóa; chỉ khi dòng điện không đổi mới thay $q=It$.

## 8. Ví dụ — Mạ bạc

Dòng $I=0,50\,\mathrm A$ chạy qua dung dịch bạc trong $t=30$ phút. Lấy $A=108$ g/mol, n=1.

Đổi $t=1800\,\mathrm s$.

$$
m=\frac{108\cdot0,50\cdot1800}{96500}\approx1,01\text{ g}.
$$

## 9. Hai bình điện phân mắc nối tiếp

Nếu hai bình mắc nối tiếp, cùng điện lượng q đi qua cả hai. Do đó:

$$
\frac{m_1}{m_2}=\frac{A_1/n_1}{A_2/n_2}.
$$

Đây là dạng rất gọn vì I và t bị triệt tiêu.

## 10. Bình điện phân trong mạch điện

Bình điện phân có thể được mô hình hóa có điện trở $R_p$ đối với phần mạch điện trong bài phổ thông. Quy trình thường là:

1. giải mạch để tìm $I_p$ qua bình;
2. xác định thời gian t;
3. dùng $m=A I_pt/(nF)$.

Nếu đề cho đèn, ampe kế, nguồn, điện trở..., tuyệt đối không nhảy ngay vào công thức Faraday trước khi tìm đúng dòng qua nhánh bình điện phân.

## 11. Ví dụ — Hai bình nối tiếp

Bình 1 giải phóng Fe với $A_1=56$, $n_1=3$. Bình 2 giải phóng Cu với $A_2=64$, $n_2=2$. Cùng điện lượng đi qua. Nếu $m_{Fe}=1,40$ g:

$$
\frac{m_{Cu}}{1,40}=\frac{64/2}{56/3}.
$$

Suy ra:

$$
m_{Cu}=2,40\text{ g}.
$$

## 12. Bẫy thường gặp

!!! danger "Dùng tổng dòng mạch thay cho dòng qua bình"
    Nếu bình nằm trong một nhánh song song, phải dùng đúng cường độ dòng qua nhánh đó.

!!! warning "Quên hóa trị n"
    Cùng điện lượng, khối lượng không chỉ phụ thuộc A mà phụ thuộc $A/n$.

!!! warning "Đơn vị thời gian"
    Công thức dùng I theo A và t theo s nếu dùng F theo C/mol.

## 13. Mở rộng thực tế

Điện phân là nền tảng của:

- mạ điện;
- điện luyện và tinh chế kim loại;
- sản xuất hóa chất;
- pin điện hóa khi xét quá trình ngược theo góc nhìn phản ứng oxi hóa–khử.

## Tóm tắt

Dòng điện trong chất điện phân do các ion chuyển động có hướng và thường gắn với phản ứng ở điện cực. Định luật Faraday định lượng mối liên hệ giữa điện lượng và khối lượng vật chất biến đổi.

## 5 điều cần nhớ

1. Hạt tải điện: ion dương và ion âm.
2. Điện phân đi kèm biến đổi hóa học.
3. Tổng quát $m=kq$; nếu dòng điện không đổi thì $m=kIt$.
4. $k=(A/n)/F$.
5. Bài mạch phải tìm đúng dòng qua bình trước khi tính m.


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/02-electrolytes-faraday/exercises.md)
- [Đáp án và lời giải](practice/02-electrolytes-faraday/solutions.md)

---

[← Bài 1](01-current-in-metals.md) | [↑ Chương](index.md) | [Bài 3 →](03-current-in-gases.md)
