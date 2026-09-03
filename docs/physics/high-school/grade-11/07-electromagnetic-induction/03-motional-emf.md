---
title: "Bài 3 — Suất điện động cảm ứng do chuyển động"
description: "Thanh dẫn chuyển động trong từ trường, suất điện động Bℓv, lực từ và cân bằng năng lượng."
order: 3
difficulty: "standard-advanced"
prerequisites:
  - faraday-law
  - magnetic-force-current-wire
tags:
  - physics
  - grade-11
  - motional-emf
---

# Bài 3 — Suất điện động cảm ứng do chuyển động

## Mục tiêu

Bạn cần:

- hiểu vì sao thanh dẫn chuyển động trong B có thể tách điện tích;
- dùng được $\mathcal E=B\ell v$ trong hình học vuông góc chuẩn;
- giải mạch thanh trượt trên ray;
- liên hệ lực kéo, công suất cơ và công suất điện;
- nhận ra khi nào công thức Bℓv không được dùng trực tiếp.

## 1. Cơ chế vi mô

Một thanh dẫn chuyển động với vận tốc $\vec v$ trong từ trường. Các electron tự do trong thanh cùng chuyển động theo thanh nên chịu lực Lorentz:

$$
\vec F=q\vec v\times\vec B.
$$

Điện tích dương và âm bị đẩy về hai phía đối diện, làm xuất hiện hiệu điện thế giữa hai đầu thanh.

Khi lực điện do điện tích phân bố cân bằng lực từ, sự tách điện tích đạt trạng thái ổn định.

## 2. Công thức chuẩn

Thanh dài $\ell$, chuyển động với v, và thanh, v, B đôi một vuông góc:

$$
\boxed{\mathcal E=B\ell v}.
$$

Đây là **suất điện động cảm ứng do chuyển động**.

Trong trường hợp tổng quát, suất điện động do chuyển động liên quan tích phân:

$$
\mathcal E=\int(\vec v\times\vec B)\cdot d\vec l.
$$

Phần này chỉ cần để hiểu giới hạn; bài chuẩn thường dùng Bℓv.

## 3. Thanh trượt trên hai ray

Một thanh dẫn dài $\ell$ trượt trên hai ray dẫn điện, tạo mạch kín có tổng điện trở R. B vuông góc mặt phẳng mạch.

Khi thanh chuyển động tốc độ v:

$$
\mathcal E=B\ell v.
$$

Dòng cảm ứng:

$$
I=\frac{B\ell v}{R}.
$$

Lực từ lên thanh:

$$
F=B I\ell=\frac{B^2\ell^2v}{R}.
$$

Theo Lenz, lực từ chống chuyển động làm tăng từ thông, nên thường là lực cản.

## 4. Công suất và bảo toàn năng lượng

Nếu kéo thanh đều, lực ngoài cân bằng lực từ:

$$
F_{ngoài}=F_t.
$$

Công suất cơ cung cấp:

$$
P_{cơ}=Fv.
$$

Thay lực từ:

$$
P_{cơ}=\frac{B^2\ell^2v^2}{R}.
$$

Công suất Joule:

$$
P_J=I^2R
=\left(\frac{B\ell v}{R}\right)^2R
=\frac{B^2\ell^2v^2}{R}.
$$

Vậy:

$$
\boxed{P_{cơ}=P_J}
$$

trong mô hình bỏ qua tổn hao khác.

Đây là một kiểm tra rất tốt. Nếu tính ra công suất điện lớn hơn công suất cơ trong hệ không có nguồn khác, có thứ gì đó đã đi du lịch khỏi định luật bảo toàn năng lượng.

## 5. Ví dụ

Thanh dài 0,40 m trượt đều với v=5 m/s trong B=0,50 T, tổng điện trở mạch R=2 Ω.

Suất điện động:

$$
\mathcal E=0,50\cdot0,40\cdot5=1,0\,\text V.
$$

Dòng:

$$
I=\frac{1,0}{2}=0,50\,\text A.
$$

Lực từ:

$$
F=B I\ell=0,50\cdot0,50\cdot0,40=0,10\,\text N.
$$

Công suất cơ khi kéo đều:

$$
P=Fv=0,10\cdot5=0,50\,\text W.
$$

Kiểm tra:

$$
I^2R=0,50^2\cdot2=0,50\,\text W.
$$

Khớp.

## 6. Dùng Faraday để suy ra Bℓv

Nếu thanh trượt làm diện tích vòng tăng:

$$
S=\ell x.
$$

Trong B vuông góc mặt vòng:

$$
\Phi=B\ell x.
$$

Do $dx/dt=v$:

$$
|\mathcal E|=\left|\frac{d\Phi}{dt}\right|=B\ell v.
$$

Như vậy Bℓv không phải công thức đứng riêng; nó là một trường hợp đẹp của Faraday.

## 7. Thanh quay — mở rộng

Một thanh dẫn dài l quay quanh một đầu với tốc độ góc $\omega$ trong B vuông góc mặt quay. Mỗi phần nhỏ ở bán kính r có tốc độ $v=\omega r$. Tích phân cho:

$$
\boxed{\mathcal E=\frac12B\omega l^2}.
$$

Đây là bài nâng cao hợp lí sau khi chắc thanh trượt.

## 8. Sai lầm thường gặp

!!! warning "Dùng Bℓv dù hình học không vuông góc"
    Công thức đơn giản giả sử hướng chuyển động, thanh và B có cấu hình thích hợp. Với góc khác, cần lấy thành phần hữu hiệu hoặc dùng biểu thức tổng quát.

!!! warning "Lực từ cùng chiều kéo"
    Với thanh trượt phát điện thuần túy, Lenz cho lực điện từ cản chuyển động gây biến thiên từ thông.

!!! warning "Quên điện trở thanh/ray"
    R phải là tổng điện trở của mạch theo dữ kiện, không mặc định chỉ là điện trở ngoài.

## 9. Phương pháp giải

1. Xác định diện tích vòng đang tăng hay giảm.
2. Tìm suất điện động Bℓv nếu cấu hình chuẩn.
3. Dùng Lenz tìm chiều dòng.
4. Tính I=E/R.
5. Dùng lực từ $F=BIl$.
6. Kiểm tra năng lượng bằng $Fv$ và $I^2R$ khi phù hợp.

## Tóm tắt

Thanh dẫn chuyển động cắt đường sức trong cấu hình chuẩn có suất điện động $\mathcal E=B\ell v$. Khi khép mạch, dòng cảm ứng sinh lực từ cản chuyển động; công cơ chuyển thành điện năng/nhiệt.

## 5 điều cần nhớ

1. Cấu hình chuẩn: $\mathcal E=B\ell v$.
2. Dòng cảm ứng theo Lenz.
3. Thanh trượt: $I=B\ell v/R$.
4. Kéo đều: lực ngoài cân bằng lực từ.
5. Bỏ tổn hao khác: $Fv=I^2R$.


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/03-motional-emf/exercises.md)
- [Đáp án và lời giải](practice/03-motional-emf/solutions.md)

---

[← Bài 2](02-lenz-faraday-law.md) | [↑ Chương](index.md) | [Bài 4 →](04-self-induction-energy.md)
