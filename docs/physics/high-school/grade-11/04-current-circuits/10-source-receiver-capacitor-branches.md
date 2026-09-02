---
title: "Bài 10 — Đoạn mạch chứa nguồn, máy thu và tụ điện"
description: "Quan hệ U–I cho đoạn mạch có nguồn hoặc máy thu, tư duy dấu, mạch chứa tụ ở trạng thái xác lập và bài phối hợp."
order: 10
difficulty: "applied-advanced"
prerequisites:
  - full-circuit-ohm-law
  - advanced-circuit-methods
tags:
  - physics
  - grade-11
  - circuits
  - sources
  - capacitors
---

# Bài 10 — Đoạn mạch chứa nguồn, máy thu và tụ điện

## Mục tiêu

Bạn cần:

- viết quan hệ điện áp–dòng điện cho một đoạn mạch có điện trở và nguồn;
- hiểu khi nào một nguồn đang phát điện và khi nào đang nhận điện;
- xử lí mô hình máy thu có suất phản điện;
- kết hợp với định luật nút;
- xử lí nhánh tụ ở trạng thái DC xác lập;
- không phụ thuộc vào một công thức dấu thuộc lòng duy nhất.

## 1. Vì sao nhóm bài này dễ sai?

Trong mạch chỉ có điện trở, đi cùng chiều dòng qua R thì điện thế giảm $IR$.

Khi đoạn mạch có thêm nguồn, chiều biến thiên điện thế còn phụ thuộc ta đi qua nguồn từ cực âm sang cực dương hay ngược lại. Nếu cố thuộc một công thức kiểu $U=E-Ir$ cho mọi đoạn mạch, rất dễ dùng sai.

Cách an toàn hơn là **đi theo mạch và cộng các biến thiên điện thế**.

## 2. Quy tắc đi qua phần tử

### Qua điện trở R

Nếu đi theo chiều dòng điện:

$$
\Delta V=-IR.
$$

Nếu đi ngược chiều dòng:

$$
\Delta V=+IR.
$$

### Qua nguồn lí tưởng

Đi từ cực âm sang cực dương:

$$
\Delta V=+\mathcal E.
$$

Đi từ cực dương sang cực âm:

$$
\Delta V=-\mathcal E.
$$

Điện trở trong r xử lí như điện trở bình thường.

## 3. Quan hệ điện áp cực của nguồn đang phát

Với nguồn có suất điện động $\mathcal E$, điện trở trong r, khi nguồn phát dòng ra mạch ngoài:

$$
\boxed{U=\mathcal E-Ir}.
$$

Điện áp cực nhỏ hơn suất điện động vì có sụt áp trong nguồn.

Nếu dòng bị ép đi **vào cực dương** của nguồn, nguồn có thể đang được nạp/nhận công. Khi đó theo cùng quy ước điện áp cực có thể lớn hơn $\mathcal E$:

$$
U=\mathcal E+Ir
$$

trong cấu hình nạp đơn giản.

## 4. Máy thu điện và suất phản điện

Một động cơ điện hoặc thiết bị biến đổi điện năng thành dạng khác có thể được mô hình hóa bằng:

- suất phản điện $\mathcal E'$ chống lại dòng;
- điện trở trong $r'$.

Nếu dòng I đi vào cực dương của máy thu, điện áp hai đầu thường có dạng:

$$
\boxed{U=\mathcal E'+Ir'}.
$$

Công suất điện nhận:

$$
P_{\text{điện}}=UI.
$$

Trong mô hình lí tưởng hóa:

$$
\begin{gathered}
P_{\text{hữu ích}}=\mathcal E'I,\\
P_{\text{nhiệt}}=I^2r'.
\end{gathered}
$$

và:

$$
UI=\mathcal E'I+I^2r'.
$$

## 5. Phương pháp hiệu điện thế giữa hai nút

Với mạng nhiều nhánh, đôi khi ta biết hiệu điện thế $U_{AB}=V_A-V_B$.

Mỗi nhánh nối A–B cho một biểu thức dòng theo $U_{AB}$. Sau đó dùng định luật nút:

$$
\sum I_{A\to B}=0
$$

với quy ước đại số thích hợp nếu không có dòng ngoài tại nút.

Phương pháp này đặc biệt hiệu quả khi nhiều nhánh song song chứa nguồn và điện trở.

## 6. Ví dụ hai nhánh nguồn song song

Hai nhánh giữa A và B:

- nhánh 1: $\mathcal E_1,r_1$;
- nhánh 2: $\mathcal E_2,r_2$.

Chọn $U=V_A-V_B$ và quy ước cực nguồn giống nhau. Dòng nhánh có thể viết:

$$
\begin{gathered}
I_1=\frac{\mathcal E_1-U}{r_1},\\
I_2=\frac{\mathcal E_2-U}{r_2}.
\end{gathered}
$$

Mạch hở ngoài nên tại nút:

$$
I_1+I_2=0.
$$

