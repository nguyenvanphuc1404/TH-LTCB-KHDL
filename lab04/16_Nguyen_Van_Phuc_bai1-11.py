#bai 1

# Nhập số nguyên dương
while True:
    try:
        n = int(input("Nhập một số nguyên dương (n): "))
        if n > 0:
            break
        else:
            print("Số phải lớn hơn 0. Vui lòng thử lại.")
    except ValueError:
        print(" hãy nhập một số nguyên.")

# a) Tính tổng S4
S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1

# b) Tính tổng S5
S5 = 0
i = 0
while i < n:
    S5 += (2*i + 1)**3
    i += 1

# c) Tính tổng S6
S6 = 0
i = 1
while i <= n:
    S6 += (2*i)**4
    i += 1

#kết quả
print("S4 =", S4)
print("S5 =", S5)
print("S6 =", S6)

            #input : 3
            #output: s4=14,s5=153,s6=1568

#baif 2

# Nhập
while True:
    try:
        n = int(input("Nhập số nguyên dương (n): "))
        if n > 0:
            break
        else:
            print("Số phải lớn hơn 0. Vui lòng thử lại.")
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập số nguyên.")

# Tính tổng a
S = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        S -= 1 / i
    else:
        S += 1 / i

print(f"Tổng a = {S:.2f}")

# Tính tổng b
S = 0
for i in range(1, n + 1):
    S += 1 / (i * (i + 1))

print(f"Tổng b = {S:.2f}")


# Tính tổng c
S = 0
for i in range(2, n + 2):
    S += 1 / (i)**(1/2)

print(f"Tổng c = {S:.2f}")

            #input : 2
            #output: a=0.5;b=0.67;c=1.28

#bài 3

import math
x = int(input("nhap vao gia tri x: "))
n = 10
cos_x = 1
term = 1
for i in range(1 , n + 1):
    term *= -x ** 2 / ((2 * 1) * (2 * i - 1))
    cos_x += term
print(f"cos(x) ={cos_x:.2f} ")
print(f"gia tri thuc cua cos_x = {math.cos(x):.2f}")

            #input: 2
            #output: cos(x) =-0.08,gia tri thuc cua cos_x = -0.42

#bài 4

# Nhập tử số và mẫu số
while True:
    try:
        tu_so = int(input("Nhập tử số: "))
        mau_so = int(input("Nhập mẫu số (khác 0): "))
        if mau_so != 0:
            break
        else:
            print("Mẫu số không được bằng 0. Vui lòng nhập lại.")
    except ValueError:
        print("Vui lòng nhập số nguyên.")

# Hiển thị kết quả
print(f"Phân số là: {tu_so}/{mau_so}")

            #input: tu_so=1;mau_so=3
            #output : 1/3

#bài 5

print("Nhập các số..")
while True:
    try:
        num = int(input("Nhập một số: "))
        if num < 0:
            print("Kết thúc chương trình.")
            break
        else:
            print(f"Bạn đã nhập: {num}")
    except ValueError:
        print("Vui lòng nhập một số nguyên.")

            #input: -4
            #output: Kết thúc chương trình.

#bài 6

so_sang_chu = {'0': "không", '1': "một", '2': "hai", '3': "ba", '4': "bốn",'5': "năm", '6': "sáu", '7': "bảy", '8': "tám", '9': "chín"}

# Nhập
so = input("Nhập một số: ")

#in ra dưới dạng chữ
ket_qua = ""
for c in so:
 if c in so_sang_chu:
        ket_qua += so_sang_chu[c] + " "  

# Loại bỏ khoảng trắng
ket_qua = ket_qua.strip()

print("Số đã nhập dưới dạng chữ:", ket_qua)

            #input: 32
            #output: ba hai

#bài 7

import math

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))

bcnn = abs(a * b) // math.gcd(a, b) 
print(f"Bội chung nhỏ nhất của {a} và {b} là {bcnn}")

            #input: thứ nhất= 3; thứ hai = 4
            #output: Bội chung nhỏ nhất của 3 và 4 là 12

#bài 8

print("Vui lòng nhập một ký tự bất kỳ:")
ky_tu = input()

if len(ky_tu) == 1:  
    gia_tri_ascii = ord(ky_tu)
    print(f"Ký tự '{ky_tu}' có giá trị ASCII là {gia_tri_ascii}.")
else:
    print("Bạn phải nhập một ký tự duy nhất!")

            #input: r
            #output: Ký tự 'r' có giá trị ASCII là 114.

#bài 9

n = input("nhap so: ")
tong = 0
for i in range(len(n)):
    tong += int(n[i])
print("tong cac chu so la: " , tong)

            #input: 1480
            #output:  13

#bài 10

so = input("Nhập một số thập phân: ")
ket_qua = ""
i = 0
while i < len(so):
    if so[i] == '0':
        ket_qua += "không "
    elif so[i] == '1':
        ket_qua += "một "
    elif so[i] == '2':
        ket_qua += "hai "
    elif so[i] == '3':
        ket_qua += "ba "
    elif so[i] == '4':
        ket_qua += "bốn "
    elif so[i] == '5':
        ket_qua += "năm "
    elif so[i] == '6':
        ket_qua += "sáu "
    elif so[i] == '7':
        ket_qua += "bảy "
    elif so[i] == '8':
        ket_qua += "tám "
    elif so[i] == '9':
        ket_qua += "chín "
    i += 1 
print(f"Số bạn nhập là: {ket_qua.strip()}")

            #input: 456
            #output: bốn năm sáu

#bài 11

print("menu")
print("1.Cafe")
print("2.Cam vắt")
print("3.Nước ép cà rốt")
print("4.Nước Lọc")
print("5.Nước dừa")
print("0.không chọn nước uống")
lua_chon = int(input("lựa chọn ở menu (1,2,3,4,5,0): "))
if lua_chon == 1:
    print("Cafe")
elif lua_chon == 2:
    print("Cam vắt")
elif  lua_chon == 3:
    print("Nước ép cà rốt")
elif  lua_chon == 4:
    print("Nước lọc")
elif  lua_chon == 5:
    print("Nước dừa")
elif  lua_chon == 0:
    print("không chọn nước uống ")
else:
    print("hãy chọn lại nước ở menu")

            #input: 4
            #output: Nước lọclọc