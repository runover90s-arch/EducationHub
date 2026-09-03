---
title: "Bài 10 — Hiệu ứng Doppler"
description: "Sự thay đổi tần số thu được khi nguồn và máy thu chuyển động tương đối; công thức, quy tắc dấu và bài tập điển hình."
order: 10
difficulty: "standard-applied"
prerequisites:
  - mechanical-wave-basics
  - sound-waves
tags:
  - physics
  - grade-11
  - waves
  - doppler
---

# Bài 10 — Hiệu ứng Doppler

## Mục tiêu

Sau bài này, bạn cần:

- hiểu vì sao người nghe có thể nhận một tần số khác tần số nguồn phát;
- phân biệt trường hợp **máy thu chuyển động** và **nguồn chuyển động**;
- dùng đúng dấu trong công thức Doppler của sóng âm;
- giải thích hiện tượng còi xe cao hơn khi xe tiến lại gần và trầm hơn khi xe đi xa;
- tránh nhầm vận tốc truyền âm với vận tốc nguồn hay vận tốc người nghe.

## 1. Hiện tượng Doppler là gì?

Hiệu ứng Doppler là sự thay đổi **tần số mà máy thu ghi nhận** khi có chuyển động tương đối giữa nguồn sóng và máy thu.

Điểm quan trọng là nguồn vẫn có thể phát với tần số $f_0$ không đổi. Thứ thay đổi là số mặt sóng đến máy thu trong mỗi giây.

### Trực giác

Hãy tưởng tượng nguồn âm phát đều các đỉnh sóng.

- Khi nguồn tiến về phía người nghe, các đỉnh sóng phía trước bị "dồn" lại, bước sóng phía trước nhỏ hơn nên người nghe nhận tần số lớn hơn.
- Khi nguồn đi xa, các đỉnh sóng bị "kéo giãn", bước sóng lớn hơn nên tần số nhận nhỏ hơn.
- Nếu người nghe chuyển động mà nguồn đứng yên, khoảng cách giữa các đỉnh sóng trong môi trường không đổi, nhưng người nghe gặp các đỉnh sóng nhanh hơn hoặc chậm hơn.

## 2. Kí hiệu dùng trong bài

Ta dùng:

- $v$: tốc độ truyền âm trong môi trường;
- $f_0$: tần số nguồn phát;
- $f'$: tần số máy thu nhận được;
- $v_M$: độ lớn vận tốc của máy thu đối với môi trường;
- $v_S$: độ lớn vận tốc của nguồn đối với môi trường.

!!! warning "Vận tốc phải xét đối với môi trường"
    Với sóng âm, môi trường truyền âm là mốc tự nhiên. Không được chỉ lấy vận tốc tương đối nguồn–người nghe rồi thay tùy tiện vào một công thức đơn giản.

## 3. Nguồn đứng yên, máy thu chuyển động

Nguồn đứng yên nên bước sóng trong môi trường:

$$
\lambda=\frac{v}{f_0}.
$$

Nếu máy thu chuyển động về phía nguồn, tốc độ các mặt sóng đi qua máy thu tăng thành $v+v_M$. Vì vậy:

$$
f'=\frac{v+v_M}{\lambda}=f_0\frac{v+v_M}{v}.
$$

Nếu máy thu đi xa nguồn:

$$
f'=f_0\frac{v-v_M}{v}.
$$

### Cách nhớ

Máy thu nằm ở **tử số**:

- máy thu tiến lại gần nguồn → dấu $+$;
- máy thu rời xa nguồn → dấu $-$.

## 4. Nguồn chuyển động, máy thu đứng yên

Bây giờ máy thu đứng yên. Tốc độ truyền âm trong môi trường vẫn là $v$, nhưng khoảng cách giữa các mặt sóng thay đổi.

Trong một chu kì $T=1/f_0$, nguồn dịch chuyển đoạn $v_ST$.

### Nguồn tiến về phía máy thu

Bước sóng phía trước nguồn:

$$
\lambda'=(v-v_S)T=\frac{v-v_S}{f_0}.
$$

Do đó:

$$
f'=\frac{v}{\lambda'}=f_0\frac{v}{v-v_S}.
$$

### Nguồn đi xa máy thu

$$
\lambda'=\frac{v+v_S}{f_0}
$$

và:

$$
f'=f_0\frac{v}{v+v_S}.
$$

### Cách nhớ

Nguồn nằm ở **mẫu số**:

- nguồn tiến lại gần máy thu → mẫu nhỏ đi → dùng $v-v_S$;
- nguồn đi xa → mẫu lớn lên → dùng $v+v_S$.

## 5. Công thức tổng quát theo quy tắc "lại gần thì tần số tăng"

Trong chuyển động thẳng cùng phương truyền âm:

