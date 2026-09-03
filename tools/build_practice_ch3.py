from practice_bank_common import *
import math

CH='03-electric-field'

def l1():
    return [
        mcq(r'''Một vật trung hòa nhận thêm $5\cdot10^{12}$ electron. Điện tích của vật là

A. $+8,0\cdot10^{-7}$ C.  
B. $-8,0\cdot10^{-7}$ C.  
C. $+3,2\cdot10^{-7}$ C.  
D. $-3,2\cdot10^{-7}$ C.''', r'''Chọn **B**. $q=-Ne=-5\cdot10^{12}\cdot1,6\cdot10^{-19}=-8,0\cdot10^{-7}$ C.'''),
        mcq(r'''Trong quá trình nhiễm điện thông thường của vật rắn, hạt thường dịch chuyển từ vật này sang vật khác là

A. proton.  
B. neutron.  
C. electron.  
D. hạt nhân.''', r'''Chọn **C**. Electron ngoài cùng có thể dịch chuyển; hạt nhân gắn trong mạng vật chất.'''),
        mcq(r'''Một hệ cô lập gồm hai vật có điện tích ban đầu $+3\,\mu$C và $-1\,\mu$C. Sau khi cho tương tác rồi tách ra, tổng điện tích của hệ bằng

A. $-4\,\mu$C.  
B. $-2\,\mu$C.  
C. $+2\,\mu$C.  
D. $+4\,\mu$C.''', r'''Chọn **C**. Tổng điện tích hệ cô lập được bảo toàn: $+3-1=+2\,\mu$C.'''),
        mcq(r'''Vật dẫn điện khác vật cách điện chủ yếu ở chỗ

A. vật dẫn luôn mang điện dương.  
B. vật dẫn có các hạt mang điện tự do có thể dịch chuyển dễ hơn.  
C. vật cách điện không chứa điện tích.  
D. vật dẫn không có electron.''', r'''Chọn **B**.'''),
        tf(r'''Xét các phát biểu về điện tích:

a) Điện tích của electron là âm.  
b) Độ lớn điện tích electron bằng điện tích proton.  
c) Một vật nhiễm điện âm thường là vật thừa electron.  
d) Trong hệ cô lập, tổng đại số điện tích có thể tự tăng lên mà không có trao đổi với bên ngoài.''', r'''a) **Đúng**.  
b) **Đúng** về độ lớn.  
c) **Đúng**.  
d) **Sai** theo định luật bảo toàn điện tích.'''),
        tf(r'''Về các cách nhiễm điện:

a) Cọ xát có thể làm electron chuyển từ vật này sang vật kia.  
b) Tiếp xúc với vật nhiễm điện có thể làm điện tích phân bố lại.  
c) Hưởng ứng đòi hỏi bắt buộc hai vật chạm nhau.  
d) Sau hưởng ứng, điện tích trong vật dẫn có thể phân bố không đều.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: hưởng ứng xảy ra do tác dụng điện từ xa, không cần tiếp xúc.  
d) **Đúng**.'''),
        short(r'''Một vật mất $2,5\cdot10^{13}$ electron. Tính điện tích của vật.''', r'''Mất electron nên vật dương: $q=Ne=2,5\cdot10^{13}\cdot1,6\cdot10^{-19}=4,0\cdot10^{-6}$ C $=4\,\mu$C.'''),
        short(r'''Điện tích của một vật là $-3,2\cdot10^{-8}$ C. Vật thừa bao nhiêu electron?''', r'''$N=|q|/e=3,2\cdot10^{-8}/1,6\cdot10^{-19}=2,0\cdot10^{11}$ electron.'''),
        short(r'''Hai quả cầu kim loại giống nhau mang điện $q_1=+8\,\mu$C và $q_2=-2\,\mu$C. Cho tiếp xúc rồi tách xa. Bỏ qua mất mát điện tích. Tính điện tích mỗi quả cầu sau cùng.''', r'''Tổng điện tích $Q=+6\,\mu$C. Hai quả cầu giống nhau nên sau tiếp xúc điện tích chia đều: $q'_1=q'_2=Q/2=+3\,\mu$C.'''),
        applied(r'''Ba quả cầu kim loại giống nhau A, B, C có điện tích ban đầu lần lượt $+6\,\mu$C, $0$, $-3\,\mu$C. Cho A tiếp xúc B rồi tách ra; sau đó cho B tiếp xúc C rồi tách ra. Tính điện tích cuối cùng của A, B, C.''', r'''Lần 1, A và B giống nhau nên chia đều tổng $6\,\mu$C: $q_A=q_B=3\,\mu$C.

Lần 2, B có $+3\,\mu$C tiếp xúc C có $-3\,\mu$C. Tổng bằng 0 nên sau khi tách: $q_B=q_C=0$.

A không tham gia lần 2 nên vẫn $+3\,\mu$C.

Kết quả: $q_A=+3\,\mu$C, $q_B=0$, $q_C=0$. Tổng cuối vẫn $+3\,\mu$C, đúng bằng tổng ban đầu.''')
    ]

