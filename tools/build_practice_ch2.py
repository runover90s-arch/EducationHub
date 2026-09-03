from practice_bank_common import *
import math

CH='02-waves'

def l1():
    return [
        mcq(r'''Một sóng cơ có tần số $20$ Hz truyền với tốc độ $4$ m/s. Bước sóng là

A. $0,10$ m.  
B. $0,20$ m.  
C. $5$ m.  
D. $80$ m.''', r'''Chọn **B**. $\lambda=v/f=4/20=0,20$ m.'''),
        mcq(r'''Phát biểu đúng về sóng cơ là

A. Sóng cơ truyền được trong chân không.  
B. Khi sóng truyền, các phần tử môi trường chuyển dời theo sóng từ nguồn đến rất xa.  
C. Sóng cơ truyền dao động và năng lượng qua môi trường.  
D. Tốc độ truyền sóng chỉ phụ thuộc tần số nguồn.''', r'''Chọn **C**. Sóng cơ cần môi trường vật chất và truyền trạng thái dao động/năng lượng, không mang các phần tử môi trường đi theo.'''),
        mcq(r'''Một sóng có $\lambda=40$ cm. Hai điểm gần nhau nhất trên cùng phương truyền sóng dao động cùng pha cách nhau

A. $10$ cm.  
B. $20$ cm.  
C. $40$ cm.  
D. $80$ cm.''', r'''Chọn **C**. Hai điểm gần nhất cùng pha trên phương truyền sóng cách nhau một bước sóng.'''),
        tf(r'''Xét một sóng cơ hình sin:

a) Chu kì dao động của phần tử môi trường bằng chu kì nguồn.  
b) Bước sóng là quãng đường sóng truyền trong một chu kì.  
c) Sóng ngang luôn truyền được trong chất khí.  
d) Khi truyền sang môi trường khác, tần số do nguồn quyết định thường không đổi.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai** đối với sóng cơ trong khối môi trường thông thường; chất khí không truyền sóng cơ ngang thể tích.  
d) **Đúng**: tần số liên tục qua mặt phân cách, còn tốc độ và bước sóng có thể đổi.'''),
        short(r'''Một nguồn dao động với tần số $25$ Hz tạo sóng truyền với tốc độ $5$ m/s. Tính bước sóng và thời gian sóng truyền đi $3$ m.''', r'''$\lambda=v/f=5/25=0,20$ m. Thời gian truyền $t=s/v=3/5=0,60$ s.'''),
        short(r'''Một sóng có bước sóng $60$ cm. Tính khoảng cách ngắn nhất giữa hai điểm trên phương truyền sóng dao động ngược pha.''', r'''Ngược pha khi $\Delta d=(k+1/2)\lambda$. Khoảng cách nhỏ nhất ứng với $k=0$: $\lambda/2=30$ cm.'''),
        short(r'''Một sóng truyền qua điểm A rồi đến B cách A $1,5$ m sau $0,30$ s. Tần số nguồn là $4$ Hz. Tính tốc độ và bước sóng.''', r'''$v=1,5/0,30=5$ m/s. $\lambda=v/f=5/4=1,25$ m.'''),
        applied(r'''Một sóng hình sin truyền trên dây với tốc độ $2,4$ m/s. Hai điểm M, N trên cùng phương truyền cách nhau $45$ cm dao động lệch pha $3\pi/2$ rad theo độ lớn nhỏ nhất tương ứng với khoảng cách đó. Tính bước sóng và tần số.''', r'''Độ lệch pha theo không gian: $|\Delta\varphi|=2\pi d/\lambda$. Với $d=0,45$ m và độ lệch pha đang xét là $3\pi/2$:

$2\pi\cdot0,45/\lambda=3\pi/2$.

Suy ra $\lambda=0,60$ m. Tần số $f=v/\lambda=2,4/0,60=4$ Hz.''')
    ]

