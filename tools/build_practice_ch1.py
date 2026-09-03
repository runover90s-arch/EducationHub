from practice_bank_common import *
import math

CH='01-oscillations'

def lesson1():
    return [
        mcq(r'''Một vật dao động điều hòa theo phương trình $x=6\cos(4\pi t-\pi/3)$ cm. Biên độ và tần số của dao động là

A. $6$ cm và $2$ Hz.  
B. $4$ cm và $6$ Hz.  
C. $6$ cm và $4$ Hz.  
D. $3$ cm và $2$ Hz.''', r'''Chọn **A**. So sánh với $x=A\cos(\omega t+\varphi)$: $A=6$ cm, $\omega=4\pi$ rad/s nên $f=\omega/(2\pi)=2$ Hz.'''),
        mcq(r'''Một dao động có chu kì $T=0,25$ s. Tần số góc bằng

A. $2\pi$ rad/s.  
B. $4\pi$ rad/s.  
C. $8\pi$ rad/s.  
D. $16\pi$ rad/s.''', r'''Chọn **C**. $\omega=2\pi/T=2\pi/0,25=8\pi$ rad/s.'''),
        mcq(r'''Một vật dao động điều hòa có biên độ $A=5$ cm. Chiều dài quỹ đạo là

A. $2,5$ cm.  
B. $5$ cm.  
C. $10$ cm.  
D. $20$ cm.''', r'''Chọn **C**. Vật chuyển động giữa hai biên $-A$ và $+A$, vì vậy chiều dài quỹ đạo là $2A=10$ cm.'''),
        mcq(r'''Phát biểu nào đúng?

A. Mọi dao động tuần hoàn đều là dao động điều hòa.  
B. Dao động điều hòa là dao động có li độ biến thiên theo hàm sin hoặc cos của thời gian.  
C. Biên độ dao động điều hòa có thể âm.  
D. Tần số góc có đơn vị héc.''', r'''Chọn **B**. Dao động điều hòa là trường hợp đặc biệt của dao động tuần hoàn; biên độ được quy ước dương và tần số góc có đơn vị rad/s.'''),
        tf(r'''Xét dao động $x=8\cos(5t+\pi/6)$ cm. Đánh dấu Đúng/Sai:

a) Biên độ bằng $8$ cm.  
b) Chu kì bằng $2\pi/5$ s.  
c) Tần số bằng $5$ Hz.  
d) Pha ban đầu bằng $\pi/6$ rad.''', r'''a) **Đúng**. $A=8$ cm.  
b) **Đúng**. $T=2\pi/\omega=2\pi/5$ s.  
c) **Sai**. $f=\omega/(2\pi)=5/(2\pi)$ Hz.  
d) **Đúng**. $\varphi=\pi/6$ rad.'''),
        tf(r'''Một vật dao động điều hòa có phương trình $x=A\cos(\omega t+\varphi)$ với $A>0$, $\omega>0$. Xét các phát biểu:

a) $x$ luôn nằm trong đoạn $[-A,A]$.  
b) Sau mỗi khoảng thời gian $T$, trạng thái dao động lặp lại.  
c) Hệ số của $t$ trong pha chính là tần số $f$.  
d) Nếu đổi $A$ thành $-A$ mà giữ nguyên pha thì vẫn đang viết ở dạng chuẩn.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**. Hệ số của $t$ là $\omega$, không phải $f$.  
d) **Sai**. Dạng chuẩn lấy $A>0$; nếu gặp biên độ âm phải chuyển dấu vào pha.'''),
        short(r'''Một vật thực hiện $45$ dao động toàn phần trong $18$ s. Tính chu kì, tần số và tần số góc.''', r'''Ta có $f=N/\Delta t=45/18=2,5$ Hz. Do đó $T=1/f=0,4$ s và $\omega=2\pi f=5\pi$ rad/s.'''),
        short(r'''Vật dao động theo $x=10\cos(2\pi t+\pi/3)$ cm. Tính pha dao động và li độ tại $t=1/6$ s.''', r'''Pha tại $t=1/6$ s:

$\Phi=2\pi\cdot\frac16+\frac\pi3=\frac{2\pi}{3}$.

Suy ra $x=10\cos(2\pi/3)=-5$ cm.'''),
        short(r'''Một vật dao động điều hòa có $f=4$ Hz và quỹ đạo dài $16$ cm. Viết các giá trị $A$, $T$ và $\omega$.''', r'''Quỹ đạo dài $2A=16$ cm nên $A=8$ cm. $T=1/f=0,25$ s và $\omega=2\pi f=8\pi$ rad/s.'''),
        applied(r'''Một vật dao động điều hòa. Tại $t=0$ vật ở vị trí $x=A/2$ và đang chuyển động theo chiều âm. Biết chu kì $T=0,8$ s, biên độ $A=6$ cm. Viết phương trình dao động dạng cos.''', r'''**Chọn dạng chuẩn:** $x=A\cos(\omega t+\varphi)$.

$\omega=2\pi/T=2,5\pi$ rad/s. Tại $t=0$:

$\cos\varphi=x_0/A=1/2$.

Vì vật chuyển động theo chiều âm nên $v_0=-A\omega\sin\varphi<0$, tức $\sin\varphi>0$. Do đó chọn $\varphi=\pi/3$.

Vậy

$$
x=6\cos\left(2,5\pi t+\frac{\pi}{3}\right)\text{ cm}.
$$

Kiểm tra: tại $t=0$, $x=3$ cm và $v<0$, đúng với đề.''')
    ]

