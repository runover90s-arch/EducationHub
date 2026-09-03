from practice_bank_common import *
import math

CH='08-geometrical-optics'

def l1():
    return [
        mcq(r'''Định luật khúc xạ Snell viết

A. $n_1\sin i=n_2\sin r$.  
B. $n_1\cos i=n_2\cos r$ luôn.  
C. $n_1i=n_2r$ với góc độ.  
D. $n_1/n_2=i/r$ mọi trường hợp.''', r'''Chọn **A**.'''),
        mcq(r'''Ánh sáng đi từ không khí vào thủy tinh n=1,5. Tốc độ trong thủy tinh là

A. $1,5c$.  
B. $c$.  
C. $2,0\cdot10^8$ m/s.  
D. $4,5\cdot10^8$ m/s.''', r'''Chọn **C**. $v=c/n=3\cdot10^8/1,5=2\cdot10^8$ m/s.'''),
        mcq(r'''Tia đi từ môi trường chiết suất nhỏ sang lớn thường khúc xạ

A. xa pháp tuyến hơn.  
B. gần pháp tuyến hơn.  
C. không đổi hướng trong mọi góc.  
D. phản xạ toàn phần luôn.''', r'''Chọn **B**.'''),
        tf(r'''Khúc xạ ánh sáng:

a) Tần số không đổi khi qua mặt phân cách đứng yên.  
b) Tốc độ và bước sóng có thể thay đổi.  
c) Tia tới, tia khúc xạ và pháp tuyến cùng nằm trong một mặt phẳng.  
d) Chiết suất tuyệt đối n có thể viết $c/v$.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Đúng**.'''),
        short(r'''Ánh sáng từ không khí vào thủy tinh n=1,5 với góc tới $30^\circ$. Tính góc khúc xạ.''', r'''$\sin r=\sin30^\circ/1,5=1/3$. $r=\arcsin(1/3)\approx19,5^\circ$.'''),
        short(r'''Một môi trường có tốc độ ánh sáng $2,4\cdot10^8$ m/s. Tính chiết suất tuyệt đối.''', r'''$n=c/v=3,0/2,4=1,25$.'''),
        short(r'''Ánh sáng có bước sóng 600 nm trong chân không đi vào môi trường n=1,5. Tính bước sóng trong môi trường.''', r'''Tần số không đổi, tốc độ giảm n lần nên $\lambda=\lambda_0/n=600/1,5=400$ nm.'''),
        applied(r'''Tia sáng đi từ môi trường n1=1,2 sang môi trường n2=1,5 với góc tới $45^\circ$. Tính góc khúc xạ và kiểm tra tia lệch về phía nào so với pháp tuyến.''', r'''Snell:

$1,2\sin45^\circ=1,5\sin r$.

$\sin r=(1,2/1,5)(\sqrt2/2)\approx0,5657$.

$r\approx34,4^\circ$. Vì $r<i$, tia khúc xạ gần pháp tuyến hơn, phù hợp vì đi vào môi trường chiết suất lớn hơn.''')
    ]

