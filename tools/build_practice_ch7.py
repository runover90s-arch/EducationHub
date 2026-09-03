from practice_bank_common import *
import math

CH='07-electromagnetic-induction'

def l1():
    return [
        mcq(r'''Từ thông qua một diện tích phẳng S trong từ trường đều B được tính bởi

A. $\Phi=BS\cos\alpha$.  
B. $\Phi=BS\sin\alpha$ trong mọi quy ước.  
C. $\Phi=B/S$.  
D. $\Phi=BS^2$.''', r'''Chọn **A**, với α là góc giữa $\vec B$ và pháp tuyến mặt S.'''),
        mcq(r'''Đơn vị SI của từ thông là

A. tesla.  
B. weber.  
C. henry.  
D. ampe.''', r'''Chọn **B**.'''),
        mcq(r'''Nếu $\vec B$ song song mặt phẳng vòng dây thì từ thông qua vòng

A. cực đại.  
B. bằng 0.  
C. bằng BS.  
D. vô hạn.''', r'''Chọn **B** vì $\vec B$ vuông góc pháp tuyến, $\alpha=90^\circ$.'''),
        tf(r'''Về từ thông:

a) Là đại lượng vô hướng có dấu phụ thuộc cách chọn pháp tuyến.  
b) Có thể thay đổi do B, S hoặc góc định hướng thay đổi.  
c) Không đổi nếu vòng quay trong từ trường đều.  
d) Hiện tượng cảm ứng điện từ gắn với sự biến thiên từ thông qua mạch.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai** nói chung; quay làm góc thay đổi.  
d) **Đúng**.'''),
        short(r'''Vòng dây diện tích $50$ cm² đặt trong B=0,2 T, pháp tuyến cùng hướng B. Tính từ thông.''', r'''$S=50\cdot10^{-4}=5\cdot10^{-3}$ m². $\Phi=BS=0,2\cdot5\cdot10^{-3}=10^{-3}$ Wb.'''),
        short(r'''Vòng diện tích $100$ cm² trong B=0,5 T, pháp tuyến hợp B góc $60^\circ$. Tính từ thông.''', r'''$S=0,01$ m². $\Phi=0,5\cdot0,01\cos60^\circ=2,5\cdot10^{-3}$ Wb.'''),
        short(r'''Một vòng dây trong B không đổi quay từ vị trí pháp tuyến song song B sang vuông góc B. Từ thông thay đổi bao nhiêu về độ lớn?''', r'''Ban đầu $\Phi_1=BS$, cuối $\Phi_2=0$. Độ biến thiên về độ lớn là $|\Delta\Phi|=BS$.'''),
        applied(r'''Khung 200 vòng, mỗi vòng diện tích $20$ cm², đặt trong B tăng đều từ 0,1 T lên 0,4 T trong 0,05 s. Pháp tuyến luôn cùng hướng B. Tính độ biến thiên liên kết từ thông $N\Delta\Phi$.''', r'''Diện tích mỗi vòng $S=20\cdot10^{-4}=2\cdot10^{-3}$ m².

$\Delta\Phi=S\Delta B=2\cdot10^{-3}\cdot0,3=6\cdot10^{-4}$ Wb mỗi vòng.

Liên kết từ thông thay đổi:

$N\Delta\Phi=200\cdot6\cdot10^{-4}=0,12$ Wb-vòng.''')
    ]

