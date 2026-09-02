---
title: "Bài 1 — Dòng điện và cường độ dòng điện"
description: "Bản chất dòng điện, chiều quy ước, hạt tải điện, cường độ dòng điện và liên hệ vi mô."
order: 1
difficulty: "foundation-standard"
prerequisites:
  - electron-theory-charge-conservation
tags:
  - physics
  - grade-11
  - circuits
  - current
---

# Bài 1 — Dòng điện và cường độ dòng điện

## Mục tiêu

Bạn cần:

- định nghĩa dòng điện;
- phân biệt chiều dòng điện quy ước với chiều electron;
- nhận biết hạt tải điện trong kim loại và chất điện phân ở mức mô hình;
- dùng $I=\Delta q/\Delta t$;
- dùng $I=neSv_d$ trong dây dẫn kim loại khi phù hợp;
- tính số electron đi qua tiết diện;
- đọc đồ thị $I-t$ để tìm điện lượng.

## 1. Dòng điện

Dòng điện là dòng chuyển dời có hướng của các hạt mang điện.

Điều kiện để có dòng điện bền trong một mạch thường gồm:

- có hạt tải điện tự do hoặc có khả năng chuyển động có hướng;
- có điện trường/lực điện duy trì chuyển động có hướng;
- với mạch kín dùng nguồn, cần đường dẫn kín phù hợp.

## 2. Chiều dòng điện quy ước

Chiều dòng điện được quy ước là chiều chuyển động của **điện tích dương**.

Trong kim loại:

- electron dẫn chuyển động có hướng ngược chiều dòng điện quy ước;
- ngoài chuyển động có hướng nhỏ, electron còn có chuyển động nhiệt hỗn loạn.

!!! warning "Bẫy thường gặp"
    “Dòng điện đi từ dương sang âm” là mô tả chiều dòng quy ước trong nhiều mạch ngoài nguồn, không phải mô tả chiều electron trong kim loại.

## 3. Hạt tải điện

### Kim loại
Hạt tải điện chủ yếu là electron dẫn.

### Chất điện phân
Dòng điện do các ion dương và ion âm chuyển động có hướng ngược nhau, nhưng đóng góp của chúng vào **chiều dòng quy ước** được cộng theo quy tắc điện tích.

Nội dung sâu về cơ chế dẫn điện của các môi trường khác không cần cho phần mạch cơ bản này.

## 4. Cường độ dòng điện

Trong khoảng thời gian $\Delta t$, điện lượng đại số có độ lớn $\Delta q$ đi qua tiết diện:

$$
\boxed{I=\frac{\Delta q}{\Delta t}}
$$

cho dòng không đổi.

Đơn vị: ampere (A), với $1$ A = $1$ C/s.

Với dòng biến thiên, công thức trên cho cường độ trung bình trên khoảng thời gian; mô tả tức thời cần khái niệm giới hạn.

## 5. Dòng điện không đổi

Dòng điện không đổi có cường độ không đổi theo thời gian.

Khi đó:

$$
\boxed{q=It}.
$$

Số electron tương ứng:

$$
N=\frac{q}{e}=\frac{It}{e}.
$$

### Ví dụ
Dòng 2 A chạy trong 5 s:

$q=10$ C.

Số electron có độ lớn tương đương:

$N=10/e\approx6,24\times10^{19}$.

## 6. Liên hệ vi mô trong dây kim loại

Xét dây tiết diện S, mật độ hạt tải n (số hạt trên một đơn vị thể tích), điện tích mỗi hạt có độ lớn e và tốc độ trôi trung bình $v_d$.

Trong thời gian $\Delta t$, lớp hạt có chiều dài $v_d\Delta t$ đi qua tiết diện. Số hạt:

$$
N=nSv_d\Delta t.
$$

Điện lượng:

$$
\Delta q=neSv_d\Delta t.
$$

Suy ra:

$$
\boxed{I=neSv_d}.
$$

### Ý nghĩa

Dòng mạnh hơn có thể do:

- mật độ hạt tải lớn hơn;
- tiết diện lớn hơn;
- tốc độ trôi lớn hơn;
- điện tích mỗi hạt lớn hơn.

Trong kim loại cùng loại ở điều kiện nhất định, n gần như cố định.

## 7. Tốc độ trôi không phải tốc độ tín hiệu

$v_d$ của electron thường rất nhỏ so với tốc độ lan truyền điện trường/tín hiệu điện trong mạch. Vì vậy đèn có thể sáng gần như ngay khi đóng công tắc dù electron riêng lẻ không chạy từ công tắc đến đèn trong khoảng thời gian đó.

Đây là phân biệt quan trọng về mô hình.

## 8. Đồ thị I–t và điện lượng

Nếu I thay đổi theo thời gian, điện lượng đi qua bằng diện tích đại số dưới đồ thị I–t:

$$
q=\int I\,dt.
$$

Ở mức bài phổ thông với đoạn thẳng/hằng số, ta tính bằng diện tích hình chữ nhật, tam giác, hình thang.

### Ví dụ
I giảm đều từ 4 A về 0 trong 2 s. Diện tích tam giác:

$q=\tfrac12\cdot2\cdot4=4$ C.

## 9. Mật độ dòng điện

Ở phần mở rộng, có thể dùng mật độ dòng $J=I/S$ cho dòng phân bố đều qua tiết diện. Khi mô hình kim loại đơn giản:

$$
J=nev_d.
$$

Đây không phải đại lượng bắt buộc cho mọi bài Vật lí 11, nhưng giúp nhìn rõ vai trò tiết diện.

## 10. Bẫy thường gặp

!!! warning "Điện lượng và điện tích của dây"
    $q=It$ là lượng điện tích **đi qua tiết diện**, không phải điện tích toàn bộ dây dẫn.

!!! warning "Đổi đơn vị"
    mA = $10^{-3}$ A; $\mu$A = $10^{-6}$ A. Phút, giờ phải đổi sang giây khi dùng C/s.

## Tóm tắt

- Dòng điện là chuyển dời có hướng của điện tích.
- Chiều quy ước theo điện tích dương.
- $I=q/t$ với dòng không đổi.
- $q=It$, $N=It/e$.
- Trong mô hình kim loại: $I=neSv_d$.
- Diện tích dưới đồ thị I–t cho điện lượng.

## 5 điều cần nhớ

1. Electron trong kim loại đi ngược chiều dòng quy ước.
2. I đo mức điện lượng qua tiết diện mỗi giây.
3. Không nhầm q đi qua tiết diện với điện tích tích trên dây.
4. Tốc độ trôi của electron không phải tốc độ lan truyền tín hiệu.
5. Đồ thị I–t là công cụ tìm q khi I thay đổi.

---

[↑ Chương](index.md) | [Bài 2 →](02-resistance-ohm-law.md)
