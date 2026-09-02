---
title: "Bài 1 — Từ thông và hiện tượng cảm ứng điện từ"
description: "Từ thông qua diện tích, góc pháp tuyến, biến thiên từ thông và hiện tượng cảm ứng điện từ."
order: 1
difficulty: "foundation-standard"
prerequisites:
  - magnetic-field
tags:
  - physics
  - grade-11
  - magnetic-flux
---

# Bài 1 — Từ thông và hiện tượng cảm ứng điện từ

## Mục tiêu

Bạn cần:

- hiểu từ thông là đại lượng mô tả “mức độ xuyên qua” của từ trường qua một mặt;
- dùng đúng $\Phi=BS\cos\theta$;
- xác định đúng góc $\theta$;
- nhận ra các cách làm từ thông thay đổi;
- hiểu điều kiện xuất hiện dòng điện cảm ứng trong mạch kín.

## 1. Tại sao cần khái niệm từ thông?

Biết B tại một điểm chưa đủ để nói từ trường “đi qua” một vòng dây bao nhiêu. Một vòng lớn hứng nhiều vùng trường hơn vòng nhỏ. Một vòng quay nghiêng cũng “hứng” trường khác với vòng đặt vuông góc đường sức.

Ta cần một đại lượng kết hợp:

- độ mạnh của từ trường;
- diện tích mặt;
- hướng của mặt so với từ trường.

Đó là **từ thông**.

## 2. Vectơ pháp tuyến diện tích

Với mặt phẳng diện tích S, ta chọn một vectơ pháp tuyến $\vec n$ vuông góc mặt. Vectơ diện tích có thể viết:

$$
\vec S=S\vec n.
$$

Với mặt kín hoặc bài chiều cảm ứng, chiều pháp tuyến phải được quy ước nhất quán với chiều dương của vòng dây.

## 3. Công thức từ thông

Trong từ trường đều B xuyên qua một mặt phẳng diện tích S:

$$
\boxed{\Phi=BS\cos\theta}
$$

trong đó $\theta$ là góc giữa $\vec B$ và **pháp tuyến của mặt**.

Đơn vị SI của từ thông là **weber**, kí hiệu Wb.

$$
1\,\text{Wb}=1\,\text T\cdot\text{m}^2.
$$

## 4. Các tư thế đặc biệt

### B vuông góc mặt phẳng vòng

Lúc này B song song pháp tuyến, $\theta=0$:

$$
\Phi=BS.
$$

Từ thông có độ lớn cực đại.

### B song song mặt phẳng vòng

Lúc này B vuông góc pháp tuyến, $\theta=90^\circ$:

$$
\Phi=0.
$$

!!! warning "Góc hay bị dùng nhầm"
    Nếu đề cho góc $\beta$ giữa **mặt phẳng vòng** và $\vec B$, thì $\theta=90^\circ-\beta$ và $\Phi=BS\sin\beta$.

## 5. Từ thông có thể mang dấu

Nếu đã chọn chiều dương pháp tuyến, $\cos\theta$ có thể âm. Dấu của $\Phi$ mô tả hướng tương đối giữa B và pháp tuyến, không có nghĩa “có lượng từ thông âm” theo kiểu vật chất âm.

Trong bài chỉ hỏi độ lớn, nhiều đề dùng $|\Phi|$. Trong bài Faraday–Lenz, dấu và chiều quy ước có ý nghĩa.

## 6. Từ thông qua N vòng

Nếu cuộn dây có N vòng giống nhau, mỗi vòng có cùng từ thông $\Phi$, từ thông móc vòng tổng thường viết:

$$
N\Phi=NBS\cos\theta.
$$

Trong định luật Faraday, N xuất hiện nhân với tốc độ biến thiên từ thông của một vòng.

## 7. Làm thế nào để từ thông thay đổi?

Từ

$$
\Phi=BS\cos\theta,
$$

ta thấy có thể làm $\Phi$ đổi bằng cách:

- thay B;
- thay S;
- thay góc $\theta$;
- đưa một phần vòng vào/ra vùng có từ trường, làm diện tích hiệu dụng trong trường thay đổi;
- kết hợp nhiều yếu tố trên.

## 8. Hiện tượng cảm ứng điện từ

Khi từ thông qua mạch kín biến thiên, trong mạch xuất hiện **dòng điện cảm ứng**. Nếu mạch hở, vẫn có thể xuất hiện **suất điện động cảm ứng** nhưng không có dòng kín duy trì qua toàn mạch.

### Điểm cốt lõi

Không phải “có từ trường là có dòng cảm ứng”. Điều kiện là **từ thông qua mạch biến thiên theo thời gian**.

Một vòng dây nằm yên trong từ trường đều không đổi, không quay, không đổi diện tích → từ thông không đổi → không có suất điện động cảm ứng do Faraday.

## 9. Ví dụ 1 — vòng quay

Vòng diện tích $S=0,020$ m² trong B=0,30 T. Ban đầu pháp tuyến song song B; sau đó quay để pháp tuyến vuông góc B.

Ban đầu:

$$
\Phi_1=BS=0,006\,\text{Wb}.
$$

Sau:

$$
\Phi_2=0.
$$

Độ biến thiên:

$$
\Delta\Phi=\Phi_2-\Phi_1=-0,006\,\text{Wb}.
$$

Độ lớn biến thiên là 0,006 Wb.

## 10. Ví dụ 2 — thay B

Cuộn 100 vòng, diện tích mỗi vòng $10\,\text{cm}^2=1,0\times10^{-3}$ m², pháp tuyến song song B. B tăng từ 0,10 T lên 0,50 T.

Mỗi vòng:

$$
\Delta\Phi=S\Delta B=1,0\times10^{-3}\cdot0,40=4,0\times10^{-4}\,\text{Wb}.
$$

Từ thông móc vòng thay đổi:

$$
N\Delta\Phi=100\cdot4,0\times10^{-4}=0,040\,\text{Wb-vòng}.
$$

Bài sau sẽ dùng đại lượng này để tính suất điện động.

## 11. Bẫy thường gặp

!!! danger "Có B nhưng Phi không đổi"
    Một nam châm đứng yên trước vòng dây đứng yên không tạo dòng cảm ứng liên tục chỉ vì nó có từ trường.

!!! warning "Dùng diện tích toàn khung khi chỉ một phần nằm trong trường"
    Nếu B chỉ tồn tại trong một vùng, S trong biểu thức phải là diện tích phần mặt được trường xuyên qua theo mô hình đề bài.

!!! warning "Nhầm Wb với T"
    Tesla đo B; weber đo từ thông.

## 12. Phương pháp giải

1. Chọn mặt và pháp tuyến.
2. Tìm góc giữa B và pháp tuyến.
3. Tính $\Phi_1$ và $\Phi_2$.
4. Lấy $\Delta\Phi=\Phi_2-\Phi_1$ nếu cần dấu; lấy $|\Delta\Phi|$ nếu chỉ hỏi độ lớn biến thiên.
5. Với N vòng, nhân N khi tính suất điện động.

## Tóm tắt

Từ thông trong từ trường đều là $\Phi=BS\cos\theta$, với $\theta$ đo từ B đến pháp tuyến. Cảm ứng điện từ xảy ra khi từ thông qua mạch biến thiên. Từ thông có thể đổi do B, S hoặc góc thay đổi.

## 5 điều cần nhớ

1. $\Phi=BS\cos\theta$.
2. $\theta$ là góc giữa B và pháp tuyến.
3. Đơn vị từ thông: Wb.
4. Có từ trường chưa đủ; phải có từ thông biến thiên.
5. Cuộn N vòng: hiệu ứng cảm ứng tỉ lệ N.

---

[← Chương](index.md) | [Bài 2 →](02-lenz-faraday-law.md)