def l2():
    return [
        mcq(r'''Sóng truyền theo chiều dương Ox, nguồn tại O có $u_O=A\cos\omega t$. Phương trình tại điểm cách O một đoạn $x$ là

A. $u=A\cos(\omega t+2\pi x/\lambda)$.  
B. $u=A\cos(\omega t-2\pi x/\lambda)$.  
C. $u=A\cos(2\pi x/\lambda)$.  
D. $u=A\cos(\omega x-2\pi t/\lambda)$.''', r'''Chọn **B**. Điểm xa nguồn trễ pha $2\pi x/\lambda$.'''),
        mcq(r'''Hai điểm cách nhau $\lambda/4$ trên cùng phương truyền sóng có độ lệch pha theo độ lớn là

A. $\pi/4$.  
B. $\pi/2$.  
C. $\pi$.  
D. $2\pi$.''', r'''Chọn **B**. $\Delta\varphi=2\pi(\lambda/4)/\lambda=\pi/2$.'''),
        mcq(r'''Một sóng có phương trình $u=3\cos(8\pi t-2\pi x)$ cm, với $x$ tính bằng mét. Tốc độ truyền sóng là

A. $2$ m/s.  
B. $4$ m/s.  
C. $8$ m/s.  
D. $16$ m/s.''', r'''Chọn **B**. $\omega=8\pi$ nên $f=4$ Hz; hệ số của $x$ là $2\pi/\lambda=2\pi$ nên $\lambda=1$ m. Do đó $v=f\lambda=4$ m/s.'''),
        tf(r'''Với sóng $u=A\cos(\omega t-kx+\varphi_0)$:

a) $k=2\pi/\lambda$.  
b) Điểm ở xa hơn theo chiều truyền có pha nhỏ hơn tại cùng thời điểm.  
c) Khoảng thời gian trễ giữa hai điểm cách nhau $d$ là $d/v$.  
d) Hai điểm cách nhau $2\lambda$ ngược pha.''', r'''a) **Đúng**.  
b) **Đúng** với dạng truyền theo chiều dương Ox.  
c) **Đúng**.  
d) **Sai**: chênh pha $4\pi$, nên cùng pha.'''),
        short(r'''Sóng có $f=10$ Hz, $v=2$ m/s. Tính độ lệch pha giữa hai điểm cách nhau $15$ cm trên phương truyền.''', r'''$\lambda=v/f=0,20$ m. $\Delta\varphi=2\pi d/\lambda=2\pi\cdot0,15/0,20=3\pi/2$ rad.'''),
        short(r'''Nguồn O dao động $u_O=4\cos(10\pi t+\pi/6)$ cm. Sóng truyền với $v=2$ m/s. Viết phương trình tại M cách O $30$ cm theo chiều truyền.''', r'''$f=\omega/(2\pi)=5$ Hz nên $\lambda=v/f=0,4$ m. Độ trễ pha $2\pi d/\lambda=2\pi\cdot0,3/0,4=3\pi/2$. Do đó $u_M=4\cos(10\pi t+\pi/6-3\pi/2)$ cm, có thể rút gọn pha tương đương.'''),
        short(r'''Một ảnh chụp sóng tại một thời điểm cho thấy khoảng cách giữa hai đỉnh liên tiếp là $24$ cm. Nguồn dao động $5$ Hz. Tính tốc độ truyền sóng.''', r'''Khoảng cách giữa hai đỉnh liên tiếp chính là $\lambda=0,24$ m. $v=f\lambda=5\cdot0,24=1,20$ m/s.'''),
        applied(r'''Một sóng truyền theo chiều dương Ox có phương trình tại M là $u_M=5\cos(6\pi t-\pi/3)$ cm và tại N là $u_N=5\cos(6\pi t-5\pi/6)$ cm. Biết MN nằm theo chiều truyền và nhỏ hơn một bước sóng. Tốc độ truyền sóng $v=3$ m/s. Tính MN.''', r'''Tại cùng thời điểm, N trễ pha so với M một lượng

$\Delta\varphi=5\pi/6-\pi/3=\pi/2$.

Tần số $f=6\pi/(2\pi)=3$ Hz, nên $\lambda=v/f=1$ m.

Vì $\Delta\varphi=2\pi\,MN/\lambda$ và $MN<\lambda$:

$MN=(\pi/2)\lambda/(2\pi)=\lambda/4=0,25$ m.''')
    ]

def l3():
    return [
        mcq(r'''Hai nguồn kết hợp cùng pha. Điểm M có hiệu đường đi $d_2-d_1=3\lambda$. M là

A. cực đại giao thoa.  
B. cực tiểu giao thoa.  
C. không dao động vì hai sóng triệt tiêu.  
D. chưa đủ dữ kiện.''', r'''Chọn **A**. Với hai nguồn cùng pha, cực đại khi hiệu đường đi bằng $k\lambda$.'''),
        mcq(r'''Hai nguồn cùng pha. Cực tiểu giao thoa thỏa

A. $d_2-d_1=k\lambda$.  
B. $d_2-d_1=(k+1/2)\lambda$.  
C. $d_2+d_1=k\lambda$.  
D. $d_2d_1=\lambda^2$.''', r'''Chọn **B**.'''),
        mcq(r'''Hai nguồn cùng pha, cùng biên độ $a$. Tại điểm có hai sóng đến cùng pha, biên độ tổng hợp là

A. $0$.  
B. $a$.  
C. $\sqrt2a$.  
D. $2a$.''', r'''Chọn **D** nếu bỏ qua suy giảm biên độ trên đường truyền.'''),
        tf(r'''Trong giao thoa của hai nguồn kết hợp cùng pha:

a) Các điểm cực đại có hiệu đường đi là bội nguyên của $\lambda$.  
b) Các điểm cực tiểu có hiệu đường đi là nửa nguyên lần $\lambda$.  
c) Trên trung trực đoạn nối hai nguồn luôn là cực tiểu.  
d) Nguồn kết hợp phải có hiệu pha không đổi theo thời gian.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: với hai nguồn cùng pha, trung trực có hiệu đường đi bằng 0 nên là cực đại.  
d) **Đúng**.'''),
        short(r'''Hai nguồn cùng pha cách nhau $12$ cm, bước sóng $2$ cm. Một điểm M có $d_1=10$ cm, $d_2=14$ cm. M là cực đại hay cực tiểu?''', r'''Hiệu đường đi $|d_2-d_1|=4$ cm $=2\lambda$, nên M là cực đại.'''),
        short(r'''Hai nguồn cùng pha phát sóng bước sóng $1,5$ cm. Một điểm có hiệu đường đi $3,75$ cm. Xác định loại điểm giao thoa.''', r'''$3,75/1,5=2,5=2+1/2$, nên điểm đó thuộc cực tiểu.'''),
        short(r'''Hai nguồn cùng pha cách nhau $10$ cm, bước sóng $2$ cm. Trên đoạn nối hai nguồn, bỏ hai nguồn, có bao nhiêu vị trí cực đại nếu coi điều kiện hình học lí tưởng?''', r'''Trên đoạn AB, hiệu đường đi $|d_2-d_1|$ chạy từ 0 đến gần $AB=10$ cm. Cực đại khi $|d_2-d_1|=k\lambda$ với $k=0,1,2,3,4$ và gần $5$ thì trùng nguồn. Mỗi $k=1..4$ có hai vị trí đối xứng, $k=0$ có một vị trí giữa. Tổng $1+2\cdot4=9$ vị trí nội bộ.'''),
        applied(r'''Hai nguồn A, B cùng pha, cách nhau $20$ cm, phát sóng có $\lambda=4$ cm. Trên đường thẳng AB, tìm số điểm cực tiểu nằm **giữa** A và B, không tính hai nguồn.''', r'''Trên đoạn AB, đặt trục gốc tại trung điểm. Hiệu đường đi theo độ lớn là $|d_2-d_1|=2|x|$, biến thiên từ 0 đến nhỏ hơn $20$ cm.

Cực tiểu: $2|x|=(k+1/2)\lambda=(k+1/2)4$ cm.

Cần $(k+1/2)4<20$, tức $k+1/2<5$. Với $k=0,1,2,3,4$, mỗi giá trị cho hai vị trí đối xứng. Vậy có $10$ điểm cực tiểu giữa A và B.''')
    ]

