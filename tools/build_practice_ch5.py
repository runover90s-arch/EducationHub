from practice_bank_common import *
import math

CH='05-current-media'

def l1():
    return [
        mcq(r'''Hạt tải điện chủ yếu trong kim loại là

A. proton tự do.  
B. electron tự do.  
C. neutron.  
D. ion dương chuyển động tự do như trong dung dịch.''', r'''Chọn **B**.'''),
        mcq(r'''Với kim loại thông thường, điện trở tăng khi nhiệt độ tăng chủ yếu vì

A. mật độ va chạm của electron dẫn với mạng tinh thể tăng.  
B. electron biến mất.  
C. điện tích electron tăng.  
D. dây dài ra vô hạn.''', r'''Chọn **A** trong mô hình cổ điển phổ thông.'''),
        mcq(r'''Dây có điện trở $R_0=10\,\Omega$ ở $20^\circ$C, $\alpha=0,004$ K⁻¹. Ở $70^\circ$C, R gần bằng

A. $8\,\Omega$.  
B. $10\,\Omega$.  
C. $12\,\Omega$.  
D. $20\,\Omega$.''', r'''Chọn **C**. $R=10[1+0,004(70-20)]=12\,\Omega$.'''),
        tf(r'''Dòng điện trong kim loại:

a) Electron có chuyển động nhiệt hỗn loạn và chuyển động trôi có hướng.  
b) Chiều dòng điện quy ước ngược chiều trôi của electron.  
c) Điện trở suất là đại lượng đặc trưng vật liệu ở một nhiệt độ xác định.  
d) Mọi kim loại có điện trở bằng 0 ở nhiệt độ phòng.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**.'''),
        short(r'''Dây dài $5$ m, tiết diện $1$ mm², điện trở suất $1,7\cdot10^{-8}\,\Omega$m. Tính R.''', r'''$R=\rho l/S=1,7\cdot10^{-8}\cdot5/10^{-6}=0,085\,\Omega$.'''),
        short(r'''Một dây có R=$50\,\Omega$ ở $0^\circ$C và R=$60\,\Omega$ ở $100^\circ$C. Giả sử phụ thuộc tuyến tính, tính hệ số nhiệt điện trở α theo mốc $0^\circ$C.''', r'''$60=50(1+100\alpha)$. Suy ra $1+100\alpha=1,2$, nên $\alpha=0,002$ K⁻¹.'''),
        short(r'''Hai dây cùng vật liệu, cùng chiều dài; dây 2 có đường kính gấp đôi dây 1. So sánh điện trở.''', r'''Tiết diện tỉ lệ bình phương đường kính, nên $S_2=4S_1$. Vì $R\propto1/S$, $R_2=R_1/4$.'''),
        applied(r'''Một dây kim loại có R=$20\,\Omega$ ở $20^\circ$C, hệ số nhiệt $0,004$ K⁻¹. Dây mắc vào nguồn áp không đổi 12 V. Bỏ qua thay đổi nguồn. Tính dòng ở $20^\circ$C và $120^\circ$C, rồi nhận xét.''', r'''Ở $20^\circ$C: $I_{20}=12/20=0,60$ A.

Ở $120^\circ$C: $R=20[1+0,004(100)]=28\,\Omega$.

$I_{120}=12/28\approx0,429$ A.

Khi nhiệt độ tăng, điện trở kim loại tăng nên với nguồn áp cố định, dòng giảm.''')
    ]

def l2():
    return [
        mcq(r'''Hạt tải điện trong chất điện phân là

A. chỉ electron tự do.  
B. ion dương và ion âm.  
C. neutron.  
D. photon.''', r'''Chọn **B**.'''),
        mcq(r'''Khối lượng chất giải phóng ở điện cực theo định luật Faraday tỉ lệ với

A. điện lượng qua bình.  
B. bình phương điện lượng.  
C. nghịch đảo điện lượng.  
D. chỉ điện áp, không phụ thuộc dòng.''', r'''Chọn **A**.'''),
        mcq(r'''Nếu dòng điện qua bình điện phân tăng gấp đôi, thời gian không đổi, khối lượng bám điện cực trong cùng điều kiện sẽ

A. giảm 2 lần.  
B. không đổi.  
C. tăng 2 lần.  
D. tăng 4 lần.''', r'''Chọn **C** vì $m\propto It$.'''),
        tf(r'''Điện phân:

a) Dòng điện gắn với sự chuyển dời có hướng của ion.  
b) Phản ứng hóa học có thể xảy ra ở điện cực.  
c) Định luật Faraday liên hệ khối lượng giải phóng với điện lượng.  
d) Không có sự vận chuyển vật chất trong dung dịch.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**.'''),
        short(r'''Một bình có đương lượng điện hóa $k_e=3,3\cdot10^{-7}$ kg/C. Dòng $2$ A chạy trong $15$ phút. Tính khối lượng chất bám.''', r'''$t=900$ s. $m=k_eIt=3,3\cdot10^{-7}\cdot2\cdot900=5,94\cdot10^{-4}$ kg $=0,594$ g.'''),
        short(r'''Muốn mạ $1,0$ g kim loại với đương lượng điện hóa $2,0\cdot10^{-7}$ kg/C bằng dòng 2,5 A. Tính thời gian.''', r'''$m=10^{-3}$ kg. $t=m/(k_eI)=10^{-3}/(2,0\cdot10^{-7}\cdot2,5)=2000$ s $\approx33,3$ phút.'''),
        short(r'''Hai bình điện phân mắc nối tiếp nên cùng dòng và cùng thời gian. Đương lượng điện hóa bình 1 gấp 1,5 lần bình 2. So sánh khối lượng bám.''', r'''Vì $m=k_eIt$ và It như nhau, $m_1/m_2=k_{e1}/k_{e2}=1,5$.'''),
        applied(r'''Một bình điện phân bạc dùng $A=108$ g/mol, hóa trị n=1, Faraday $F=96500$ C/mol. Dòng 1,5 A chạy 30 phút. Tính khối lượng bạc bám.''', r'''Định luật Faraday:

$m=\frac{A}{nF}It$.

$t=1800$ s, $It=2700$ C.

$m=\frac{108}{96500}\cdot2700\text{ g}\approx3,02$ g.

Ta dùng A theo g/mol nên kết quả trực tiếp ra gam.''')
    ]