def l2():
    return [
        mcq(r'''Nhìn gần vuông góc từ không khí xuống vật dưới nước n=4/3, độ sâu biểu kiến h' liên hệ độ sâu thật h bởi

A. $h'=nh$.  
B. $h'=h/n$.  
C. $h'=h+n$.  
D. $h'=h$.''', r'''Chọn **B** trong gần đúng góc nhỏ/nhìn gần vuông góc.'''),
        mcq(r'''Vật ở độ sâu thật 1,2 m trong nước n=4/3. Độ sâu biểu kiến gần bằng

A. 0,9 m.  
B. 1,2 m.  
C. 1,6 m.  
D. 2,1 m.''', r'''Chọn **A**. $h'=1,2/(4/3)=0,9$ m.'''),
        mcq(r'''Qua bản mặt song song, tia ló so với tia tới thường

A. song song nhưng lệch ngang nếu hai môi trường ngoài giống nhau.  
B. vuông góc.  
C. luôn trùng hẳn.  
D. đổi tần số.''', r'''Chọn **A**.'''),
        tf(r'''Bản mặt song song:

a) Hai mặt giới hạn song song.  
b) Nếu môi trường trước và sau giống nhau, tia ló song song tia tới.  
c) Có thể xảy ra độ lệch ngang.  
d) Tần số ánh sáng sau khi ra khỏi bản khác tần số ban đầu.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**.'''),
        short(r'''Một bể nước sâu 80 cm, n=4/3. Nhìn gần vuông góc từ không khí, đáy có vẻ sâu bao nhiêu?''', r'''$h'=h/n=80/(4/3)=60$ cm.'''),
        short(r'''Một vật nhìn qua lớp kính dày 6 cm, n=1,5 theo phương gần vuông góc. Tính độ dày biểu kiến và độ nâng ảnh.''', r'''Độ dày biểu kiến $h'=6/1,5=4$ cm. Độ nâng $\Delta h=6-4=2$ cm.'''),
        short(r'''Một bản kính có n=1,5, tia tới $45^\circ$. Tính góc khúc xạ trong kính.''', r'''$\sin r=\sin45^\circ/1,5\approx0,4714$, nên $r\approx28,1^\circ$.'''),
        applied(r'''Bản kính dày d=4 cm, n=1,5 đặt trong không khí, tia tới $45^\circ$. Dùng công thức lệch ngang $s=d\sin(i-r)/\cos r$. Tính s.''', r'''Trước hết $r\approx28,1^\circ$.

$s=4\,\frac{\sin(45^\circ-28,1^\circ)}{\cos28,1^\circ}$ cm.

$\sin16,9^\circ\approx0,291$, $\cos28,1^\circ\approx0,882$.

$s\approx4\cdot0,291/0,882\approx1,32$ cm.''')
    ]

def l3():
    return [
        mcq(r'''Phản xạ toàn phần có thể xảy ra khi ánh sáng truyền

A. từ môi trường chiết suất nhỏ sang lớn.  
B. từ môi trường chiết suất lớn sang nhỏ và góc tới đủ lớn.  
C. trong chân không duy nhất.  
D. ở mọi góc tới.''', r'''Chọn **B**.'''),
        mcq(r'''Góc giới hạn ic thỏa

A. $\sin i_c=n_2/n_1$ khi $n_1>n_2$.  
B. $\sin i_c=n_1/n_2$.  
C. $\cos i_c=n_2/n_1$ luôn.  
D. $i_c=90^\circ$ mọi môi trường.''', r'''Chọn **A**.'''),
        mcq(r'''Thủy tinh n=1,5 ra không khí. Góc giới hạn gần bằng

A. $30^\circ$.  
B. $41,8^\circ$.  
C. $60^\circ$.  
D. $90^\circ$.''', r'''Chọn **B** vì $\sin i_c=1/1,5=2/3$, $i_c\approx41,8^\circ$.'''),
        tf(r'''Phản xạ toàn phần:

a) Không có tia khúc xạ truyền năng lượng sang môi trường hai theo mô hình tia đơn giản.  
b) Cần $n_1>n_2$.  
c) Cần $i>i_c$.  
d) Sợi quang khai thác phản xạ toàn phần.''', r'''a) **Đúng** trong mô hình phổ thông.  
b) **Đúng**.  
c) **Đúng**.  
d) **Đúng**.'''),
        short(r'''Nước n=4/3 tiếp giáp không khí. Tính góc giới hạn.''', r'''$\sin i_c=1/(4/3)=3/4=0,75$. $i_c\approx48,6^\circ$.'''),
        short(r'''Ánh sáng trong thủy tinh n=1,6 tới mặt phân cách không khí với góc 50°. Có phản xạ toàn phần không?''', r'''$\sin i_c=1/1,6=0,625$, nên $i_c\approx38,7^\circ$. Vì $50^\circ>38,7^\circ$, có phản xạ toàn phần.'''),
        short(r'''Môi trường có góc giới hạn với không khí là $30^\circ$. Tính chiết suất.''', r'''$\sin30^\circ=1/n$, nên $n=2$.'''),
        applied(r'''Một tia sáng truyền trong lõi sợi quang n1=1,50 đến biên lõi–vỏ n2=1,40. Tính góc giới hạn tại biên. Nếu góc tới trong lõi là 75°, kết luận.''', r'''$\sin i_c=n_2/n_1=1,40/1,50=0,9333$.

$i_c\approx68,96^\circ$.

Vì $75^\circ>i_c$, tia bị phản xạ toàn phần tại biên lõi–vỏ.''')
    ]

