---
title: "Bài 8 — Kirchhoff, xếp chồng, nguồn tương đương và mạch RC"
description: "Các phương pháp nâng cao để giải mạng điện nhiều nhánh và bài mạch chứa tụ ở trạng thái xác lập/chuyển mạch."
order: 8
difficulty: "advanced-enrichment"
prerequisites:
  - circuit-reading-meters
  - capacitors
  - source-combinations
tags:
  - physics
  - grade-11
  - circuits
  - kirchhoff
  - advanced
---

# Bài 8 — Kirchhoff, xếp chồng, nguồn tương đương và mạch RC

## Mức độ

**Mức 4–5 — Nâng cao / Mở rộng.** Không cần học phần này trước khi nắm chắc mạch điện trở và định luật Ohm toàn mạch.

> Đây là cách phân loại phục vụ mục đích sư phạm, không phải phân loại học thuật chính thức.

## Mục tiêu

Bạn cần:

- dùng hai định luật Kirchhoff có hệ thống;
- chọn chiều dòng giả định và xử lí nghiệm âm;
- dùng phương pháp xếp chồng cho mạch tuyến tính;
- thay phần mạng bằng nguồn tương đương trong bài phù hợp;
- giải mạch chứa tụ ở trạng thái xác lập một chiều;
- dùng bảo toàn điện tích vùng cô lập và cân bằng năng lượng khi chuyển mạch.

## 1. Khi nào cần Kirchhoff?

Mạch không rút gọn được hoàn toàn bằng nối tiếp–song song, đặc biệt có:

- nhiều nguồn;
- cầu không cân bằng;
- nhiều vòng kín;
- nhánh chung,

thì phương pháp Kirchhoff cho hệ phương trình tổng quát.

## 2. Định luật nút Kirchhoff

Tại một nút:

$$
\boxed{\sum I_{\text{vào}}=\sum I_{\text{ra}}}.
$$

Tương đương tổng đại số dòng tại nút bằng 0.

Đây là biểu hiện của bảo toàn điện tích: ở trạng thái ổn định, điện tích không tích lũy vô hạn tại nút.

### Quy tắc dấu
Có thể chọn:
- dòng vào dương, ra âm;
- hoặc ngược lại.

Chỉ cần nhất quán.

## 3. Định luật vòng Kirchhoff

Đi quanh một vòng kín, tổng đại số các biến thiên điện thế bằng 0:

$$
\boxed{\sum \Delta V=0}.
$$

Một cách viết thường dùng:

$$
\sum \mathcal E-\sum IR=0
$$

sau khi gán dấu theo chiều đi vòng và chiều dòng.

### Quy tắc qua điện trở
- đi **cùng chiều dòng**: điện thế giảm $IR$;
- đi **ngược chiều dòng**: điện thế tăng $IR$.

### Quy tắc qua nguồn
- đi từ cực âm sang cực dương: tăng $\mathcal E$;
- đi từ cực dương sang cực âm: giảm $\mathcal E$.

Với điện trở trong, coi r như một điện trở nối tiếp với nguồn trong phương trình vòng.

## 4. Chiều dòng giả định

Bạn có thể giả định chiều dòng ban đầu.

Nếu giải ra $I<0$, nghĩa là dòng thực chạy ngược chiều giả định, không phải bài sai.

Điều này giúp tránh phải đoán đúng chiều ngay từ đầu.

## 5. Số phương trình độc lập

Không cần viết mọi nút và mọi vòng nếu chúng phụ thuộc nhau. Chiến lược thực hành:

1. đặt các dòng nhánh;
2. dùng đủ phương trình nút độc lập;
3. chọn các vòng độc lập còn lại;
4. kiểm tra số phương trình bằng số ẩn.

## 6. Phương pháp xếp chồng

Cho mạch tuyến tính chứa nhiều nguồn độc lập. Dòng/điện áp tổng bằng tổng đại số các đáp ứng do từng nguồn tạo riêng.

Khi “tắt” các nguồn còn lại trong mô hình lý tưởng:

- nguồn điện áp lí tưởng $\mathcal E=0$ → thay bằng dây nối;
- nguồn dòng lí tưởng bằng 0 → thay bằng mạch hở (nếu học mô hình nguồn dòng).