def l2():
    return [
        mcq(r'''Hai điện tích điểm $q_1=2\,\mu$C, $q_2=3\,\mu$C cách nhau $0,30$ m trong chân không. Lấy $k=9\cdot10^9$. Lực Coulomb có độ lớn

A. $0,2$ N.  
B. $0,4$ N.  
C. $0,6$ N.  
D. $1,8$ N.''', r'''Chọn **C**. $F=kq_1q_2/r^2=9\cdot10^9\cdot6\cdot10^{-12}/0,09=0,6$ N.'''),
        mcq(r'''Nếu khoảng cách giữa hai điện tích điểm tăng 3 lần, các điện tích không đổi, lực Coulomb

A. tăng 3 lần.  
B. giảm 3 lần.  
C. giảm 9 lần.  
D. tăng 9 lần.''', r'''Chọn **C** vì $F\propto1/r^2$.'''),
        mcq(r'''Hai điện tích cùng dấu đặt gần nhau sẽ

A. hút nhau.  
B. đẩy nhau.  
C. không tương tác.  
D. chỉ tương tác nếu cùng độ lớn.''', r'''Chọn **B**.'''),
        mcq(r'''Trong điện môi có hằng số điện môi tương đối $\varepsilon_r=4$, lực giữa hai điện tích so với chân không giảm

A. 2 lần.  
B. 4 lần.  
C. 8 lần.  
D. 16 lần.''', r'''Chọn **B** trong mô hình $F=F_0/\varepsilon_r$.'''),
        tf(r'''Về lực Coulomb giữa hai điện tích điểm:

a) Hai lực tác dụng lên hai điện tích có cùng độ lớn và ngược hướng.  
b) Lực nằm trên đường thẳng nối hai điện tích.  
c) Độ lớn tỉ lệ với tích độ lớn hai điện tích.  
d) Đổi đồng thời dấu cả hai điện tích làm độ lớn lực thay đổi.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: tích độ lớn không đổi; tính hút/đẩy cũng không đổi vì quan hệ cùng dấu/trái dấu giữ nguyên.'''),
        tf(r'''Hai điện tích điểm cách nhau $r$:

a) Nếu một điện tích tăng 2 lần thì lực tăng 2 lần.  
b) Nếu cả hai điện tích tăng 2 lần thì lực tăng 4 lần.  
c) Nếu $r$ giảm một nửa thì lực tăng 2 lần.  
d) Nếu $r$ giảm một nửa thì lực tăng 4 lần.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**.  
d) **Đúng**.'''),
        short(r'''Hai điện tích $+4\,\mu$C và $-5\,\mu$C cách nhau $20$ cm trong chân không. Tính độ lớn lực và cho biết hút hay đẩy.''', r'''$F=9\cdot10^9\cdot(4\cdot10^{-6})(5\cdot10^{-6})/0,20^2=4,5$ N. Hai điện tích trái dấu nên hút nhau.'''),
        short(r'''Hai điện tích bằng nhau đặt cách nhau $10$ cm trong chân không đẩy nhau lực $0,90$ N. Tính độ lớn mỗi điện tích.''', r'''$F=kq^2/r^2$ nên $q=\sqrt{Fr^2/k}=\sqrt{0,90\cdot0,10^2/(9\cdot10^9)}=10^{-6}$ C $=1\,\mu$C.'''),
        short(r'''Lực giữa hai điện tích trong chân không là $1,2$ N. Đưa nguyên hệ vào điện môi, giữ khoảng cách, lực còn $0,30$ N. Tính hằng số điện môi tương đối.''', r'''$F=F_0/\varepsilon_r$ nên $\varepsilon_r=1,2/0,30=4$.'''),
        applied(r'''Ba điện tích đặt thẳng hàng: $q_A=+2\,\mu$C tại A, $q_B=+1\,\mu$C tại B, $q_C=-4\,\mu$C tại C. Biết AB=$0,20$ m, BC=$0,30$ m. Tính lực tổng hợp tác dụng lên $q_B$ trong chân không.''', r'''Lực của A lên B: cùng dấu nên đẩy B sang phải.

$F_{AB}=k|q_Aq_B|/AB^2=9\cdot10^9\cdot2\cdot10^{-12}/0,04=0,45$ N.

Lực của C lên B: trái dấu nên hút B về C, cũng sang phải.

$F_{CB}=9\cdot10^9\cdot4\cdot10^{-12}/0,09=0,40$ N.

Hai lực cùng chiều nên $F=0,45+0,40=0,85$ N, hướng từ B về C.''')
    ]