Từ đó tìm U. Nếu $I_i$ âm, chiều thực của nhánh i ngược giả định.

## 7. Nhánh chứa tụ trong DC xác lập

Sau khi mạch đã ổn định đủ lâu với nguồn một chiều:

$$
I_C=0.
$$

Vì vậy nhánh chỉ chứa tụ không mang dòng dẫn DC. Tuy nhiên **hiệu điện thế hai đầu tụ vẫn có thể khác 0**.

Quy trình:

1. bỏ nhánh tụ khi tính dòng DC;
2. tính điện thế hai nút gắn với tụ;
3. lấy $U_C=V_A-V_B$;
4. tính $Q=CU_C$ theo đại số, hoặc độ lớn $|Q|=C|U_C|$.

## 8. Tụ mắc song song với một điện trở

Nếu tụ C song song với R và cả hai nối giữa cùng hai nút A,B, ở xác lập:

- $U_C=U_R=U_{AB}$;
- dòng qua tụ bằng 0;
- dòng qua R vẫn bằng $U_{AB}/R$.

Không được xóa luôn hiệu điện thế của nhánh tụ chỉ vì $I_C=0$.

## 9. Tụ nối giữa hai điểm của cầu điện trở

Đây là dạng hay:

1. giải mạch điện trở để tìm điện thế hai điểm giữa;
2. lấy hiệu điện thế giữa hai điểm đó;
3. suy ra điện tích tụ.

Nếu cầu cân bằng thì hai điểm giữa cùng điện thế nên $U_C=0$ và tụ không tích điện ở trạng thái xác lập.

## 10. Bài toán chuyển mạch

Khi khóa đổi trạng thái:

- trước chuyển: xác định điện tích ban đầu;
- sau chuyển đủ lâu: tìm điện áp cuối;
- nếu có vùng dẫn cô lập, bảo toàn tổng điện tích của vùng;
- nếu hỏi nhiệt lượng, dùng cân bằng năng lượng chứ không bảo toàn riêng năng lượng tụ.

Phần này liên hệ trực tiếp với [Bài 8 — phương pháp mạch nâng cao](08-advanced-circuit-methods.md).

## 11. Ví dụ — Nguồn đang được nạp

Nguồn $\mathcal E=6$ V, $r=1\,\Omega$ được nối với bộ nạp làm dòng 2 A đi vào cực dương.

Điện áp ngoài cần có:

$$
U=\mathcal E+Ir=6+2=8\text{ V}.
$$

Công suất nhận từ bộ nạp:

$$
P=UI=16\text{ W}.
$$

Trong mô hình:

- công suất tích lũy hóa học: $\mathcal E I=12$ W;
- nhiệt trong nguồn: $I^2r=4$ W.

Tổng đúng 16 W.

## 12. Bẫy thường gặp

!!! danger "Dùng U = E - Ir không nhìn chiều dòng"
    Công thức này mô tả nguồn đang phát theo quy ước thông thường. Khi nguồn bị nạp, dấu của thành phần $Ir$ đổi trong quan hệ điện áp cực.

!!! danger "Tụ xác lập có U = 0"
    Sai. Chỉ có $I_C=0$ trong trạng thái xác lập DC; điện áp tụ có thể bằng điện áp nguồn.

!!! warning "Máy thu không phải điện trở thuần"
    Nếu mô hình có suất phản điện, công suất nhận không chỉ biến thành nhiệt.

## 13. Phương pháp tổng quát cho đoạn mạch phức tạp

Thay vì học một bảng dấu dài:

1. chọn chiều đi từ A đến B;
2. chọn chiều dòng từng nhánh;
3. qua R: cùng dòng giảm $IR$;
4. qua nguồn: âm→dương tăng $\mathcal E$;
5. cộng tất cả biến thiên để liên hệ $V_B-V_A$;
6. dùng định luật nút nếu cần.

Đây là cách ít phụ thuộc trí nhớ và nhất quán với Kirchhoff.

## Tóm tắt

- Nguồn đang phát thường có $U=\mathcal E-Ir$.
- Nguồn đang nạp có thể có $U=\mathcal E+Ir$.
- Máy thu: $U=\mathcal E'+Ir'$ trong quy ước nhận dòng.
- Tụ xác lập DC: $I_C=0$ nhưng $U_C$ không nhất thiết bằng 0.
- Bài nhiều nhánh nên quay về điện thế nút và Kirchhoff.

## 5 điều cần nhớ

1. Hãy đi theo mạch, đừng đoán dấu.
2. Nghiệm dòng âm chỉ báo chiều thực ngược giả định.
3. Phân biệt nguồn phát và nguồn đang nạp.
4. Phân biệt máy thu với điện trở thuần.
5. Tụ ở xác lập là nhánh hở đối với dòng DC.

---

[← Bài 9](09-practical-emf-internal-resistance.md) | [↑ Chương](index.md) | [Bài tập →](exercises.md)
