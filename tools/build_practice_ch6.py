from practice_bank_common import *
import math

CH='06-magnetism'

def l1():
    return [
        mcq(r'''Đơn vị SI của cảm ứng từ là

A. tesla (T).  
B. weber (Wb).  
C. vôn (V).  
D. henry (H).''', r'''Chọn **A**.'''),
        mcq(r'''Đường sức từ của nam châm thẳng ở bên ngoài nam châm có chiều

A. từ cực Nam sang cực Bắc.  
B. từ cực Bắc sang cực Nam.  
C. không có chiều.  
D. luôn thẳng song song.''', r'''Chọn **B** ở bên ngoài nam châm; bên trong khép kín ngược lại để tạo đường kín.'''),
        mcq(r'''Hai đường sức từ trong cùng một từ trường

A. có thể cắt nhau tại nhiều điểm.  
B. không cắt nhau.  
C. luôn là đường thẳng.  
D. luôn là đường tròn.''', r'''Chọn **B**, vì nếu cắt nhau sẽ có hai hướng của $\vec B$ tại một điểm.'''),
        tf(r'''Về từ trường:

a) Từ trường tác dụng lực lên nam châm, dòng điện hoặc điện tích chuyển động.  
b) Vectơ $\vec B$ đặc trưng từ trường về phương diện tác dụng lực.  
c) Đường sức từ là các đường kín.  
d) Ở nơi đường sức dày hơn, từ trường thường được biểu diễn là mạnh hơn.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng** trong mô hình đường sức từ.  
d) **Đúng** về quy ước biểu diễn.'''),
        short(r'''Một từ trường đều có $B=0,20$ T. Viết độ lớn cảm ứng từ theo mT.''', r'''$0,20$ T = $200$ mT.'''),
        short(r'''Một kim nam châm nhỏ đặt tự do trong từ trường đều. Trục Bắc–Nam của kim ổn định như thế nào so với $\vec B$?''', r'''Kim có xu hướng quay để trục từ của nó song song với $\vec B$, đầu Bắc của kim chỉ theo chiều của vectơ cảm ứng từ.'''),
        short(r'''Nêu hai dấu hiệu phân biệt từ trường đều và từ trường không đều bằng hình ảnh đường sức.''', r'''Từ trường đều được biểu diễn bằng các đường sức **song song, cùng chiều và cách đều**. Từ trường không đều có khoảng cách hoặc hướng đường sức thay đổi theo vị trí.'''),
        applied(r'''Một kim nam châm đặt ở hai vị trí A và B. Ở A đường sức gần nhau gấp khoảng hai lần so với B trong cùng cách vẽ định tính. Có thể kết luận chính xác $B_A=2B_B$ không? Giải thích.''', r'''Không thể kết luận định lượng chính xác chỉ từ mật độ nét vẽ nếu sơ đồ không quy ước tỉ lệ. Hình đường sức cho **trực giác định tính**: nơi đường dày hơn thường mạnh hơn. Muốn khẳng định $B_A/B_B$ cần số liệu hoặc quy ước định lượng của sơ đồ.''')
    ]