def l3():
    return [
        mcq(r'''Cường độ điện trường tại một điểm được xác định bởi

A. $\vec E=\vec F/q$ với điện tích thử dương đủ nhỏ.  
B. $E=q/F$.  
C. $E=Fr^2$.  
D. $E=Uq$.''', r'''Chọn **A** về định nghĩa vectơ.'''),
        mcq(r'''Điện trường của điện tích điểm dương có chiều

A. hướng vào điện tích.  
B. hướng ra xa điện tích.  
C. tiếp tuyến vòng tròn quanh điện tích.  
D. không xác định.''', r'''Chọn **B**.'''),
        mcq(r'''Điện tích điểm $Q=+4\,\mu$C. Tại điểm cách Q $0,30$ m trong chân không, cường độ điện trường bằng

A. $4\cdot10^4$ V/m.  
B. $4\cdot10^5$ V/m.  
C. $4\cdot10^6$ V/m.  
D. $1,2\cdot10^5$ V/m.''', r'''Chọn **B**. $E=kQ/r^2=9\cdot10^9\cdot4\cdot10^{-6}/0,09=4\cdot10^5$ V/m.'''),
        mcq(r'''Đơn vị nào tương đương với đơn vị cường độ điện trường?

A. N/C.  
B. C/N.  
C. J/C².  
D. W/A.''', r'''Chọn **A**; cũng có thể dùng V/m.'''),
        tf(r'''Đường sức điện:

a) Có hướng trùng hướng vectơ cường độ điện trường tại mỗi điểm.  
b) Các đường sức tĩnh điện không cắt nhau.  
c) Mật độ đường sức dày hơn thường biểu diễn điện trường mạnh hơn.  
d) Đường sức của điện tích điểm âm hướng ra xa điện tích.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng** về cách biểu diễn.  
d) **Sai**: hướng vào điện tích âm.'''),
        tf(r'''Xét cường độ điện trường do điện tích điểm Q:

a) $E\propto|Q|$.  
b) $E\propto1/r^2$.  
c) Độ lớn E phụ thuộc điện tích thử đặt tại điểm xét.  
d) Nếu Q đổi dấu thì độ lớn E không đổi nhưng hướng đảo.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai** trong định nghĩa điện trường nguồn; điện tích thử chỉ dùng để thăm dò.  
d) **Đúng**.'''),
        short(r'''Điện tích $Q=-2\,\mu$C. Tính cường độ điện trường tại điểm cách Q $15$ cm trong chân không và nêu hướng.''', r'''$E=9\cdot10^9\cdot2\cdot10^{-6}/0,15^2=8,0\cdot10^5$ V/m. Vì Q âm, vectơ $\vec E$ hướng từ điểm xét về Q.'''),
        short(r'''Tại một điểm, điện tích thử $q=+2$ nC chịu lực điện $6\cdot10^{-5}$ N theo hướng Đông. Tính $\vec E$.''', r'''$E=F/q=6\cdot10^{-5}/(2\cdot10^{-9})=3\cdot10^4$ V/m. Vì q dương, $\vec E$ cùng chiều lực: hướng Đông.'''),
        short(r'''Điện trường đều có $E=500$ V/m. Điện tích $q=-4\,\mu$C đặt trong trường chịu lực điện có độ lớn bao nhiêu và hướng thế nào so với $\vec E$?''', r'''$F=|q|E=4\cdot10^{-6}\cdot500=2\cdot10^{-3}$ N. Vì q âm, lực ngược chiều $\vec E$.'''),
        applied(r'''Một điện tích điểm Q tạo cường độ điện trường $E_1=9\cdot10^4$ V/m tại điểm cách nó $20$ cm. Tính cường độ tại điểm cách Q $30$ cm và độ lớn Q.''', r'''Vì $E\propto1/r^2$:

$E_2=E_1(r_1/r_2)^2=9\cdot10^4(0,20/0,30)^2=4\cdot10^4$ V/m.

Từ $E_1=k|Q|/r_1^2$:

$|Q|=E_1r_1^2/k=9\cdot10^4\cdot0,04/(9\cdot10^9)=4\cdot10^{-7}$ C $=0,4\,\mu$C.''')
    ]