def l3():
    return [
        mcq(r'''Trong điều kiện thường, chất khí dẫn điện kém vì

A. hầu hết phân tử trung hòa, rất ít hạt tải tự do.  
B. có quá nhiều electron tự do.  
C. điện trở bằng 0.  
D. ion không tồn tại trong mọi trường hợp.''', r'''Chọn **A**.'''),
        mcq(r'''Quá trình tạo ion và electron tự do trong chất khí gọi là

A. ngưng tụ.  
B. ion hóa.  
C. kết tinh.  
D. phân cực cơ học.''', r'''Chọn **B**.'''),
        mcq(r'''Hồ quang điện đặc trưng bởi

A. dòng rất nhỏ và không phát sáng.  
B. dòng tương đối lớn, phát sáng mạnh giữa hai điện cực.  
C. chỉ xảy ra trong chân không tuyệt đối.  
D. không có ion hóa.''', r'''Chọn **B**.'''),
        tf(r'''Dòng điện trong chất khí:

a) Cần có hạt tải điện tự do.  
b) Tia tử ngoại, nhiệt độ cao hoặc va chạm có thể gây ion hóa.  
c) Phóng điện tia lửa thường liên quan điện trường mạnh.  
d) Chất khí đã ion hóa hoàn toàn không chịu tác dụng điện trường.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**.'''),
        short(r'''Một ống khí có dòng $2$ mA trong $10$ s. Tính điện lượng chuyển qua tiết diện.''', r'''$q=It=2\cdot10^{-3}\cdot10=0,020$ C.'''),
        short(r'''Nêu hai cơ chế có thể tạo hạt tải điện trong chất khí trong nội dung phổ thông.''', r'''Có thể nêu: **ion hóa do tác nhân ngoài** (tia tử ngoại, bức xạ, nhiệt) và **ion hóa do va chạm** khi hạt mang điện được gia tốc đủ mạnh va vào phân tử khí.'''),
        short(r'''Phân biệt ngắn gọn phóng điện tia lửa và hồ quang điện theo điều kiện/cường độ dòng.''', r'''Tia lửa thường là phóng điện ngắn trong điện trường rất mạnh, có thể không duy trì liên tục. Hồ quang là phóng điện tự duy trì với dòng lớn hơn, nhiệt độ và độ phát sáng cao giữa các điện cực.'''),
        applied(r'''Một khe khí dài 5 mm bắt đầu phóng điện khi hiệu điện thế đạt khoảng 15 kV. Ước tính cường độ điện trường trung bình lúc đánh thủng và giải thích vì sao đây chỉ là ước tính.''', r'''$E\approx U/d=15\cdot10^3/(5\cdot10^{-3})=3\cdot10^6$ V/m.

Đây chỉ là ước tính vì điện trường thực tế có thể không đều, ngưỡng đánh thủng phụ thuộc áp suất, nhiệt độ, hình dạng điện cực, độ ẩm và thành phần khí.''')
    ]

