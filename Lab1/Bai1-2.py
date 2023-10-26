print("1. Tính:")
print("a) (a + b)")
def tinh_tong(a, b):
    return a + b
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
tong = tinh_tong(a, b)
print("Tổng của a và b là:", tong)

print("b) a/b")
def tinh_thuong(a, b):
    return a / b
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
thuong = tinh_thuong(a, b)
print("Thương của a và b là:", thuong)

print("c) a^b")
def tinh_luy_thua(a, b):
    return a ** b
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
luy_thua = tinh_luy_thua(a, b)
print("Lũy thừa của a và b là:", luy_thua)

print("2. Tính diện tích hình chữ nhật khi biết bán kính")
def tinh_dien_tich_chu_nhat(chieu_dai, chieu_rong):
    dien_tich = chieu_dai * chieu_rong
    return dien_tich
chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: "))
chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
dien_tich = tinh_dien_tich_chu_nhat(chieu_dai, chieu_rong)
print("Diện tích của hình chữ nhật là:", dien_tich)

print("3. Xuất tất cả các số nguyên tố trong 1 khoảng cho trước")
def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True
start = int(input("Nhập giá trị bắt đầu của khoảng: "))
end = int(input("Nhập giá trị kết thúc của khoảng: "))
print("Các số nguyên tố trong khoảng từ", start, "đến", end, "là:")
for num in range(start, end + 1):
    if kiem_tra_so_nguyen_to(num):
        print(num)

print("4. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không")
def kiem_tra_so_fibonacci(n):
    a = 0
    b = 1
    while b < n:
        temp = b
        b = a + b
        a = temp
    if b == n:
        return True
    else:
        return False
n = int(input("Nhập số nguyên n: "))
if kiem_tra_so_fibonacci(n):
    print(n, "là số Fibonacci")
else:
    print(n, "không là số Fibonacci")

print("5. Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)")
print("Dùng đệ quy")
def fibonacci_dequy(n):
    if n <= 1:
        return n
    else:
        return fibonacci_dequy(n-1) + fibonacci_dequy(n-2)
