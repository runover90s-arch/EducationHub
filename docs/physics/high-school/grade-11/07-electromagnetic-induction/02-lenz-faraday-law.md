---
title: "Bài 2 — Định luật Faraday và định luật Lenz"
description: "Độ lớn và chiều suất điện động cảm ứng, quy tắc Lenz, bài biến thiên từ thông."
order: 2
difficulty: "standard-applied"
prerequisites:
  - magnetic-flux
tags:
  - physics
  - grade-11
  - faraday-law
  - lenz-law
---

# Bài 2 — Định luật Faraday và định luật Lenz

## Mục tiêu

Bạn cần:

- tính được suất điện động cảm ứng trung bình;
- hiểu dấu trừ trong Faraday;
- xác định chiều dòng cảm ứng bằng Lenz;
- xử lí đồ thị $\Phi-t$;
- phân biệt “chống sự biến thiên từ thông” với “chống từ trường ban đầu”.

## 1. Định luật Faraday

Với một vòng dây, suất điện động cảm ứng trung bình trong khoảng $\Delta t$:

$$
\boxed{\mathcal E_c=-\frac{\Delta\Phi}{\Delta t}}.
$$

Với N vòng giống nhau:

$$
\boxed{\mathcal E_c=-N\frac{\Delta\Phi}{\Delta t}}.
$$

Nếu chỉ hỏi độ lớn:

$$
\boxed{|\mathcal E_c|=N\frac{|\Delta\Phi|}{\Delta t}}.
$$

Trong giới hạn tức thời:

$$
\mathcal E_c=-N\frac{d\Phi}{dt}.
$$

## 2. Ý nghĩa vật lí

Suất điện động cảm ứng lớn khi:

- từ thông thay đổi nhiều;
- sự thay đổi xảy ra trong thời gian ngắn;
- số vòng N lớn.

Không phải B lớn nhất thì suất điện động lớn nhất. Một B rất lớn nhưng không đổi có thể cho $\mathcal E_c=0$.

## 3. Định luật Lenz

Dòng điện cảm ứng có chiều sao cho từ trường do nó sinh ra **chống lại nguyên nhân làm từ thông qua mạch biến thiên**.

Cách nói ngắn thường dùng: từ trường cảm ứng chống lại **sự biến thiên từ thông**.

### Phân biệt hai trường hợp

- Từ thông theo một chiều đang **tăng** → trường cảm ứng tạo theo chiều ngược để chống tăng.
- Từ thông theo một chiều đang **giảm** → trường cảm ứng tạo cùng chiều đó để chống giảm.

!!! danger "Lenz không nói luôn ngược B ngoài"
    Nếu B ngoài đang giảm, B cảm ứng có thể **cùng chiều** B ngoài. Nó chống sự giảm chứ không chống bản thân B.

## 4. Quy trình xác định chiều dòng cảm ứng

1. Xác định chiều từ trường ngoài qua vòng.
2. Xác định từ thông theo chiều đó đang tăng hay giảm.
3. Chọn chiều $\vec B_c$ để chống biến thiên.
4. Dùng quy tắc nắm tay phải của vòng dây để suy ra chiều dòng cảm ứng.

## 5. Ví dụ — nam châm tiến lại gần vòng

Cực Bắc N của nam châm hướng về vòng và tiến lại gần. Từ trường xuyên qua vòng do nam châm tăng.

Vòng phải tạo trường chống sự tăng, nghĩa là mặt vòng gần nam châm trở thành **cực Bắc** để đẩy cực Bắc đang tới gần.

Từ đó dùng quy tắc tay phải suy chiều dòng nhìn từ phía nam châm.

Nếu nam châm rời xa, từ thông giảm; vòng tạo trường cùng chiều ban đầu, mặt gần nam châm trở thành cực Nam để “giữ” nam châm lại. Đây là biểu hiện trực quan của bảo toàn năng lượng.

## 6. Đồ thị từ thông theo thời gian

Từ Faraday:

$$
|\mathcal E_c|=N\left|\frac{\Delta\Phi}{\Delta t}\right|.
$$

Trên đồ thị $\Phi-t$, độ lớn suất điện động bằng N lần **độ lớn hệ số góc**.

- đoạn ngang: $\mathcal E=0$;
- đoạn thẳng dốc không đổi: $|\mathcal E|$ không đổi;
- dốc càng lớn: suất điện động càng lớn.