def l2():
    return [
        mcq(r'''Định luật Faraday cho độ lớn suất điện động cảm ứng trung bình của cuộn N vòng là

A. $|\mathcal E|=N|\Delta\Phi|/\Delta t$.  
B. $|\mathcal E|=N\Delta t/|\Delta\Phi|$.  
C. $|\mathcal E|=N\Phi$.  
D. $|\mathcal E|=I/R$.''', r'''Chọn **A**.'''),
        mcq(r'''Định luật Lenz xác định

A. độ lớn điện trở.  
B. chiều dòng cảm ứng sao cho từ trường cảm ứng chống lại nguyên nhân biến thiên từ thông.  
C. khối lượng electron.  
D. màu ánh sáng.''', r'''Chọn **B**.'''),
        mcq(r'''Từ thông qua một vòng tăng đều $0,02$ Wb trong $0,10$ s. Suất điện động cảm ứng trung bình có độ lớn

A. $0,02$ V.  
B. $0,2$ V.  
C. $2$ V.  
D. $20$ V.''', r'''Chọn **B**. $|\mathcal E|=0,02/0,10=0,2$ V.'''),
        tf(r'''Cảm ứng điện từ:

a) Dòng cảm ứng chỉ xuất hiện khi mạch kín có suất điện động cảm ứng.  
b) Dấu trừ trong định luật Faraday biểu diễn quy tắc Lenz.  
c) Nếu từ thông không đổi thì suất điện động cảm ứng bằng 0.  
d) Dòng cảm ứng luôn làm tăng biến thiên từ thông ban đầu.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: hiệu ứng cảm ứng chống lại sự biến thiên gây ra nó.'''),
        short(r'''Cuộn 100 vòng, từ thông mỗi vòng giảm từ $4\cdot10^{-4}$ Wb xuống $1\cdot10^{-4}$ Wb trong 0,02 s. Tính độ lớn suất điện động trung bình.''', r'''$|\Delta\Phi|=3\cdot10^{-4}$ Wb. $|\mathcal E|=100\cdot3\cdot10^{-4}/0,02=1,5$ V.'''),
        short(r'''Một vòng dây có từ thông $\Phi=0,01\cos(100t)$ Wb. Viết biểu thức suất điện động cảm ứng tức thời.''', r'''$\mathcal E=-d\Phi/dt=-[-0,01\cdot100\sin(100t)]=\sin(100t)$ V.'''),
        short(r'''Khung 50 vòng, diện tích mỗi vòng $0,01$ m², B vuông góc mặt khung tăng đều từ 0 lên 0,2 T trong 0,5 s. Tính suất điện động trung bình.''', r'''$|\mathcal E|=N S\Delta B/\Delta t=50\cdot0,01\cdot0,2/0,5=0,2$ V.'''),
        applied(r'''Một vòng dây kín có điện trở 2 Ω. Từ thông qua vòng biến thiên đều từ $+0,06$ Wb xuống $-0,02$ Wb trong 0,04 s. Tính suất điện động và cường độ dòng cảm ứng trung bình; giải thích vì sao phải dùng hiệu đại số từ thông.''', r'''Độ biến thiên đại số:

$\Delta\Phi=\Phi_2-\Phi_1=-0,02-0,06=-0,08$ Wb.

Độ lớn suất điện động trung bình:

$|\mathcal E|=|\Delta\Phi|/\Delta t=0,08/0,04=2$ V.

Dòng cảm ứng trung bình $I=|\mathcal E|/R=2/2=1$ A.

Phải dùng từ thông có dấu vì từ thông đi qua 0 rồi đổi hướng; nếu chỉ lấy $0,06-0,02$ sẽ bỏ mất phần biến thiên do đảo chiều.''')
    ]

def l3():
    return [
        mcq(r'''Thanh dẫn dài l chuyển động với vận tốc v vuông góc cả thanh và B. Suất điện động cảm ứng giữa hai đầu thanh có độ lớn

A. $Blv$.  
B. $Bv/l$.  
C. $Bl/v$.  
D. $B^2lv$.''', r'''Chọn **A**.'''),
        mcq(r'''Nếu thanh chuyển động song song $\vec B$ thì suất điện động cảm ứng do chuyển động lý tưởng

A. cực đại.  
B. bằng 0.  
C. bằng Blv.  
D. không phụ thuộc v.''', r'''Chọn **B**.'''),
        mcq(r'''Thanh dài 0,5 m chuyển động 4 m/s vuông góc B=0,2 T. Suất điện động là

A. 0,04 V.  
B. 0,4 V.  
C. 4 V.  
D. 40 V.''', r'''Chọn **B**. $\mathcal E=0,2\cdot0,5\cdot4=0,4$ V.'''),
        tf(r'''Suất điện động do chuyển động:

a) Có thể hiểu từ lực Lorentz tách điện tích trong thanh.  
b) Đổi chiều v có thể đảo cực tính hai đầu thanh.  
c) Đổi chiều B có thể đảo cực tính.  
d) Nếu v=0 vẫn luôn có Blv khác 0.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**.'''),
        short(r'''Thanh dài 0,30 m chuyển động 5 m/s vuông góc B=0,4 T. Tính suất điện động.''', r'''$\mathcal E=Blv=0,4\cdot0,30\cdot5=0,60$ V.'''),
        short(r'''Thanh có suất điện động 1,2 V khi l=0,4 m, v=6 m/s và chuyển động vuông góc B. Tính B.''', r'''$B=\mathcal E/(lv)=1,2/(0,4\cdot6)=0,50$ T.'''),
        short(r'''Thanh dài 0,5 m chuyển động với v=4 m/s hợp B góc $30^\circ$, thanh bố trí để thành phần v vuông góc B có hiệu quả. B=0,6 T. Tính suất điện động dùng $\mathcal E=Blv\sin30^\circ$.''', r'''$\mathcal E=0,6\cdot0,5\cdot4\cdot0,5=0,60$ V.'''),
        applied(r'''Thanh dẫn dài 0,40 m trượt không ma sát trên hai ray tạo mạch kín tổng điện trở 2 Ω trong B=0,5 T vuông góc mặt ray. Thanh chuyển động đều 3 m/s. Tính suất điện động, dòng cảm ứng và lực từ cản trên thanh.''', r'''Suất điện động:

$\mathcal E=Blv=0,5\cdot0,40\cdot3=0,60$ V.

Dòng: $I=\mathcal E/R=0,60/2=0,30$ A.

Lực từ lên thanh có độ lớn $F=BIl=0,5\cdot0,30\cdot0,40=0,060$ N.

Theo Lenz, lực từ có chiều cản chuyển động. Công suất cơ cần để giữ v không đổi là $Fv=0,18$ W, bằng $I^2R=0,18$ W, kiểm tra năng lượng nhất quán.''')
    ]

