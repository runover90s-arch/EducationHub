from practice_bank_common import *
import math

CH='04-current-circuits'

def l1():
    return [
        mcq(r'''Điện lượng $12$ C đi qua tiết diện dây trong $4$ s. Cường độ dòng điện trung bình là

A. $0,33$ A.  
B. $3$ A.  
C. $8$ A.  
D. $48$ A.''', r'''Chọn **B**. $I=\Delta q/\Delta t=12/4=3$ A.'''),
        mcq(r'''Dòng điện không đổi là dòng điện có

A. chiều không đổi nhưng cường độ luôn biến đổi.  
B. cường độ và chiều không đổi theo thời gian.  
C. điện lượng bằng 0.  
D. chỉ tồn tại trong kim loại.''', r'''Chọn **B**.'''),
        mcq(r'''Dòng điện trong kim loại có chiều quy ước

A. cùng chiều chuyển động có hướng của electron.  
B. ngược chiều chuyển động có hướng của electron.  
C. không liên quan điện trường.  
D. từ cực âm sang cực dương ngoài nguồn.''', r'''Chọn **B**. Chiều dòng điện quy ước là chiều chuyển động của điện tích dương.'''),
        mcq(r'''Dòng điện $I=2$ A chạy trong $30$ s. Điện lượng qua tiết diện là

A. $15$ C.  
B. $28$ C.  
C. $60$ C.  
D. $120$ C.''', r'''Chọn **C**. $q=It=2\cdot30=60$ C.'''),
        tf(r'''Xét cường độ dòng điện:

a) $1$ A = $1$ C/s.  
b) $I=\Delta q/\Delta t$.  
c) Trong kim loại, hạt tải điện chủ yếu là electron tự do.  
d) Electron chuyển động nhiệt hỗn loạn hoàn toàn dừng lại khi có dòng điện.''', r'''a) **Đúng**.  
b) **Đúng** cho giá trị trung bình; dòng không đổi thì dùng trực tiếp.  
c) **Đúng**.  
d) **Sai**: chuyển động nhiệt vẫn tồn tại, chồng thêm chuyển động trôi có hướng.'''),
        tf(r'''Một dây dẫn kim loại có mật độ electron tự do n, tiết diện S, tốc độ trôi trung bình v:

a) $I=neSv$ về độ lớn.  
b) Tăng S, các yếu tố khác giữ nguyên, I tăng.  
c) Tốc độ trôi bằng tốc độ lan truyền tín hiệu điện trong dây.  
d) Điện lượng qua tiết diện trong thời gian t là $It$ với dòng không đổi.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: tốc độ trôi của electron rất nhỏ so với tốc độ truyền trường/tín hiệu.  
d) **Đúng**.'''),
        short(r'''Dòng điện $0,50$ A chạy trong $2$ phút. Tính điện lượng và số electron qua tiết diện. Lấy $e=1,6\cdot10^{-19}$ C.''', r'''$t=120$ s. $q=It=0,5\cdot120=60$ C. Số electron $N=q/e=60/(1,6\cdot10^{-19})=3,75\cdot10^{20}$.'''),
        short(r'''Trong $0,20$ s có $5\cdot10^{17}$ electron đi qua tiết diện dây. Tính cường độ dòng điện.''', r'''$q=Ne=5\cdot10^{17}\cdot1,6\cdot10^{-19}=0,08$ C. $I=q/t=0,08/0,20=0,40$ A.'''),
        short(r'''Dây dẫn có tiết diện $S=1$ mm², mật độ electron tự do $n=8,5\cdot10^{28}$ m⁻³, dòng điện $I=1,36$ A. Tính tốc độ trôi trung bình. Lấy $e=1,6\cdot10^{-19}$ C.''', r'''$S=10^{-6}$ m². Từ $I=neSv$: $v=I/(neS)=1,36/(8,5\cdot10^{28}\cdot1,6\cdot10^{-19}\cdot10^{-6})=10^{-4}$ m/s $=0,1$ mm/s.'''),
        applied(r'''Một dây dẫn hình trụ có đường kính giảm dần nhưng cùng vật liệu và cùng dòng điện không đổi chạy qua. Ở tiết diện 1, bán kính $r_1=2r_2$. Giả sử mật độ hạt tải n như nhau. So sánh tốc độ trôi $v_1$ và $v_2$.''', r'''Dòng điện liên tục nên $I=neSv$ như nhau tại hai tiết diện.

$S\propto r^2$, nên $S_1/S_2=(r_1/r_2)^2=4$.

Do $S_1v_1=S_2v_2$, suy ra $v_2=4v_1$. Hạt tải phải trôi nhanh hơn ở tiết diện nhỏ hơn để duy trì cùng dòng điện.''')
    ]

