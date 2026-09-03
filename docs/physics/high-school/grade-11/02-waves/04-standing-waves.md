---
title: "Bài 4 — Sóng dừng"
description: "Cơ chế hình thành, nút–bụng, điều kiện sóng dừng trên dây và phương pháp đếm."
order: 4
difficulty: "standard-applied"
prerequisites:
  - mechanical-interference
tags:
  - physics
  - grade-11
  - waves
  - standing-wave
---

# Bài 4 — Sóng dừng

## Mục tiêu

Bạn cần:

- hiểu sóng dừng là giao thoa của hai sóng cùng tần số truyền ngược chiều;
- phân biệt nút và bụng;
- nhớ đúng khoảng cách $\lambda/2$, $\lambda/4$;
- thiết lập điều kiện hai đầu cố định, một đầu cố định–một đầu tự do;
- tính số nút, số bụng và họ tần số riêng;
- không nhầm sóng dừng với “sóng không có dao động”.

## 1. Cơ chế hình thành

Khi sóng tới gặp biên và phản xạ, sóng tới và sóng phản xạ có thể chồng chất. Nếu hai sóng cùng tần số truyền ngược chiều, hệ giao thoa tạo ra các vị trí có biên độ cố định theo không gian.

Một mô hình đối xứng:

$$
u_1=a\cos(\omega t-kx),\qquad
u_2=a\cos(\omega t+kx).
$$

Cộng hai sóng:

$$
u=2a\cos(kx)\cos(\omega t).
$$

Biên độ dao động tại vị trí $x$ là:

$$
A(x)=2a|\cos(kx)|.
$$

Biên độ phụ thuộc vị trí nhưng không trôi theo thời gian: đó là đặc trưng của sóng dừng.

## 2. Nút sóng

**Nút** là điểm có biên độ bằng 0.

Với biểu thức trên:

$$
\cos(kx)=0.
$$

Các nút liên tiếp cách nhau:

$$
\boxed{\frac{\lambda}{2}}.
$$

## 3. Bụng sóng

**Bụng** là điểm có biên độ cực đại.

Các bụng liên tiếp cũng cách nhau $\lambda/2$.

Một nút và bụng gần nhất cách nhau:

$$
\boxed{\frac{\lambda}{4}}.
$$

## 4. Pha dao động giữa các điểm

Trong cùng một “bó sóng”, tức đoạn giữa hai nút liên tiếp, các điểm dao động cùng pha.

Hai bó kề nhau dao động ngược pha.

Ngay tại nút, biên độ bằng 0 nên không gán pha dao động theo cách thông thường.

## 5. Hai đầu cố định

Hai đầu cố định đều là nút. Nếu dây dài $L$, phải chứa một số nguyên $n$ nửa bước sóng:

$$
\boxed{L=n\frac{\lambda}{2}},\qquad n=1,2,3,\ldots
$$

Suy ra:

$$
\lambda_n=\frac{2L}{n},\qquad
f_n=\frac{nv}{2L}.
$$

Đây là các mode dao động riêng của dây.

### Số nút và số bụng

Với mode $n$:

- số bụng = $n$;
- số nút kể cả hai đầu = $n+1$.

## 6. Một đầu cố định, một đầu tự do

Đầu cố định là nút; đầu tự do lí tưởng là bụng. Chiều dài dây phải là số lẻ lần $\lambda/4$:

$$
\boxed{L=(2n+1)\frac{\lambda}{4}},\qquad n=0,1,2,\ldots
$$

Tần số:

$$
\boxed{f_n=\frac{(2n+1)v}{4L}}.
$$

Chỉ các bội lẻ của tần số cơ bản xuất hiện trong mô hình này.

## 7. Phản xạ và đảo pha

Ở đầu cố định, sóng phản xạ bị đảo pha $\pi$ đối với li độ ngang của dây. Ở đầu tự do lí tưởng, phản xạ không đảo pha theo quy ước li độ.

Bạn không nhất thiết phải dùng quy tắc này trong mọi bài đếm nút–bụng, nhưng nó giải thích vì sao đầu cố định là nút và đầu tự do là bụng.

## 8. Bài toán từ số bó sóng

Nếu nhìn thấy $n$ bó trên dây hai đầu cố định, ta có:

$$
L=n\frac{\lambda}{2}.
$$

Ví dụ dây dài $1,2$ m có 3 bó:

$\lambda=2L/3=0,8$ m.

Nếu $v=40$ m/s thì $f=v/\lambda=50$ Hz.

## 9. Bài toán tần số liên tiếp

### Hai đầu cố định

Hai tần số riêng liên tiếp:

$$
f_n=\frac{nv}{2L},\qquad f_{n+1}=\frac{(n+1)v}{2L}.
$$

Hiệu:

$$
\boxed{\Delta f=\frac{v}{2L}}.
$$

### Một đầu cố định, một đầu tự do