def l4():
    return [
        mcq(r'''Lăng kính có tác dụng tán sắc ánh sáng trắng vì

A. chiết suất phụ thuộc bước sóng.  
B. mọi màu có cùng chiết suất.  
C. ánh sáng trắng chỉ có một màu.  
D. tần số mọi màu bằng nhau.''', r'''Chọn **A**.'''),
        mcq(r'''Trong thủy tinh thông thường, tia tím qua lăng kính thường lệch

A. ít hơn tia đỏ.  
B. nhiều hơn tia đỏ.  
C. bằng tia đỏ trong mọi trường hợp.  
D. không khúc xạ.''', r'''Chọn **B**.'''),
        mcq(r'''Với lăng kính mỏng góc A nhỏ, góc lệch xấp xỉ có thể viết

A. $\delta\approx(n-1)A$.  
B. $\delta\approx n/A$.  
C. $\delta\approx A/(n-1)$.  
D. $\delta=0$ mọi n.''', r'''Chọn **A** trong gần đúng lăng kính mỏng.'''),
        tf(r'''Lăng kính và tán sắc:

a) Tia sáng bị khúc xạ ở cả hai mặt lăng kính.  
b) Ánh sáng đơn sắc không bị tách thành nhiều màu do tán sắc.  
c) Góc lệch phụ thuộc chiết suất.  
d) Đỏ thường lệch nhiều hơn tím trong thủy tinh thường.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**.'''),
        short(r'''Lăng kính mỏng có góc A=6°, n=1,50. Ước tính góc lệch.''', r'''$\delta\approx(n-1)A=0,5\cdot6^\circ=3^\circ$.'''),
        short(r'''Cùng lăng kính A=6°, $n_đ=1,50$, $n_t=1,54$. Ước tính độ tách góc giữa tím và đỏ.''', r'''$\delta_t-\delta_đ\approx(n_t-n_đ)A=0,04\cdot6^\circ=0,24^\circ$.'''),
        short(r'''Một tia đơn sắc đi qua lăng kính mỏng A=4° và lệch 2,2°. Tính chiết suất gần đúng.''', r'''$\delta=(n-1)A$ nên $n=1+\delta/A=1+2,2/4=1,55$.'''),
        applied(r'''Lăng kính mỏng A=5° có $n_đỏ=1,51$, $n_tím=1,55$. Tính góc lệch gần đúng từng màu và khoảng tách góc.''', r'''Đỏ: $\delta_đ\approx(1,51-1)5^\circ=2,55^\circ$.

Tím: $\delta_t\approx(1,55-1)5^\circ=2,75^\circ$.

Khoảng tách $\Delta\delta\approx0,20^\circ$. Tím lệch nhiều hơn, đúng với $n_t>n_đ$.''')
    ]