def lesson2():
    return [
        mcq(r'''Trong dao động điều hòa, gia tốc và li độ liên hệ bởi

A. $a=\omega x$.  
B. $a=-\omega x$.  
C. $a=-\omega^2x$.  
D. $a=\omega^2v$.''', r'''Chọn **C**. Gia tốc luôn hướng về vị trí cân bằng và có độ lớn tỉ lệ với $|x|$: $a=-\omega^2x$.'''),
        mcq(r'''Vật dao động điều hòa có $A=4$ cm, $\omega=5$ rad/s. Tốc độ cực đại bằng

A. $5$ cm/s.  
B. $9$ cm/s.  
C. $20$ cm/s.  
D. $80$ cm/s.''', r'''Chọn **C**. $v_{\max}=\omega A=5\cdot4=20$ cm/s.'''),
        mcq(r'''Tại vị trí biên của dao động điều hòa, đại lượng nào bằng không?

A. Li độ.  
B. Vận tốc.  
C. Gia tốc.  
D. Cả vận tốc và gia tốc.''', r'''Chọn **B**. Ở biên $|x|=A$ nên $v=0$, còn $|a|=\omega^2A$ đạt cực đại.'''),
        mcq(r'''Vận tốc trong dao động điều hòa sớm pha hay trễ pha so với li độ?

A. Sớm pha $\pi/2$.  
B. Trễ pha $\pi/2$.  
C. Cùng pha.  
D. Ngược pha.''', r'''Chọn **A**. Nếu $x=A\cos\Phi$ thì $v=A\omega\cos(\Phi+\pi/2)$.'''),
        tf(r'''Một vật dao động điều hòa có $x=5\cos(4t)$ cm. Xét các phát biểu:

a) $v_{\max}=20$ cm/s.  
b) $a_{\max}=80$ cm/s².  
c) Tại $x=3$ cm, độ lớn vận tốc là $16$ cm/s.  
d) Khi $x>0$ thì gia tốc cũng dương.''', r'''a) **Đúng**: $v_{\max}=\omega A=20$ cm/s.  
b) **Đúng**: $a_{\max}=\omega^2A=16\cdot5=80$ cm/s².  
c) **Đúng**: $|v|=\omega\sqrt{A^2-x^2}=4\sqrt{25-9}=16$ cm/s.  
d) **Sai**: $a=-\omega^2x$, nên $x>0$ thì $a<0$.'''),
        tf(r'''Xét một vật dao động điều hòa:

a) Khi đi từ biên về vị trí cân bằng, tốc độ tăng.  
b) Khi đi từ vị trí cân bằng ra biên, độ lớn gia tốc giảm.  
c) Ở vị trí cân bằng, gia tốc bằng không.  
d) Ở cùng một li độ, độ lớn vận tốc luôn như nhau.''', r'''a) **Đúng**.  
b) **Sai**: $|a|=\omega^2|x|$ tăng khi ra xa vị trí cân bằng.  
c) **Đúng**.  
d) **Đúng**: $v^2=\omega^2(A^2-x^2)$ chỉ phụ thuộc $x^2$.'''),
        short(r'''Vật có $A=10$ cm, $\omega=6$ rad/s. Tại $x=8$ cm, tính tốc độ và độ lớn gia tốc.''', r'''$|v|=\omega\sqrt{A^2-x^2}=6\sqrt{100-64}=36$ cm/s. $|a|=\omega^2|x|=36\cdot8=288$ cm/s².'''),
        short(r'''Một vật dao động điều hòa có $v_{\max}=40$ cm/s và $a_{\max}=200$ cm/s². Tính $\omega$ và $A$.''', r'''Từ $a_{\max}=\omega v_{\max}$ suy ra $\omega=200/40=5$ rad/s. Sau đó $A=v_{\max}/\omega=40/5=8$ cm.'''),
        short(r'''Tại li độ $x=3$ cm, một vật có gia tốc $a=-48$ cm/s². Biết biên độ $A=5$ cm. Tính $\omega$ và tốc độ tại vị trí này.''', r'''Từ $a=-\omega^2x$: $\omega^2=48/3=16$, nên $\omega=4$ rad/s. Khi đó $|v|=4\sqrt{25-9}=16$ cm/s.'''),
        applied(r'''Một vật dao động điều hòa. Tại $x_1=3$ cm, tốc độ là $v_1=20$ cm/s; tại $x_2=4$ cm, tốc độ là $v_2=10\sqrt3$ cm/s. Tính $\omega$ và biên độ $A$.''', r'''Dùng hệ thức độc lập $v^2=\omega^2(A^2-x^2)$ cho hai trạng thái:

$v_1^2-v_2^2=\omega^2(x_2^2-x_1^2)$.

Suy ra $400-300=\omega^2(16-9)$, nên $\omega^2=100/7$ và $\omega=10/\sqrt7$ rad/s.

Thay vào trạng thái thứ nhất:

$A^2=x_1^2+v_1^2/\omega^2=9+400/(100/7)=37$.

Vậy $A=\sqrt{37}$ cm. Kết quả thỏa $A>|x_1|,|x_2|$.''')
    ]