def l4():
    return [
        mcq(r'''Nguyên lí chồng chất điện trường phát biểu

A. cường độ tổng hợp bằng tổng đại số mọi độ lớn.  
B. vectơ cường độ tổng hợp bằng tổng vectơ các cường độ thành phần.  
C. chỉ áp dụng cho hai điện tích.  
D. điện trường không thể tổng hợp.''', r'''Chọn **B**.'''),
        mcq(r'''Hai vectơ điện trường vuông góc có độ lớn $E_1=3$ kV/m và $E_2=4$ kV/m. Điện trường tổng hợp có độ lớn

A. $1$ kV/m.  
B. $5$ kV/m.  
C. $7$ kV/m.  
D. $12$ kV/m.''', r'''Chọn **B** theo định lí Pythagore.'''),
        mcq(r'''Hai điện tích dương bằng nhau đặt tại A và B. Tại trung điểm M của AB, cường độ điện trường tổng hợp bằng

A. 0.  
B. gấp đôi điện trường của một điện tích.  
C. vô hạn.  
D. không xác định.''', r'''Chọn **A** vì hai vectơ bằng nhau và ngược hướng.'''),
        mcq(r'''Hai điện tích trái dấu có độ lớn bằng nhau đặt tại A và B. Tại trung điểm M, hai vectơ điện trường do chúng gây ra

A. ngược chiều nên triệt tiêu.  
B. cùng chiều từ điện tích dương sang điện tích âm.  
C. vuông góc nhau.  
D. bằng 0 từng vectơ.''', r'''Chọn **B**, nên điện trường tổng hợp khác 0.'''),
        tf(r'''Về điểm có điện trường tổng hợp bằng 0 do hai điện tích điểm:

a) Với hai điện tích cùng dấu, điểm cân bằng có thể nằm giữa chúng.  
b) Với hai điện tích trái dấu, điểm E=0 không nằm giữa hai điện tích.  
c) Nếu hai điện tích cùng dấu bằng nhau, trung điểm là điểm E=0.  
d) Chỉ cần độ lớn hai điện trường bằng nhau, không cần xét hướng.''', r'''a) **Đúng**.  
b) **Đúng** trong bài toán trên đường nối hai điện tích.  
c) **Đúng**.  
d) **Sai**: để tổng vectơ bằng 0 cần hai vectơ cùng phương, ngược chiều và cùng độ lớn.'''),
        tf(r'''Hai điện trường thành phần $\vec E_1,\vec E_2$ có cùng độ lớn E:

a) Cùng chiều thì $E_{tổng}=2E$.  
b) Ngược chiều thì $E_{tổng}=0$.  
c) Vuông góc thì $E_{tổng}=E\sqrt2$.  
d) Hợp góc $120^\circ$ thì $E_{tổng}=2E$.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: $E_t^2=E^2+E^2+2E^2\cos120^\circ=E^2$, nên $E_t=E$.'''),
        short(r'''Hai điện trường thành phần có $E_1=6$ kV/m, $E_2=8$ kV/m và vuông góc. Tính độ lớn điện trường tổng hợp.''', r'''$E=\sqrt{6^2+8^2}=10$ kV/m.'''),
        short(r'''Hai điện tích dương $q_1=4\,\mu$C, $q_2=1\,\mu$C cách nhau $30$ cm. Tìm vị trí trên đoạn nối hai điện tích nơi điện trường tổng hợp bằng 0.''', r'''Gọi điểm M giữa hai điện tích, cách $q_1$ một đoạn x. Hai điện trường ngược chiều và cần bằng nhau:

$kq_1/x^2=kq_2/(0,30-x)^2$.

$\sqrt{q_1}/x=\sqrt{q_2}/(0,30-x)$, tức $2/x=1/(0,30-x)$.

$0,60-2x=x$ nên $x=0,20$ m. M cách $q_1$ 20 cm, cách $q_2$ 10 cm, tức gần điện tích nhỏ hơn.'''),
        short(r'''Tại một điểm, hai vectơ điện trường có độ lớn $5$ kV/m và hợp nhau góc $60^\circ$. Tính độ lớn tổng hợp.''', r'''$E=\sqrt{E_1^2+E_2^2+2E_1E_2\cos60^\circ}=5\sqrt3$ kV/m $\approx8,66$ kV/m.'''),
        applied(r'''Hai điện tích $q_1=+9\,\mu$C tại A và $q_2=-4\,\mu$C tại B, AB=$50$ cm. Tìm điểm trên đường thẳng AB nơi điện trường tổng hợp bằng 0.''', r'''Giữa A và B, hai điện trường cùng chiều từ dương sang âm nên không thể triệt tiêu.

Điểm E=0 phải ở ngoài đoạn AB và gần điện tích có độ lớn nhỏ hơn, tức phía ngoài B.

Gọi khoảng cách từ điểm M đến B là x, khi đó đến A là $x+0,50$ m. Hai điện trường ngược chiều và bằng nhau:

$9/(x+0,50)^2=4/x^2$.

Lấy căn dương: $3/(x+0,50)=2/x$.

$3x=2x+1,0$ nên $x=1,0$ m.

Vậy M nằm phía ngoài B, cách B $1,0$ m.''')
    ]

def l5():
    return [
        mcq(r'''Công của lực điện khi điện tích q di chuyển từ M đến N trong điện trường tĩnh có thể viết

A. $A_{MN}=q(V_M-V_N)$.  
B. $A_{MN}=q(V_N-V_M)$.  
C. $A_{MN}=V_MV_N/q$.  
D. $A_{MN}=q(V_M+V_N)$.''', r'''Chọn **A** với quy ước $U_{MN}=V_M-V_N$.'''),
        mcq(r'''Đơn vị điện thế là

A. N/C.  
B. J/C.  
C. C/J.  
D. N·m²/C².''', r'''Chọn **B**, tên riêng là vôn (V).'''),
        mcq(r'''Điện tích dương chuyển động tự do theo chiều đường sức điện trong điện trường tĩnh. Điện thế của nó thường

A. tăng.  
B. giảm.  
C. không đổi.  
D. luôn bằng 0.''', r'''Chọn **B**: chiều $\vec E$ là chiều điện thế giảm.'''),
        mcq(r'''Trong điện trường đều, nếu hai điểm cách nhau d theo đúng chiều điện trường thì

A. $V_M-V_N=Ed$ khi M ở phía trước theo ngược chiều E và N ở phía sau theo chiều E.  
B. hiệu điện thế luôn bằng 0.  
C. $U=E/d$.  
D. $E=Ud$.''', r'''Chọn **A** với cách đặt M ở phía điện thế cao hơn và N theo chiều $\vec E$.'''),
        tf(r'''Xét công của lực điện trong điện trường tĩnh:

a) Chỉ phụ thuộc vị trí đầu và cuối, không phụ thuộc đường đi.  
b) Trên đường kín, tổng công bằng 0.  
c) Nếu q dương đi từ nơi điện thế cao xuống thấp, lực điện thực hiện công dương.  
d) Thế năng điện luôn dương.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng** vì $A=q(V_M-V_N)>0$.  
d) **Sai**: dấu thế năng phụ thuộc mốc và hệ điện tích.'''),
        tf(r'''Về điện thế và hiệu điện thế:

a) Điện thế là đại lượng vô hướng.  
b) Hiệu điện thế $U_{MN}=V_M-V_N$.  
c) $1$ V = $1$ J/C.  
d) Cường độ điện trường đều có thể tính $E=U/d$ nếu d là khoảng cách theo phương vuông góc đường sức.''', r'''a) **Đúng**.  
b) **Đúng** theo quy ước đang dùng.  
c) **Đúng**.  
d) **Sai**: $d$ phải là độ dịch chuyển theo phương điện trường giữa hai mặt đẳng thế tương ứng.'''),
        short(r'''Điện tích $q=2\,\mu$C đi từ điểm M có điện thế $120$ V đến N có điện thế $20$ V. Tính công của lực điện.''', r'''$A=q(V_M-V_N)=2\cdot10^{-6}(120-20)=2\cdot10^{-4}$ J.'''),
        short(r'''Hai bản phẳng tạo điện trường đều $E=2\cdot10^4$ V/m, cách nhau $5$ mm. Tính hiệu điện thế giữa hai bản.''', r'''$U=Ed=2\cdot10^4\cdot5\cdot10^{-3}=100$ V.'''),
        short(r'''Một electron đi qua hiệu điện thế tăng thêm về độ lớn $200$ V và được gia tốc từ nghỉ. Tính độ tăng động năng theo eV.''', r'''Độ tăng động năng của electron qua hiệu điện thế 200 V là $200$ eV. Nếu đổi sang J: $200\cdot1,6\cdot10^{-19}=3,2\cdot10^{-17}$ J.'''),
        applied(r'''Trong điện trường đều $E=500$ V/m hướng theo trục Ox dương. Điểm M có tọa độ $x_M=0,20$ m, điểm N có $x_N=0,70$ m. Tính $V_M-V_N$ và công của lực điện khi điện tích $q=-4\,\mu$C đi từ M đến N.''', r'''N nằm theo chiều điện trường so với M, nên điện thế giảm:

$V_M-V_N=E(x_N-x_M)=500(0,70-0,20)=250$ V.

Công lực điện:

$A_{MN}=q(V_M-V_N)=-4\cdot10^{-6}\cdot250=-1,0\cdot10^{-3}$ J.

Dấu âm phù hợp: điện tích âm đi theo chiều điện trường thì lực điện hướng ngược chuyển động, nên lực điện thực hiện công âm.''')
    ]