n = int(input("Nhập số Fibonacci thứ n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương")
else:
    print("Số Fibonacci thứ", n, "là:", fibonacci_dequy(n))
print("Không dùng đệ quy")
def fibonacci_khongdequy(n):
    if n <= 0:
        return "Vui lòng nhập một số nguyên dương"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(3, n+1):
            c = a + b
            a = b
            b = c
        return b
n = int(input("Nhập số Fibonacci thứ n: "))
print("Số Fibonacci thứ", n, "là:", fibonacci_khongdequy(n))

print("6. Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)")
print("Dùng đệ quy")
def fibonacci_dequy(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_dequy(n-1) + fibonacci_dequy(n-2)
n = int(input("Nhập số n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương")
else:
    tong = sum(fibonacci_dequy(i) for i in range(n))
    print("Tổng", n, "số Fibonacci đầu tiên là:", tong)
print("Không dùng đệ quy")
def fibonacci_khongdequy(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        tong = 1
        for _ in range(2, n):
            c = a + b
            a = b
            b = c
            tong += c
        return tong
n = int(input("Nhập số n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương")
else:
    tong = fibonacci_khongdequy(n)
    print("Tổng", n, "số Fibonacci đầu tiên là:", tong)

print("7. Tính tổng căn bậc 2 của n số nguyên đầu tiên")
import math
def tinh_tong_can_bac_2(n):
    tong = 0
    for i in range(1, n+1):
        tong += math.sqrt(i)
    return tong
n = int(input("Nhập số n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương")
else:
    tong_can_bac_2 = tinh_tong_can_bac_2(n)
    print("Tổng căn bậc 2 của", n, "số nguyên đầu tiên là:", tong_can_bac_2)

print("8. Giải phương trình bậc 2: ax2 + bx + c=0")
import math

def giai_phuong_trinh_bac_2(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return "Phương trình có hai nghiệm phân biệt: x1 =", x1, "và x2 =", x2
    elif delta == 0:
        x = -b / (2*a)
        return "Phương trình có nghiệm kép: x =", x
    else:
        return "Phương trình vô nghiệm"
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
if a == 0:
    print("Đây không phải là phương trình bậc 2")
else:
    ket_qua = giai_phuong_trinh_bac_2(a, b, c)
    print(ket_qua)

print("9. Tính n!")
def tinh_giai_thua(n):
    giai_thua = 1
    if n < 0:
        return "Không thể tính giai thừa của số âm"
    elif n == 0:
        return 1
    else:
        for i in range(1, n+1):
            giai_thua *= i
        return giai_thua
n = int(input("Nhập số n: "))
ket_qua = tinh_giai_thua(n)
print("Giai thừa của", n, "là:", ket_qua)

print("10. In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)")
def in_tam_giac(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()
so_hang = int(input("Nhập số hàng: "))
in_tam_giac(so_hang)

print("11. Đổi giờ - phút – giây: thời gian đầu vào là giây được đổi thành giờ, phút, giây. Xuất kết quả ra màn hình dưới dạng: giờ:phút:giây. Ví dụ: soGiay = 3770 thì xuất ra màn hình 1:2:50.")
def doi_giay_gio(giay):
    gio = giay // 3600
    phut = (giay % 3600) // 60
    giay = (giay % 3600) % 60
    return f"{gio}:{phut}:{giay}"
so_giay = int(input("Nhập số giây: "))
ket_qua = doi_giay_gio(so_giay)
print("Kết quả: ", ket_qua)

print("12.Cho một mảng số nguyên: (nên viết 2-3 cách)")
mang_so_nguyen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 2, 5, 7, 1, 5, 2, 8, 3, 9, 7, 4, 6, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 123, 456, 789, 101112]
print("a) Xuất tất cả các số lẻ không chia hết cho 5")
#Cách 1
for so in mang_so_nguyen:
    if so % 2 != 0 and so % 5 != 0:
        print(so)

#Cách 2
ket_qua = [so for so in mang_so_nguyen if so % 2 != 0 and so % 5 != 0]
print(ket_qua)

#Cách 3
ket_qua = list(filter(lambda so: so % 2 != 0 and so % 5 != 0, mang_so_nguyen))
print(ket_qua)

print("b) Xuất tất cả các số Fibonacci")
# Cách 1
a, b = 0, 1
while b <= max(mang_so_nguyen):
    if b in mang_so_nguyen:
        print(b)
    a, b = b, a + b

# Cách 2
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
for so in mang_so_nguyen:
    if so == fibonacci(so):
        print(so)

# Cách 3
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
ket_qua = [so for so in mang_so_nguyen if so == fibonacci(so)]
print(ket_qua)

print("c) Tìm số nguyên tố lớn nhất")
# Cách 1
so_nguyen_to_lon_nhat = None
for so in mang_so_nguyen:
    if so > 1:
        la_so_nguyen_to = True
        for i in range(2, int(so ** 0.5) + 1):
            if so % i == 0:
                la_so_nguyen_to = False
                break
        if la_so_nguyen_to and (so_nguyen_to_lon_nhat is None or so > so_nguyen_to_lon_nhat):
            so_nguyen_to_lon_nhat = so
print(so_nguyen_to_lon_nhat)

# Cách 2
def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
so_nguyen_to = [so for so in mang_so_nguyen if la_so_nguyen_to(so)]
so_nguyen_to_lon_nhat = max(so_nguyen_to) if so_nguyen_to else None
print(so_nguyen_to_lon_nhat)

# Cách 3
def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
so_nguyen_to = list(filter(la_so_nguyen_to, mang_so_nguyen))
so_nguyen_to_lon_nhat = max(so_nguyen_to) if so_nguyen_to else None
print(so_nguyen_to_lon_nhat)

print("d) Tìm số Fibonacci bé nhất")
# Cách 1
a, b = 0, 1
so_fibonacci_be_nhat = None
while b <= max(mang_so_nguyen):
    if b in mang_so_nguyen:
        so_fibonacci_be_nhat = b
        break
    a, b = b, a + b
print(so_fibonacci_be_nhat)

# Cách 2
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
so_fibonacci_be_nhat = None
for so in mang_so_nguyen:
    if so == fibonacci(so):
        so_fibonacci_be_nhat = so
        break
print(so_fibonacci_be_nhat)

# Cách 3
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
so_fibonacci = [so for so in mang_so_nguyen if so == fibonacci(so)]
so_fibonacci_be_nhat = min(so_fibonacci) if so_fibonacci else None
print(so_fibonacci_be_nhat)

print("e) Tính trung bình các số lẻ")
# Cách 1
so_le = []
for so in mang_so_nguyen:
    if so % 2 != 0:
        so_le.append(so)
trung_binh_so_le = sum(so_le) / len(so_le) if so_le else None
print(trung_binh_so_le)

# Cách 2
so_le = [so for so in mang_so_nguyen if so % 2 != 0]
trung_binh_so_le = sum(so_le) / len(so_le) if so_le else None
print(trung_binh_so_le)

# Cách 3
from functools import reduce
so_le = list(filter(lambda x: x % 2 != 0, mang_so_nguyen))
trung_binh_so_le = reduce(lambda x, y: x + y, so_le) / len(so_le) if so_le else None
print(trung_binh_so_le)

print("f) Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng")
# Cách 1
tich_so_le = 1
for so in mang_so_nguyen:
    if so % 2 != 0 and so % 3 != 0:
        tich_so_le *= so
print(tich_so_le)

# Cách 2
so_le_khong_chia_3 = [so for so in mang_so_nguyen if so % 2 != 0 and so % 3 != 0]
tich_so_le = 1
for so in so_le_khong_chia_3:
    tich_so_le *= so
print(tich_so_le)

# Cách 3
from functools import reduce
so_le_khong_chia_3 = list(filter(lambda x: x % 2 != 0 and x % 3 != 0, mang_so_nguyen))
tich_so_le = reduce(lambda x, y: x * y, so_le_khong_chia_3) if so_le_khong_chia_3 else None
print(tich_so_le)

print("g) Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ")
vi_tri_1 = 2
vi_tri_2 = 7

# Cách 1
mang_so_nguyen[vi_tri_1], mang_so_nguyen[vi_tri_2] = mang_so_nguyen[vi_tri_2], mang_so_nguyen[vi_tri_1]
print(mang_so_nguyen)

# Cách 2
temp = mang_so_nguyen[vi_tri_1]
mang_so_nguyen[vi_tri_1] = mang_so_nguyen[vi_tri_2]
mang_so_nguyen[vi_tri_2] = temp
print(mang_so_nguyen)

# Cách 3
mang_so_nguyen[vi_tri_1:vi_tri_1 + 1], mang_so_nguyen[vi_tri_2:vi_tri_2 + 1] = mang_so_nguyen[vi_tri_2:vi_tri_2 + 1], mang_so_nguyen[vi_tri_1:vi_tri_1 + 1]
print(mang_so_nguyen)

print("h) Đảo ngược trật tự các phần tử của danh sách")
# Cách 1
mang_so_nguyen.reverse()
print(mang_so_nguyen)

# Cách 2
mang_so_nguyen = mang_so_nguyen[::-1]
print(mang_so_nguyen)

# Cách 3
i = 0
j = len(mang_so_nguyen) - 1
while i < j:
    mang_so_nguyen[i], mang_so_nguyen[j] = mang_so_nguyen[j], mang_so_nguyen[i]
    i += 1
    j -= 1
print(mang_so_nguyen)

print("i) Xuất tất cả các số lớn thứ nhì của danh sách")
# Cách 1
mang_da_sap_xep = sorted(mang_so_nguyen)
so_lon_thu_nhi = mang_da_sap_xep[-2]
print(so_lon_thu_nhi)

# Cách 2
so_lon_nhat = max(mang_so_nguyen)
mang_so_nguyen.remove(so_lon_nhat)
so_lon_thu_nhi = max(mang_so_nguyen)
print(so_lon_thu_nhi)

# Cách 3
so_lon_nhat = float('-inf')
so_lon_thu_nhi = float('-inf')
for so in mang_so_nguyen:
    if so > so_lon_nhat:
        so_lon_thu_nhi = so_lon_nhat
        so_lon_nhat = so
    elif so > so_lon_thu_nhi and so != so_lon_nhat:
        so_lon_thu_nhi = so
print(so_lon_thu_nhi)

print("j) Tính tổng các chữ số của tất cả các số trong danh sách")
# Cách 1
tong_chu_so = 0
for so in mang_so_nguyen:
    chuoi_so = str(so)
    for chu_so in chuoi_so:
        tong_chu_so += int(chu_so)
print(tong_chu_so)

# Cách 2
tong_chu_so = sum(int(chu_so) for so in mang_so_nguyen for chu_so in str(so))
print(tong_chu_so)

# Cách 3
from functools import reduce
tong_chu_so = reduce(lambda x, y: x + y, (int(chu_so) for so in mang_so_nguyen for chu_so in str(so)))
print(tong_chu_so)

print("k) Đếm số lần xuất hiện của một số trong danh sách")
# Cách 1
so_can_dem = 2
so_lan_xuat_hien = mang_so_nguyen.count(so_can_dem)
print(so_lan_xuat_hien)

# Cách 2
so_can_dem = 2
so_lan_xuat_hien = 0
for so in mang_so_nguyen:
    if so == so_can_dem:
        so_lan_xuat_hien += 1
print(so_lan_xuat_hien)

# Cách 3
from collections import Counter
so_can_dem = 2
so_lan_xuat_hien = Counter(mang_so_nguyen)[so_can_dem]
print(so_lan_xuat_hien)

print("l) Xuất các số xuất hiện n lần trong danh sách")


print("m) Xuất các số xuất hiện nhiều lần nhất trong danh sách")
