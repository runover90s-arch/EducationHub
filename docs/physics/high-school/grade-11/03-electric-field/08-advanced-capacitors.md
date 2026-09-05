---
title: "Bài 8 — Ghép tụ và các bài toán tụ điện nâng cao"
description: "Ghép nối tiếp–song song, chia điện áp, bảo toàn điện tích, chuyển mạch, điện môi và chiến lược giải."
order: 8
difficulty: "advanced"
prerequisites:
  - capacitors
tags:
  - physics
  - grade-11
  - electric-field
  - capacitor
  - advanced
---

# Bài 8 — Ghép tụ và các bài toán tụ điện nâng cao

## Mức độ

**Mức 4 — Nâng cao.** Phần này nên học sau khi đã chắc $Q=CU$ và năng lượng của một tụ.

## Mục tiêu

Bạn cần:

- tính điện dung tương đương;
- phân phối điện tích và điện áp trong bộ tụ;
- nhận ra các nút cô lập để dùng bảo toàn điện tích;
- giải bài chuyển mạch theo từng trạng thái;
- xử lí thay đổi C khi nối nguồn hoặc cô lập;
- kiểm tra năng lượng và giới hạn điện áp.

## 1. Ghép song song

Các tụ song song có cùng hiệu điện thế U.

Tổng điện tích:

$$
Q=Q_1+Q_2+\cdots.
$$

Vì $Q_i=C_iU$:

$$
\boxed{C_{\text{ss}}=C_1+C_2+\cdots}.
$$

Điện dung tương đương lớn hơn từng tụ thành phần.

## 2. Ghép nối tiếp

Trong chuỗi tụ nối tiếp lý tưởng ban đầu không tích điện ở các nút giữa, độ lớn điện tích trên các tụ bằng nhau:

$$
Q_1=Q_2=\cdots=Q.
$$

Hiệu điện thế tổng:

$$
U=U_1+U_2+\cdots.
$$

Suy ra:

$$
\boxed{
\frac1{C_{\text{nt}}}
=
\frac1{C_1}+\frac1{C_2}+\cdots
}.
$$

Với hai tụ:

$$
C_{\text{nt}}=\frac{C_1C_2}{C_1+C_2}.
$$

## 3. Chia điện áp trong chuỗi nối tiếp

Vì Q bằng nhau:

$$
U_i=\frac{Q}{C_i}.
$$

Do đó điện áp **tỉ lệ nghịch điện dung**. Tụ có C nhỏ hơn chịu điện áp lớn hơn.

Với hai tụ:

$$
\frac{U_1}{U_2}=\frac{C_2}{C_1}.
$$

Điều này quan trọng khi kiểm tra điện áp định mức.

## 4. Mạch hỗn hợp

Chiến lược:

1. đánh dấu các nút cùng điện thế;
2. tìm nhóm thực sự song song/nối tiếp;
3. rút gọn từng tầng;
4. tính C tương đương;
5. đi ngược để tìm Q,U từng tụ.

Không được kết luận hai tụ song song chỉ vì hình vẽ “nằm song song”; phải kiểm tra hai đầu của chúng nối vào **cùng hai nút**.

## 5. Nút cô lập và bảo toàn điện tích

Trong mạch tụ, một vật dẫn/nút bị cô lập điện có tổng điện tích không đổi.

Nếu nút B nối các bản tụ nhưng không nối nguồn hay đất:

$$
\boxed{\sum q_B=\text{hằng số}}.
$$

Đây là công cụ mạnh khi có chuyển mạch hoặc tụ ban đầu đã tích điện.

## 6. Nối hai tụ đã tích điện

Nếu hai tụ được nối song song cùng cực tính và hệ cô lập:

Tổng điện tích bảo toàn:

$$
Q_{\text{tot}}=C_1U_1+C_2U_2.
$$

Điện áp cuối chung:

$$
\boxed{
U_f=\frac{C_1U_1+C_2U_2}{C_1+C_2}
}.
$$

Nếu nối ngược cực tính, phải gán dấu điện tích theo nút trước khi cộng.

### Năng lượng
Năng lượng điện trường sau nối thường nhỏ hơn tổng ban đầu; phần chênh chuyển thành nhiệt, bức xạ điện từ và các dạng khác trong quá trình quá độ. Không được áp dụng bảo toàn năng lượng **chỉ cho năng lượng tụ** mà bỏ hệ ngoài.

## 7. Bài thay C khi tụ nối nguồn

Nguồn lí tưởng giữ U không đổi.

Ví dụ tăng C từ C lên $\alpha C$:

- $Q$ tăng $\alpha$ lần;
- $W=\tfrac12CU^2$ tăng $\alpha$ lần.

Nguồn cung cấp điện tích và năng lượng.

## 8. Bài thay C khi tụ cô lập

Q không đổi.

Nếu $C'=\alpha C$:

- $U'=U/\alpha$;
- $W'=W/\alpha$.