def l6():
    return [
        mcq(r'''Điện dung của tụ điện được xác định bởi

A. $C=Q/U$.  
B. $C=U/Q$.  
C. $C=QU$.  
D. $C=Q^2/U$.''', r'''Chọn **A**.'''),
        mcq(r'''Tụ $5\,\mu$F được đặt dưới hiệu điện thế $12$ V. Điện tích của tụ là

A. $0,42\,\mu$C.  
B. $17\,\mu$C.  
C. $60\,\mu$C.  
D. $240\,\mu$C.''', r'''Chọn **C**. $Q=CU=5\cdot12=60\,\mu$C.'''),
        mcq(r'''Năng lượng của tụ có thể viết

A. $W=CU^2$.  
B. $W=\frac12CU^2$.  
C. $W=Q/U$.  
D. $W=2QU$.''', r'''Chọn **B**.'''),
        mcq(r'''Điện dung tụ phẳng tăng khi

A. tăng khoảng cách hai bản.  
B. giảm diện tích đối diện.  
C. tăng hằng số điện môi giữa hai bản.  
D. giảm hằng số điện môi.''', r'''Chọn **C** vì $C=\varepsilon_0\varepsilon_r S/d$.'''),
        tf(r'''Xét một tụ điện lí tưởng:

a) Đơn vị điện dung là fara.  
b) Với cấu tạo không đổi, C không phụ thuộc Q và U trong miền tuyến tính.  
c) Khi nối với nguồn áp không đổi, tăng C làm Q tăng.  
d) Năng lượng của tụ luôn bằng $QU$.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng** vì $Q=CU$.  
d) **Sai**: $W=QU/2$.'''),
        tf(r'''Tụ phẳng có diện tích bản S và khoảng cách d:

a) $C\propto S$.  
b) $C\propto1/d$.  
c) Đưa điện môi có $\varepsilon_r>1$ lấp đầy khe làm C tăng.  
d) Giữ Q không đổi mà C tăng thì U tăng.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: $U=Q/C$ nên U giảm.'''),
        short(r'''Tụ $20\,\mu$F tích điện đến $30$ V. Tính điện tích và năng lượng.''', r'''$Q=CU=20\cdot10^{-6}\cdot30=600\,\mu$C. $W=\frac12CU^2=0,5\cdot20\cdot10^{-6}\cdot900=9\cdot10^{-3}$ J.'''),
        short(r'''Một tụ có điện tích $Q=80\,\mu$C khi hiệu điện thế $U=20$ V. Tính điện dung.''', r'''$C=Q/U=(80\,\mu\text{C})/(20\,\text{V})=4\,\mu\text{F}$.'''),
        short(r'''Tụ phẳng trong chân không có diện tích mỗi bản $200$ cm², khoảng cách $1$ mm. Lấy $\varepsilon_0=8,85\cdot10^{-12}$ F/m. Tính C.''', r'''Đổi $S=200$ cm² $=0,02$ m², $d=10^{-3}$ m. $C=\varepsilon_0S/d=8,85\cdot10^{-12}\cdot0,02/10^{-3}=1,77\cdot10^{-10}$ F $=177$ pF.'''),
        applied(r'''Tụ $C=10\,\mu$F nối với nguồn $U=100$ V. Sau khi tích điện, ngắt khỏi nguồn rồi tăng khoảng cách hai bản lên gấp đôi, bỏ qua mép. Tính Q, U mới và năng lượng mới.''', r'''Trước khi ngắt: $Q=CU=10\,\mu$F$\cdot100$ V $=1,0$ mC.

Sau khi ngắt, tụ cô lập nên **Q bảo toàn**. Tăng khoảng cách gấp đôi làm $C'=C/2=5\,\mu$F.

$U'=Q/C'=1,0\cdot10^{-3}/(5\cdot10^{-6})=200$ V.

Năng lượng mới $W'=Q^2/(2C')=0,1$ J. Ban đầu $W=\frac12CU^2=0,05$ J. Năng lượng tăng vì ngoại lực thực hiện công khi kéo hai bản xa nhau.''')
    ]