def l5():
    return [
        mcq(r'''Thấu kính hội tụ có tiêu cự theo quy ước dấu thường dùng là

A. f>0.  
B. f<0.  
C. f=0.  
D. không có tiêu điểm.''', r'''Chọn **A**.'''),
        mcq(r'''Công thức thấu kính mỏng với vật thật và quy ước đại số chuẩn là

A. $1/f=1/d+1/d'$.  
B. $f=d+d'$.  
C. $1/f=d+d'$.  
D. $f=dd'$.''', r'''Chọn **A**.'''),
        mcq(r'''Vật thật đặt ngoài 2f trước thấu kính hội tụ cho ảnh

A. thật, ngược chiều, nhỏ hơn vật, nằm giữa f và 2f.  
B. ảo, cùng chiều, lớn hơn.  
C. thật, cùng chiều.  
D. không có ảnh.''', r'''Chọn **A**.'''),
        tf(r'''Thấu kính mỏng:

a) Tia qua quang tâm trong gần đúng mỏng truyền thẳng.  
b) Tia tới song song trục chính qua thấu kính hội tụ ló qua tiêu điểm ảnh.  
c) Thấu kính phân kì với vật thật thường cho ảnh ảo, cùng chiều, nhỏ hơn.  
d) Ảnh thật có thể hứng trên màn.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Đúng**.'''),
        short(r'''Thấu kính hội tụ f=10 cm, vật thật cách kính d=30 cm. Tính d' và độ phóng đại đại số k=-d'/d.''', r'''$1/d'=1/f-1/d=1/10-1/30=1/15$, nên $d'=15$ cm. $k=-15/30=-0,5$: ảnh thật, ngược chiều, cao bằng nửa vật.'''),
        short(r'''Thấu kính hội tụ f=20 cm, vật đặt d=10 cm. Tính vị trí ảnh.''', r'''$1/d'=1/20-1/10=-1/20$, nên $d'=-20$ cm: ảnh ảo nằm cùng phía vật, cách kính 20 cm.'''),
        short(r'''Thấu kính phân kì f=-15 cm, vật thật d=30 cm. Tính d'.''', r'''$1/d'=1/f-1/d=-1/15-1/30=-1/10$, nên $d'=-10$ cm.'''),
        applied(r'''Một vật cao 2 cm đặt trước thấu kính hội tụ f=12 cm, cách kính 18 cm. Tính vị trí, tính chất và chiều cao ảnh.''', r'''$1/d'=1/12-1/18=(3-2)/36=1/36$, nên $d'=36$ cm, ảnh thật.

Độ phóng đại $k=-d'/d=-36/18=-2$.

Chiều cao ảnh $h'=kh=-2\cdot2=-4$ cm. Dấu âm cho biết ảnh ngược chiều; độ lớn ảnh 4 cm, gấp đôi vật.''')
    ]