def l4():
    return [
        mcq(r'''Một sợi dây hai đầu cố định dài $L$. Điều kiện có sóng dừng là

A. $L=k\lambda$.  
B. $L=k\lambda/2$.  
C. $L=(2k+1)\lambda/4$.  
D. $L=\lambda/8$.''', r'''Chọn **B**, với $k=1,2,3,\ldots$'''),
        mcq(r'''Khoảng cách giữa hai nút liên tiếp của sóng dừng là

A. $\lambda/4$.  
B. $\lambda/2$.  
C. $\lambda$.  
D. $2\lambda$.''', r'''Chọn **B**.'''),
        mcq(r'''Khoảng cách từ một nút đến bụng gần nhất bằng

A. $\lambda/8$.  
B. $\lambda/4$.  
C. $\lambda/2$.  
D. $\lambda$.''', r'''Chọn **B**.'''),
        tf(r'''Sóng dừng trên dây:

a) Các nút có biên độ bằng 0.  
b) Các bụng có biên độ cực đại.  
c) Khoảng cách hai bụng liên tiếp là $\lambda/2$.  
d) Mọi điểm trên dây dao động cùng pha.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: các đoạn giữa hai nút liên tiếp dao động cùng pha, hai đoạn kề nhau ngược pha.'''),
        short(r'''Dây dài $1,2$ m hai đầu cố định có 6 bụng sóng. Tính bước sóng.''', r'''Với hai đầu cố định, số bụng $k=6$ và $L=k\lambda/2$. Do đó $\lambda=2L/k=2,4/6=0,40$ m.'''),
        short(r'''Dây dài $0,90$ m, hai đầu cố định, vận tốc sóng $180$ m/s. Tính tần số cơ bản.''', r'''Ở họa âm cơ bản $\lambda_1=2L=1,8$ m. $f_1=v/\lambda_1=180/1,8=100$ Hz.'''),
        short(r'''Một đầu dây cố định, đầu kia tự do. Chiều dài dây $0,75$ m. Ở mode cơ bản, tính bước sóng.''', r'''Một đầu nút, một đầu bụng: mode cơ bản có $L=\lambda/4$. Vậy $\lambda=4L=3,0$ m.'''),
        applied(r'''Một dây dài $1$ m hai đầu cố định. Khi kích thích ở $120$ Hz thấy có 4 bụng. Giữ nguyên lực căng và khối lượng riêng dài của dây. Muốn có 5 bụng thì cần tần số bao nhiêu?''', r'''Với hai đầu cố định, $f_n=n\,v/(2L)$ nên tần số tỉ lệ số bụng $n$.

$f_5/f_4=5/4$.

Do $f_4=120$ Hz, $f_5=120\cdot5/4=150$ Hz.''')
    ]

def l5():
    return [
        mcq(r'''Âm truyền từ không khí vào nước. Đại lượng nào không đổi khi qua mặt phân cách?

A. Tốc độ.  
B. Bước sóng.  
C. Tần số.  
D. Cả tốc độ và bước sóng.''', r'''Chọn **C**. Tần số do nguồn quyết định; tốc độ và bước sóng thay đổi theo môi trường.'''),
        mcq(r'''Mức cường độ âm tăng thêm $10$ dB thì cường độ âm tăng

A. 2 lần.  
B. 5 lần.  
C. 10 lần.  
D. 100 lần.''', r'''Chọn **C** vì $\Delta L=10\log(I_2/I_1)=10$ dB suy ra $I_2/I_1=10$.'''),
        mcq(r'''Độ cao của âm chủ yếu gắn với

A. biên độ.  
B. tần số.  
C. tốc độ âm.  
D. cường độ âm.''', r'''Chọn **B**.'''),
        tf(r'''Xét sóng âm:

a) Âm nghe được là sóng cơ.  
b) Trong cùng một môi trường tuyến tính, tốc độ âm gần như không phụ thuộc tần số trong miền thông thường.  
c) Âm càng to thì tần số nhất thiết càng lớn.  
d) Cường độ âm có đơn vị W/m².''', r'''a) **Đúng**.  
b) **Đúng** trong mô hình phổ thông.  
c) **Sai**: độ to liên quan cường độ/mức cường độ, không đồng nhất với tần số.  
d) **Đúng**.'''),
        short(r'''Một âm có tần số $680$ Hz truyền trong không khí với tốc độ $340$ m/s. Tính bước sóng.''', r'''$\lambda=v/f=340/680=0,50$ m.'''),
        short(r'''Cường độ âm tại điểm M là $10^{-6}$ W/m². Lấy $I_0=10^{-12}$ W/m². Tính mức cường độ âm.''', r'''$L=10\log(I/I_0)=10\log(10^6)=60$ dB.'''),
        short(r'''Một nguồn điểm phát âm đều mọi hướng. Bỏ hấp thụ. Khi khoảng cách đến nguồn tăng từ $2$ m lên $6$ m, cường độ giảm bao nhiêu lần?''', r'''$I\propto1/r^2$. Vì $r$ tăng 3 lần nên cường độ giảm $3^2=9$ lần.'''),
        applied(r'''Một ống khí một đầu kín, một đầu hở cộng hưởng ở hai chiều dài liên tiếp $L_1=18$ cm và $L_2=42$ cm với cùng âm thoa. Tính bước sóng và tần số âm nếu tốc độ âm $v=336$ m/s.''', r'''Với ống một đầu kín, các chiều dài cộng hưởng liên tiếp hơn kém nhau $\lambda/2$.

$L_2-L_1=42-18=24$ cm $=\lambda/2$.

Suy ra $\lambda=48$ cm $=0,48$ m. Tần số $f=v/\lambda=336/0,48=700$ Hz.''')
    ]