def l7():
    return [
        mcq(r'''Hạt mang điện q trong điện trường đều chịu gia tốc có độ lớn

A. $a=|q|E/m$.  
B. $a=mE/|q|$.  
C. $a=|q|/(mE)$.  
D. $a=E$.''', r'''Chọn **A** khi chỉ xét lực điện.'''),
        mcq(r'''Electron đặt trong điện trường đều có gia tốc

A. cùng chiều $\vec E$.  
B. ngược chiều $\vec E$.  
C. vuông góc $\vec E$.  
D. bằng 0.''', r'''Chọn **B** vì electron mang điện âm.'''),
        mcq(r'''Một proton và một electron cùng đặt trong cùng điện trường đều. Bỏ qua trọng lực. Độ lớn lực điện trên chúng

A. bằng nhau.  
B. lực proton lớn hơn rất nhiều.  
C. lực electron lớn hơn rất nhiều.  
D. đều bằng 0.''', r'''Chọn **A** vì $|q_p|=|q_e|=e$. Gia tốc khác nhau do khối lượng khác.'''),
        mcq(r'''Điện tích dương bay vào điện trường đều với vận tốc ban đầu vuông góc $\vec E$. Quỹ đạo trong miền điện trường đều lý tưởng có dạng

A. đường thẳng.  
B. đường tròn.  
C. parabol.  
D. elip.''', r'''Chọn **C**, tương tự chuyển động ném ngang với gia tốc không đổi theo phương điện trường.'''),
        tf(r'''Chuyển động hạt mang điện trong điện trường đều:

a) Lực điện không đổi nếu E không đổi.  
b) Gia tốc không đổi nếu q, m không đổi.  
c) Hạt bay song song E luôn chuyển động đều.  
d) Nếu vận tốc đầu vuông góc E, một thành phần chuyển động là đều và thành phần kia biến đổi đều.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai** trừ trường hợp q=0; hạt mang điện chịu gia tốc.  
d) **Đúng**.'''),
        tf(r'''Một electron được tăng tốc từ nghỉ qua hiệu điện thế U:

a) Độ tăng động năng có độ lớn $eU$.  
b) Tốc độ có thể tìm từ $\frac12mv^2=eU$ nếu phi tương đối tính.  
c) Tăng U gấp 4 lần thì v tăng 4 lần trong mô hình cổ điển.  
d) Tăng U gấp 4 lần thì v tăng 2 lần trong mô hình cổ điển.''', r'''a) **Đúng**.  
b) **Đúng** trong miền vận tốc không tương đối tính.  
c) **Sai**.  
d) **Đúng** vì $v\propto\sqrt U$.'''),
        short(r'''Hạt có $q=2\,\mu$C, $m=4\cdot10^{-6}$ kg trong điện trường $E=3000$ V/m. Tính gia tốc.''', r'''$a=qE/m=2\cdot10^{-6}\cdot3000/(4\cdot10^{-6})=1500$ m/s², cùng chiều E vì q dương.'''),
        short(r'''Electron được tăng tốc từ nghỉ qua hiệu điện thế $100$ V. Lấy $e=1,6\cdot10^{-19}$ C, $m_e=9,1\cdot10^{-31}$ kg. Tính tốc độ theo cơ học cổ điển.''', r'''$\frac12m_ev^2=eU$. $v=\sqrt{2eU/m_e}=\sqrt{2\cdot1,6\cdot10^{-19}\cdot100/(9,1\cdot10^{-31})}\approx5,93\cdot10^6$ m/s.'''),
        short(r'''Điện tích dương đi vào điện trường đều $E=2\cdot10^4$ V/m với vận tốc đầu $v_0=10^5$ m/s vuông góc E. Biết $q/m=10^7$ C/kg, chiều dài vùng điện trường theo phương v0 là $5$ cm. Tính thời gian ở trong trường.''', r'''Chuyển động theo phương $v_0$ là đều: $t=L/v_0=0,05/10^5=5\cdot10^{-7}$ s.'''),
        applied(r'''Tiếp câu trên, tính độ lệch theo phương điện trường khi hạt ra khỏi vùng điện trường và vận tốc theo phương E lúc đó.''', r'''Gia tốc theo E: $a=(q/m)E=10^7\cdot2\cdot10^4=2\cdot10^{11}$ m/s².

Thời gian $t=5\cdot10^{-7}$ s.

Độ lệch:

$y=\frac12at^2=0,5\cdot2\cdot10^{11}(5\cdot10^{-7})^2=0,025$ m $=2,5$ cm.

Thành phần vận tốc theo E khi ra: $v_y=at=2\cdot10^{11}\cdot5\cdot10^{-7}=10^5$ m/s.

Thành phần dọc ban đầu vẫn $v_x=10^5$ m/s.''')
    ]

