---
title: "Bài 9 — Thực hành đo tốc độ truyền âm"
description: "Đo tốc độ truyền âm bằng cộng hưởng cột khí hoặc thời gian truyền; xử lí số liệu và kiểm tra kết quả."
order: 9
difficulty: "standard-applied"
prerequisites:
  - sound-waves
  - standing-waves
  - practical-sound-frequency
tags:
  - physics
  - grade-11
  - waves
  - sound
  - experiment
---

# Bài 9 — Thực hành đo tốc độ truyền âm

## Mục tiêu

Sau bài này, bạn cần:

- hiểu hai cách phổ biến để đo tốc độ truyền âm;
- dùng quan hệ $v=\lambda f$;
- xác định bước sóng từ hai vị trí cộng hưởng liên tiếp của cột khí;
- biết vì sao lấy **hiệu hai chiều dài cộng hưởng** giúp giảm ảnh hưởng của sai lệch ở miệng ống;
- biết xử lí số liệu theo từng bước, không nhảy công thức.

## 1. Tốc độ truyền âm phụ thuộc môi trường

Tần số do nguồn quyết định. Khi âm truyền sang môi trường khác, tần số của dao động cưỡng bức tại biên không tự đổi chỉ vì môi trường đổi.

Do:

$$
v=\lambda f,
$$

nếu $f$ giữ nguyên mà tốc độ $v$ thay đổi thì bước sóng $\lambda$ thay đổi theo.

Trong những điều kiện thông thường, âm thường truyền nhanh hơn trong chất rắn và chất lỏng so với trong chất khí, nhưng giá trị cụ thể còn phụ thuộc vật liệu và nhiệt độ. Không nên biến nhận xét định tính này thành một công thức tuyệt đối cho mọi chất.

## 2. Phương pháp 1 — Cộng hưởng cột khí một đầu kín

Một ống có một đầu kín và một đầu hở có thể tạo sóng dừng với:

- nút dịch chuyển gần đầu kín;
- bụng dịch chuyển gần đầu hở.

Trong mô hình lí tưởng, các chiều dài cộng hưởng là:

$$
L_k=\frac{(2k+1)\lambda}{4},\qquad k=0,1,2,\ldots
$$

Hai vị trí cộng hưởng liên tiếp có hiệu:

$$
L_{k+1}-L_k=\frac{\lambda}{2}.
$$

Suy ra:

$$
\boxed{\lambda=2\Delta L},
\qquad
\boxed{v=2f\Delta L}.
$$

Đây là công thức rất tiện cho thực hành.

## 3. Vì sao dùng hai vị trí cộng hưởng liên tiếp?

Ở ống thật, bụng sóng không nhất thiết nằm đúng ngay mép hình học của miệng ống. Có một hiệu chỉnh đầu ống nhỏ.

Nếu chỉ dùng một chiều dài cộng hưởng duy nhất rồi coi $L=\lambda/4$, sai lệch này có thể ảnh hưởng đáng kể.

Khi lấy hiệu hai chiều dài cộng hưởng liên tiếp, phần hiệu chỉnh gần giống nhau ở cả hai lần đo và phần lớn bị triệt tiêu. Vì vậy phép đo dựa trên $\Delta L$ thường ổn định hơn.

## 4. Dụng cụ cho phương pháp cộng hưởng

Có thể dùng:

- ống cộng hưởng có chiều dài cột khí thay đổi được;
- cột nước hoặc pittông để thay đổi chiều dài phần không khí;
- âm thoa hoặc loa phát tần số đã biết;
- thước đo chiều dài.

Nếu dùng điện thoại làm nguồn âm, nên khóa ở một tần số ổn định.

## 5. Quy trình đo bằng cộng hưởng

### Bước 1 — Biết tần số nguồn

Dùng giá trị ghi trên âm thoa hoặc đo bằng phương pháp ở Bài 8.

### Bước 2 — Thay đổi chiều dài cột khí

Di chuyển mặt nước hoặc pittông từ từ. Khi âm nghe tăng rõ rệt, ghi lại chiều dài cộng hưởng $L_1$.

### Bước 3 — Tìm cộng hưởng tiếp theo

Tiếp tục thay đổi chiều dài theo cùng chiều cho đến khi âm lại tăng rõ rệt. Ghi $L_2$.

### Bước 4 — Tính bước sóng

$$
\Delta L=L_2-L_1,
\qquad
\lambda=2\Delta L.
$$

### Bước 5 — Tính tốc độ truyền âm

$$
v=f\lambda=2f\Delta L.
$$

### Bước 6 — Đo thêm nếu có thể

Nếu thu được $L_1,L_2,L_3,L_4$, hãy tính nhiều khoảng liên tiếp rồi lấy trung bình. Cách này giảm phụ thuộc vào một lần nghe cộng hưởng duy nhất.

## 6. Bảng số liệu gợi ý