def l6():
    return [
        mcq(r'''Sóng điện từ truyền được

A. chỉ trong chất rắn.  
B. chỉ trong không khí.  
C. trong chân không.  
D. chỉ trong chất dẫn điện.''', r'''Chọn **C**. Sóng điện từ không cần môi trường vật chất.'''),
        mcq(r'''Trong chân không, sóng điện từ có tần số $100$ MHz. Bước sóng gần bằng

A. $0,3$ m.  
B. $3$ m.  
C. $30$ m.  
D. $300$ m.''', r'''Chọn **B**. $\lambda=c/f=3\cdot10^8/10^8=3$ m.'''),
        mcq(r'''Trong sóng điện từ, vectơ điện trường và vectơ cảm ứng từ

A. song song nhau.  
B. vuông góc nhau và vuông góc phương truyền sóng.  
C. luôn ngược pha.  
D. không biến thiên theo thời gian.''', r'''Chọn **B**. Trong mô hình sóng phẳng, $\vec E$, $\vec B$ và phương truyền đôi một vuông góc; $E$ và $B$ dao động cùng pha.'''),
        tf(r'''Xét sóng điện từ trong chân không:

a) Tốc độ bằng $c\approx3\cdot10^8$ m/s.  
b) Tần số càng lớn thì bước sóng càng nhỏ.  
c) Sóng điện từ là sóng dọc.  
d) Ánh sáng nhìn thấy là một phần của phổ điện từ.''', r'''a) **Đúng**.  
b) **Đúng** vì $c=\lambda f$.  
c) **Sai**: là sóng ngang.  
d) **Đúng**.'''),
        short(r'''Một bức xạ điện từ có bước sóng $600$ nm trong chân không. Tính tần số.''', r'''$f=c/\lambda=3\cdot10^8/(600\cdot10^{-9})=5\cdot10^{14}$ Hz.'''),
        short(r'''Một sóng vô tuyến có tần số $75$ MHz. Tính bước sóng trong chân không.''', r'''$\lambda=3\cdot10^8/(75\cdot10^6)=4$ m.'''),
        short(r'''Tín hiệu điện từ truyền từ vệ tinh đến trạm mặt đất khoảng $3,6\cdot10^7$ m. Bỏ qua đường đi cong. Ước tính thời gian truyền.''', r'''$t=s/c=3,6\cdot10^7/(3\cdot10^8)=0,12$ s.'''),
        applied(r'''Một bức xạ có tần số $6,0\cdot10^{14}$ Hz đi từ chân không vào thủy tinh có chiết suất $n=1,5$. Tính tốc độ, tần số và bước sóng trong thủy tinh.''', r'''Tốc độ trong thủy tinh $v=c/n=2,0\cdot10^8$ m/s. Tần số không đổi khi qua mặt phân cách: $f=6,0\cdot10^{14}$ Hz. Bước sóng trong thủy tinh:

$\lambda=v/f=2,0\cdot10^8/(6,0\cdot10^{14})=3,33\cdot10^{-7}$ m $=333$ nm.''')
    ]

def l7():
    return [
        mcq(r'''Trong thí nghiệm Young, khoảng vân được tính bởi

A. $i=aD/\lambda$.  
B. $i=\lambda D/a$.  
C. $i=\lambda a/D$.  
D. $i=D/(\lambda a)$.''', r'''Chọn **B**.'''),
        mcq(r'''Nếu tăng khoảng cách từ hai khe đến màn gấp đôi, các đại lượng khác không đổi, khoảng vân

A. giảm 2 lần.  
B. không đổi.  
C. tăng 2 lần.  
D. tăng 4 lần.''', r'''Chọn **C** vì $i\propto D$.'''),
        mcq(r'''Vân sáng bậc $k$ có vị trí

A. $x=ki$.  
B. $x=(k+1/2)i$.  
C. $x=i/k$.  
D. $x=2ki$.''', r'''Chọn **A**, với $k=0,\pm1,\pm2,\ldots$'''),
        tf(r'''Trong thí nghiệm Young với ánh sáng đơn sắc:

a) Vân trung tâm là vân sáng.  
b) Hai vân sáng liên tiếp cách nhau một khoảng vân.  
c) Vân tối thứ nhất cách vân trung tâm $i$.  
d) Tăng bước sóng làm khoảng vân tăng.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: vân tối gần trung tâm nhất cách $i/2$.  
d) **Đúng**.'''),
        short(r'''Hai khe cách nhau $1$ mm, màn cách $2$ m, dùng ánh sáng $600$ nm. Tính khoảng vân.''', r'''$i=\lambda D/a=600\cdot10^{-9}\cdot2/10^{-3}=1,2\cdot10^{-3}$ m $=1,2$ mm.'''),
        short(r'''Khoảng vân là $1,5$ mm. Tính vị trí vân sáng bậc 4 và vân tối gần phía dương thứ 4 kể từ trung tâm.''', r'''Vân sáng bậc 4: $x_4=4i=6$ mm. Các vân tối phía dương có $x=(k+1/2)i$, $k=0,1,2,3$. Vân tối thứ 4: $x=3,5i=5,25$ mm.'''),
        short(r'''Trong thí nghiệm Young, $D=1,5$ m, $a=0,75$ mm, khoảng vân $i=1,2$ mm. Tính bước sóng.''', r'''$\lambda=ia/D=1,2\cdot10^{-3}\cdot0,75\cdot10^{-3}/1,5=6,0\cdot10^{-7}$ m $=600$ nm.'''),
        applied(r'''Trong thí nghiệm Young, trên đoạn đối xứng quanh vân trung tâm dài $18$ mm quan sát được 13 vân sáng, trong đó hai đầu đoạn đúng tại hai vân sáng ngoài cùng. Tính khoảng vân.''', r'''Có 13 vân sáng từ vân ngoài bên trái đến vân ngoài bên phải nên có $12$ khoảng vân giữa chúng. Do chiều dài đoạn là $18$ mm:

$i=18/12=1,5$ mm.

Cách đếm số khoảng giữa các vân là điểm dễ sai: số khoảng luôn bằng số vân trừ 1 khi cả hai đầu là vân.''')
    ]