def l8():
    return [
        mcq(r'''Hai tụ $C_1=3\,\mu$F, $C_2=6\,\mu$F mắc song song. Điện dung tương đương là

A. $2\,\mu$F.  
B. $3\,\mu$F.  
C. $9\,\mu$F.  
D. $18\,\mu$F.''', r'''Chọn **C**. Song song: $C_b=C_1+C_2$.'''),
        mcq(r'''Hai tụ $3\,\mu$F và $6\,\mu$F mắc nối tiếp. Điện dung tương đương là

A. $2\,\mu$F.  
B. $3\,\mu$F.  
C. $9\,\mu$F.  
D. $18\,\mu$F.''', r'''Chọn **A**. $C_b=C_1C_2/(C_1+C_2)=18/9=2\,\mu$F.'''),
        mcq(r'''Trong mạch hai tụ nối tiếp đã ổn định, độ lớn điện tích trên mỗi tụ

A. luôn bằng nhau nếu nút giữa cô lập ban đầu trung hòa.  
B. tỉ lệ điện dung.  
C. luôn bằng 0.  
D. bằng hiệu điện thế.''', r'''Chọn **A** trong cấu hình nối tiếp chuẩn.'''),
        mcq(r'''Hai tụ song song đặt cùng hiệu điện thế U. Tụ có điện dung lớn hơn sẽ

A. có điện tích nhỏ hơn.  
B. có điện tích lớn hơn.  
C. có điện tích bằng nhau bắt buộc.  
D. không tích điện.''', r'''Chọn **B** vì $Q=CU$.'''),
        tf(r'''Ghép tụ điện:

a) Song song: hiệu điện thế trên các tụ bằng nhau.  
b) Nối tiếp chuẩn: độ lớn điện tích trên các tụ bằng nhau.  
c) Điện dung tương đương nối tiếp lớn hơn mọi điện dung thành phần.  
d) Điện dung tương đương song song bằng tổng các điện dung.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: nhỏ hơn điện dung nhỏ nhất.  
d) **Đúng**.'''),
        tf(r'''Một tụ cô lập sau khi ngắt khỏi nguồn:

a) Tổng điện tích trên mỗi bản được bảo toàn nếu không rò điện.  
b) Thay đổi điện dung có thể làm hiệu điện thế thay đổi.  
c) Nếu C tăng mà Q giữ nguyên thì năng lượng $Q^2/(2C)$ giảm.  
d) Q luôn bằng CU với U không đổi bất kể thao tác.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: U không nhất thiết không đổi khi đã ngắt nguồn.'''),
        short(r'''Hai tụ $4\,\mu$F và $12\,\mu$F mắc nối tiếp vào $32$ V. Tính điện tích trên mỗi tụ và hiệu điện thế mỗi tụ.''', r'''$C_b=4\cdot12/(4+12)=3\,\mu$F. $Q=C_bU=96\,\mu$C. Nối tiếp nên mỗi tụ có $|Q|=96\,\mu$C. $U_1=96/4=24$ V; $U_2=96/12=8$ V.'''),
        short(r'''Hai tụ $2\,\mu$F và $3\,\mu$F mắc song song vào $20$ V. Tính điện tích từng tụ và tổng năng lượng.''', r'''$Q_1=C_1U=40\,\mu$C; $Q_2=60\,\mu$C. $C_b=5\,\mu$F. $W=\frac12C_bU^2=0,5\cdot5\cdot10^{-6}\cdot400=1,0\cdot10^{-3}$ J.'''),
        short(r'''Tụ $C_1=6\,\mu$F tích đến $12$ V rồi ngắt nguồn. Nối song song với tụ $C_2=3\,\mu$F ban đầu chưa tích điện, cùng cực tính. Tính hiệu điện thế cuối.''', r'''Điện tích tổng bảo toàn: $Q_{tot}=C_1U_1=72\,\mu$C. Sau nối song song, $C_{tot}=9\,\mu$F. $U_f=Q_{tot}/C_{tot}=8$ V.'''),
        applied(r'''Hai tụ $C_1=4\,\mu$F và $C_2=6\,\mu$F được tích riêng đến cùng hiệu điện thế $U=10$ V. Sau đó ngắt nguồn và nối bản dương của tụ 1 với bản âm của tụ 2, hai bản còn lại nối với nhau. Tính hiệu điện thế cuối về độ lớn.''', r'''Đây là nối song song **ngược cực tính**. Chọn chiều điện tích dương của tụ 1 là dương. Điện tích đại số ban đầu trên nút nối tương ứng:

$Q_{net}=C_1U-C_2U=(4-6)\cdot10=-20\,\mu$C.

Sau khi nối, hai tụ có cùng độ lớn hiệu điện thế cuối và tổng điện dung $C_1+C_2=10\,\mu$F.

$U_f=|Q_{net}|/(C_1+C_2)=20/10=2$ V.

Chiều cực tính cuối theo tụ 2 vì $C_2U>C_1U$.''')
    ]