def l2():
    return [
        mcq(r'''Điện trở dây đồng chất dài l, tiết diện S, điện trở suất ρ là

A. $R=\rho S/l$.  
B. $R=\rho l/S$.  
C. $R=l/(\rho S)$.  
D. $R=\rho lS$.''', r'''Chọn **B**.'''),
        mcq(r'''Hai điện trở $4\,\Omega$ và $6\,\Omega$ mắc nối tiếp. Điện trở tương đương

A. $2,4\,\Omega$.  
B. $5\,\Omega$.  
C. $10\,\Omega$.  
D. $24\,\Omega$.''', r'''Chọn **C**.'''),
        mcq(r'''Hai điện trở $6\,\Omega$ và $3\,\Omega$ mắc song song. Điện trở tương đương

A. $2\,\Omega$.  
B. $3\,\Omega$.  
C. $4,5\,\Omega$.  
D. $9\,\Omega$.''', r'''Chọn **A**. $R=6\cdot3/(6+3)=2\,\Omega$.'''),
        mcq(r'''Một điện trở thuần $R=10\,\Omega$ đặt dưới hiệu điện thế $20$ V. Dòng điện là

A. $0,5$ A.  
B. $2$ A.  
C. $10$ A.  
D. $200$ A.''', r'''Chọn **B**. $I=U/R=2$ A.'''),
        tf(r'''Điện trở kim loại trong mô hình phổ thông:

a) $R=\rho l/S$.  
b) Tăng chiều dài dây làm R tăng.  
c) Tăng tiết diện dây làm R tăng.  
d) Với nhiều kim loại trong khoảng nhiệt độ vừa phải, R tăng gần tuyến tính theo nhiệt độ.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: R giảm khi S tăng.  
d) **Đúng** trong gần đúng tuyến tính.'''),
        tf(r'''Định luật Ohm cho đoạn mạch chỉ có điện trở:

a) $I=U/R$.  
b) Với R không đổi, đồ thị I–U là đường thẳng qua gốc.  
c) Điện trở tương đương song song lớn hơn từng điện trở thành phần.  
d) Mạch nối tiếp có cùng dòng điện qua các phần tử.''', r'''a) **Đúng**.  
b) **Đúng** với vật dẫn ohmic.  
c) **Sai**.  
d) **Đúng**.'''),
        short(r'''Dây nicrom dài $2$ m, tiết diện $0,5$ mm², điện trở suất $1,1\cdot10^{-6}\,\Omega$m. Tính điện trở.''', r'''$S=0,5\cdot10^{-6}$ m². $R=\rho l/S=1,1\cdot10^{-6}\cdot2/(0,5\cdot10^{-6})=4,4\,\Omega$.'''),
        short(r'''Một dây có $R_0=20\,\Omega$ ở $20^\circ$C, hệ số nhiệt điện trở $\alpha=4\cdot10^{-3}$ K⁻¹. Tính R ở $70^\circ$C.''', r'''$R=R_0[1+\alpha(T-T_0)]=20[1+0,004\cdot50]=24\,\Omega$.'''),
        short(r'''Ba điện trở $2\,\Omega$, $3\,\Omega$, $6\,\Omega$ mắc song song. Tính điện trở tương đương.''', r'''$1/R=1/2+1/3+1/6=1$, nên $R=1\,\Omega$.'''),
        applied(r'''Một dây đồng chất có điện trở R. Kéo đều dây sao cho chiều dài tăng gấp đôi, thể tích coi như không đổi và điện trở suất không đổi. Tính điện trở mới theo R.''', r'''Thể tích $V=lS$ không đổi. Khi $l'=2l$ thì $S'=S/2$.

$R'=\rho l'/S'=\rho(2l)/(S/2)=4\rho l/S=4R$.

Điện trở tăng 4 lần, không chỉ 2 lần, vì vừa tăng chiều dài vừa giảm tiết diện.''')
    ]

def l3():
    return [
        mcq(r'''Suất điện động của nguồn được định nghĩa bởi

A. $\mathcal E=A_{ng}/q$.  
B. $\mathcal E=q/A_{ng}$.  
C. $\mathcal E=IR$.  
D. $\mathcal E=P/t$.''', r'''Chọn **A**, với $A_{ng}$ là công của lực lạ bên trong nguồn để dịch chuyển điện tích q.'''),
        mcq(r'''Nguồn có suất điện động $12$ V, điện trở trong $1\,\Omega$, đang phát dòng $2$ A. Hiệu điện thế hai cực nguồn là

A. $10$ V.  
B. $12$ V.  
C. $14$ V.  
D. $24$ V.''', r'''Chọn **A**. Khi nguồn phát điện: $U=\mathcal E-Ir=12-2=10$ V.'''),
        mcq(r'''Khi mạch ngoài hở, dòng điện bằng 0, hiệu điện thế hai cực của nguồn lí tưởng mô hình hóa bằng

A. 0.  
B. $Ir$.  
C. $\mathcal E$.  
D. $\mathcal E/2$.''', r'''Chọn **C** vì sụt áp trong bằng 0.'''),
        mcq(r'''Điện trở trong của nguồn gây ra

A. sụt áp $Ir$ khi có dòng.  
B. tăng vô hạn điện áp ngoài.  
C. làm dòng bằng 0 trong mọi mạch.  
D. không ảnh hưởng mạch.''', r'''Chọn **A**.'''),
        tf(r'''Nguồn đang phát điện:

a) $U=\mathcal E-Ir$.  
b) Khi I tăng, U thường giảm nếu $\mathcal E,r$ không đổi.  
c) Khi hở mạch, U bằng suất điện động.  
d) Suất điện động có đơn vị ampe.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: đơn vị vôn.'''),
        tf(r'''Về công của nguồn:

a) $\mathcal E$ biểu thị công của lực lạ trên một đơn vị điện tích.  
b) Công của nguồn trong thời gian t có thể viết $A_{ng}=\mathcal E It$ khi dòng không đổi.  
c) Điện trở trong càng lớn luôn làm hiệu suất nguồn tăng.  
d) Nguồn thực có thể nóng lên do tổn hao trong.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**.  
d) **Đúng**.'''),
        short(r'''Nguồn có $\mathcal E=9$ V, $r=0,5\,\Omega$, phát dòng $I=1,2$ A. Tính U hai cực.''', r'''$U=9-1,2\cdot0,5=8,4$ V.'''),
        short(r'''Một nguồn hở mạch đo được $12$ V. Khi phát dòng $2$ A, hiệu điện thế hai cực còn $11$ V. Tính điện trở trong.''', r'''$\mathcal E\approx12$ V khi hở mạch. $r=(\mathcal E-U)/I=(12-11)/2=0,5\,\Omega$.'''),
        short(r'''Nguồn $6$ V, $r=1\,\Omega$ phát dòng $0,50$ A trong 2 phút. Tính công của nguồn và nhiệt tỏa trên điện trở trong.''', r'''$t=120$ s. Công nguồn $A=\mathcal E It=6\cdot0,5\cdot120=360$ J. Nhiệt trên r: $Q=I^2rt=0,25\cdot1\cdot120=30$ J.'''),
        applied(r'''Một nguồn có $\mathcal E=12$ V. Khi dòng phát là $1$ A, U hai cực $11,5$ V. Khi dòng phát $3$ A, U hai cực là bao nhiêu nếu mô hình nguồn tuyến tính không đổi?''', r'''Từ trạng thái đầu: $r=(12-11,5)/1=0,5\,\Omega$.

Ở $I=3$ A:

$U=\mathcal E-Ir=12-3\cdot0,5=10,5$ V.

Ta đã dùng giả thiết $\mathcal E$ và r không đổi trong khoảng làm việc.''')
    ]