def l6():
    return [
        mcq(r'''Nếu vật và ảnh thật qua thấu kính hội tụ cách nhau một khoảng L=d+d', phương pháp dịch chuyển thấu kính có hai vị trí cho ảnh rõ khi

A. L>4f.  
B. L<2f.  
C. L=f.  
D. L=0.''', r'''Chọn **A**.'''),
        mcq(r'''Trong hai vị trí liên hợp của vật và ảnh với L cố định, các khoảng d và d'

A. hoán đổi cho nhau.  
B. luôn bằng nhau.  
C. đều âm.  
D. không liên quan.''', r'''Chọn **A**.'''),
        mcq(r'''Vật thật qua thấu kính hội tụ cho ảnh thật lớn gấp 2. Nếu k=-2 thì

A. d'=2d.  
B. d'=d/2.  
C. d'=-2d.  
D. d'=0.''', r'''Chọn **A** vì k=-d'/d=-2.'''),
        tf(r'''Giải bài thấu kính:

a) Cần nhất quán quy ước dấu.  
b) Có thể kiểm tra kết quả bằng tính chất ảnh mong đợi.  
c) Với vật thật và ảnh thật qua hội tụ, d và d' đều dương theo quy ước thông dụng.  
d) Mọi nghiệm đại số đều phải chấp nhận dù mâu thuẫn mô hình hình học.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: phải kiểm tra điều kiện vật lý và quy ước dấu.'''),
        short(r'''Thấu kính hội tụ tạo ảnh thật bằng vật. Nếu f=15 cm, tìm d và d'.''', r'''Ảnh thật bằng vật có $|k|=1$ nên d'=d. Từ $1/f=2/d$, d=d'=2f=30 cm.'''),
        short(r'''Thấu kính hội tụ f=10 cm tạo ảnh thật lớn gấp 3. Tính d và d'.''', r'''$d'=3d$. $1/10=1/d+1/(3d)=4/(3d)$ nên $d=40/3\approx13,33$ cm; $d'=40$ cm.'''),
        short(r'''Khoảng cách vật–màn L=100 cm, hai vị trí thấu kính cho ảnh rõ cách nhau l=60 cm. Dùng công thức Bessel $f=(L^2-l^2)/(4L)$ tính f.''', r'''$f=(100^2-60^2)/(400)=(10000-3600)/400=16$ cm.'''),
        applied(r'''Một vật và màn cố định cách nhau 90 cm. Thấu kính hội tụ có f=20 cm. Tìm hai vị trí của thấu kính tính từ vật để ảnh rõ trên màn.''', r'''Gọi d là khoảng vật–kính, d'=90-d. Công thức:

$1/20=1/d+1/(90-d)$.

$d(90-d)=20\cdot90=1800$.

$d^2-90d+1800=0$.

$\Delta=8100-7200=900$, $\sqrt\Delta=30$.

$d=(90\pm30)/2=30$ cm hoặc 60 cm.

Hai vị trí hoán đổi d và d', đúng tính chất liên hợp.''')
    ]

def l7():
    return [
        mcq(r'''Mắt cận thị khi không điều tiết có điểm cực viễn

A. ở vô cực.  
B. hữu hạn trước mắt.  
C. sau võng mạc vô hạn.  
D. bằng điểm cực cận của mắt thường.''', r'''Chọn **B**.'''),
        mcq(r'''Kính sửa cận thị thường là

A. thấu kính hội tụ.  
B. thấu kính phân kì.  
C. gương phẳng.  
D. lăng kính.''', r'''Chọn **B**.'''),
        mcq(r'''Kính sửa viễn thị/lão thị khi nhìn gần thường dùng

A. thấu kính hội tụ.  
B. thấu kính phân kì.  
C. kính không độ.  
D. gương cầu lồi.''', r'''Chọn **A** trong mô hình cơ bản.'''),
        tf(r'''Mắt và tật khúc xạ:

a) Mắt điều tiết bằng thay đổi độ tụ của hệ quang học mắt.  
b) Cận thị khó nhìn rõ vật xa khi không đeo kính.  
c) Kính phân kì có thể đưa ảnh của vật ở vô cực về cực viễn của mắt cận.  
d) Viễn thị luôn sửa bằng kính phân kì.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: thường dùng kính hội tụ.'''),
        short(r'''Mắt cận có cực viễn 50 cm. Kính đeo sát mắt để nhìn vật ở vô cực cần tiêu cự bao nhiêu?''', r'''Vật ở vô cực qua kính phải cho ảnh ảo tại cực viễn $d'=-50$ cm. Với d=∞, f=d'=-50 cm. Độ tụ $D=1/f(m)=-2$ điốp.'''),
        short(r'''Mắt cận có cực viễn 1 m. Kính sát mắt cần độ tụ bao nhiêu để nhìn xa vô cực?''', r'''f=-1 m nên $D=1/f=-1$ điốp.'''),
        short(r'''Một người cần kính hội tụ +2 D. Tính tiêu cự kính.''', r'''$f=1/D=1/2=0,50$ m = 50 cm.'''),
        applied(r'''Một mắt cận có cực viễn 40 cm và cực cận 10 cm. Đeo kính phân kì sát mắt có f=-40 cm để nhìn xa vô cực. Khi đeo kính này, vật gần nhất có thể đặt cách kính bao nhiêu để ảnh ảo của kính nằm tại cực cận cũ 10 cm?''', r'''Với vật gần nhất, kính phải tạo ảnh ảo tại cực cận của mắt: $d'=-10$ cm. Kính có f=-40 cm.

$1/f=1/d+1/d'$:

$-1/40=1/d-1/10$.

$1/d=1/10-1/40=3/40$.

$d=40/3\approx13,3$ cm.

Vậy khi đeo kính sửa cận, điểm gần nhất của vật đối với kính khoảng 13,3 cm trong mô hình kính sát mắt.''')
    ]