def lesson3():
    return [
        mcq(r'''Một vật xuất phát từ biên dương. Thời gian ngắn nhất để đến vị trí cân bằng bằng

A. $T/2$.  
B. $T/3$.  
C. $T/4$.  
D. $T/8$.''', r'''Chọn **C**. Từ biên đến vị trí cân bằng tương ứng góc quét $\pi/2$, bằng một phần tư chu kì.'''),
        mcq(r'''Trong một chu kì, vật dao động điều hòa đi qua vị trí $x=A/2$ bao nhiêu lần?

A. 1.  
B. 2.  
C. 3.  
D. 4.''', r'''Chọn **B**. Mỗi li độ nằm giữa hai biên được vật đi qua hai lần trong một chu kì, một lần theo mỗi chiều.'''),
        mcq(r'''Một vật dao động với biên độ $A$. Trong đúng nửa chu kì, quãng đường vật đi được luôn bằng

A. $A$.  
B. $2A$.  
C. $3A$.  
D. $4A$.''', r'''Chọn **B**. Trong mọi khoảng thời gian dài $T/2$, vật đi từ một trạng thái đến trạng thái đối pha và tổng quãng đường bằng $2A$.'''),
        mcq(r'''Vật xuất phát từ biên dương. Thời gian ngắn nhất để đến $x=A/2$ là

A. $T/12$.  
B. $T/8$.  
C. $T/6$.  
D. $T/4$.''', r'''Chọn **C**. $x/A=\cos\Delta\varphi=1/2$ nên $\Delta\varphi=\pi/3$. Do $T$ ứng với $2\pi$, thời gian là $T/6$.'''),
        tf(r'''Xét dao động điều hòa có chu kì $T$:

a) Từ biên này sang biên kia mất $T/2$.  
b) Từ vị trí cân bằng đến một biên gần nhất mất $T/4$.  
c) Trong $T$, quãng đường luôn bằng $4A$.  
d) Trong $T/4$, quãng đường luôn bằng $A$ bất kể thời điểm bắt đầu.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**. Quãng đường trong $T/4$ phụ thuộc pha ban đầu; chỉ một số đoạn đặc biệt mới bằng $A$.'''),
        tf(r'''Trên đường tròn lượng giác biểu diễn dao động điều hòa:

a) Góc quét tăng đều theo thời gian với tốc độ góc $\omega$.  
b) Hình chiếu lên trục dao động cho li độ.  
c) Hai điểm có cùng hình chiếu luôn tương ứng cùng chiều chuyển động.  
d) Có thể dùng góc quét để tính thời gian ngắn nhất giữa hai trạng thái.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: cùng li độ có thể đi theo hai chiều trái nhau.  
d) **Đúng**, với $\Delta t=\Delta\varphi/\omega$.'''),
        short(r'''Vật dao động với $A=8$ cm, $T=1,2$ s. Từ biên dương, tính thời gian ngắn nhất để đến $x=-4$ cm.''', r'''Từ biên dương, $x/A=-1/2$ ứng với góc quét nhỏ nhất $2\pi/3$. Do đó $\Delta t=(2\pi/3)/(2\pi/T)=T/3=0,4$ s.'''),
        short(r'''Vật dao động với $A=6$ cm, chu kì $0,8$ s. Tính quãng đường đi được trong $2,4$ s.''', r'''$2,4$ s $=3T$. Mỗi chu kì vật đi $4A=24$ cm. Vậy quãng đường là $3\cdot24=72$ cm.'''),
        short(r'''Một vật đi từ $x=-A/2$ theo chiều dương đến $x=A/2$ theo chiều dương. Tính thời gian ngắn nhất theo $T$.''', r'''Ở $x=-A/2$ theo chiều dương, pha có thể chọn $4\pi/3$; ở $x=A/2$ theo chiều dương, trạng thái kế tiếp có pha $5\pi/3$. Chênh pha $\pi/3$, nên $\Delta t=T/6$.'''),
        applied(r'''Vật dao động điều hòa có $T=1,2$ s. Tại thời điểm ban đầu vật ở $x=A/2$ và đi theo chiều dương. Tính thời gian ngắn nhất kể từ đó để vật đi qua $x=-A/2$ lần thứ hai.''', r'''Chọn pha ban đầu $\Phi_0=5\pi/3$ vì $\cos\Phi_0=1/2$ và $v=-A\omega\sin\Phi_0>0$.

Các trạng thái $x=-A/2$ có pha $2\pi/3+2k\pi$ hoặc $4\pi/3+2k\pi$.

Sau $5\pi/3$, lần thứ nhất là $2\pi/3+2\pi=8\pi/3$; lần thứ hai là $4\pi/3+2\pi=10\pi/3$.

Chênh pha đến lần thứ hai: $10\pi/3-5\pi/3=5\pi/3$.

Vì $2\pi$ ứng với $T$, $\Delta t=(5/6)T=1,0$ s.''')
    ]