def l4():
    return [
        mcq(r'''Công suất tiêu thụ của điện trở R có thể viết

A. $P=UI$.  
B. $P=U/I$.  
C. $P=It/U$.  
D. $P=R/U^2$.''', r'''Chọn **A**; với điện trở thuần còn có $P=I^2R=U^2/R$.'''),
        mcq(r'''Điện trở $10\,\Omega$ có dòng $2$ A chạy qua. Công suất tỏa nhiệt là

A. $5$ W.  
B. $20$ W.  
C. $40$ W.  
D. $200$ W.''', r'''Chọn **C**. $P=I^2R=4\cdot10=40$ W.'''),
        mcq(r'''Một thiết bị ghi 220 V – 1100 W. Dòng định mức gần bằng

A. $0,2$ A.  
B. $5$ A.  
C. $10$ A.  
D. $242$ A.''', r'''Chọn **B**. $I=P/U=1100/220=5$ A.'''),
        mcq(r'''Định luật Joule–Lenz cho nhiệt lượng tỏa ra trên điện trở trong dòng không đổi là

A. $Q=I^2Rt$.  
B. $Q=IR/t$.  
C. $Q=U/I$.  
D. $Q=R/(I^2t)$.''', r'''Chọn **A**.'''),
        tf(r'''Điện năng và công suất:

a) $1$ kWh là đơn vị năng lượng.  
b) $1$ kWh = $3,6\cdot10^6$ J.  
c) Với điện trở thuần, $P=U^2/R$.  
d) Tăng R trong khi giữ I không đổi làm công suất giảm.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: với I không đổi, $P=I^2R$ nên tăng.'''),
        tf(r'''Một nguồn có suất điện động E, phát dòng I:

a) Công suất của nguồn là $\mathcal E I$.  
b) Công suất hao phí trong nguồn là $I^2r$.  
c) Công suất mạch ngoài bằng $UI$.  
d) Hiệu suất nguồn luôn 100% nếu r khác 0.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai** vì có tổn hao trong.'''),
        short(r'''Ấm điện $1200$ W hoạt động 15 phút. Tính điện năng theo kWh và J.''', r'''$P=1,2$ kW, $t=0,25$ h nên $A=0,30$ kWh. Đổi ra J: $0,30\cdot3,6\cdot10^6=1,08\cdot10^6$ J.'''),
        short(r'''Điện trở $R=44\,\Omega$ mắc vào $220$ V trong 5 phút. Tính dòng, công suất và nhiệt lượng.''', r'''$I=U/R=220/44=5$ A. $P=UI=1100$ W. $Q=Pt=1100\cdot300=3,3\cdot10^5$ J.'''),
        short(r'''Một bếp điện truyền $1,5\cdot10^6$ J nhiệt hữu ích cho nước khi tiêu thụ $2,0\cdot10^6$ J điện năng. Tính hiệu suất.''', r'''$H=A_{ích}/A_{vào}=1,5/2,0=0,75=75\%$.'''),
        applied(r'''Ấm điện công suất danh định $1000$ W dùng để đun $1,5$ kg nước từ $20^\circ$C lên $100^\circ$C. Hiệu suất 80%, lấy $c=4200$ J/(kg·K). Tính thời gian đun.''', r'''Nhiệt nước cần nhận:

$Q=mc\Delta T=1,5\cdot4200\cdot80=504000$ J.

Vì hiệu suất $H=0,80$, điện năng cần cung cấp:

$A=Q/H=504000/0,80=630000$ J.

$t=A/P=630000/1000=630$ s $=10,5$ phút.''')
    ]