$$
\boxed{f'=f_0\frac{v\pm v_M}{v\mp v_S}}.
$$

Dấu phải chọn theo chuyển động thực tế:

- máy thu tiến về nguồn: $v+v_M$;
- máy thu rời nguồn: $v-v_M$;
- nguồn tiến về máy thu: $v-v_S$;
- nguồn rời máy thu: $v+v_S$.

Một cách kiểm tra nhanh rất hữu ích:

> Nếu nguồn và máy thu **đang tiến lại gần nhau**, kết quả phải cho $f'>f_0$. Nếu chúng **đang rời xa nhau**, phải có $f'<f_0$.

## 6. Ví dụ 1 — Người nghe tiến về nguồn đứng yên

Một còi phát âm $f_0=600$ Hz. Tốc độ âm $v=340$ m/s. Người nghe chạy về phía nguồn với $v_M=10$ m/s.

Ta có:

$$
f'=600\frac{340+10}{340}\approx617,6\text{ Hz}.
$$

Người nghe tiến về nguồn nên nghe âm cao hơn.

## 7. Ví dụ 2 — Nguồn tiến về người nghe

Xe cứu thương phát còi $f_0=800$ Hz, chạy về phía người đứng yên với $v_S=20$ m/s. Lấy $v=340$ m/s.

$$
f'=800\frac{340}{340-20}=850\text{ Hz}.
$$

Nếu xe chạy ra xa:

$$
f'=800\frac{340}{340+20}\approx755,6\text{ Hz}.
$$

Sự đổi cao độ đột ngột khi xe vừa đi qua người nghe chính là biểu hiện rất quen thuộc của hiệu ứng Doppler.

## 8. Ví dụ 3 — Cả nguồn và máy thu cùng chuyển động

Nguồn phát $f_0=1000$ Hz. Nguồn đi sang phải với 15 m/s, người nghe ở phía trước cũng đi sang phải với 5 m/s. Hai vật đang **tiến gần nhau hay xa nhau**?

Nguồn phía sau chạy nhanh hơn nên khoảng cách giảm: nguồn tiến về máy thu. Máy thu lại chạy cùng chiều sóng, tức chạy ra xa nguồn.

Vậy:

$$
f'=1000\frac{340-5}{340-15}\approx1030,8\text{ Hz}.
$$

Kết quả lớn hơn 1000 Hz, phù hợp trực giác vì khoảng cách giữa nguồn và máy thu đang giảm.

## 9. Sóng phản xạ và bài toán "hai lần Doppler"

Khi âm phản xạ từ một vật **đứng yên**, tần số của sóng phản xạ bằng tần số mà vật cản nhận được.

Nếu vật phản xạ đang chuyển động, có thể phải xét hai bước:

1. vật chuyển động đóng vai trò **máy thu** đối với nguồn ban đầu;
2. sau đó vật đóng vai trò **nguồn thứ cấp** phát sóng phản xạ về người quan sát.

Đây là lý do radar/siêu âm Doppler có thể liên hệ tần số phản hồi với vận tốc mục tiêu. Trong bài phổ thông, hãy tách thành hai lần Doppler thay vì cố nhớ một công thức dài.

## 10. Khi nào không dùng công thức trên?

Công thức đơn giản ở trên giả thiết:

- vận tốc chuyển động nằm trên đường nối nguồn–máy thu;
- tốc độ nguồn nhỏ hơn tốc độ truyền sóng trong môi trường;
- môi trường đứng yên trong hệ quy chiếu đang xét;
- ta đang xét Doppler cổ điển cho sóng cơ.

Nếu chuyển động xiên, chỉ thành phần vận tốc theo phương nối nguồn–máy thu mới trực tiếp làm thay đổi khoảng cách theo phương truyền sóng tại thời điểm xét.

## 11. Bẫy thường gặp

!!! danger "Đổi dấu theo trái/phải"
    Dấu không phụ thuộc máy vẽ nguồn bên trái hay bên phải. Dấu phụ thuộc **đang tiến lại gần hay rời xa**.

!!! warning "Nguồn chuyển động không làm tốc độ âm thành v + vS"
    Tốc độ âm đối với môi trường vẫn là $v$. Nguồn chuyển động làm thay đổi **bước sóng**, không làm âm chạy nhanh hơn trong môi trường.

!!! warning "Máy thu chuyển động không đổi bước sóng trong môi trường"
    Khi nguồn đứng yên, $\lambda=v/f_0$ vẫn cố định trong môi trường; máy thu chỉ gặp các mặt sóng với tốc độ tương đối khác.

## Phương pháp giải nhanh

1. Vẽ nguồn S, máy thu M và chiều truyền âm.
2. Ghi $v$, $v_S$, $v_M$, $f_0$.
3. Xét từng vật đang tiến về hay rời vật kia.
4. Chọn dấu ở tử và mẫu.
5. Tính $f'$.
6. Kiểm tra bằng trực giác: lại gần → cao hơn; rời xa → thấp hơn.

## Tóm tắt

Hiệu ứng Doppler không phải là nguồn "tự đổi tần số". Nó xuất hiện vì quan hệ giữa nguồn, môi trường và máy thu làm số mặt sóng đến máy thu trong một giây thay đổi.

## 5 điều cần nhớ

1. Máy thu chuyển động ảnh hưởng tử số.
2. Nguồn chuyển động ảnh hưởng mẫu số.
3. Lại gần nhau thì $f'$ tăng.
4. Rời xa nhau thì $f'$ giảm.
5. Luôn xét vận tốc đối với môi trường truyền sóng.


<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/10-doppler-effect/exercises.md)
- [Đáp án và lời giải](practice/10-doppler-effect/solutions.md)

---

[← Bài 9](09-practical-sound-speed.md) | [↑ Chương](index.md) | [Bài 11 →](11-light-wave-diffraction-dispersion.md)