def l2():
    return [
        mcq(r'''Lực từ lên đoạn dây dài l có dòng I trong từ trường đều B có độ lớn

A. $F=BIl\sin\alpha$.  
B. $F=BIl\cos\alpha$ trong mọi trường hợp.  
C. $F=BI/l$.  
D. $F=B/I$.''', r'''Chọn **A**, với α là góc giữa chiều dòng điện và $\vec B$.'''),
        mcq(r'''Dây dẫn song song với $\vec B$ thì lực từ

A. cực đại.  
B. bằng 0.  
C. bằng BIl.  
D. không xác định.''', r'''Chọn **B** vì $\sin0=0$.'''),
        mcq(r'''Dây vuông góc với $\vec B$ thì lực từ

A. bằng 0.  
B. có độ lớn BIl.  
C. bằng BI/l.  
D. chỉ phụ thuộc l.''', r'''Chọn **B**.'''),
        tf(r'''Lực từ lên dây có dòng:

a) Vuông góc cả chiều dòng và $\vec B$.  
b) Đổi chiều dòng làm lực đảo chiều.  
c) Đổi chiều $\vec B$ làm lực đảo chiều.  
d) Tăng I gấp đôi, các yếu tố khác giữ nguyên, lực không đổi.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: lực tăng gấp đôi.'''),
        short(r'''Đoạn dây dài $0,20$ m mang dòng 5 A đặt vuông góc từ trường $B=0,40$ T. Tính lực từ.''', r'''$F=BIl=0,40\cdot5\cdot0,20=0,40$ N.'''),
        short(r'''Dây dài $0,50$ m mang dòng 2 A trong từ trường 0,30 T, hợp với $\vec B$ góc $30^\circ$. Tính lực.''', r'''$F=BIl\sin30^\circ=0,30\cdot2\cdot0,50\cdot0,5=0,15$ N.'''),
        short(r'''Một đoạn dây chịu lực $0,12$ N khi vuông góc B. Biết I=3 A, l=0,20 m. Tính B.''', r'''$B=F/(Il)=0,12/(3\cdot0,20)=0,20$ T.'''),
        applied(r'''Một thanh dẫn dài $0,40$ m, khối lượng $20$ g nằm ngang trong từ trường đều thẳng đứng. Dòng điện chạy qua thanh theo phương vuông góc B sao cho lực từ hướng lên. Lấy $B=0,50$ T, $g=10$ m/s². Tính dòng để thanh vừa cân bằng trọng lực.''', r'''Cần $F_t=mg$.

$BIl=mg$ vì dây vuông góc B.

$I=mg/(Bl)=0,020\cdot10/(0,50\cdot0,40)=1,0$ A.

Chiều dòng phải chọn theo quy tắc bàn tay sao cho lực từ hướng lên.''')
    ]

def l3():
    return [
        mcq(r'''Cảm ứng từ cách dây thẳng dài mang dòng I một khoảng r trong chân không là

A. $B=\mu_0I/(2\pi r)$.  
B. $B=\mu_0Ir$.  
C. $B=\mu_0I/(4\pi r^2)$.  
D. $B=Ir/\mu_0$.''', r'''Chọn **A**.'''),
        mcq(r'''Tại tâm vòng dây tròn bán kính R mang dòng I một vòng, cảm ứng từ là

A. $\mu_0I/(2R)$.  
B. $\mu_0I/(2\pi R)$.  
C. $\mu_0IR$.  
D. 0.''', r'''Chọn **A**.'''),
        mcq(r'''Ống dây dài có mật độ vòng n và dòng I, từ trường bên trong gần đều có

A. $B=\mu_0nI$.  
B. $B=\mu_0I/(2\pi r)$.  
C. $B=n/I$.  
D. $B=\mu_0n/I$.''', r'''Chọn **A** trong mô hình ống dây dài.'''),
        tf(r'''Từ trường do dòng điện:

a) Quanh dây thẳng dài, đường sức là các đường tròn đồng tâm quanh dây.  
b) Chiều xác định bằng quy tắc nắm tay phải.  
c) Độ lớn B của dây thẳng tỉ lệ nghịch khoảng cách r.  
d) Hai từ trường chồng chất cộng theo độ lớn mà không cần xét hướng.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: phải cộng vectơ.'''),
        short(r'''Dây thẳng dài mang dòng 10 A. Tính B tại điểm cách dây 5 cm. Lấy $\mu_0=4\pi\cdot10^{-7}$ H/m.''', r'''$B=\mu_0I/(2\pi r)=4\pi\cdot10^{-7}\cdot10/(2\pi\cdot0,05)=4\cdot10^{-5}$ T.'''),
        short(r'''Vòng dây bán kính 10 cm mang dòng 5 A. Tính B tại tâm.''', r'''$B=\mu_0I/(2R)=4\pi\cdot10^{-7}\cdot5/(0,20)=\pi\cdot10^{-5}$ T $\approx3,14\cdot10^{-5}$ T.'''),
        short(r'''Ống dây dài có 1000 vòng trên chiều dài 0,50 m, dòng 0,8 A. Tính B bên trong.''', r'''$n=N/l=2000$ vòng/m. $B=\mu_0nI=4\pi\cdot10^{-7}\cdot2000\cdot0,8\approx2,01\cdot10^{-3}$ T.'''),
        applied(r'''Hai dây thẳng dài song song cách nhau 20 cm, mang dòng $I_1=4$ A và $I_2=9$ A cùng chiều. Tìm điểm trên đoạn nối hai dây nơi từ trường tổng hợp bằng 0.''', r'''Giữa hai dây có dòng cùng chiều, từ trường do hai dây tại các điểm giữa ngược hướng. Gọi x là khoảng cách đến dây 1:

$\mu_0I_1/(2\pi x)=\mu_0I_2/[2\pi(0,20-x)]$.

$I_1/x=I_2/(0,20-x)$.

$4(0,20-x)=9x$ nên $0,80=13x$, $x\approx0,0615$ m.

Vậy điểm nằm giữa hai dây, cách dây 4 A khoảng $6,15$ cm, gần dây có dòng nhỏ hơn.''')
    ]

