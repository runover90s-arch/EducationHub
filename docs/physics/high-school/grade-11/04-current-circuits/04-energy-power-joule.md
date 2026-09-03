---
title: "Bài 4 — Năng lượng điện, công suất và định luật Joule–Lenz"
description: "Điện năng, công suất, nhiệt lượng, định mức thiết bị, hiệu suất và bài toán sử dụng điện."
order: 4
difficulty: "standard-applied"
prerequisites:
  - resistance-ohm-law
  - emf-internal-resistance
tags:
  - physics
  - grade-11
  - circuits
  - power
---

# Bài 4 — Năng lượng điện, công suất và định luật Joule–Lenz

## Mục tiêu

Bạn cần:

- tính điện năng bằng UIt;
- dùng các dạng công suất của điện trở;
- dùng Joule–Lenz;
- đọc công suất/điện áp định mức;
- tính điện năng kWh;
- giải bài nhiệt điện và hiệu suất;
- hiểu điều kiện công suất cực đại ở tải biến đổi.

## 1. Điện năng trên đoạn mạch

Nếu hiệu điện thế U và dòng I không đổi trong thời gian t:

$$
\boxed{A=UIt}.
$$

Đơn vị SI: joule (J).

Vì $q=It$, cũng có $A=Uq$.

## 2. Công suất điện

$$
\boxed{P=\frac{A}{t}=UI}.
$$

Đơn vị: watt (W).

Với điện trở ohmic:

$$
\boxed{P=I^2R=\frac{U^2}{R}}.
$$

Ba dạng tương đương khi U,I,R thuộc **cùng phần tử điện trở**.

## 3. Định luật Joule–Lenz

Nhiệt lượng tỏa trên điện trở:

$$
\boxed{Q=I^2Rt}.
$$

Nếu điện năng hoàn toàn chuyển thành nhiệt trong điện trở, $Q=A$.

Nếu thiết bị còn tạo cơ năng, ánh sáng hữu ích..., không nên đồng nhất toàn bộ điện năng với nhiệt lượng hữu ích.

## 4. Đơn vị kWh

Điện năng thương mại thường dùng kWh:

$$
1\ \text{kWh}=3,6\times10^6\ \text{J}.
$$

Thiết bị công suất P kW chạy t giờ tiêu thụ:

$$
A=P\,t\ \text{kWh}.
$$

## 5. Định mức thiết bị

Thiết bị ghi 220 V – 1000 W nghĩa là khi hoạt động ở điện áp định mức 220 V trong điều kiện thiết kế, công suất khoảng 1000 W.

Nếu coi thiết bị là điện trở cố định quanh trạng thái định mức:

$$
R_{\text{đm}}=\frac{U_{\text{đm}}^2}{P_{\text{đm}}}.
$$

Không mặc định mọi thiết bị điện hiện đại là điện trở thuần cố định.

## 6. Nối thiết bị sai điện áp

Với điện trở thuần R không đổi:

$$
P=\frac{U^2}{R}.
$$

Nếu U tăng 10%, P tăng theo bình phương, khoảng 21%.

Đây là lí do quá áp có thể gây quá nhiệt.

## 7. Bài đun nóng

Điện năng hữu ích làm tăng nhiệt độ:

$$
Q_{\text{ích}}=mc\Delta T
$$

và có thể thêm nhiệt hóa hơi/nóng chảy nếu đề có chuyển pha.

Hiệu suất:

$$
\boxed{H=\frac{Q_{\text{ích}}}{A_{\text{điện}}}}.
$$

Do đó:

$$
t=\frac{Q_{\text{ích}}}{HP}
$$

nếu P không đổi.

## 8. Công suất của nguồn

Nguồn có suất điện động $\mathcal E$:

$$
P_{\text{nguồn}}=\mathcal EI.
$$

Công suất hữu ích ở mạch ngoài R:

$$
P_R=I^2R.
$$

Hao phí trong nguồn:

$$
P_r=I^2r.
$$

Cân bằng:

$$
P_{\text{nguồn}}=P_R+P_r
$$

trong mạch chỉ gồm R ngoài và r trong.

## 9. Công suất tải cực đại

Nguồn $\mathcal E,r$ cấp điện trở tải R:

$$
P_R=I^2R
=\frac{\mathcal E^2R}{(R+r)^2}.
$$

P_R đạt cực đại khi:

$$
\boxed{R=r}.
$$

Khi đó:

$$
P_{\max}=\frac{\mathcal E^2}{4r}.
$$

### Đừng nhầm với hiệu suất cực đại

Khi R=r, hiệu suất nguồn chỉ:

$$
H=\frac{R}{R+r}=\frac12.
$$

Muốn hiệu suất gần 100% cần R≫r, nhưng khi đó công suất tải không cực đại. Đây là hai mục tiêu khác nhau.

## 10. Ví dụ

### Ví dụ 1
Điện trở 6 Ω có dòng 2 A trong 5 phút:

$P=I^2R=24$ W.

$Q=Pt=24\cdot300=7200$ J.

### Ví dụ 2 — Điện năng
Máy 1,5 kW chạy 2 giờ: 3 kWh.

### Ví dụ 3 — Đun nước
Nếu cần 360 kJ nhiệt hữu ích, bếp 1000 W hiệu suất 80%:

$t=360000/(0,8\cdot1000)=450$ s.

## 11. Bẫy

!!! danger "Công suất định mức"
    Không phải cứ cắm thiết bị ở điện áp bất kì thì công suất vẫn bằng công suất ghi trên nhãn.

!!! warning "Chọn công thức P"
    $P=U^2/R$ chỉ dùng khi U là điện áp trên chính điện trở R.

## Tóm tắt

- $A=UIt$.
- $P=UI=I^2R=U^2/R$ cho điện trở.
- $Q=I^2Rt$.
- 1 kWh = 3,6 MJ.
- Tải cực đại: R=r.
- Hiệu suất và công suất cực đại là hai tiêu chí khác nhau.

## 5 điều cần nhớ

1. Đổi thời gian về s khi tính J bằng W·s.
2. kWh là đơn vị năng lượng.
3. Nhãn điện áp–công suất gắn với điều kiện định mức.
4. Bài nhiệt cần hiệu suất nếu có tổn hao.
5. P tải cực đại khi R=r trong mô hình nguồn đơn giản.

<!-- V9_SOURCE_TYPES -->

## Các dạng bài được hệ thống hóa từ ngân hàng PDF

Các dạng dưới đây chỉ sử dụng những nhóm bài đã được gọi tên rõ trong các tài liệu bài tập. Phần trình bày được tổ chức lại để người học nhận diện đề, chọn công cụ và tự kiểm tra kết quả; không tạo thêm tên dạng mới.

### Dạng 1 — Năng lượng, công suất điện

Chọn đúng công thức theo đại lượng đã biết: $A=UIt$, $P=UI$; với điện trở thuần có thể dùng $P=I^2R=U^2/R$. Nhiệt lượng Joule bằng $Q=I^2Rt$ nếu điện năng chuyển hoàn toàn thành nhiệt.

Ở bài thiết bị định mức, từ $U_{đm}$ và $P_{đm}$ suy $R=U_{đm}^2/P_{đm}$ nếu coi điện trở thiết bị không đổi; sau đó mới xét điều kiện mạch thực tế.

<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/04-energy-power-joule/exercises.md)
- [Đáp án và lời giải](practice/04-energy-power-joule/solutions.md)

---

[← Bài 3](03-emf-internal-resistance.md) | [↑ Chương](index.md) | [Bài 5 →](05-full-circuit-ohm-law.md)