def l5():
    return [
        mcq(r'''Mạch kín gồm nguồn $\mathcal E=12$ V, $r=1\,\Omega$ và điện trở ngoài $R=5\,\Omega$. Dòng điện là

A. $1$ A.  
B. $2$ A.  
C. $2,4$ A.  
D. $12$ A.''', r'''Chọn **B**. $I=\mathcal E/(R+r)=12/6=2$ A.'''),
        mcq(r'''Hiệu suất của nguồn trong mạch đơn R nối tiếp r có thể viết

A. $H=R/(R+r)$.  
B. $H=r/(R+r)$.  
C. $H=(R+r)/R$.  
D. $H=Rr$.''', r'''Chọn **A** vì $H=P_{ngoài}/P_{nguồn}=UI/(\mathcal EI)=U/\mathcal E=R/(R+r)$.'''),
        mcq(r'''Dòng ngắn mạch của nguồn là

A. $I_{sc}=\mathcal E/R$.  
B. $I_{sc}=\mathcal E/r$.  
C. $I_{sc}=r/\mathcal E$.  
D. 0.''', r'''Chọn **B** trong mô hình nguồn có điện trở trong r.'''),
        mcq(r'''Trong mạch đơn, công suất mạch ngoài đạt cực đại khi

A. $R=0$.  
B. $R=r$.  
C. $R=2r$.  
D. $R\to\infty$.''', r'''Chọn **B** theo định lí truyền công suất cực đại.'''),
        tf(r'''Định luật Ohm toàn mạch:

a) $I=\mathcal E/(R+r)$.  
b) $U_R=IR=\mathcal E-Ir$.  
c) Tăng R luôn làm I tăng.  
d) Khi R rất lớn, I tiến về 0 và U hai cực tiến gần $\mathcal E$.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**.  
d) **Đúng**.'''),
        tf(r'''Công suất mạch ngoài $P_R=\mathcal E^2R/(R+r)^2$:

a) Bằng 0 khi R=0.  
b) Tiến về 0 khi R rất lớn.  
c) Có cực đại tại R=r.  
d) Tại cực đại, hiệu suất nguồn là 100%.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: khi R=r thì $H=R/(R+r)=1/2=50\%$.'''),
        short(r'''Nguồn $9$ V, $r=1\,\Omega$ nối với $R=8\,\Omega$. Tính I, U ngoài và hiệu suất.''', r'''$I=9/(8+1)=1$ A. $U=IR=8$ V. $H=U/\mathcal E=8/9\approx88,9\%$.'''),
        short(r'''Nguồn có $\mathcal E=6$ V, r chưa biết. Mắc R=$5\,\Omega$ thì I=$1$ A. Tính r.''', r'''$R+r=\mathcal E/I=6\,\Omega$, nên $r=1\,\Omega$.'''),
        short(r'''Nguồn $12$ V, $r=3\,\Omega$. Tìm R để công suất mạch ngoài cực đại và giá trị cực đại.''', r'''Cực đại khi $R=r=3\,\Omega$. $P_{max}=\mathcal E^2/(4r)=144/12=12$ W.'''),
        applied(r'''Nguồn có $\mathcal E=10$ V, $r=1\,\Omega$. Mạch ngoài là biến trở R. Tìm hai giá trị R để công suất trên R bằng $16$ W.''', r'''Ta có

$P_R=\frac{\mathcal E^2R}{(R+r)^2}=\frac{100R}{(R+1)^2}=16$.

Suy ra $100R=16(R^2+2R+1)$,

$16R^2-68R+16=0$, chia 4: $4R^2-17R+4=0$.

$R=[17\pm\sqrt{289-64}]/8=[17\pm15]/8$.

Vậy $R=4\,\Omega$ hoặc $R=0,25\,\Omega$. Hai giá trị có tích $R_1R_2=r^2=1$, phù hợp tính chất đối xứng của bài cực trị công suất.''')
    ]

