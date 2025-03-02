nam = float(input("nhập năm:  "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(nam,"là năm nhuận")
else:
    print(nam,"không phải là năm nhuận")

        #input: 2024
        #output: là năm nhuận

#bai 2
x = float(input("nhap x:"))
y = float(input("Nhap y:"))
a = float(input("nhap a:"))
b = float(input("nhap b:"))
r = float(input("nhap r:"))
khoang_cach = ((x-a)**2 + (y-b)**2)**(1/2)
if khoang_cach <= r**2:
    print("True-diem M(x,y) nam trong hoac tren duong tron ")
else:
    print("False-diem M(x,y) nam ngoai duong tron")
print(khoang_cach)

        #input :x=2,y=3,a=3,b=4,r=5
        #output : true, khoảng canh= 2.83

#bai 3
a = float(input("nhap canh a : "))
b = float(input("nhap canh b : "))
c = float(input("nhap canh c : "))
if a + b > c and b + c > a and a + c > b :
    if  a == b == c:
            print("là tam giác đều")
    elif a == b or b == c or c == a :
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2 :
            print("là tam giác vuông cân")
        else :
            print("là tam giác cân")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2 :
        print("là tam giác vuông")
    else :
        print("là tam giác thường")
else:
    print(" không phải là tam giác")

        #input: a=5,b=6,c=7
        #output: là tam giác thường

#bai 4
x = float(input("nhập số x:"))
y = float(input("nhập số y:"))
z = float(input("nhập số z:"))
if x >= y and x >= z :
    so_lon_nhat = x
elif y >= x and y >= z  :
    so_lon_nhat = y
else:
    so_lon_nhat = z
print("số lớn nhất trong ba số là : ", so_lon_nhat)

        #input: x=3,y=4,z=5
        #output: số lớn nhất trong ba số là : 5.0

#bai 5
ky_tu = input("Nhập một ký tự: ")
if ky_tu.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f"Ký tự '{ky_tu}' là nguyên âm.")
else:
    print(f"Ký tự '{ky_tu}' là phụ âm.")

        #input: a
        #output: a là nguyên âm

#bai 6
print("menu")
print("1.phim hành động")
print("2.phim ma")
print("3.phim tuổi học trò")
print("4.phim tình cảm")
print("5.phim tình cảm gia đình")
print("0.không chọn phim nào")
lua_chon = int(input("lựa chọn ở menu (1,2,3,4,5,0): "))
if lua_chon == 1:
    print("phim hành động")
if lua_chon == 2:
    print("phim ma")
if lua_chon == 3:
    print("phim tuổi học trò")
if lua_chon == 4:
    print("phim tình cảm")
if lua_chon == 5:
    print("phim tình cảm gia đình")
if lua_chon == 0:
    print("không chọn phim nào")
else:
    print("nhập lại đúng menu")

        #input: chọn 2
        #output: phim ma


#bai 8
diem = input("điểm của sinh viên (A, B, C, D, E, F): ").upper()
if diem == "A":
    phan_loai = "sinh viên xuất sắc"
elif diem == "B":
    phan_loai = "sinh viên loại giỏi"
elif diem == "C":
    phan_loai = "sinh viên loại khá"
elif diem == "D":
    phan_loai = "sinh vien loai trung binh"
elif diem == "E":
    phan_loai = "sinh vien loai yeu"
elif diem == "F":
    phan_loai = "sinh vien loai kem"
else:
    phan_loai = "Điểm không hợp lệ"
print("sinh viên là :", phan_loai)
 #input:A
        #output: sinh viên xuất sắc
#bai 9

# Nhập lương 
luong = float(input("Nhập lương của nhân viên (triệu): "))
# Tính 
if luong >= 15:
    thue_thu_nhap = luong * 0.30
elif luong >= 7:
    thue_thu_nhap = luong * 0.20
else:
    thue_thu_nhap = luong * 0.10
# Tính lương ròng
luong_rong = luong - thue_thu_nhap
# kết quả
print("Thuế thu nhập:", thue_thu_nhap, "triệu VND")
print("Lương ròng:", luong_rong, "triệu VND")

        #input : 20
        #output: thuế thu nhập=6.0 triệu , lương ròng=14.0 triệu

#bai 10

thang = float(input("nhập tháng (1->12):  "))
if thang in [ 1,3,5,7,8,10,12] :
    print("tháng đó có 31 ngày")
elif thang in [ 4,6,9,11] :
    print("tháng đó có 30 ngày")
elif thang == 2:
    nam = float(input("nhập năm:  "))
    # Kiểm tra năm nhuận
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("tháng 2 có 29 ngày")
    else:
        print("tháng 2 có 28 ngày")
else :
    print("nhập lại tháng tù 1-> 12")

    #input: 8
    #output: tháng có 31 ngày

#bai 11
chu_so = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
while True: 
    n = int(input("Nhap chu so can doc la : "))
    if  100 <= n <= 999 :
        break
    else :
        print("ban nhap ko dung , hay nhap lai ")
if n < 0 : 
    ket_qua = "âm"
    n = abs(n)
else :
    ket_qua = " "
hang_tram = n // 100 
hang_chuc = (n // 10) % 10 
hang_don_vi = n % 10 
ket_qua += chu_so[hang_tram] + " trăm"
if hang_chuc == 0 and hang_don_vi != 0 :
    ket_qua += " lẻ " + chu_so[hang_don_vi]
elif hang_chuc == 1:
    ket_qua += " mười"
    if hang_don_vi != 0:
        ket_qua += " " + chu_so[hang_don_vi]
elif hang_chuc > 1:
    ket_qua += " " + chu_so[hang_chuc] + " mươi"
    if hang_don_vi == 1:
        ket_qua += " mốt"
    elif hang_don_vi == 5:
        ket_qua += " lăm"
    elif hang_don_vi != 0:
        ket_qua += " " + chu_so[hang_don_vi]
print("Cách đọc:", ket_qua)

        #input:234
        #output:Hai trăm Ba mươi Bốn

#bài 12
t_n_c_t = float(input("nhập thâm niên (tháng):"))
luong_cb = 1.35
if t_n_c_t >= 60:
    luong = luong_cb * 3.99
elif 36 <= t_n_c_t < 60 :
    luong = luong_cb * 3.66
elif 12 <= t_n_c_t < 36 :
    luong = luong_cb *3.33
else :
    luong = luong_cb* 2.34
print(f"lương nhân viên đó nhận được là :{luong:.3f} " )

        #input: 36
        #output: 4.941