def l8():
    return [
        mcq(r'''Khi đo tần số bằng màn hình dao động kí, nếu $5$ chu kì chiếm $10$ ms thì tần số là

A. $50$ Hz.  
B. $100$ Hz.  
C. $500$ Hz.  
D. $2000$ Hz.''', r'''Chọn **C**. $T=10\text{ ms}/5=2$ ms, nên $f=1/T=500$ Hz.'''),
        mcq(r'''Để giảm sai số khi đo chu kì trên đồ thị, nên

A. chỉ đo một phần rất nhỏ của một chu kì.  
B. đo thời gian của nhiều chu kì rồi chia cho số chu kì.  
C. bỏ qua đơn vị thời gian.  
D. chọn hai điểm bất kì không cùng pha.''', r'''Chọn **B**. Đo trên nhiều chu kì giúp giảm ảnh hưởng sai số đọc một mốc thời gian.'''),
        mcq(r'''Hai đỉnh liên tiếp trên tín hiệu âm cách nhau $0,8$ ms. Tần số gần bằng

A. $125$ Hz.  
B. $800$ Hz.  
C. $1250$ Hz.  
D. $8000$ Hz.''', r'''Chọn **C**. $f=1/(0,8\cdot10^{-3})=1250$ Hz.'''),
        tf(r'''Trong thí nghiệm đo tần số âm:

a) Hai điểm dùng để đo một chu kì phải ở cùng trạng thái pha.  
b) Đo 10 chu kì thường ổn định hơn đo 1 chu kì.  
c) Biên độ tín hiệu quyết định trực tiếp tần số.  
d) Cần đổi đúng đơn vị ms sang s trước khi tính Hz.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**.  
d) **Đúng**.'''),
        short(r'''Trên màn hình, 8 chu kì chiếm $16,4$ ms. Tính tần số.''', r'''$T=16,4/8=2,05$ ms $=2,05\cdot10^{-3}$ s. $f=1/T\approx487,8$ Hz.'''),
        short(r'''Một tín hiệu có tần số danh định $440$ Hz. Nếu đo được $10$ chu kì trong $22,9$ ms, tính tần số đo và sai lệch tương đối so với giá trị danh định.''', r'''$T=2,29$ ms, nên $f_{đo}=1/0,00229\approx436,7$ Hz. Sai lệch tương đối $\approx|436,7-440|/440\cdot100\%\approx0,75\%$.'''),
        short(r'''Thang thời gian là $0,5$ ms/ô. Khoảng cách giữa hai đỉnh liên tiếp là $4,8$ ô. Tính tần số.''', r'''$T=4,8\cdot0,5=2,4$ ms. $f=1/(2,4\cdot10^{-3})\approx416,7$ Hz.'''),
        applied(r'''Ba lần đo thời gian của 20 chu kì cho các giá trị $45,2$ ms; $45,6$ ms; $45,4$ ms. Tính tần số từ giá trị trung bình và nêu vì sao nên dùng nhiều chu kì.''', r'''Thời gian trung bình của 20 chu kì:

$\bar t=(45,2+45,6+45,4)/3=45,4$ ms.

$T=45,4/20=2,27$ ms, nên $f\approx1/0,00227\approx440,5$ Hz.

Đo nhiều chu kì làm sai số đọc mốc thời gian được chia cho số chu kì, nên sai số tương đối của chu kì giảm đáng kể.''')
    ]