def l6():
    return [
        mcq(r'''Ba nguồn giống nhau, mỗi nguồn có suất điện động E và điện trở trong r, ghép nối tiếp cùng chiều. Bộ nguồn có

A. $\mathcal E_b=E$, $r_b=3r$.  
B. $\mathcal E_b=3E$, $r_b=3r$.  
C. $\mathcal E_b=3E$, $r_b=r/3$.  
D. $\mathcal E_b=E/3$, $r_b=r/3$.''', r'''Chọn **B**.'''),
        mcq(r'''Ba nguồn giống nhau ghép song song đúng cực. Bộ nguồn có

A. $\mathcal E_b=E$, $r_b=r/3$.  
B. $\mathcal E_b=3E$, $r_b=r/3$.  
C. $\mathcal E_b=E/3$, $r_b=3r$.  
D. $\mathcal E_b=3E$, $r_b=3r$.''', r'''Chọn **A**.'''),
        mcq(r'''Ghép nối tiếp nguồn giống nhau phù hợp khi cần

A. tăng suất điện động bộ.  
B. giữ suất điện động bằng một nguồn và giảm điện trở trong.  
C. làm suất điện động bằng 0 trong mọi trường hợp.  
D. chỉ để trang trí mạch.''', r'''Chọn **A**.'''),
        mcq(r'''Ghép song song các nguồn giống nhau đúng cực thường nhằm

A. tăng suất điện động lên n lần.  
B. giảm điện trở trong tương đương.  
C. đảo cực mọi nguồn.  
D. làm r tăng n lần.''', r'''Chọn **B**.'''),
        tf(r'''Với n nguồn giống nhau:

a) Nối tiếp: $\mathcal E_b=n\mathcal E$, $r_b=nr$.  
b) Song song: $\mathcal E_b=\mathcal E$, $r_b=r/n$.  
c) Ghép song song tùy ý các nguồn có suất điện động rất khác nhau luôn an toàn.  
d) Khi thiết kế bộ hỗn hợp đối xứng cần xét cả suất điện động và điện trở trong.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: có thể xuất hiện dòng tuần hoàn lớn giữa nguồn.  
d) **Đúng**.'''),
        tf(r'''Bộ gồm m nhánh song song, mỗi nhánh có n nguồn giống nhau mắc nối tiếp:

a) Tổng số nguồn N=mn.  
b) Suất điện động mỗi nhánh là $n\mathcal E$.  
c) Điện trở trong bộ là $nr/m$.  
d) Suất điện động bộ là $m\mathcal E$.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: các nhánh song song cùng suất điện động $n\mathcal E$, nên suất điện động bộ bằng $n\mathcal E$.'''),
        short(r'''Bốn pin giống nhau, mỗi pin $1,5$ V, $r=0,5\,\Omega$, ghép nối tiếp. Tính $\mathcal E_b$, $r_b$.''', r'''$\mathcal E_b=4\cdot1,5=6$ V; $r_b=4\cdot0,5=2\,\Omega$.'''),
        short(r'''Bốn pin giống nhau như trên ghép song song. Tính $\mathcal E_b$, $r_b$.''', r'''$\mathcal E_b=1,5$ V; $r_b=0,5/4=0,125\,\Omega$.'''),
        short(r'''Sáu nguồn giống nhau $\mathcal E=2$ V, $r=1\,\Omega$ ghép thành 2 nhánh song song, mỗi nhánh 3 nguồn nối tiếp. Tính bộ nguồn.''', r'''Mỗi nhánh: $\mathcal E_n=3\cdot2=6$ V, $r_n=3\,\Omega$. Hai nhánh song song giống nhau: $\mathcal E_b=6$ V, $r_b=3/2=1,5\,\Omega$.'''),
        applied(r'''Có 12 nguồn giống nhau, mỗi nguồn $\mathcal E=1,5$ V, $r=0,5\,\Omega$. Ghép thành m nhánh song song giống nhau, mỗi nhánh n nguồn nối tiếp, mn=12. Mạch ngoài R=$2\,\Omega$. So sánh dòng mạch chính cho các phương án n=1,2,3,4,6,12 và chọn phương án lớn nhất.''', r'''Với cấu hình n nguồn nối tiếp mỗi nhánh và m=12/n nhánh song song:

$\mathcal E_b=1,5n$, $r_b=nr/m=n^2r/12=n^2/24\,\Omega$.

$I=\frac{1,5n}{2+n^2/24}$.

Tính nhanh:

- n=1: $I\approx0,735$ A.
- n=2: $I\approx1,385$ A.
- n=3: $I\approx1,895$ A.
- n=4: $I=6/(2+2/3)=2,25$ A.
- n=6: $I=9/(2+1,5)=2,571$ A.
- n=12: $I=18/(2+6)=2,25$ A.

Trong các phương án nguyên cho trước, **n=6, m=2** cho dòng lớn nhất. Kết quả phù hợp nguyên tắc tối ưu khi điện trở trong bộ gần điện trở ngoài.''')
    ]

def l7():
    return [
        mcq(r'''Ampe kế lí tưởng có điện trở

A. bằng 0.  
B. vô hạn.  
C. bằng 1 Ω.  
D. thay đổi tùy dòng.''', r'''Chọn **A**.'''),
        mcq(r'''Vôn kế lí tưởng có điện trở

A. bằng 0.  
B. rất nhỏ.  
C. vô hạn.  
D. bằng điện trở mạch.''', r'''Chọn **C**.'''),
        mcq(r'''Hai điểm nối trực tiếp bằng dây dẫn lí tưởng, không có phần tử giữa chúng, được xem là

A. khác điện thế bất kì.  
B. cùng một nút điện thế.  
C. luôn có dòng bằng 0.  
D. luôn hở mạch.''', r'''Chọn **B**.'''),
        mcq(r'''Vôn kế lí tưởng mắc nối tiếp trong mạch sẽ gần như

A. ngắn mạch.  
B. làm hở nhánh đó.  
C. không ảnh hưởng.  
D. tăng dòng vô hạn.''', r'''Chọn **B** vì điện trở vô hạn.'''),
        tf(r'''Khi đọc mạch:

a) Dây nối lí tưởng có thể dùng để nhận diện các điểm cùng điện thế.  
b) Ampe kế lí tưởng được thay bằng dây dẫn.  
c) Vôn kế lí tưởng được thay bằng nhánh hở khi tính dòng mạch chính.  
d) Hai điện trở có một đầu chung thì chắc chắn mắc song song.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: muốn song song phải chung cả hai nút đầu cuối.'''),
        tf(r'''Mạch có R1 và R2 nối tiếp:

a) Dòng qua hai điện trở bằng nhau.  
b) Hiệu điện thế phân chia tỉ lệ điện trở.  
c) Vôn kế lí tưởng đo áp trên R1 nếu mắc song song hai đầu R1.  
d) Ampe kế lí tưởng phải mắc song song R1 để đo dòng qua R1.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: ampe kế phải mắc nối tiếp với nhánh cần đo.'''),
        short(r'''R1=$4\,\Omega$, R2=$6\,\Omega$ nối tiếp vào 20 V. Ampe kế lí tưởng nối tiếp mạch chỉ bao nhiêu? Vôn kế lí tưởng mắc hai đầu R2 chỉ bao nhiêu?''', r'''$R_t=10\,\Omega$, $I=20/10=2$ A. Vôn kế trên R2: $U_2=IR_2=12$ V.'''),
        short(r'''R1=$6\,\Omega$, R2=$3\,\Omega$ song song dưới 12 V. Tính dòng mạch chính và dòng mỗi nhánh.''', r'''$I_1=12/6=2$ A; $I_2=12/3=4$ A. Dòng chính $I=6$ A.'''),
        short(r'''Một mạch có R1=$2\,\Omega$ nối tiếp với bộ song song R2=$3\,\Omega$, R3=$6\,\Omega$. Đặt 12 V. Tính dòng qua từng điện trở.''', r'''$R_{23}=3\cdot6/(3+6)=2\,\Omega$. Tổng $R=4\,\Omega$, dòng chính và qua R1: $I_1=3$ A. Điện áp trên bộ song song $U_{23}=3\cdot2=6$ V. $I_2=6/3=2$ A; $I_3=6/6=1$ A.'''),
        applied(r'''Mạch cầu gồm bốn điện trở: R1=2 Ω, R2=4 Ω ở nhánh trên; R3=3 Ω, R4=6 Ω ở nhánh dưới, nối giữa cùng hai nút nguồn. Một vôn kế lí tưởng nối giữa hai điểm giữa hai nhánh. Chứng minh vôn kế chỉ 0.''', r'''Hai nhánh là các bộ chia điện áp độc lập vì vôn kế lí tưởng không lấy dòng.

Điểm giữa nhánh trên có tỉ phần điện áp theo R1:R2 = 2:4 = 1:2. Nhánh dưới có R3:R4 = 3:6 = 1:2. Vì tỉ số giống nhau, điện thế tại hai điểm giữa bằng nhau.

Có thể viết điều kiện cầu cân bằng:

$R_1/R_2=R_3/R_4$.

Ở đây $2/4=3/6=1/2$, nên $U_V=0$.''')
    ]