def lesson4():
    return [
        mcq(r'''Con lắc lò xo có $m=0,20$ kg, $k=80$ N/m. Tần số góc bằng

A. $10$ rad/s.  
B. $20$ rad/s.  
C. $40$ rad/s.  
D. $400$ rad/s.''', r'''Chọn **B**. $\omega=\sqrt{k/m}=\sqrt{80/0,20}=20$ rad/s.'''),
        mcq(r'''Con lắc lò xo treo thẳng đứng có độ dãn cân bằng $\Delta\ell_0=4$ cm tại nơi $g=10$ m/s². Tần số góc bằng

A. $5$ rad/s.  
B. $10$ rad/s.  
C. $15$ rad/s.  
D. $20$ rad/s.''', r'''Chọn **A**. $\omega=\sqrt{g/\Delta\ell_0}=\sqrt{10/0,04}=5\sqrt{10}\approx15,81$ rad/s.''', 'Mức 2 — Phát hiện sai sót'),
        mcq(r'''Một lò xo có độ cứng $k=60$ N/m. Cắt lò xo thành ba phần bằng nhau. Độ cứng của mỗi phần bằng

A. $20$ N/m.  
B. $60$ N/m.  
C. $120$ N/m.  
D. $180$ N/m.''', r'''Chọn **D**. Với lò xo đều, $k$ tỉ lệ nghịch chiều dài. Đoạn dài bằng $1/3$ ban đầu nên độ cứng gấp 3: $k'=180$ N/m.'''),
        mcq(r'''Hai lò xo có $k_1=60$ N/m và $k_2=30$ N/m ghép nối tiếp. Độ cứng tương đương là

A. $20$ N/m.  
B. $30$ N/m.  
C. $45$ N/m.  
D. $90$ N/m.''', r'''Chọn **A**. $k_{nt}=k_1k_2/(k_1+k_2)=60\cdot30/90=20$ N/m.'''),
        tf(r'''Con lắc lò xo treo thẳng đứng dao động quanh vị trí cân bằng. Xét các phát biểu:

a) Ở vị trí cân bằng, lực đàn hồi luôn bằng trọng lực.  
b) Độ dãn cân bằng thỏa $k\Delta\ell_0=mg$.  
c) Nếu $A>\Delta\ell_0$, trong một phần chu kì lò xo bị nén.  
d) Chu kì phụ thuộc biên độ nếu lò xo lí tưởng và dao động nhỏ quanh cân bằng.''', r'''a) **Đúng** về vị trí cân bằng tĩnh.  
b) **Đúng**.  
c) **Đúng**: li độ lên trên đủ lớn làm chiều dài nhỏ hơn chiều dài tự nhiên.  
d) **Sai**: $T=2\pi\sqrt{m/k}$ không phụ thuộc biên độ trong mô hình lí tưởng.'''),
        tf(r'''Con lắc lò xo nằm ngang lí tưởng:

a) Lực kéo về là $F=-kx$.  
b) Tốc độ cực đại ở hai biên.  
c) Gia tốc cực đại về độ lớn ở hai biên.  
d) Tăng khối lượng vật thì chu kì tăng.''', r'''a) **Đúng**.  
b) **Sai**: tốc độ cực đại ở vị trí cân bằng.  
c) **Đúng**.  
d) **Đúng** vì $T\propto\sqrt m$.'''),
        short(r'''Con lắc lò xo có $m=250$ g, chu kì $T=0,5$ s. Tính độ cứng $k$ theo $\pi^2\approx10$.''', r'''$T=2\pi\sqrt{m/k}$ nên $k=4\pi^2m/T^2$. Thay $m=0,25$ kg, $T=0,5$ s: $k=4\cdot10\cdot0,25/0,25=40$ N/m.'''),
        short(r'''Con lắc lò xo treo thẳng đứng có $m=0,20$ kg, $k=50$ N/m, $g=10$ m/s². Tính độ dãn cân bằng.''', r'''$\Delta\ell_0=mg/k=0,20\cdot10/50=0,04$ m $=4$ cm.'''),
        short(r'''Một con lắc lò xo nằm ngang có $k=100$ N/m, biên độ $A=4$ cm. Tính lực kéo về cực đại.''', r'''$F_{\max}=kA=100\cdot0,04=4$ N.'''),
        applied(r'''Con lắc lò xo treo thẳng đứng có $m=0,10$ kg, $k=40$ N/m, $g=10$ m/s² và biên độ $A=4$ cm. Chọn chiều dương hướng xuống, gốc tại vị trí cân bằng. Tính lực đàn hồi lớn nhất và nhỏ nhất trong quá trình dao động; cho biết lò xo có bị nén không.''', r'''Độ dãn cân bằng:

$\Delta\ell_0=mg/k=0,1\cdot10/40=0,025$ m $=2,5$ cm.

Độ biến dạng tức thời so với chiều dài tự nhiên là $\Delta\ell=\Delta\ell_0+x$.

- Lớn nhất tại $x=+A$: $\Delta\ell_{\max}=2,5+4=6,5$ cm, nên $F_{dh,\max}=40\cdot0,065=2,6$ N.
- Nhỏ nhất về độ giãn tại $x=-A$: $\Delta\ell=2,5-4=-1,5$ cm. Dấu âm cho biết lò xo **bị nén** $1,5$ cm. Độ lớn lực đàn hồi khi đó là $40\cdot0,015=0,6$ N.

Trong chu kì còn có thời điểm $\Delta\ell=0$, khi đó lực đàn hồi bằng 0. Vì thế **độ lớn lực đàn hồi nhỏ nhất trong cả quá trình là 0 N**, còn độ lớn cực đại là $2,6$ N. Đây là điểm dễ nhầm nếu chỉ so hai biên.''')
    ]

