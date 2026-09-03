---
title: "Bài 7 — Chuyển động của điện tích trong điện trường đều"
description: "Gia tốc điện, chuyển động thẳng biến đổi đều, quỹ đạo parabol và phương pháp năng lượng."
order: 7
difficulty: "applied"
prerequisites:
  - work-potential-voltage
  - electric-field-intensity
tags:
  - physics
  - grade-11
  - electric-field
  - charged-particle
---

# Bài 7 — Chuyển động của điện tích trong điện trường đều

## Mục tiêu

Bạn cần:

- xác định lực và gia tốc của hạt mang điện;
- giải chuyển động khi vận tốc ban đầu song song E;
- giải chuyển động khi vận tốc ban đầu vuông góc E;
- dùng định lí động năng khi bài không cần thời gian/quỹ đạo;
- xử lí đúng dấu của electron;
- nhận biết điểm tương đồng và khác với chuyển động ném trong trọng trường.

## 1. Phương trình động lực học

Trong điện trường đều, bỏ qua lực khác:

$$
\vec F=q\vec E.
$$

Do đó:

$$
\boxed{\vec a=\frac{q}{m}\vec E}.
$$

Gia tốc không đổi nếu E không đổi.

- q dương: a cùng E;
- q âm: a ngược E.

## 2. Hạt ban đầu đứng yên

Nếu thả từ nghỉ trong trường đều, chuyển động là thẳng nhanh dần đều theo hướng lực điện.

Độ lớn gia tốc:

$$
a=\frac{|q|E}{m}.
$$

Sau thời gian t:

$$
v=at,\qquad s=\frac12at^2.
$$

Dùng vectơ hoặc trục có dấu nếu cần xác định chiều.

## 3. Vận tốc ban đầu song song điện trường

Chọn trục Ox cùng chiều E. Khi đó:

$$
a_x=\frac{qE}{m}.
$$

Công thức động học:

$$
\begin{aligned}
&v=v_0+at\\
&x=x_0+v_0t+\frac12at^2,
\end{aligned}
$$

$$
v^2-v_0^2=2a(x-x_0).
$$

Nếu q âm, a có dấu âm trên trục này.

## 4. Phương pháp năng lượng

Nếu hạt đi từ M đến N:

$$
K_N-K_M=qU_{MN}.
$$

Với $K=\tfrac12mv^2$:

$$
\boxed{
\frac12m(v_N^2-v_M^2)=qU_{MN}
}.
$$

Đây thường là cách nhanh nhất khi chỉ hỏi tốc độ sau khi qua hiệu điện thế.

### Electron tăng tốc qua hiệu điện thế

Nếu electron được gia tốc từ nghỉ qua độ chênh điện thế có độ lớn U sao cho lực điện làm công dương:

$$
\frac12mv^2=eU.
$$

Chú ý đây là công thức theo **độ lớn** trong tình huống tăng tốc, tránh nhầm dấu.

## 5. Vận tốc ban đầu vuông góc E

Chọn:

- Ox theo $\vec v_0$;
- Oy theo chiều lực điện.

Theo Ox: chuyển động đều:

$$
x=v_0t.
$$

Theo Oy: chuyển động nhanh dần đều từ $v_{0y}=0$:

$$
y=\frac12at^2.
$$

Loại t bằng $t=x/v_0$:

$$
\boxed{
y=\frac{a}{2v_0^2}x^2
}.
$$

Quỹ đạo là parabol.

Nếu chọn Oy theo E thì $a=qE/m$ có thể âm với q âm, khi đó parabol cong về phía ngược E.

## 6. Hạt qua vùng điện trường hữu hạn

Giữa hai bản dài $\ell$ theo phương x, hạt bay vào với $v_0$ ngang:

Thời gian trong trường:

$$
t=\frac{\ell}{v_0}.
$$

Độ lệch theo y:

$$
y=\frac12\frac{qE}{m}\left(\frac{\ell}{v_0}\right)^2.
$$

Vận tốc ra:

$$
v_x=v_0,\qquad
v_y=\frac{qE}{m}\frac{\ell}{v_0}.
$$

Sau khi ra khỏi điện trường, nếu bỏ qua lực khác, hạt chuyển động thẳng đều theo hướng tiếp tuyến tại điểm ra.

## 7. Góc lệch

Tại cửa ra:

$$
\tan\theta=\frac{v_y}{v_x}
=\frac{qE\ell}{mv_0^2}.
$$

Nếu chỉ cần độ lớn góc, dùng trị tuyệt đối ở tử.

## 8. Điện trường và trọng trường

Bài hạt điện trong điện trường đều có cấu trúc toán giống ném ngang trong trọng trường:

- gia tốc không đổi;
- một phương chuyển động đều;
- phương kia biến đổi đều;
- quỹ đạo parabol.

Nhưng gia tốc điện phụ thuộc $q/m$ và đổi chiều theo dấu q; gia tốc trọng trường gần mặt đất không phụ thuộc khối lượng của vật thử trong mô hình cơ học cổ điển.

## 9. Có thêm trọng lực

Nếu trọng lực không bỏ qua:

$$
m\vec a=q\vec E+m\vec g.
$$

Ta cộng vectơ hai gia tốc:

$$
\vec a=\frac{q}{m}\vec E+\vec g.
$$

Trong bài vi mô electron/proton, trọng lực thường rất nhỏ so với lực điện và được bỏ qua nếu đề cho phép.

## 10. Ví dụ

### Ví dụ 1 — Proton trong E
Proton trong trường $E=10^4$ V/m:

$a=eE/m_p$.

Chỉ cần công thức; nếu đề cho $m_p$ mới thay số.

### Ví dụ 2 — Electron qua U
Electron từ nghỉ được tăng tốc qua $U=100$ V:

$$
v=\sqrt{\frac{2eU}{m_e}}.
$$

### Ví dụ 3 — Lệch trong hai bản
Hạt q dương bay ngang vào trường E hướng lên. Quỹ đạo cong lên vì lực và gia tốc hướng lên.

## 11. Bẫy thường gặp

!!! danger "Electron"
    Electron có $q=-e$. Nếu trục Oy chọn cùng E thì $a_y=-eE/m_e$, không phải $+eE/m_e$.

!!! warning "Năng lượng và dấu U"
    Dùng $K_N-K_M=qU_{MN}$ với đúng thứ tự điểm. Nếu dùng công thức tăng tốc $eU$, phải hiểu U là độ lớn độ giảm thế năng trên điện tích electron trong tình huống đó.

## Tóm tắt

- $\vec a=q\vec E/m$.
- Song song E → chuyển động thẳng biến đổi đều.
- Vuông góc E → parabol.
- Năng lượng: $\Delta K=qU_{MN}$.
- Sau khi ra khỏi vùng E, hạt đi thẳng đều nếu không còn lực.

## 5 điều cần nhớ

1. Dấu q quyết định chiều a.
2. Tách hai phương độc lập khi E vuông góc v0.
3. Dùng năng lượng nếu không cần thời gian.
4. Đổi đơn vị electron/proton cẩn thận.
5. Kiểm tra xem trọng lực có được bỏ qua không.


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/07-charged-particle-motion/exercises.md)
- [Đáp án và lời giải](practice/07-charged-particle-motion/solutions.md)

---

[← Bài 6](06-capacitors.md) | [↑ Chương](index.md) | [Bài 8 →](08-advanced-capacitors.md)