def l4():
    return [
        mcq(r'''Hai dòng điện thẳng dài song song cùng chiều

A. hút nhau.  
B. đẩy nhau.  
C. không tương tác.  
D. chỉ tương tác khi dòng bằng nhau.''', r'''Chọn **A**.'''),
        mcq(r'''Hai dòng song song ngược chiều

A. hút nhau.  
B. đẩy nhau.  
C. lực bằng 0.  
D. chỉ có lực lên một dây.''', r'''Chọn **B**.'''),
        mcq(r'''Mômen từ tác dụng lên khung dây N vòng diện tích S, dòng I trong B có độ lớn cực đại

A. $NIBS$.  
B. $NIB/S$.  
C. $BI/(NS)$.  
D. 0.''', r'''Chọn **A**, khi pháp tuyến khung vuông góc $\vec B$.'''),
        tf(r'''Hai dây song song:

a) Lực trên mỗi đơn vị chiều dài tỉ lệ $I_1I_2/d$.  
b) Hai dây cùng chiều hút nhau.  
c) Hai dây ngược chiều đẩy nhau.  
d) Lực một dây tác dụng lên dây kia có độ lớn khác hẳn lực ngược lại trong cùng đoạn xét.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: chúng tạo cặp lực tương tác bằng nhau về độ lớn trên các đoạn tương ứng.'''),
        short(r'''Hai dây dài song song cách $0,10$ m, mang dòng 5 A và 8 A cùng chiều. Tính lực trên mỗi mét dây. Lấy $\mu_0=4\pi\cdot10^{-7}$.''', r'''$F/l=\mu_0I_1I_2/(2\pi d)=4\pi\cdot10^{-7}\cdot40/(2\pi\cdot0,10)=8\cdot10^{-5}$ N/m. Lực hút.'''),
        short(r'''Khung một vòng diện tích $0,02$ m² mang dòng 3 A trong B=0,5 T. Pháp tuyến khung hợp B góc $90^\circ$. Tính mômen.''', r'''$\tau=NIBS\sin\theta=1\cdot3\cdot0,5\cdot0,02\cdot1=0,03$ N·m.'''),
        short(r'''Khung 50 vòng, diện tích mỗi vòng $20$ cm², dòng 0,2 A trong B=0,1 T. Tính mômen cực đại.''', r'''$S=20\cdot10^{-4}=0,002$ m². $\tau_{max}=NIBS=50\cdot0,2\cdot0,1\cdot0,002=0,002$ N·m.'''),
        applied(r'''Hai dây thẳng dài song song cách 15 cm, cùng mang dòng 10 A cùng chiều. Một đoạn dài 50 cm của mỗi dây được xét. Tính lực hút giữa hai đoạn theo mô hình dây dài.''', r'''Lực trên đơn vị chiều dài:

$F/l=\mu_0I^2/(2\pi d)=4\pi\cdot10^{-7}\cdot100/(2\pi\cdot0,15)=1,333\cdot10^{-4}$ N/m.

Với $l=0,50$ m:

$F\approx6,67\cdot10^{-5}$ N, là lực hút.''')
    ]