def lesson5():
    return [
        mcq(r'''Chu kì con lắc đơn dao động góc nhỏ là

A. $2\pi\sqrt{g/\ell}$.  
B. $2\pi\sqrt{\ell/g}$.  
C. $\sqrt{\ell/g}$.  
D. $2\pi\ell/g$.''', r'''Chọn **B**. Công thức dao động góc nhỏ: $T=2\pi\sqrt{\ell/g}$.'''),
        mcq(r'''Giữ nguyên nơi thí nghiệm, tăng chiều dài con lắc đơn lên 4 lần. Chu kì

A. giảm 4 lần.  
B. giảm 2 lần.  
C. tăng 2 lần.  
D. tăng 4 lần.''', r'''Chọn **C** vì $T\propto\sqrt\ell$.'''),
        mcq(r'''Con lắc đơn dài $1$ m tại nơi $g=\pi^2$ m/s² có chu kì

A. $1$ s.  
B. $2$ s.  
C. $\pi$ s.  
D. $2\pi$ s.''', r'''Chọn **B**. $T=2\pi\sqrt{1/\pi^2}=2$ s.'''),
        mcq(r'''Trong gần đúng góc nhỏ, tần số góc của con lắc đơn là

A. $\sqrt{\ell/g}$.  
B. $g/\ell$.  
C. $\sqrt{g/\ell}$.  
D. $2\pi\sqrt{g/\ell}$.''', r'''Chọn **C**. $\omega=\sqrt{g/\ell}$.'''),
        tf(r'''Xét con lắc đơn dao động góc nhỏ:

a) Chu kì không phụ thuộc khối lượng vật nặng.  
b) Chu kì tăng khi tăng chiều dài dây.  
c) Chu kì giảm khi gia tốc trọng trường tăng.  
d) Công thức $T=2\pi\sqrt{\ell/g}$ đúng chính xác cho mọi biên độ góc.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: công thức chuẩn này dựa trên gần đúng góc nhỏ.'''),
        tf(r'''Con lắc đơn không ma sát, chọn thế năng bằng 0 ở vị trí cân bằng:

a) Cơ năng bảo toàn.  
b) Ở biên, động năng bằng 0.  
c) Ở vị trí cân bằng, thế năng cực đại.  
d) Tốc độ cực đại ở vị trí cân bằng.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: với mốc ở cân bằng, thế năng nhỏ nhất bằng 0 tại đó.  
d) **Đúng**.'''),
        short(r'''Con lắc đơn dài $0,81$ m tại nơi $g=10$ m/s². Tính chu kì gần đúng với $\pi\approx3,14$.''', r'''$T=2\pi\sqrt{0,81/10}\approx6,28\cdot0,2846\approx1,79$ s.'''),
        short(r'''Một con lắc đơn có chu kì $T_1=2$ s. Tăng chiều dài thêm $21\%$. Tính chu kì mới.''', r'''$\ell_2=1,21\ell_1$, nên $T_2/T_1=\sqrt{1,21}=1,1$. Vậy $T_2=2,2$ s.'''),
        short(r'''Con lắc đơn dài $1$ m, biên độ góc nhỏ $0,08$ rad, $g=10$ m/s². Tính tốc độ cực đại theo gần đúng góc nhỏ.''', r'''Với $s_0=\ell\alpha_0=0,08$ m và $\omega=\sqrt{g/\ell}=\sqrt{10}$ rad/s, $v_{\max}=\omega s_0\approx0,253$ m/s.'''),
        applied(r'''Một con lắc đơn dài $1$ m được kéo lệch đến góc $60^\circ$ rồi thả không vận tốc đầu. Bỏ qua ma sát, lấy $g=10$ m/s². Tính tốc độ ở vị trí thấp nhất và lực căng dây tại đó đối với vật nặng khối lượng $0,20$ kg.''', r'''Không dùng gần đúng góc nhỏ vì biên độ $60^\circ$ lớn.

Bảo toàn cơ năng từ biên đến vị trí thấp nhất:

$\frac12mv^2=mg\ell(1-\cos60^\circ)$.

Suy ra $v^2=2g\ell(1-1/2)=10$, nên $v=\sqrt{10}\approx3,16$ m/s.

Tại vị trí thấp nhất, phương bán kính hướng lên:

$T-mg=mv^2/\ell$.

Do đó $T=mg+mv^2/\ell=0,2\cdot10+0,2\cdot10=4$ N.''')
    ]