def l8():
    return [
        mcq(r'''Kính lúp là

A. thấu kính hội tụ có tiêu cự ngắn dùng quan sát vật nhỏ.  
B. thấu kính phân kì tiêu cự dài.  
C. gương phẳng.  
D. lăng kính.''', r'''Chọn **A**.'''),
        mcq(r'''Bội giác kính lúp khi ngắm chừng ở vô cực thường lấy gần đúng

A. $G=D/f$ với D khoảng cực cận quy ước.  
B. $G=f/D$.  
C. $G=fD$.  
D. $G=0$.''', r'''Chọn **A**.'''),
        mcq(r'''Kính thiên văn khúc xạ cơ bản gồm

A. vật kính hội tụ tiêu cự dài và thị kính hội tụ tiêu cự ngắn.  
B. hai thấu kính phân kì.  
C. một gương phẳng.  
D. một lăng kính duy nhất.''', r'''Chọn **A** theo mô hình Kepler.'''),
        tf(r'''Dụng cụ quang:

a) Kính lúp tạo ảnh ảo lớn hơn vật khi vật đặt trong tiêu cự.  
b) Kính hiển vi dùng vật kính tạo ảnh trung gian phóng đại rồi thị kính quan sát.  
c) Kính thiên văn dùng để tăng góc trông của vật rất xa.  
d) Bội giác không liên quan tiêu cự của các bộ phận quang học.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**.'''),
        short(r'''Kính lúp f=5 cm, lấy D=25 cm, ngắm chừng vô cực. Tính bội giác.''', r'''$G=D/f=25/5=5$.'''),
        short(r'''Kính thiên văn có vật kính f1=1 m, thị kính f2=5 cm, ngắm chừng vô cực. Tính độ lớn bội giác góc.''', r'''$|G|=f_1/f_2=100/5=20$.'''),
        short(r'''Kính lúp có độ tụ +20 D. Tính tiêu cự và bội giác vô cực với D=25 cm.''', r'''f=1/20 m=0,05 m=5 cm. $G=25/5=5$.'''),
        applied(r'''Một kính thiên văn Kepler ngắm chừng vô cực có vật kính f1=80 cm và thị kính f2=4 cm. a) Tính bội giác góc. b) Tính khoảng cách hai kính trong trạng thái ngắm chừng vô cực.''', r'''a) Độ lớn bội giác:

$|G|=f_1/f_2=80/4=20$.

Ảnh bị đảo chiều trong kính Kepler nên nếu xét dấu có thể ghi $G=-20$.

b) Khi ngắm chừng vô cực, tiêu diện ảnh của vật kính trùng tiêu diện vật của thị kính, nên khoảng cách hai kính:

$L=f_1+f_2=80+4=84$ cm.''')
    ]

LESSONS={
'01-refraction-refractive-index.md': l1(),
'02-parallel-slab-apparent-depth.md': l2(),
'03-total-internal-reflection.md': l3(),
'04-prism-dispersion.md': l4(),
'05-thin-lenses-image-construction.md': l5(),
'06-lens-problem-methods.md': l6(),
'07-eye-and-defects.md': l7(),
'08-optical-instruments.md': l8(),
}

if __name__=='__main__':
    for lf, probs in LESSONS.items():
        write_lesson_practice(CH, lf, probs)
        add_practice_links(CH, lf)
    write_practice_index(CH, list(LESSONS))
    print('chapter 8', sum(len(v) for v in LESSONS.values()), 'problems')