def l9():
    return [
        mcq(r'''Đo được bước sóng âm $0,68$ m và tần số $500$ Hz. Tốc độ âm là

A. $250$ m/s.  
B. $340$ m/s.  
C. $500$ m/s.  
D. $680$ m/s.''', r'''Chọn **B**. $v=f\lambda=500\cdot0,68=340$ m/s.'''),
        mcq(r'''Trong phương pháp cộng hưởng cột khí một đầu kín, chênh lệch giữa hai chiều dài cộng hưởng liên tiếp bằng

A. $\lambda/4$.  
B. $\lambda/2$.  
C. $\lambda$.  
D. $2\lambda$.''', r'''Chọn **B**.'''),
        mcq(r'''Đo tốc độ âm bằng tiếng vọng: khoảng cách đến vách là $51$ m, thời gian từ phát đến nghe vọng là $0,30$ s. Tốc độ âm là

A. $170$ m/s.  
B. $255$ m/s.  
C. $340$ m/s.  
D. $680$ m/s.''', r'''Chọn **C**. Âm đi và về quãng đường $2d=102$ m; $v=102/0,30=340$ m/s.'''),
        tf(r'''Trong thí nghiệm đo tốc độ âm:

a) Có thể dùng $v=f\lambda$.  
b) Nếu dùng tiếng vọng phải tính quãng đường hai chiều.  
c) Tần số âm thoa tự thay đổi khi dịch ống cộng hưởng.  
d) Nhiệt độ không khí có thể ảnh hưởng kết quả.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**.  
d) **Đúng**.'''),
        short(r'''Hai vị trí cộng hưởng liên tiếp của cột khí là $17,2$ cm và $51,5$ cm. Tần số âm thoa $500$ Hz. Tính tốc độ âm.''', r'''$\lambda=2(L_2-L_1)=2(51,5-17,2)=68,6$ cm $=0,686$ m. $v=f\lambda=500\cdot0,686=343$ m/s.'''),
        short(r'''Một phép đo tiếng vọng: người đứng cách vách $85$ m, thời gian nghe vọng $0,50$ s. Tính tốc độ âm.''', r'''Quãng đường âm đi và về là $170$ m. $v=170/0,50=340$ m/s.'''),
        short(r'''Một nguồn $400$ Hz phát âm trong không khí. Đo được khoảng cách giữa hai nút áp suất tương ứng một bước sóng là $0,86$ m. Tính tốc độ.''', r'''$v=f\lambda=400\cdot0,86=344$ m/s.'''),
        applied(r'''Trong thí nghiệm cột khí, ba chiều dài cộng hưởng liên tiếp đo được là $L_1=16,8$ cm, $L_2=50,9$ cm, $L_3=85,3$ cm với âm thoa $500$ Hz. Hãy lấy trung bình hai hiệu liên tiếp để ước tính tốc độ âm.''', r'''Hai hiệu: $L_2-L_1=34,1$ cm; $L_3-L_2=34,4$ cm. Trung bình $34,25$ cm.

Vì hiệu hai cộng hưởng liên tiếp bằng $\lambda/2$, ta có $\lambda=68,5$ cm $=0,685$ m.

$v=f\lambda=500\cdot0,685=342,5$ m/s.

Dùng nhiều khoảng liên tiếp giúp giảm tác động sai số đọc từng chiều dài.''')
    ]

def l10():
    return [
        mcq(r'''Nguồn âm chuyển động lại gần người nghe đứng yên. Tần số người nghe nhận được so với tần số nguồn

A. nhỏ hơn.  
B. bằng nhau.  
C. lớn hơn.  
D. bằng 0.''', r'''Chọn **C**.'''),
        mcq(r'''Người nghe chuyển động lại gần nguồn đứng yên trong không khí. Công thức phù hợp là

A. $f'=f\frac{v-v_o}{v}$.  
B. $f'=f\frac{v+v_o}{v}$.  
C. $f'=f\frac{v}{v+v_o}$.  
D. $f'=f\frac{v}{v-v_o}$.''', r'''Chọn **B**, với $v_o$ là tốc độ người nghe hướng về nguồn.'''),
        mcq(r'''Nguồn đứng yên phát $500$ Hz. Người nghe đứng yên. Không có chuyển động tương đối thì tần số nhận được là

A. $0$ Hz.  
B. $250$ Hz.  
C. $500$ Hz.  
D. phụ thuộc khoảng cách.''', r'''Chọn **C**.'''),
        tf(r'''Hiệu ứng Doppler trong môi trường đứng yên:

a) Nguồn tiến lại gần làm bước sóng phía trước nguồn ngắn lại.  
b) Nguồn lùi ra xa làm tần số nghe được giảm.  
c) Chỉ cần thay đổi biên độ nguồn cũng gây Doppler.  
d) Hiện tượng liên quan chuyển động tương đối theo phương truyền sóng.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**.  
d) **Đúng**.'''),
        short(r'''Nguồn âm $600$ Hz chuyển động lại gần người nghe đứng yên với tốc độ $20$ m/s. Lấy tốc độ âm $340$ m/s. Tính tần số nghe được.''', r'''Nguồn tiến lại gần: $f'=f\,v/(v-v_s)=600\cdot340/(340-20)=637,5$ Hz.'''),
        short(r'''Nguồn đứng yên phát $680$ Hz. Người nghe chạy lại gần nguồn với $v_o=10$ m/s. Tốc độ âm $340$ m/s. Tính tần số nghe được.''', r'''$f'=f(v+v_o)/v=680\cdot350/340=700$ Hz.'''),
        short(r'''Một xe phát còi $500$ Hz chạy ra xa người đứng yên với tốc độ $30$ m/s. Tốc độ âm $330$ m/s. Tính tần số nghe được.''', r'''Nguồn đi xa: $f'=f\,v/(v+v_s)=500\cdot330/360\approx458,3$ Hz.'''),
        applied(r'''Một nguồn phát $800$ Hz chuyển động với tốc độ $20$ m/s về phía người nghe; người nghe đồng thời chuyển động về phía nguồn với tốc độ $10$ m/s. Không khí đứng yên, tốc độ âm $340$ m/s. Tính tần số người nghe nhận được.''', r'''Khi cả người nghe và nguồn tiến lại gần nhau trong môi trường đứng yên:

$f'=f\frac{v+v_o}{v-v_s}$.

Thay số:

$f'=800\frac{340+10}{340-20}=800\frac{350}{320}=875$ Hz.

Dấu cộng ở tử vì người nghe tiến về nguồn; dấu trừ ở mẫu vì nguồn tiến về người nghe.''')
    ]