def l4():
    return [
        mcq(r'''Suất điện động tự cảm có độ lớn

A. $|\mathcal E_L|=L|\Delta I|/\Delta t$.  
B. $|\mathcal E_L|=I/L$.  
C. $|\mathcal E_L|=LI^2$.  
D. $|\mathcal E_L|=R/L$.''', r'''Chọn **A** cho biến thiên đều/trung bình.'''),
        mcq(r'''Đơn vị của hệ số tự cảm L là

A. tesla.  
B. henry.  
C. weber trên mét vuông.  
D. coulomb.''', r'''Chọn **B**.'''),
        mcq(r'''Năng lượng từ trường trong cuộn cảm mang dòng I là

A. $W=LI^2$.  
B. $W=\frac12LI^2$.  
C. $W=I^2/(2L)$.  
D. $W=L/I$.''', r'''Chọn **B**.'''),
        tf(r'''Tự cảm:

a) Xuất hiện khi dòng qua chính mạch biến thiên.  
b) Suất điện động tự cảm chống lại sự biến thiên dòng theo Lenz.  
c) Cuộn cảm tích trữ năng lượng từ trường.  
d) Khi I không đổi theo thời gian, suất điện động tự cảm lý tưởng khác 0.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: $dI/dt=0$ nên $\mathcal E_L=0$.'''),
        short(r'''Cuộn cảm L=0,5 H, dòng tăng đều từ 0 lên 2 A trong 0,1 s. Tính độ lớn suất điện động tự cảm.''', r'''$|\mathcal E_L|=L\Delta I/\Delta t=0,5\cdot2/0,1=10$ V.'''),
        short(r'''Cuộn cảm 0,2 H mang dòng 3 A. Tính năng lượng từ trường.''', r'''$W=\frac12LI^2=0,5\cdot0,2\cdot9=0,9$ J.'''),
        short(r'''Một cuộn cảm tạo suất điện động tự cảm 6 V khi dòng giảm đều 3 A trong 0,25 s. Tính L.''', r'''$L=|\mathcal E|\Delta t/|\Delta I|=6\cdot0,25/3=0,5$ H.'''),
        applied(r'''Cuộn cảm L=0,40 H đang mang dòng 2 A. Dòng giảm tuyến tính về 0 trong 0,05 s. Tính độ lớn suất điện động tự cảm trung bình và năng lượng từ trường ban đầu. Nếu toàn bộ năng lượng cuối cùng tỏa trên điện trở, có bao nhiêu joule được tỏa?''', r'''Suất điện động trung bình:

$|\mathcal E_L|=L|\Delta I|/\Delta t=0,40\cdot2/0,05=16$ V.

Năng lượng ban đầu:

$W_0=\frac12LI^2=0,5\cdot0,40\cdot4=0,80$ J.

Nếu cuối cùng dòng bằng 0 và bỏ qua các kênh khác, toàn bộ $0,80$ J được chuyển thành nhiệt trên điện trở.''')
    ]

LESSONS={
'01-magnetic-flux-induction.md': l1(),
'02-lenz-faraday-law.md': l2(),
'03-motional-emf.md': l3(),
'04-self-induction-energy.md': l4(),
}

if __name__=='__main__':
    for lf, probs in LESSONS.items():
        write_lesson_practice(CH, lf, probs)
        add_practice_links(CH, lf)
    write_practice_index(CH, list(LESSONS))
    print('chapter 7', sum(len(v) for v in LESSONS.values()), 'problems')