def l8():
    return [
        mcq(r'''Định luật nút Kirchhoff dựa trên

A. bảo toàn điện tích.  
B. bảo toàn khối lượng cơ học.  
C. định luật phản xạ ánh sáng.  
D. lực Lorentz.''', r'''Chọn **A**: tổng dòng vào nút bằng tổng dòng ra ở trạng thái ổn định.'''),
        mcq(r'''Định luật vòng Kirchhoff phát biểu tổng đại số các độ tăng và sụt điện thế quanh một vòng kín bằng

A. 1.  
B. 0.  
C. vô hạn.  
D. dòng điện.''', r'''Chọn **B**.'''),
        mcq(r'''Định lí Thévenin cho phép thay mạng tuyến tính nhìn từ hai cực bằng

A. một nguồn áp Thévenin nối tiếp điện trở Thévenin.  
B. chỉ một điện trở bằng 0.  
C. chỉ một tụ điện.  
D. một nguồn dòng nối tiếp điện trở.''', r'''Chọn **A**.'''),
        mcq(r'''Trong trạng thái xác lập DC lâu dài, tụ điện lí tưởng trong nhánh mạch được xem gần như

A. dây dẫn ngắn mạch.  
B. nhánh hở đối với dòng một chiều.  
C. nguồn dòng.  
D. điện trở âm.''', r'''Chọn **B**.'''),
        tf(r'''Về phương pháp mạch nâng cao:

a) Kirchhoff dùng được cho mạng nhiều vòng.  
b) Xếp chồng áp dụng cho mạng tuyến tính với nhiều nguồn độc lập.  
c) Khi “tắt” nguồn áp lí tưởng trong xếp chồng, thay nó bằng ngắn mạch.  
d) Khi “tắt” nguồn dòng lí tưởng, thay bằng ngắn mạch.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: nguồn dòng lí tưởng bị thay bằng hở mạch.'''),
        tf(r'''Tụ điện trong mạch DC:

a) Ngay sau thao tác đóng/ngắt, điện áp trên tụ không thể nhảy đột ngột trong mô hình lí tưởng nếu không có dòng xung vô hạn.  
b) Ở xác lập lâu dài, dòng qua tụ bằng 0.  
c) Năng lượng tụ là $\frac12CU^2$.  
d) Tụ luôn tương đương ngắn mạch ở mọi thời điểm.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**.'''),
        short(r'''Tại một nút có dòng $I_1=2$ A và $I_2=1,5$ A đi vào; dòng $I_3=0,8$ A đi ra và dòng I4 chưa biết đi ra. Tính I4.''', r'''Bảo toàn điện tích tại nút: $I_1+I_2=I_3+I_4$. $I_4=2+1,5-0,8=2,7$ A.'''),
        short(r'''Một nguồn Thévenin có $V_{th}=12$ V, $R_{th}=3\,\Omega$ cấp tải $R_L=9\,\Omega$. Tính dòng và áp tải.''', r'''$I=V_{th}/(R_{th}+R_L)=12/12=1$ A. $U_L=IR_L=9$ V.'''),
        short(r'''Tụ $C=100\,\mu$F được nạp đến 20 V. Tính điện tích và năng lượng trước khi chuyển mạch.''', r'''$Q=CU=100\cdot10^{-6}\cdot20=2\cdot10^{-3}$ C. $W=\frac12CU^2=0,5\cdot100\cdot10^{-6}\cdot400=0,020$ J.'''),
        applied(r'''Mạch hai vòng có một nguồn 12 V. Vòng trái gồm nguồn và R1=2 Ω; điện trở chung giữa hai vòng R3=4 Ω; vòng phải có R2=6 Ω. Chọn dòng vòng I1 theo chiều kim đồng hồ ở vòng trái và I2 theo chiều kim đồng hồ ở vòng phải, nên dòng qua R3 theo hướng vòng trái là I1-I2. Lập và giải hệ dòng vòng.''', r'''Phương trình vòng trái:

$12-2I_1-4(I_1-I_2)=0$, hay $6I_1-4I_2=12$.

Vòng phải không có nguồn:

$-6I_2-4(I_2-I_1)=0$, hay $-4I_1+10I_2=0$.

Từ phương trình hai: $I_1=2,5I_2$. Thay vào phương trình một:

$6(2,5I_2)-4I_2=12\Rightarrow11I_2=12$.

$I_2=12/11\approx1,091$ A; $I_1=30/11\approx2,727$ A.

Dòng qua R3 theo hướng vòng trái: $I_3=I_1-I_2=18/11\approx1,636$ A.''')
    ]