def lesson6():
    return [
        mcq(r'''Cơ năng của con lắc lò xo dao động điều hòa là

A. $\frac12kA^2$.  
B. $kA^2$.  
C. $\frac12mA^2$.  
D. $m\omega A$.''', r'''Chọn **A**. $W=\frac12kA^2=\frac12m\omega^2A^2$.'''),
        mcq(r'''Khi $|x|=A/2$, tỉ số thế năng trên cơ năng bằng

A. $1/2$.  
B. $1/4$.  
C. $3/4$.  
D. $1$.''', r'''Chọn **B** vì $W_t/W=x^2/A^2=1/4$.'''),
        mcq(r'''Khi động năng bằng thế năng, độ lớn li độ bằng

A. $A/2$.  
B. $A/\sqrt2$.  
C. $A\sqrt3/2$.  
D. $0$.''', r'''Chọn **B**. $W_t=W_d=W/2$ nên $x^2/A^2=1/2$.'''),
        mcq(r'''Trong dao động điều hòa lí tưởng, đại lượng nào không đổi theo thời gian?

A. Động năng.  
B. Thế năng.  
C. Cơ năng.  
D. Công suất tức thời của lực kéo về.''', r'''Chọn **C** nếu không có lực cản hay tác động làm thay đổi cơ năng.'''),
        tf(r'''Xét dao động điều hòa lí tưởng:

a) Động năng cực đại ở vị trí cân bằng.  
b) Thế năng cực đại ở hai biên.  
c) Động năng và thế năng biến thiên với cùng chu kì bằng $T$.  
d) Tổng động năng và thế năng không đổi.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: mỗi năng lượng biến thiên với chu kì $T/2$.  
d) **Đúng**.'''),
        tf(r'''Một con lắc lò xo có biên độ tăng từ $A$ lên $2A$ trong khi $k$ không đổi:

a) Cơ năng tăng 2 lần.  
b) Cơ năng tăng 4 lần.  
c) Tốc độ cực đại tăng 2 lần.  
d) Gia tốc cực đại tăng 2 lần.''', r'''a) **Sai**.  
b) **Đúng** vì $W\propto A^2$.  
c) **Đúng** vì $v_{\max}=\omega A$.  
d) **Đúng** vì $a_{\max}=\omega^2A$.'''),
        short(r'''Con lắc lò xo có $k=50$ N/m, $A=6$ cm. Tính cơ năng.''', r'''$W=\frac12kA^2=\frac12\cdot50\cdot0,06^2=0,09$ J.'''),
        short(r'''Một vật dao động điều hòa có cơ năng $0,20$ J. Tại một vị trí, thế năng bằng $0,05$ J. Tính động năng và tỉ số $|v|/v_{\max}$.''', r'''$W_d=W-W_t=0,15$ J. Vì $W_d/W=v^2/v_{\max}^2$, ta có $|v|/v_{\max}=\sqrt{0,15/0,20}=\sqrt3/2$.'''),
        short(r'''Tại một vị trí, động năng bằng 3 lần thế năng. Tìm $|x|/A$.''', r'''$W_d=3W_t$ nên $W=4W_t$. Do $W_t/W=x^2/A^2=1/4$, suy ra $|x|/A=1/2$.'''),
        applied(r'''Một con lắc lò xo có $m=0,25$ kg, $k=100$ N/m. Tại một thời điểm vật có $x=3$ cm và $v=0,40$ m/s. Tính biên độ và cơ năng của dao động.''', r'''Tần số góc $\omega=\sqrt{k/m}=\sqrt{100/0,25}=20$ rad/s.

Dùng hệ thức độc lập:

$A^2=x^2+v^2/\omega^2=0,03^2+0,40^2/20^2=0,0009+0,0004=0,0013$.

Suy ra $A=\sqrt{0,0013}\approx0,0361$ m $=3,61$ cm.

Cơ năng:

$W=\frac12kA^2=50\cdot0,0013=0,065$ J.

Có thể kiểm tra lại bằng $W=\frac12kx^2+\frac12mv^2=0,045+0,020=0,065$ J.''')
    ]