def l11():
    return [
        mcq(r'''Nhiễu xạ ánh sáng rõ hơn khi kích thước khe

A. rất lớn so với bước sóng.  
B. cùng cỡ với bước sóng.  
C. không liên quan bước sóng.  
D. bằng vô hạn.''', r'''Chọn **B**.'''),
        mcq(r'''Trong lăng kính thủy tinh thông thường, ánh sáng tím so với ánh sáng đỏ thường

A. lệch ít hơn.  
B. lệch nhiều hơn.  
C. không lệch.  
D. có cùng chiết suất.''', r'''Chọn **B** vì chiết suất đối với tím thường lớn hơn đối với đỏ.'''),
        mcq(r'''Tán sắc ánh sáng chứng tỏ chiết suất môi trường

A. không phụ thuộc bước sóng.  
B. phụ thuộc bước sóng.  
C. luôn bằng 1.  
D. chỉ phụ thuộc cường độ.''', r'''Chọn **B**.'''),
        tf(r'''Xét nhiễu xạ và tán sắc:

a) Nhiễu xạ là biểu hiện tính chất sóng.  
b) Ánh sáng trắng qua lăng kính có thể tách thành nhiều màu.  
c) Trong thủy tinh thông thường, đỏ thường có chiết suất lớn hơn tím.  
d) Khe càng hẹp so với bước sóng thì hiệu ứng nhiễu xạ càng đáng kể.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: thông thường $n_{tím}>n_{đỏ}$.  
d) **Đúng** trong giới hạn so sánh kích thước khe với bước sóng.'''),
        short(r'''Một bức xạ đỏ có $\lambda=650$ nm và tím có $\lambda=430$ nm trong chân không. Bức xạ nào có tần số lớn hơn và lớn hơn khoảng bao nhiêu lần?''', r'''Vì $f=c/\lambda$, bước sóng ngắn hơn có tần số lớn hơn. $f_{tím}/f_{đỏ}=\lambda_{đỏ}/\lambda_{tím}=650/430\approx1,51$.'''),
        short(r'''Một khe có bề rộng $0,5$ mm. So sánh định tính mức nhiễu xạ của sóng vô tuyến $\lambda=0,3$ m với ánh sáng $\lambda=600$ nm qua cùng khe.''', r'''Với sóng vô tuyến, khe rất nhỏ so với $\lambda$ nên nhiễu xạ cực mạnh. Với ánh sáng, khe rộng khoảng $833$ lần bước sóng nên nhiễu xạ hẹp hơn nhiều. Đây là so sánh định tính, không dùng công thức nhiễu xạ khe đơn chi tiết.'''),
        short(r'''Chiết suất của lăng kính đối với đỏ là $1,50$, đối với tím là $1,54$. Tính tốc độ hai bức xạ trong lăng kính theo $c=3\cdot10^8$ m/s.''', r'''$v_{đỏ}=c/1,50=2,00\cdot10^8$ m/s. $v_{tím}=c/1,54\approx1,95\cdot10^8$ m/s.'''),
        applied(r'''Một chùm sáng trắng đi từ không khí vào thủy tinh với cùng góc tới. Biết $n_{đỏ}=1,50$, $n_{tím}=1,54$. Không cần tính số cụ thể, hãy dùng định luật Snell để chứng minh tia tím khúc xạ gần pháp tuyến hơn tia đỏ.''', r'''Định luật Snell từ không khí ($n_1\approx1$) vào thủy tinh:

$\sin r=\sin i/n$.

Với cùng $i$, $n$ càng lớn thì $\sin r$ càng nhỏ, do đó $r$ càng nhỏ trong miền $0^\circ$ đến $90^\circ$.

Vì $n_{tím}=1,54>1,50=n_{đỏ}$, suy ra $r_{tím}<r_{đỏ}$. Vậy tia tím gần pháp tuyến hơn và bị lệch nhiều hơn.''')
    ]

def l12():
    return [
        mcq(r'''Bức xạ có bước sóng ngắn nhất trong các bức xạ sau là

A. hồng ngoại.  
B. ánh sáng đỏ.  
C. tia tử ngoại.  
D. sóng vô tuyến.''', r'''Chọn **C**.'''),
        mcq(r'''Tia X có tần số so với ánh sáng nhìn thấy thường

A. nhỏ hơn nhiều.  
B. lớn hơn.  
C. bằng nhau.  
D. bằng 0.''', r'''Chọn **B**.'''),
        mcq(r'''Quang phổ liên tục thường do

A. chất rắn, lỏng hoặc khí áp suất lớn được nung nóng phát ra.  
B. khí loãng phát ra từng vạch riêng.  
C. mọi nguồn đều giống nhau.  
D. chỉ laser phát ra.''', r'''Chọn **A** theo mô hình phổ thông.'''),
        tf(r'''Xét thang sóng điện từ:

a) Khi tần số tăng thì bước sóng trong chân không giảm.  
b) Hồng ngoại có bước sóng dài hơn ánh sáng đỏ.  
c) Tử ngoại có bước sóng dài hơn hồng ngoại.  
d) Tia gamma có tần số rất cao.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**.  
d) **Đúng**.'''),
        short(r'''Một bức xạ có $\lambda=3\cdot10^{-7}$ m. Tính tần số trong chân không.''', r'''$f=c/\lambda=3\cdot10^8/(3\cdot10^{-7})=10^{15}$ Hz.'''),
        short(r'''Sắp xếp theo bước sóng tăng dần: tia X, hồng ngoại, ánh sáng nhìn thấy, sóng vô tuyến.''', r'''Thứ tự: **tia X → ánh sáng nhìn thấy → hồng ngoại → sóng vô tuyến**.'''),
        short(r'''Một bức xạ có tần số $3\cdot10^{16}$ Hz. Tính bước sóng trong chân không và đổi sang nm.''', r'''$\lambda=c/f=3\cdot10^8/(3\cdot10^{16})=10^{-8}$ m $=10$ nm.'''),
        applied(r'''Hai bức xạ A và B có tần số lần lượt $5\cdot10^{14}$ Hz và $10^{19}$ Hz. Tính bước sóng trong chân không và nhận xét vùng phổ tương đối của chúng.''', r'''A: $\lambda_A=3\cdot10^8/(5\cdot10^{14})=6\cdot10^{-7}$ m $=600$ nm, thuộc vùng ánh sáng nhìn thấy.

B: $\lambda_B=3\cdot10^8/10^{19}=3\cdot10^{-11}$ m $=0,03$ nm, thuộc vùng bức xạ rất ngắn, điển hình vùng tia X cứng/tia gamma tùy cách phân loại nguồn. Ở mức phổ thông, chỉ cần nhận xét B có tần số rất cao và bước sóng rất ngắn.''')
    ]