| Cặp cộng hưởng | $L_k$ (m) | $L_{k+1}$ (m) | $\Delta L$ (m) | $v=2f\Delta L$ (m/s) |
|---:|---:|---:|---:|---:|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

## 7. Ví dụ cộng hưởng cột khí

Nguồn âm có $f=500$ Hz. Hai vị trí cộng hưởng liên tiếp của cột khí là:

$L_1=0,18$ m và $L_2=0,52$ m.

Hiệu chiều dài:

$\Delta L=0,34$ m.

Bước sóng:

$\lambda=2\Delta L=0,68$ m.

Vậy:

$$
v=f\lambda=500\cdot0,68=340\ \text{m/s}.
$$

## 8. Phương pháp 2 — Đo thời gian truyền hoặc tiếng vọng

Nếu âm đi từ nguồn đến vật phản xạ cách một khoảng $d$, rồi quay về micro, tổng quãng đường là $2d$.

Nếu đo được thời gian khứ hồi $\Delta t$:

$$
\boxed{v=\frac{2d}{\Delta t}}.
$$

### Ví dụ

Tường cách micro 34 m. Từ xung âm phát ra đến lúc thu tiếng vọng là $0,20$ s.

$$
v=\frac{2\cdot34}{0,20}=340\ \text{m/s}.
$$

## 9. So sánh hai phương pháp

### Cộng hưởng cột khí

Ưu điểm:

- liên hệ trực tiếp với sóng dừng;
- không đòi hỏi đo khoảng thời gian rất ngắn;
- hiệu hai cộng hưởng giúp giảm một số sai lệch hình học.

Khó khăn:

- phải nhận biết vị trí âm lớn nhất;
- tiếng ồn phòng có thể làm điểm cộng hưởng kém rõ.

### Thời gian truyền

Ưu điểm:

- trực quan: quãng đường chia thời gian;
- phù hợp khi thiết bị ghi thời gian đủ tốt.

Khó khăn:

- độ trễ của loa, micro hoặc phần mềm có thể đáng kể;
- khoảng cách ngắn làm $\Delta t$ quá nhỏ, tăng sai số tương đối.

## 10. Kiểm tra tính hợp lí của kết quả

Sau khi tính, đừng chỉ chép số.

Hãy kiểm tra:

- đơn vị đã là m/s chưa;
- có dùng đúng quãng đường khứ hồi $2d$ trong bài tiếng vọng không;
- có lấy đúng **hai cộng hưởng liên tiếp** hay không;
- tần số có đổi từ kHz sang Hz chưa;
- kết quả có cùng bậc độ lớn với tốc độ âm quen thuộc trong không khí hay không.

## 11. Bài tập thực hành nhanh

### Câu 1
Nguồn âm 680 Hz. Hai cộng hưởng liên tiếp của cột khí cách nhau 25 cm. Tính tốc độ truyền âm.

### Câu 2
Hai chiều dài cộng hưởng liên tiếp là 16 cm và 50 cm, tần số nguồn 500 Hz. Tính tốc độ âm.

### Câu 3
Một người đứng cách vách đá 68 m và nghe tiếng vọng sau $0,40$ s. Tính tốc độ âm.

### Câu 4
Âm có tần số 400 Hz truyền trong môi trường A với tốc độ 320 m/s rồi sang môi trường B với tốc độ 480 m/s. Tần số và bước sóng trong B là bao nhiêu?

## Đáp án và hướng dẫn

1. $\Delta L=0,25$ m nên $v=2\cdot680\cdot0,25=340$ m/s.
2. $\Delta L=0,34$ m nên $v=2\cdot500\cdot0,34=340$ m/s.
3. Âm đi và về nên quãng đường $2d=136$ m. $v=136/0,40=340$ m/s.
4. Tần số không đổi: $f=400$ Hz. Trong B: $\lambda_B=v_B/f=480/400=1,20$ m.

## Tóm tắt

- $v=\lambda f$.
- Ống một đầu kín: hai cộng hưởng liên tiếp cách nhau $\lambda/2$.
- Vì vậy $v=2f\Delta L$.
- Đo tiếng vọng: $v=2d/\Delta t$.
- Luôn kiểm tra đơn vị, quãng đường và ý nghĩa vật lí của số đo.

## 5 điều cần nhớ

1. Không lấy nhầm $\Delta L$ thành $\lambda$.
2. Hai cộng hưởng liên tiếp cho $\Delta L=\lambda/2$.
3. Tiếng vọng đi hai lượt nên quãng đường là $2d$.
4. Khi đổi môi trường, nguồn không đổi thì tần số không đổi.
5. Kết quả đo phải được kiểm tra về bậc độ lớn và điều kiện thí nghiệm.

---

[← Bài 8](08-practical-sound-frequency.md) | [↑ Chương](index.md) | [Bài 10 →](10-doppler-effect.md)