def lesson7():
    return [
        mcq(r'''Hai dao động cùng phương, cùng tần số và cùng pha có biên độ $A_1=3$ cm, $A_2=5$ cm. Biên độ tổng hợp là

A. $2$ cm.  
B. $4$ cm.  
C. $8$ cm.  
D. $15$ cm.''', r'''Chọn **C**. Hai dao động cùng pha nên $A=A_1+A_2=8$ cm.'''),
        mcq(r'''Hai dao động cùng phương, cùng tần số, ngược pha có $A_1=7$ cm, $A_2=4$ cm. Biên độ tổng hợp là

A. $3$ cm.  
B. $11$ cm.  
C. $\sqrt{33}$ cm.  
D. $28$ cm.''', r'''Chọn **A**. Ngược pha nên $A=|A_1-A_2|=3$ cm.'''),
        mcq(r'''Trong dao động cưỡng bức ổn định, tần số dao động của hệ bằng

A. tần số riêng của hệ trong mọi trường hợp.  
B. tần số của ngoại lực cưỡng bức.  
C. tổng hai tần số.  
D. bằng 0.''', r'''Chọn **B**. Trạng thái cưỡng bức ổn định dao động theo tần số của ngoại lực.'''),
        mcq(r'''Cộng hưởng xảy ra rõ nhất khi

A. tần số ngoại lực gần bằng tần số riêng và lực cản nhỏ.  
B. tần số ngoại lực bằng 0.  
C. lực cản rất lớn.  
D. hệ không chịu ngoại lực.''', r'''Chọn **A**.'''),
        tf(r'''Xét dao động tắt dần:

a) Biên độ giảm theo thời gian.  
b) Cơ năng cơ học thường giảm do lực cản.  
c) Không có sự chuyển hóa cơ năng sang dạng năng lượng khác.  
d) Giảm chấn ô tô là một ứng dụng có lợi của dao động tắt dần.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: một phần cơ năng chuyển thành nhiệt và các dạng khác.  
d) **Đúng**.'''),
        tf(r'''Xét hiện tượng cộng hưởng:

a) Biên độ cưỡng bức phụ thuộc độ chênh giữa tần số ngoại lực và tần số riêng.  
b) Lực cản càng nhỏ thì đỉnh cộng hưởng thường càng rõ.  
c) Cộng hưởng luôn có lợi.  
d) Thiết kế cầu và máy móc cần xét khả năng cộng hưởng.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: có thể có lợi hoặc có hại.  
d) **Đúng**.'''),
        short(r'''Hai dao động $x_1=3\cos\omega t$ cm và $x_2=4\cos(\omega t+\pi/2)$ cm. Tính biên độ dao động tổng hợp.''', r'''Độ lệch pha $\Delta\varphi=\pi/2$. $A=\sqrt{A_1^2+A_2^2+2A_1A_2\cos\Delta\varphi}=\sqrt{9+16}=5$ cm.'''),
        short(r'''Hai dao động cùng phương có $A_1=A_2=5$ cm và lệch pha $120^\circ$. Tính biên độ tổng hợp.''', r'''$A^2=25+25+50\cos120^\circ=50-25=25$. Vậy $A=5$ cm.'''),
        short(r'''Một hệ có tần số riêng $4$ Hz. Ngoại lực tuần hoàn có thể chọn các tần số $3,5$ Hz; $4,0$ Hz; $5,0$ Hz. Khi lực cản nhỏ, chọn tần số nào để biên độ ổn định lớn nhất?''', r'''Chọn $4,0$ Hz vì bằng tần số riêng, gần điều kiện cộng hưởng.'''),
        applied(r'''Hai dao động cùng phương:

$x_1=4\cos(10t+\pi/6)$ cm, $x_2=3\cos(10t-\pi/3)$ cm.

Tìm biên độ và pha ban đầu của dao động tổng hợp.''', r'''Hai dao động cùng tần số. Tách theo trục cos–sin:

$C=A_1\cos\varphi_1+A_2\cos\varphi_2=4\frac{\sqrt3}{2}+3\frac12=2\sqrt3+\frac32$.

$S=A_1\sin\varphi_1+A_2\sin\varphi_2=4\frac12+3\left(-\frac{\sqrt3}{2}\right)=2-\frac{3\sqrt3}{2}$.

Biên độ:

$A=\sqrt{C^2+S^2}=\sqrt{4^2+3^2+2\cdot4\cdot3\cos(\pi/2)}=5$ cm.

Pha $\varphi$ thỏa $\cos\varphi=C/5$, $\sin\varphi=S/5$. Giá trị gần đúng:

$C\approx4,964$, $S\approx-0,598$ nên $\varphi\approx-0,120$ rad.

Vậy có thể viết $x\approx5\cos(10t-0,120)$ cm.''')
    ]

LESSONS={
'01-harmonic-oscillation-foundations.md': lesson1(),
'02-displacement-velocity-acceleration.md': lesson2(),
'03-phase-circle-time-distance.md': lesson3(),
'04-spring-oscillator.md': lesson4(),
'05-simple-pendulum.md': lesson5(),
'06-oscillation-energy.md': lesson6(),
'07-combined-damped-forced-resonance.md': lesson7(),
}

if __name__=='__main__':
    for lf, probs in LESSONS.items():
        write_lesson_practice(CH, lf, probs)
        add_practice_links(CH, lf)
    write_practice_index(CH, list(LESSONS))
    print('chapter 1', sum(len(v) for v in LESSONS.values()), 'problems')