Các tần số là $f=(2n+1)v/(4L)$. Hai tần số cho phép liên tiếp cũng cách nhau $v/(2L)$.

## 10. Ví dụ

### Ví dụ 1 — Hai đầu cố định

Dây dài $0,90$ m, có 3 bụng. Vì $n=3$:

$\lambda=2L/n=0,60$ m.

Nếu $f=100$ Hz thì $v=60$ m/s.

### Ví dụ 2 — Một đầu tự do

Ống/đoạn môi trường mô hình một đầu nút, một đầu bụng có chiều dài $L=0,50$ m ở mode cơ bản. Khi đó $L=\lambda/4$, nên $\lambda=2,0$ m.

### Ví dụ 3 — Khoảng cách nút–bụng

Hai nút liên tiếp cách nhau $12$ cm → $\lambda=24$ cm. Nút đến bụng gần nhất là $6$ cm.

## 11. Bẫy thường gặp

!!! danger "Nhầm số bó"
    Với dây hai đầu cố định, mỗi bó ứng với **một nửa bước sóng**, không phải một bước sóng.

!!! warning "Điểm nút không phải đứng yên toàn bộ dây"
    Sóng dừng vẫn có các phần tử dao động mạnh tại bụng. Chỉ các nút có biên độ bằng 0.

## 🔬 Mở rộng

Sóng dừng là cách trực quan để hiểu **mode riêng** và **tần số riêng** của hệ liên tục. Ý tưởng mode riêng sẽ xuất hiện lại trong âm học, dao động của cột khí và nhiều bài toán vật lí hiện đại.

## Tóm tắt

- Nút–nút: $\lambda/2$.
- Bụng–bụng: $\lambda/2$.
- Nút–bụng gần nhất: $\lambda/4$.
- Hai đầu cố định: $L=n\lambda/2$.
- Một đầu cố định, một đầu tự do: $L=(2n+1)\lambda/4$.

## 5 điều cần nhớ

1. Sóng dừng do giao thoa hai sóng ngược chiều.
2. Nút có biên độ 0.
3. Cùng một bó dao động cùng pha.
4. Hai bó kề nhau ngược pha.
5. Điều kiện biên quyết định họ tần số cho phép.

<!-- V9_SOURCE_TYPES -->

## Các dạng bài được hệ thống hóa từ ngân hàng PDF

Các dạng dưới đây chỉ sử dụng những nhóm bài đã được gọi tên rõ trong các tài liệu bài tập. Phần trình bày được tổ chức lại để người học nhận diện đề, chọn công cụ và tự kiểm tra kết quả; không tạo thêm tên dạng mới.

### Dạng 1 — Xác định chiều dài, bước sóng, tốc độ, tần số, số nút, số bụng khi có sóng dừng

Trước hết xác định điều kiện ở hai đầu dây: cố định hay tự do. Hai nút liên tiếp hoặc hai bụng liên tiếp cách nhau $\lambda/2$; một nút và bụng kề nhau cách $\lambda/4$.

Sau khi liên hệ chiều dài dây với số đoạn nửa bước sóng, tìm $\lambda$, rồi dùng $v=\lambda f$. Khi đếm nút/bụng, phải tính đúng hai đầu theo điều kiện biên.

### Dạng 2 — Xác định biên độ của sóng dừng, vị trí các phần tử

Biên độ dao động trong sóng dừng phụ thuộc vị trí. Từ phương trình tổng hợp, biên độ là hệ số đứng trước phần dao động theo thời gian; nó bằng 0 tại nút và cực đại tại bụng.

Khi tìm vị trí có một biên độ cho trước, giải phương trình lượng giác theo tọa độ rồi lọc nghiệm trong đoạn dây thực tế.

### Dạng 14 — Sóng dừng trong các dụng cụ

Xác định mô hình biên của dụng cụ trước: cột khí hở–hở, kín–kín hay kín–hở; dây có hai đầu cố định hay một đầu tự do. Mỗi loại có dãy tần số cộng hưởng khác nhau.

Với ống kín một đầu, chiều dài cộng hưởng thường chứa số lẻ phần tư bước sóng; với hai đầu cùng loại, chiều dài chứa số nguyên nửa bước sóng.

### Dạng 15 — Phương trình – biên độ của sóng dừng

Viết hai sóng truyền ngược chiều có cùng $\omega$, $k$ rồi dùng công thức lượng giác để đưa tổng về tích của một hàm theo vị trí và một hàm theo thời gian. Hệ số theo vị trí chính là biên độ dao động tại điểm xét.

Từ nhân tử không gian có thể suy trực tiếp vị trí nút, bụng và khoảng cách giữa chúng.

<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/04-standing-waves/exercises.md)
- [Đáp án và lời giải](practice/04-standing-waves/solutions.md)

---

[← Bài 3](03-mechanical-interference.md) | [↑ Chương](index.md) | [Bài 5 →](05-sound-waves.md)
