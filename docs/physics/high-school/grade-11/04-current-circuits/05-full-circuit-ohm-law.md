---
title: "Bài 5 — Định luật Ohm cho toàn mạch"
description: "Dòng điện toàn mạch, hiệu điện thế cực, đoản mạch, hiệu suất và biến thiên theo tải."
order: 5
difficulty: "standard-applied"
prerequisites:
  - emf-internal-resistance
  - energy-power-joule
tags:
  - physics
  - grade-11
  - circuits
  - full-circuit-ohm
---

# Bài 5 — Định luật Ohm cho toàn mạch

## Mục tiêu

Bạn cần:

- dùng $I=\mathcal E/(R+r)$;
- tính U cực;
- phân tích đoản mạch;
- dùng hiệu suất nguồn;
- đọc đồ thị I–R hoặc U–I;
- xử lí mạch ngoài có điện trở tương đương;
- hiểu sự đánh đổi giữa dòng, điện áp tải, công suất và hiệu suất.

## 1. Toàn mạch đơn giản

Nguồn $(\mathcal E,r)$ nối mạch ngoài có điện trở tương đương R.

Dòng điện:

$$
\boxed{I=\frac{\mathcal E}{R+r}}.
$$

Đây là định luật Ohm cho toàn mạch.

Nếu mạch ngoài gồm nhiều điện trở, trước hết tìm $R_{eq}$ rồi thay vào R.

## 2. Hiệu điện thế hai cực nguồn

Khi nguồn phát điện:

$$
\boxed{U=\mathcal E-Ir}.
$$

Vì U cũng là điện áp mạch ngoài:

$$
U=IR.
$$

Kết hợp:

$$
\mathcal E=I(R+r).
$$

## 3. Mạch hở

R ngoài rất lớn, I gần 0:

$$
U\approx\mathcal E.
$$

Vôn kế lí tưởng có điện trở vô hạn nên khi mắc trực tiếp hai cực nguồn hở sẽ đọc $\mathcal E$ theo mô hình.

## 4. Đoản mạch

Nếu R ngoài gần 0:

$$
\boxed{I_{\text{sc}}\approx\frac{\mathcal E}{r}}.
$$

Nếu r nhỏ, dòng có thể rất lớn, gây tỏa nhiệt mạnh và nguy hiểm.

!!! danger "An toàn"
    Không thử đoản mạch pin/ắc quy thực tế để “kiểm chứng công thức”. Dòng lớn có thể làm nóng dây, hỏng pin hoặc gây cháy.

## 5. Hiệu suất

Với mạch ngoài R:

$$
H=\frac{P_R}{P_{\text{nguồn}}}
=\frac{R}{R+r}
=\frac{U}{\mathcal E}.
$$

- R tăng → H tăng;
- nhưng I giảm;
- công suất tải không tăng mãi.

## 6. Khi thay đổi tải R

$I=\mathcal E/(R+r)$ giảm khi R tăng.

$U=IR=\mathcal E R/(R+r)$ tăng từ gần 0 về gần $\mathcal E$ khi R tăng.

$P_R=\mathcal E^2R/(R+r)^2$ tăng đến cực đại tại R=r rồi giảm.

Ba đại lượng I, U, P có xu hướng khác nhau; cần tránh suy luận “R tăng thì mọi thứ giảm”.

## 7. Đồ thị U–I

$$
U=\mathcal E-rI.
$$

Đường thẳng có:

- intercept U khi I=0: $\mathcal E$;
- intercept I khi U=0: $\mathcal E/r$;
- độ dốc -r.

Từ hai điểm thí nghiệm có thể tìm $\mathcal E,r$.

## 8. Nhiều điện trở ngoài

Ví dụ R1 nối tiếp với nhóm R2//R3:

1. tính $R_{23}=R_2R_3/(R_2+R_3)$;
2. $R_{eq}=R_1+R_{23}$;
3. tính dòng mạch chính $I=\mathcal E/(R_{eq}+r)$;
4. tìm điện áp nhóm song song;
5. chia dòng từng nhánh.

Không dùng định luật toàn mạch riêng cho từng nhánh như thể mỗi nhánh nối trực tiếp nguồn.

## 9. Bài tìm r hoặc E từ hai trạng thái

Nếu cùng nguồn nối hai tải R1,R2 tạo dòng I1,I2:

$$
\mathcal E=I_1(R_1+r)=I_2(R_2+r).
$$

Hai phương trình đủ để tìm $\mathcal E,r$.

Tương tự nếu biết U và I:

$$
U=\mathcal E-rI.
$$

## 10. Ví dụ

### Ví dụ 1
$\mathcal E=12$ V, r=1 Ω, R=5 Ω:

I=2 A; U=10 V; H=5/6≈83,3%.

### Ví dụ 2 — Đoản mạch
$\mathcal E=1,5$ V, r=0,5 Ω → $I_{sc}=3$ A.

### Ví dụ 3 — Hai trạng thái
Nếu U giảm tuyến tính 0,5 V khi I tăng 1 A, độ dốc -0,5 V/A → r=0,5 Ω.

## 11. Bẫy

!!! warning "R trong và R ngoài"
    r không được cộng vào R khi tính riêng điện áp mạch ngoài bằng U=IR; nhưng phải cộng trong mẫu của dòng toàn mạch.

!!! warning "Hiệu suất"
    H tăng theo R không nghĩa là tải nhận công suất lớn hơn.

## Tóm tắt

- $I=\mathcal E/(R+r)$.
- $U=\mathcal E-Ir=IR$.
- Đoản mạch: $I_{sc}=\mathcal E/r$.
- $H=R/(R+r)$.
- Đồ thị U–I cho E và r.

## 5 điều cần nhớ

1. R là điện trở tương đương mạch ngoài.
2. Mạch hở: U gần E.
3. Đoản mạch nguy hiểm vì I lớn.
4. U cực giảm khi dòng tải tăng.
5. Công suất tải cực đại khác hiệu suất cực đại.


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/05-full-circuit-ohm-law/exercises.md)
- [Đáp án và lời giải](practice/05-full-circuit-ohm-law/solutions.md)

---

[← Bài 4](04-energy-power-joule.md) | [↑ Chương](index.md) | [Bài 6 →](06-source-combinations.md)