def l9():
    return [
        mcq(r'''Khi đo quan hệ U–I của nguồn đang phát điện, đồ thị lí tưởng có dạng

A. $U=\mathcal E-rI$.  
B. $U=\mathcal E+rI$.  
C. $U=r/I$.  
D. $U=0$ mọi I.''', r'''Chọn **A**.'''),
        mcq(r'''Trên đồ thị U theo I của nguồn, tung độ gốc biểu diễn

A. điện trở ngoài.  
B. suất điện động $\mathcal E$.  
C. công suất.  
D. điện lượng.''', r'''Chọn **B**.'''),
        mcq(r'''Độ lớn hệ số góc của đường thẳng U–I bằng

A. $\mathcal E$.  
B. r.  
C. R ngoài.  
D. I ngắn mạch.''', r'''Chọn **B** vì hệ số góc là $-r$.'''),
        mcq(r'''Trong thí nghiệm, thao tác nào không an toàn cho nguồn thực?

A. Thay đổi biến trở để lấy nhiều điểm U–I.  
B. Đo U và I trong giới hạn dụng cụ.  
C. Nối tắt trực tiếp nguồn trong thời gian dài để đo dòng ngắn mạch.  
D. Mở khóa K giữa các lần chỉnh mạch.''', r'''Chọn **C** vì dòng ngắn mạch có thể rất lớn và làm nóng/hỏng nguồn, dây, dụng cụ.'''),
        tf(r'''Thí nghiệm xác định $\mathcal E,r$:

a) Cần đo nhiều cặp (I,U) để giảm ảnh hưởng sai số.  
b) Có thể lấy $\mathcal E$ từ giao điểm trục U.  
c) r lấy từ độ lớn độ dốc của đồ thị U theo I.  
d) Chỉ cần một cặp U,I bất kì là luôn xác định được cả $\mathcal E$ và r mà không có dữ kiện khác.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: một phương trình $U=\mathcal E-rI$ có hai ẩn.'''),
        tf(r'''Với nguồn đang phát điện:

a) U giảm gần tuyến tính khi I tăng nếu $\mathcal E,r$ không đổi.  
b) I=0 cho U=$\mathcal E$.  
c) Giao điểm trục I của đường kéo dài là $I_{sc}=\mathcal E/r$.  
d) Nên luôn trực tiếp đo I_sc để chính xác nhất.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng** về mô hình.  
d) **Sai** vì nguy cơ ngắn mạch; thường suy ra từ đường thẳng an toàn hơn.'''),
        short(r'''Hai điểm đo: $(I_1,U_1)=(0,5\text{ A},5,7\text{ V})$ và $(I_2,U_2)=(1,5\text{ A},5,1\text{ V})$. Tính r và $\mathcal E$.''', r'''Từ $U=\mathcal E-rI$: $r=(U_1-U_2)/(I_2-I_1)=(5,7-5,1)/(1,5-0,5)=0,6\,\Omega$. $\mathcal E=U_1+rI_1=5,7+0,6\cdot0,5=6,0$ V.'''),
        short(r'''Đồ thị U–I đi qua $(0,6\text{ A},8,7\text{ V})$ và $(1,8\text{ A},8,1\text{ V})$. Tính $\mathcal E,r$.''', r'''$r=(8,7-8,1)/(1,8-0,6)=0,5\,\Omega$. $\mathcal E=8,7+0,5\cdot0,6=9,0$ V.'''),
        short(r'''Nguồn có $\mathcal E=3,0$ V, $r=0,40\,\Omega$. Dự đoán U khi I=2,0 A.''', r'''$U=3,0-0,40\cdot2,0=2,2$ V.'''),
        applied(r'''Bốn cặp số đo $(I,U)$ là: (0,5 A; 5,82 V), (1,0 A; 5,61 V), (1,5 A; 5,39 V), (2,0 A; 5,20 V). Hãy ước tính r và $\mathcal E$ bằng cách dùng hai điểm đầu–cuối, sau đó kiểm tra hai điểm giữa có phù hợp gần đúng không.''', r'''Dùng đầu–cuối:

$r\approx(5,82-5,20)/(2,0-0,5)=0,62/1,5\approx0,413\,\Omega$.

$\mathcal E\approx U+rI=5,82+0,413\cdot0,5\approx6,03$ V.

Dự đoán tại I=1,0 A: $U\approx6,03-0,413=5,62$ V, rất gần 5,61 V.

Tại I=1,5 A: $U\approx6,03-0,620=5,41$ V, gần 5,39 V.

Các điểm phù hợp với mô hình tuyến tính trong sai số đo nhỏ. Khi làm thực nghiệm thật, nên hồi quy tuyến tính toàn bộ dữ liệu thay vì chỉ hai điểm.''')
    ]