Trong phạm vi nguồn điện áp và điện trở của giáo trình, chủ yếu dùng quy tắc thứ nhất.

### Quy trình

1. Chọn đại lượng cần tìm.
2. Giữ nguồn 1, tắt nguồn khác → tính $I^{(1)}$.
3. Giữ nguồn 2 → tính $I^{(2)}$.
4. Cộng đại số:
   $I=I^{(1)}+I^{(2)}+\cdots$.

!!! warning "Không xếp chồng công suất"
    Công suất phụ thuộc bình phương dòng/điện áp, nên không cộng trực tiếp công suất do từng nguồn rồi coi là công suất tổng.

## 7. Nguồn tương đương hai cực

Một mạng tuyến tính nhìn từ hai cực A–B có thể trong nhiều bài được thay bằng:

- một nguồn điện áp tương đương $\mathcal E_{eq}$;
- điện trở trong tương đương $r_{eq}$ nối tiếp.

Cách xác định thường dùng:

1. $\mathcal E_{eq}$ là điện áp hở mạch giữa A–B;
2. $r_{eq}$ là điện trở nhìn vào A–B khi các nguồn điện áp độc lập được đặt $\mathcal E=0$, nếu mô hình nguồn cho phép.

Đây là tư tưởng tương đương kiểu Thévenin, dù bài phổ thông có thể gọi đơn giản là “nguồn tương đương”.

### Nguồn nối tiếp
Nguồn cùng chiều: E cộng đại số, r cộng.

### Nhiều nhánh nguồn song song tổng quát
Nếu các nhánh có nguồn $\mathcal E_i$ nối tiếp $r_i$ và cùng nối giữa hai nút, điện áp hở mạch U thỏa cân bằng dòng:

$$
\sum_i\frac{\mathcal E_i-U}{r_i}=0
$$

theo quy ước cực tính thống nhất.

Suy ra:

$$
\boxed{
U=\frac{\sum_i \mathcal E_i/r_i}{\sum_i1/r_i}
}.
$$

Điện trở tương đương khi tắt các E:

$$
\boxed{
r_{eq}=\left(\sum_i\frac1{r_i}\right)^{-1}.
$$

Với các nguồn giống nhau, quay về $\mathcal E_{eq}=\mathcal E$, $r_{eq}=r/n$.

## 8. Mạch RC ở trạng thái xác lập một chiều

Trong các bài nguồn một chiều sau khi mạch đã ổn định đủ lâu, tụ lí tưởng không cho dòng điện một chiều đi qua nhánh tụ:

$$
\boxed{I_C=0\quad\text{ở trạng thái xác lập DC}}.
$$

Do đó:

1. tạm coi nhánh tụ là mạch hở để tính điện thế các nút;
2. tìm hiệu điện thế hai đầu tụ;
3. tính $Q=CU$.

Đây là quy tắc trung tâm của nhóm bài RC trong corpus.

## 9. Chuyển mạch với tụ

Khi khóa K thay trạng thái:

### Trước chuyển
Tìm trạng thái xác lập cũ và điện tích các tụ.

### Sau chuyển, trạng thái xác lập mới
Tìm cấu trúc liên kết mạch mới; nhánh tụ lại không có dòng DC khi đã ổn định.

### Nút/vùng cô lập
Nếu một nhóm bản tụ và dây dẫn bị cô lập khỏi nguồn/đất, tổng điện tích của vùng đó được bảo toàn:

$$
\boxed{Q_{\text{vùng}}=\text{hằng số}}.
$$

Công cụ này thay cho việc cố “bảo toàn điện tích từng tụ”, điều thường sai khi các tụ trao đổi điện tích qua dây.

## 10. Năng lượng trong quá trình đóng/ngắt

Năng lượng tụ:

$$
W_C=\frac12CU^2.
$$

Khi có nguồn tham gia, năng lượng điện trường của các tụ không nhất thiết bảo toàn.

Dùng cân bằng năng lượng:

$$
\boxed{A_{\text{nguồn}}=\Delta W_C+Q_{\text{nhiệt}}}
$$

trong mô hình chỉ có nguồn, tụ và điện trở tiêu tán.

Với nhiều nguồn, $A_{\text{nguồn}}$ là tổng công đại số của các nguồn theo điện lượng đi qua từng nguồn.

## 11. Không đưa hàm mũ nếu bài chỉ hỏi trạng thái

Các bài trong mạch RC của corpus chủ yếu khai thác:

- trạng thái xác lập;
- điện lượng chuyển qua khóa;
- bảo toàn điện tích vùng cô lập;
- nhiệt lượng khi chuyển mạch.

Vì vậy giáo trình này **không ép thêm phương trình nạp/xả theo hàm mũ** vào phần cốt lõi nếu đề không yêu cầu mô tả thời gian quá độ.

## 12. Ví dụ Kirchhoff

Mạch có hai vòng chia sẻ điện trở R3. Đặt dòng nhánh I1,I2 đi vào nút, I3 ra:

$$
I_1+I_2=I_3.
$$

Viết hai phương trình vòng độc lập theo quy tắc dấu, giải hệ ba ẩn. Nếu một I âm, đảo chiều thực tế.

Điểm quan trọng là quy trình, không phải một sơ đồ thuộc lòng.

## 13. Ví dụ RC xác lập

Tụ C nối giữa hai nút A,B của một mạch điện trở. Sau khi ổn định:

1. bỏ nhánh tụ khi tìm dòng qua điện trở;
2. tính $V_A,V_B$;
3. $U_C=V_A-V_B$;
4. $Q=C|U_C|$; dấu trên từng bản theo điện thế cao/thấp.

## 14. Bẫy thường gặp

!!! danger "Tụ xác lập không phải dây nối"
    Trong mạch DC đã ổn định, tụ lí tưởng là **mạch hở đối với dòng dẫn**, không phải R=0.

!!! danger "Bảo toàn sai đối tượng"
    Khi các tụ được nối với nhau, điện tích từng tụ có thể đổi. Hãy tìm **vùng dẫn cô lập** rồi bảo toàn tổng điện tích của vùng.

!!! warning "Nguồn tương đương"
    Chỉ dùng biến đổi nguồn/xếp chồng cho mạng tuyến tính trong phạm vi giả thiết. Không áp dụng máy móc cho phần tử phi tuyến.

## Tóm tắt

- Nút: tổng dòng vào = tổng dòng ra.
- Vòng: tổng biến thiên điện thế = 0.
- Chiều dòng có thể giả định.
- Xếp chồng áp dụng cho đại lượng tuyến tính I,U.
- Nguồn tương đương giúp rút mạng hai cực.
- Tụ ở xác lập DC: dòng qua tụ bằng 0.
- Chuyển mạch RC: cấu trúc liên kết mạch + bảo toàn điện tích vùng + năng lượng.

## 5 điều cần nhớ

1. Ghi quy ước dấu trước khi lập hệ.
2. Nghiệm dòng âm chỉ đảo chiều thực.
3. Không cộng công suất bằng xếp chồng.
4. RC xác lập: tụ là nhánh hở.
5. Năng lượng tụ riêng không bảo toàn khi có nguồn/điện trở trao đổi năng lượng.

## Các dạng bài trọng tâm

Các nhóm bài dưới đây được tổ chức theo dấu hiệu nhận biết và công cụ giải để người học chọn phương pháp phù hợp và tự kiểm tra kết quả.

### Dạng 2 — Công suất cực đại

Với một nguồn có suất điện động $\mathcal E$ và điện trở trong $r$ cấp cho tải biến đổi $R$, công suất tải $P=\mathcal E^2R/(R+r)^2$ đạt cực đại khi $R=r$.

Nếu tải nhìn thấy một mạng mạch phức tạp, trước hết tìm nguồn tương đương và điện trở tương đương nhìn từ hai cực tải, sau đó mới áp dụng điều kiện cực đại. Không dùng $R=r$ nếu $r$ chưa phải điện trở tương đương mà tải thực sự nhìn thấy.

<!-- LESSON_PRACTICE_LINKS -->
## Luyện tập sau bài

- [Bài tập theo bài](practice/08-advanced-circuit-methods/exercises.md)
- [Đáp án và lời giải](practice/08-advanced-circuit-methods/solutions.md)

---

[← Bài 7](07-circuit-reading-meters.md) | [↑ Chương](index.md) | [Bài 9 →](09-practical-emf-internal-resistance.md)