### Ví dụ

Từ thông mỗi vòng giảm tuyến tính từ 5 mWb xuống 1 mWb trong 0,20 s, N=50:

$$
|\mathcal E|=50\frac{4\times10^{-3}}{0,20}=1,0\,\text V.
$$

## 7. Cuộn quay đều trong từ trường

Nếu cuộn N vòng diện tích S quay đều với tốc độ góc $\omega$ trong B, chọn

$$
\Phi=BS\cos\omega t.
$$

Khi đó:

$$
\mathcal E=NBS\omega\sin\omega t.
$$

Biên độ suất điện động:

$$
\mathcal E_0=NBS\omega.
$$

Đây là nền của máy phát điện xoay chiều; phần điện xoay chiều thường được học sâu hơn ở lớp sau.

## 8. Năng lượng và Lenz

Nếu dòng cảm ứng lại làm tăng thêm biến đổi ban đầu, hệ có thể tự khuếch đại chuyển động và sinh năng lượng không cần nguồn. Điều đó trái bảo toàn năng lượng. Lenz đảm bảo tác dụng điện từ có xu hướng chống biến đổi gây ra nó.

Ví dụ, kéo nam châm vào cuộn dây có dòng cảm ứng khiến ta cảm thấy lực cản. Công cơ học của tay chuyển hóa thành điện năng/nhiệt trong mạch.

## 9. Dòng điện cảm ứng và điện trở mạch

Nếu mạch kín có điện trở R:

$$
I_c=\frac{|\mathcal E_c|}{R}
$$

trong mô hình mạch thuần trở và bỏ qua tự cảm.

Nếu R tăng mà biến thiên từ thông giữ nguyên, suất điện động không đổi nhưng dòng cảm ứng giảm.

## 10. Ví dụ tổng hợp

Cuộn N=200, S=25 cm² đặt vuông góc B. B giảm đều từ 0,80 T về 0 trong 0,10 s. Điện trở toàn cuộn R=4 Ω.

$S=2,5\times10^{-3}$ m².

Độ lớn suất điện động:

$$
|\mathcal E|=NS\frac{|\Delta B|}{\Delta t}
=200\cdot2,5\times10^{-3}\cdot\frac{0,80}{0,10}=4,0\,\text V.
$$

Dòng cảm ứng:

$$
I=\frac4{4}=1,0\,\text A.
$$

Vì B ngoài đang giảm, B cảm ứng cùng chiều B ngoài để chống sự giảm.

## 11. Sai lầm thường gặp

!!! warning "Quên số vòng N"
    $\Phi$ thường là từ thông một vòng. Suất điện động của cuộn N vòng phải nhân N nếu các vòng cùng điều kiện.

!!! warning "Lấy Phi chia t thay vì Delta Phi chia Delta t"
    Faraday phụ thuộc **biến thiên** từ thông.

!!! warning "Dùng Lenz trước khi xác định tăng hay giảm"
    Câu đầu tiên phải là “từ thông theo chiều đã chọn đang tăng hay giảm?”.

## 12. Phương pháp bài tập

### Dạng tính độ lớn

1. đổi S sang m²;
2. tính $\Phi_1,\Phi_2$;
3. tính $|\Delta\Phi|$;
4. dùng $|\mathcal E|=N|\Delta\Phi|/\Delta t$;
5. nếu mạch thuần trở, dùng I=E/R.

### Dạng chiều

1. xác định $\vec B$ ngoài;
2. xác định tăng/giảm;
3. suy $\vec B_c$;
4. dùng tay phải suy I.

## Tóm tắt

Faraday cho độ lớn/tốc độ biến thiên từ thông; Lenz cho chiều. Dấu trừ trong $\mathcal E=-N\,d\Phi/dt$ biểu diễn đúng mối quan hệ chống lại biến thiên từ thông.

## 5 điều cần nhớ

1. $|\mathcal E|=N|\Delta\Phi|/\Delta t$.
2. Lenz chống **biến thiên**, không phải luôn chống B ngoài.
3. Đồ thị $\Phi-t$: độ dốc quyết định suất điện động.
4. B không đổi và hình học không đổi → E cảm ứng bằng 0.
5. Chiều cảm ứng phù hợp bảo toàn năng lượng.

---

[← Bài 1](01-magnetic-flux-induction.md) | [↑ Chương](index.md) | [Bài 3 →](03-motional-emf.md)