def l13():
    return [
        mcq(r'''Trong thí nghiệm Young dùng đồng thời hai bức xạ, tại vị trí hai vân sáng trùng nhau phải có

A. $k_1\lambda_1=k_2\lambda_2$.  
B. $k_1/\lambda_1=k_2/\lambda_2$ luôn sai.  
C. $\lambda_1+\lambda_2=0$.  
D. $k_1=k_2$ trong mọi trường hợp.''', r'''Chọn **A** vì vị trí vân sáng $x=k\lambda D/a$.'''),
        mcq(r'''Với ánh sáng trắng trong thí nghiệm Young, vân trung tâm thường

A. tối.  
B. trắng vì các cực đại trung tâm trùng nhau.  
C. chỉ đỏ.  
D. chỉ tím.''', r'''Chọn **B**.'''),
        mcq(r'''Hai bức xạ $\lambda_1=600$ nm, $\lambda_2=450$ nm. Cặp bậc vân sáng nhỏ nhất khác 0 cho cùng vị trí là

A. $k_1=1,k_2=1$.  
B. $k_1=2,k_2=3$.  
C. $k_1=3,k_2=4$.  
D. $k_1=4,k_2=3$.''', r'''Chọn **C** vì $3\cdot600=4\cdot450=1800$ nm.'''),
        tf(r'''Giao thoa nhiều bức xạ:

a) Mỗi bước sóng có khoảng vân riêng.  
b) Bước sóng lớn hơn cho khoảng vân lớn hơn nếu $D,a$ giống nhau.  
c) Vân trung tâm của các bức xạ đơn sắc cùng hệ khe trùng nhau.  
d) Hai vân sáng bất kì của hai màu luôn trùng nhau.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**; chỉ những bậc thỏa điều kiện số nguyên thích hợp mới trùng.'''),
        short(r'''Hai bức xạ $500$ nm và $600$ nm. Tìm bậc vân sáng dương nhỏ nhất của mỗi bức xạ trùng nhau.''', r'''Cần $k_1\cdot500=k_2\cdot600$. Rút gọn $5k_1=6k_2$. Nghiệm nguyên dương nhỏ nhất: $k_1=6$, $k_2=5$.'''),
        short(r'''Khoảng vân của ánh sáng đỏ là $1,5$ mm, của tím là $1,0$ mm. Vị trí dương gần trung tâm nhất mà hai vân sáng trùng nhau là bao nhiêu?''', r'''Cần $k_đ\,1,5=k_t\,1,0$. Giá trị chung nhỏ nhất khác 0 là $3,0$ mm: đỏ bậc 2, tím bậc 3.'''),
        short(r'''Trong cùng thí nghiệm, $\lambda_đ=650$ nm, $\lambda_t=450$ nm. Tính tỉ số khoảng vân đỏ/tím.''', r'''Vì $i\propto\lambda$, $i_đ/i_t=650/450=13/9\approx1,44$.'''),
        applied(r'''Trong thí nghiệm Young, dùng đồng thời $\lambda_1=480$ nm và $\lambda_2=600$ nm. Khoảng vân ứng với $\lambda_1$ là $i_1=1,2$ mm. Tính khoảng cách từ vân trung tâm đến vị trí trùng vân sáng gần nhất khác trung tâm.''', r'''Trước hết $i_2/i_1=\lambda_2/\lambda_1=600/480=5/4$, nên $i_2=1,5$ mm.

Vị trí trùng thỏa $k_1i_1=k_2i_2$. Cần $1,2k_1=1,5k_2$, hay $4k_1=5k_2$. Nghiệm dương nhỏ nhất $k_1=5$, $k_2=4$.

Vị trí: $x=5\cdot1,2=6,0$ mm.''')
    ]

LESSONS={
'01-mechanical-wave-basics.md': l1(),
'02-wave-equation-phase-graphs.md': l2(),
'03-mechanical-interference.md': l3(),
'04-standing-waves.md': l4(),
'05-sound-waves.md': l5(),
'06-electromagnetic-waves.md': l6(),
'07-light-interference.md': l7(),
'08-practical-sound-frequency.md': l8(),
'09-practical-sound-speed.md': l9(),
'10-doppler-effect.md': l10(),
'11-light-wave-diffraction-dispersion.md': l11(),
'12-spectra-electromagnetic-spectrum.md': l12(),
'13-multiwavelength-white-light-interference.md': l13(),
}

if __name__=='__main__':
    for lf, probs in LESSONS.items():
        write_lesson_practice(CH, lf, probs)
        add_practice_links(CH, lf)
    write_practice_index(CH, list(LESSONS))
    print('chapter 2', sum(len(v) for v in LESSONS.values()), 'problems')