def l4():
    return [
        mcq(r'''Bán dẫn tinh khiết có hạt tải điện là

A. chỉ electron.  
B. chỉ lỗ trống.  
C. electron và lỗ trống.  
D. proton tự do.''', r'''Chọn **C**.'''),
        mcq(r'''Bán dẫn loại n có hạt tải đa số là

A. lỗ trống.  
B. electron.  
C. proton.  
D. ion âm chuyển động tự do.''', r'''Chọn **B**.'''),
        mcq(r'''Điốt bán dẫn có tính chất cơ bản

A. dẫn tốt như nhau theo hai chiều.  
B. chỉnh lưu: dẫn thuận tốt hơn dẫn ngược.  
C. không bao giờ dẫn điện.  
D. chỉ hoạt động trong chân không.''', r'''Chọn **B**.'''),
        tf(r'''Bán dẫn:

a) Độ dẫn điện nằm giữa chất dẫn tốt và chất cách điện điển hình.  
b) Nhiệt độ có thể ảnh hưởng mạnh mật độ hạt tải.  
c) Pha tạp có thể tạo bán dẫn loại n hoặc p.  
d) Lỗ trống là một proton tự do nằm trong mạng tinh thể.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**: lỗ trống là mô hình trạng thái thiếu electron liên kết, không phải proton tự do.'''),
        short(r'''Nêu hạt tải đa số và thiểu số trong bán dẫn loại n.''', r'''Loại n: **electron là hạt tải đa số**, lỗ trống là hạt tải thiểu số.'''),
        short(r'''Nêu hạt tải đa số và thiểu số trong bán dẫn loại p.''', r'''Loại p: **lỗ trống là hạt tải đa số**, electron là hạt tải thiểu số.'''),
        short(r'''Một điốt được mắc thuận và dòng tăng mạnh sau ngưỡng đặc trưng. Nếu đảo cực, dòng rất nhỏ. Hiện tượng này minh họa tính chất nào?''', r'''Minh họa **tính chỉnh lưu** của tiếp giáp p–n: dẫn thuận mạnh hơn nhiều so với dẫn ngược trong điều kiện làm việc bình thường.'''),
        applied(r'''Một điện trở 1 kΩ nối tiếp điốt silic được phân cực thuận với nguồn 5 V. Lấy sụt áp thuận điốt xấp xỉ 0,7 V. Ước tính dòng mạch.''', r'''Điện áp trên điện trở $U_R\approx5-0,7=4,3$ V.

$I\approx U_R/R=4,3/1000=4,3$ mA.

Mô hình 0,7 V là gần đúng phổ thông; giá trị thật phụ thuộc dòng và nhiệt độ.''')
    ]

def l5():
    return [
        mcq(r'''Trong ống chân không, dòng điện có thể được tạo bởi

A. electron phát ra từ catot rồi chuyển động về anot.  
B. proton bay khỏi anot trong mọi trường hợp.  
C. ion dung dịch.  
D. sóng cơ.''', r'''Chọn **A**.'''),
        mcq(r'''Phát xạ nhiệt electron xảy ra khi

A. kim loại catot được nung nóng đủ.  
B. làm lạnh catot về 0 K.  
C. không có electron.  
D. chỉ khi có nước.''', r'''Chọn **A**.'''),
        mcq(r'''Tia catot trong ống chân không là dòng

A. electron năng lượng cao.  
B. neutron.  
C. photon nhìn thấy duy nhất.  
D. ion dương trong dung dịch.''', r'''Chọn **A**.'''),
        tf(r'''Dòng điện trong chân không và tế bào quang điện:

a) Chân không không có hạt tải sẵn đáng kể nên cần cơ chế phát electron từ điện cực.  
b) Electron có thể bị điện trường gia tốc trong chân không.  
c) Tế bào quang điện có thể biến tín hiệu ánh sáng thành tín hiệu điện.  
d) Tia catot là sóng âm.''', r'''a) **Đúng**.  
b) **Đúng**.  
c) **Đúng**.  
d) **Sai**.'''),
        short(r'''Electron tăng tốc qua hiệu điện thế 2 kV. Tính động năng thu được theo eV.''', r'''Electron thu được động năng $2000$ eV = $2$ keV.'''),
        short(r'''Đổi $2$ keV sang joule, lấy $1$ eV=$1,6\cdot10^{-19}$ J.''', r'''$2$ keV = $2000$ eV, nên $K=2000\cdot1,6\cdot10^{-19}=3,2\cdot10^{-16}$ J.'''),
        short(r'''Một tế bào quang điện tạo dòng $20\,\mu$A khi chiếu sáng ổn định. Trong 1 s có điện lượng bao nhiêu qua mạch?''', r'''$q=It=20\cdot10^{-6}\cdot1=20\,\mu$C.'''),
        applied(r'''Electron được gia tốc từ nghỉ qua 5 kV trong chân không. Tính tốc độ theo cơ học cổ điển, dùng $e=1,6\cdot10^{-19}$ C, $m_e=9,1\cdot10^{-31}$ kg. Nhận xét mô hình.''', r'''$\frac12m_ev^2=eU$.

$v=\sqrt{2eU/m_e}=\sqrt{2\cdot1,6\cdot10^{-19}\cdot5000/(9,1\cdot10^{-31})}\approx4,19\cdot10^7$ m/s.

Giá trị khoảng $0,14c$, nên cơ học cổ điển vẫn cho ước tính tương đối hợp lí nhưng khi điện áp tăng rất cao cần xét hiệu ứng tương đối tính.''')
    ]

LESSONS={
'01-current-in-metals.md': l1(),
'02-electrolytes-faraday.md': l2(),
'03-current-in-gases.md': l3(),
'04-semiconductors.md': l4(),
'05-vacuum-photoelectric-cell.md': l5(),
}

if __name__=='__main__':
    for lf, probs in LESSONS.items():
        write_lesson_practice(CH, lf, probs)
        add_practice_links(CH, lf)
    write_practice_index(CH, list(LESSONS))
    print('chapter 5', sum(len(v) for v in LESSONS.values()), 'problems')