def l10():
    return [
        mcq(r'''Trong trạng thái xác lập DC, một tụ điện lí tưởng mắc nối tiếp trong một nhánh làm dòng nhánh

A. khác 0 không đổi.  
B. bằng 0.  
C. vô hạn.  
D. bằng điện dung.''', r'''Chọn **B** sau khi quá trình nạp đã kết thúc.'''),
        mcq(r'''Máy thu điện có suất phản điện $\mathcal E'$ và điện trở trong r, nhận dòng I vào cực dương. Hiệu điện thế hai đầu thường thỏa

A. $U=\mathcal E'-Ir$.  
B. $U=\mathcal E'+Ir$.  
C. $U=Ir-\mathcal E'$ luôn.  
D. $U=0$.''', r'''Chọn **B** trong quy ước máy thu: điện áp ngoài phải thắng suất phản điện và sụt áp trong.'''),
        mcq(r'''Công suất có ích điện–cơ của máy thu lí tưởng mô hình bằng suất phản điện là

A. $P_{ích}=\mathcal E'I$.  
B. $P_{ích}=I^2r$.  
C. $P_{ích}=U/I$.  
D. $P_{ích}=0$.''', r'''Chọn **A**; tổn hao Joule trong máy thu là $I^2r$.'''),
        mcq(r'''Một nguồn đang được nạp điện có dòng đi vào cực dương. Khi đó nó hoạt động về mặt mạch như

A. nguồn phát.  
B. máy thu.  
C. điện trở thuần không có suất điện động.  
D. tụ hở mạch.''', r'''Chọn **B**.'''),
        tf(r'''Đoạn mạch có nguồn/máy thu/tụ:

a) Cần chọn chiều dòng và quy ước dấu nhất quán.  
b) Máy thu nhận điện năng và có thể biến một phần thành cơ năng/hóa năng.  
c) Ở xác lập DC, tụ lí tưởng không mang điện tích.  
d) Sau khi nạp, tụ có thể có hiệu điện thế dù dòng qua nhánh bằng 0.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Sai**: tụ có thể tích điện.  
d) **Đúng**.'''),
        tf(r'''Máy thu có $U=\mathcal E'+Ir$:

a) Công suất điện nhận là UI.  
b) Công suất có ích mô hình là $\mathcal E'I$.  
c) Tổn hao trong là $I^2r$.  
d) Hiệu suất bằng $U/\mathcal E'$.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: hiệu suất phần có ích là $\eta=\mathcal E'I/(UI)=\mathcal E'/U<1$.'''),
        short(r'''Máy thu có $\mathcal E'=8$ V, $r=1\,\Omega$, dòng vào cực dương $I=2$ A. Tính U hai đầu máy thu.''', r'''$U=\mathcal E'+Ir=8+2\cdot1=10$ V.'''),
        short(r'''Máy thu trên nhận dòng 2 A. Tính công suất điện nhận, công suất có ích và công suất tỏa nhiệt.''', r'''$P_{vào}=UI=10\cdot2=20$ W. $P_{ích}=\mathcal E'I=8\cdot2=16$ W. $P_{hao}=I^2r=4$ W. Kiểm tra $20=16+4$.'''),
        short(r'''Tụ $C=20\,\mu$F mắc song song với điện trở R trong mạch DC. Ở xác lập, hiệu điện thế trên R là 12 V. Tính điện tích của tụ.''', r'''Song song nên U tụ bằng 12 V. $Q=CU=20\cdot10^{-6}\cdot12=240\,\mu$C.'''),
        applied(r'''Nguồn phát $\mathcal E=18$ V, $r=1\,\Omega$ nối nối tiếp với máy thu có $\mathcal E'=10$ V, $r'=2\,\Omega$ và điện trở ngoài $R=5\,\Omega$. Dòng đi từ nguồn phát qua máy thu vào cực dương của máy thu. Tính dòng và hiệu suất của máy thu.''', r'''Viết phương trình vòng theo chiều dòng. Suất điện động nguồn phát đẩy dòng, suất phản điện máy thu chống lại:

$I=\frac{\mathcal E-\mathcal E'}{R+r+r'}=\frac{18-10}{5+1+2}=1$ A.

Điện áp hai đầu máy thu:

$U_{thu}=\mathcal E'+Ir'=10+1\cdot2=12$ V.

Công suất vào máy thu $P_{vào}=12$ W; công suất có ích $P_{ích}=\mathcal E'I=10$ W.

Hiệu suất máy thu $\eta=P_{ích}/P_{vào}=10/12\approx83,3\%$.''')
    ]

LESSONS={
'01-current-intensity.md': l1(),
'02-resistance-ohm-law.md': l2(),
'03-emf-internal-resistance.md': l3(),
'04-energy-power-joule.md': l4(),
'05-full-circuit-ohm-law.md': l5(),
'06-source-combinations.md': l6(),
'07-circuit-reading-meters.md': l7(),
'08-advanced-circuit-methods.md': l8(),
'09-practical-emf-internal-resistance.md': l9(),
'10-source-receiver-capacitor-branches.md': l10(),
}

if __name__=='__main__':
    for lf, probs in LESSONS.items():
        write_lesson_practice(CH, lf, probs)
        add_practice_links(CH, lf)
    write_practice_index(CH, list(LESSONS))
    print('chapter 4', sum(len(v) for v in LESSONS.values()), 'problems')