def l9():
    return [
        mcq(r'''Một quả cầu nhỏ khối lượng m, điện tích dương q treo bằng dây trong điện trường đều nằm ngang E. Ở cân bằng, dây lệch góc θ so với phương thẳng đứng. Hệ thức đúng là

A. $\tan\theta=mg/(qE)$.  
B. $\tan\theta=qE/(mg)$.  
C. $\sin\theta=qE/(mg)$ luôn đúng.  
D. $\tan\theta=q/(mE)$.''', r'''Chọn **B** từ cân bằng hai thành phần lực: $T\sin\theta=qE$, $T\cos\theta=mg$.'''),
        mcq(r'''Nếu q âm trong điện trường ngang hướng sang phải, quả cầu cân bằng lệch về

A. bên phải.  
B. bên trái.  
C. không lệch.  
D. lên trên.''', r'''Chọn **B** vì lực điện ngược chiều E.'''),
        mcq(r'''Trong điện trường đều thẳng đứng cùng chiều trọng lực, điện tích dương chịu gia tốc hiệu dụng về độ lớn

A. $g-qE/m$.  
B. $g+qE/m$.  
C. $qE/(mg)$.  
D. luôn bằng g.''', r'''Chọn **B** nếu lực điện cùng chiều trọng lực.'''),
        mcq(r'''Hai điện tích dương giống nhau treo đối xứng bằng hai sợi dây. Khi điện tích tăng, các yếu tố khác giữ nguyên, góc lệch cân bằng thường

A. giảm.  
B. tăng.  
C. không đổi.  
D. bằng 0.''', r'''Chọn **B** vì lực đẩy Coulomb tăng.'''),
        tf(r'''Con lắc tích điện trong điện trường đều ngang:

a) Ở cân bằng, tổng lực bằng 0.  
b) Có thể gộp trọng lực và lực điện thành một “trọng lực hiệu dụng” về mặt động lực học.  
c) Nếu E ngang thì $g_{hiệu}=g+qE/m$ theo đại số một chiều.  
d) Dấu điện tích quyết định phía lệch.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: hai gia tốc vuông góc nên $g_{hiệu}=\sqrt{g^2+(qE/m)^2}$.  
d) **Đúng**.'''),
        tf(r'''Hai quả cầu nhỏ giống nhau tích điện cùng dấu, treo đối xứng:

a) Lực Coulomb là lực đẩy.  
b) Ở cân bằng, thành phần ngang của lực căng cân bằng lực Coulomb.  
c) Có thể bỏ trọng lực khi tính góc lệch mà không cần điều kiện.  
d) Khoảng cách giữa hai quả cầu phụ thuộc chiều dài dây và góc lệch.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**.  
d) **Đúng**.'''),
        short(r'''Quả cầu $m=20$ g, $q=2\,\mu$C treo trong điện trường ngang $E=5\cdot10^4$ V/m. Lấy $g=10$ m/s². Tính góc lệch cân bằng.''', r'''$qE=2\cdot10^{-6}\cdot5\cdot10^4=0,10$ N; $mg=0,20$ N. $\tan\theta=qE/(mg)=0,5$, nên $\theta\approx26,6^\circ$.'''),
        short(r'''Với dữ kiện trên, tính lực căng dây ở cân bằng.''', r'''$T=\sqrt{(mg)^2+(qE)^2}=\sqrt{0,20^2+0,10^2}=0,224$ N.'''),
        short(r'''Một con lắc tích điện dương đặt trong điện trường thẳng đứng hướng xuống, $qE/m=2$ m/s², $g=10$ m/s². Tính chu kì góc nhỏ nếu $\ell=0,75$ m.''', r'''Gia tốc hiệu dụng $g'=g+qE/m=12$ m/s². $T=2\pi\sqrt{\ell/g'}=2\pi\sqrt{0,75/12}=2\pi\cdot0,25=\pi/2\approx1,57$ s.'''),
        applied(r'''Hai quả cầu nhỏ giống nhau, mỗi quả có khối lượng $m=10$ g và điện tích $q=0,20\,\mu$C, treo từ cùng một điểm bằng hai dây dài $\ell=0,50$ m. Ở cân bằng mỗi dây lệch góc nhỏ θ so với phương thẳng đứng. Lấy $g=10$ m/s², $k=9\cdot10^9$. Dùng gần đúng $\sin\theta\approx\tan\theta\approx\theta$ để ước tính θ.''', r'''Khoảng cách hai quả cầu với góc nhỏ: $r\approx2\ell\theta$.

Lực đẩy Coulomb:

$F_e=kq^2/r^2\approx kq^2/(4\ell^2\theta^2)$.

Cân bằng theo phương ngang: $mg\tan\theta\approx mg\theta=F_e$.

Suy ra

$mg\theta=\frac{kq^2}{4\ell^2\theta^2}$,

$\theta^3=\frac{kq^2}{4mg\ell^2}$.

Thay số: $q=2\cdot10^{-7}$ C, $m=0,01$ kg, $\ell=0,5$ m:

$\theta^3=\frac{9\cdot10^9\cdot4\cdot10^{-14}}{4\cdot0,01\cdot10\cdot0,25}=0,0036$.

$\theta\approx0,153$ rad $\approx8,8^\circ$. Giá trị khá nhỏ nên gần đúng góc nhỏ chấp nhận được ở mức ước tính.''')
    ]

LESSONS={
'01-electron-theory-charge-conservation.md': l1(),
'02-coulomb-law.md': l2(),
'03-electric-field-intensity.md': l3(),
'04-field-superposition-equilibrium.md': l4(),
'05-work-potential-voltage.md': l5(),
'06-capacitors.md': l6(),
'07-charged-particle-motion.md': l7(),
'08-advanced-capacitors.md': l8(),
'09-electrostatic-equilibrium-charged-pendulum.md': l9(),
}

if __name__=='__main__':
    for lf, probs in LESSONS.items():
        write_lesson_practice(CH, lf, probs)
        add_practice_links(CH, lf)
    write_practice_index(CH, list(LESSONS))
    print('chapter 3', sum(len(v) for v in LESSONS.values()), 'problems')