Sự thay đổi năng lượng liên hệ công cơ học khi thay hình học/điện môi.

## 9. Lắp điện môi một phần

Nếu điện môi chỉ lấp **một phần diện tích** giữa hai bản và mặt phân cách song song với đường sức theo kiểu chia diện tích, có thể mô hình như hai tụ **song song**.

Nếu điện môi xếp thành lớp theo chiều đường sức, có thể mô hình như các lớp tụ **nối tiếp**.

Không dùng một công thức duy nhất cho mọi cách đặt điện môi; phải nhìn hình học.

## 10. Chuyển mạch

Bài chuyển mạch nên chia thành trạng thái.

### Trạng thái 1
Tính điện tích từng tụ trước khi chuyển.

### Thời điểm chuyển
Điện tích trên tụ không thể đổi “vô hạn tức thời” nếu không có dòng xung; trong bài lí tưởng có thể có quá trình quá độ rất nhanh. Ta quan tâm trạng thái sau khi đã ổn định mới.

### Trạng thái 2
Xác định:
- nút nào nối nguồn → điện thế bị khống chế;
- nút nào cô lập → bảo toàn điện tích;
- nhóm nào song song/nối tiếp ở cấu hình mới.

Sau đó giải hệ $Q=CU$ và phương trình nút.

## 11. Ví dụ

### Ví dụ 1 — Hai tụ nối tiếp
$C_1=2\,\mu$F, $C_2=3\,\mu$F, U=12 V.

$C_{eq}=1,2\,\mu$F.  
$Q=C_{eq}U=14,4\,\mu$C.

$U_1=Q/C_1=7,2$ V; $U_2=4,8$ V.

### Ví dụ 2 — Nối song song hai tụ đã tích
$C_1=2\,\mu$F ở 10 V, $C_2=3\,\mu$F ở 0 V. Nối cùng cực tính:

$$
U_f=\frac{2\cdot10+3\cdot0}{5}=4\ \text{V}.
$$

### Ví dụ 3 — Tụ cô lập đưa điện môi
$\varepsilon_r=5$ lấp đầy, nên C tăng 5 lần. Q không đổi → U giảm 5 lần, năng lượng giảm 5 lần.

## 12. Kiểm tra định mức

Sau khi tìm U từng tụ, phải so sánh $|U_i|$ với điện áp định mức. Một bộ tụ có C tương đương đúng vẫn có thể không an toàn nếu một tụ riêng chịu quá áp.

## 13. Bẫy thường gặp

!!! danger "Nối tiếp không phải lúc nào cũng Q bằng nhau"
    Quy tắc độ lớn điện tích bằng nhau áp dụng cho chuỗi nối tiếp với các nút giữa ban đầu trung hòa/cô lập trong cấu hình chuẩn. Nếu nút giữa mang điện tích ban đầu, cần dùng bảo toàn điện tích nút.

!!! warning "Hình vẽ"
    Nhìn dây nối và nút điện, không nhìn vị trí hình học của kí hiệu tụ.

## Tóm tắt

- Song song: $C_{eq}=\sum C_i$, cùng U.
- Nối tiếp chuẩn: $1/C_{eq}=\sum1/C_i$, cùng |Q|.
- Nút cô lập: tổng điện tích bảo toàn.
- Chuyển mạch: chia trạng thái.
- Nối nguồn giữ U; cô lập giữ Q.

## 5 điều cần nhớ

1. Gán tên nút trước khi rút gọn.
2. Điện áp chia nghịch với C trong nối tiếp chuẩn.
3. Bảo toàn điện tích theo nút là công cụ cốt lõi.
4. Năng lượng của riêng các tụ không nhất thiết bảo toàn khi nối lại.
5. Luôn kiểm tra điện áp định mức.

## Các dạng bài trọng tâm

Các nhóm bài dưới đây được tổ chức theo dấu hiệu nhận biết và công cụ giải để người học chọn phương pháp phù hợp và tự kiểm tra kết quả.

### Dạng 2 — Ghép các tụ điện

Trước hết nhận dạng chính xác các nút để xác định tụ nối tiếp hay song song. Tụ song song có cùng hiệu điện thế và điện dung tương đương bằng tổng; tụ nối tiếp có cùng độ lớn điện tích và nghịch đảo điện dung tương đương bằng tổng các nghịch đảo.

Với mạch nhiều tầng, rút gọn từng nhóm từ trong ra ngoài rồi quay ngược để tìm điện áp và điện tích từng tụ. Kiểm tra cuối bằng bảo toàn điện tích ở các nút cô lập.

<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/08-advanced-capacitors/exercises.md)
- [Đáp án và lời giải](practice/08-advanced-capacitors/solutions.md)

---

[← Bài 7](07-charged-particle-motion.md) | [↑ Chương](index.md) | [Bài 9 →](09-electrostatic-equilibrium-charged-pendulum.md)