def l5():
    return [
        mcq(r'''Độ lớn lực Lorentz lên hạt điện tích q chuyển động vận tốc v trong từ trường B là

A. $F=|q|vB\sin\alpha$.  
B. $F=|q|vB\cos\alpha$ luôn.  
C. $F=|q|B/v$.  
D. $F=mv^2$.''', r'''Chọn **A**.'''),
        mcq(r'''Hạt chuyển động song song $\vec B$ thì lực Lorentz

A. cực đại.  
B. bằng 0.  
C. bằng qvB.  
D. đổi khối lượng.''', r'''Chọn **B**.'''),
        mcq(r'''Hạt tích điện chuyển động vuông góc B chỉ chịu lực từ sẽ

A. tăng tốc độ liên tục.  
B. chuyển động tròn đều.  
C. đứng yên.  
D. chuyển động thẳng nhanh dần đều.''', r'''Chọn **B** vì lực từ luôn vuông góc vận tốc, đóng vai trò lực hướng tâm.'''),
        tf(r'''Lực Lorentz:

a) Luôn vuông góc vận tốc tức thời.  
b) Không sinh công cơ học lên hạt nếu chỉ có từ trường.  
c) Có thể đổi hướng vận tốc nhưng không đổi độ lớn tốc độ.  
d) Hạt trung hòa vẫn chịu lực $qvB$ với q=0 khác 0.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: q=0 thì lực Lorentz từ bằng 0.'''),
        short(r'''Electron có tốc độ $2\cdot10^6$ m/s vuông góc B=0,02 T. Tính độ lớn lực, lấy e=$1,6\cdot10^{-19}$ C.''', r'''$F=evB=1,6\cdot10^{-19}\cdot2\cdot10^6\cdot0,02=6,4\cdot10^{-15}$ N.'''),
        short(r'''Proton có $m=1,67\cdot10^{-27}$ kg, q=$1,6\cdot10^{-19}$ C, v=$10^6$ m/s vuông góc B=0,5 T. Tính bán kính quỹ đạo.''', r'''$r=mv/(qB)=1,67\cdot10^{-27}\cdot10^6/(1,6\cdot10^{-19}\cdot0,5)\approx0,0209$ m $=2,09$ cm.'''),
        short(r'''Tính chu kì cyclotron của proton trong B=0,5 T với dữ kiện trên.''', r'''$T=2\pi m/(qB)=2\pi\cdot1,67\cdot10^{-27}/(1,6\cdot10^{-19}\cdot0,5)\approx1,31\cdot10^{-7}$ s.'''),
        applied(r'''Một hạt điện tích dương đi vào vùng từ trường đều B vuông góc mặt phẳng chuyển động với v vuông góc B. Sau khi đi trong vùng, quỹ đạo là nửa đường tròn bán kính 5 cm. Biết $q/m=2\cdot10^7$ C/kg. Tính B nếu v=$2\cdot10^6$ m/s và thời gian hạt ở trong vùng.''', r'''Từ $r=mv/(qB)=v/[(q/m)B]$:

$B=v/[(q/m)r]=2\cdot10^6/(2\cdot10^7\cdot0,05)=2$ T.

Chu kì tròn $T=2\pi/[(q/m)B]=2\pi/(4\cdot10^7)\approx1,57\cdot10^{-7}$ s.

Đi nửa vòng nên thời gian $t=T/2\approx7,85\cdot10^{-8}$ s.''')
    ]

LESSONS={
'01-magnetic-field-field-lines.md': l1(),
'02-magnetic-force-current-wire.md': l2(),
'03-fields-of-currents-superposition.md': l3(),
'04-parallel-currents-current-loop.md': l4(),
'05-lorentz-force-charged-particle.md': l5(),
}

if __name__=='__main__':
    for lf, probs in LESSONS.items():
        write_lesson_practice(CH, lf, probs)
        add_practice_links(CH, lf)
    write_practice_index(CH, list(LESSONS))
    print('chapter 6', sum(len(v) for v in LESSONS.values()), 'problems')
