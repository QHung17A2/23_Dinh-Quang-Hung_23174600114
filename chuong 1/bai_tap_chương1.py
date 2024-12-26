#1
class HinhChuNhat:
    def __init__(self):
        self.chieu_dai = 0
        self.chieu_rong = 0

    def nhap_du_lieu(self):
        self.chieu_dai = float(input("Nhập chiều dài: "))
        self.chieu_rong = float(input("Nhập chiều rộng: "))

    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def hien_thi_thong_tin(self):
        print(f"Chiều dài: {self.chieu_dai}, Chiều rộng: {self.chieu_rong}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")


# Sử dụng lớp
hcn = HinhChuNhat()
hcn.nhap_du_lieu()
hcn.hien_thi_thong_tin()

#2

class TS:
    def __init__(self):
        self.ho_ten = ""
        self.diem_toan = 0
        self.diem_ly = 0
        self.diem_hoa = 0

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hóa: "))

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def hien_thi_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}, Lý: {self.diem_ly}, Hóa: {self.diem_hoa}")
        print(f"Tổng điểm: {self.tinh_tong_diem()}")

# Sử dụng lớp
danh_sach_thi_sinh = []
so_thi_sinh = int(input("Nhập số thí sinh: "))

for _ in range(so_thi_sinh):
    ts = TS()
    ts.nhap_thong_tin()
    danh_sach_thi_sinh.append(ts)

diem_chuan = 20
danh_sach_trung_tuyen = [ts for ts in danh_sach_thi_sinh if ts.tinh_tong_diem() >= diem_chuan]
danh_sach_trung_tuyen.sort(key=lambda x: x.tinh_tong_diem(), reverse=True)

print("\nDanh sách thí sinh trúng tuyển:")
for ts in danh_sach_trung_tuyen:
    ts.hien_thi_thong_tin()
    print()

#3

class PS:
    def __init__(self):
        self.tu_so = 0
        self.mau_so = 1

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        while not self.kiem_tra_hop_le():
            print("Mẫu số không hợp lệ. Vui lòng nhập lại.")
            self.mau_so = int(input("Nhập mẫu số: "))

    def hien_thi(self):
        print(f"{self.tu_so}/{self.mau_so}")

# Sử dụng lớp
ps = PS()
ps.nhap_phan_so()
ps.hien_thi()

#4
class Stack:
    def __init__(self, size):
        self.size = size
        self.items = []

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            print("Ngăn xếp đã đầy")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Ngăn xếp rỗng")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size

# Sử dụng lớp
stack = Stack(5)
print(stack.is_empty()) 
stack.push(1.5)
print(stack.is_empty()) 
stack.push(2.7)
print(stack.pop())  
print(stack.pop()) 
print(stack.is_full()) 

#5
class Stack:
    # ... (giữ nguyên các phương thức khác)

    def count(self):
        return len(self.items)

# Sử dụng lớp
stack = Stack(5)
stack.push(1.5)
stack.push(2.7)
print(stack.count())  

#6
class Stack:
    # ... (giữ nguyên các phương thức khác)

    def print(self):
        print("Nội dung ngăn xếp:", self.items)

# Sử dụng lớp
stack = Stack(5)
stack.push(1.5)
stack.push(2.7)
stack.print()  # In ra: Nội dung ngăn xếp: [1.5, 2.7]

#7
class Date:
    def __init__(self, day=1, month=1, year=2023):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    def next(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
            days_in_month[1] = 29

        self.day += 1
        if self.day > days_in_month[self.month - 1]:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1

# Sử dụng lớp
date = Date(1, 11, 2024)
date.display()
date.next()
date.display()
#8
class Date:
    def __init__(self, day=1, month=1, year=2023):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

class Employee:
    def __init__(self, name, birth_date, join_date):
        self.name = name
        self.birth_date = birth_date
        self.join_date = join_date

    def display(self):
        return f"Tên: {self.name}, Ngày sinh: {self.birth_date.display()}, Ngày vào công ty: {self.join_date.display()}"

class QuanLyNhanVien:
    def __init__(self):
        self.employees = []

    def them_nhan_vien(self, employee):
        self.employees.append(employee)

    def hien_thi_tat_ca(self):
        for i, emp in enumerate(self.employees, 1):
            print(f"Nhân viên {i}: {emp.display()}")

# Sử dụng lớp
qlnv = QuanLyNhanVien()

# Thêm 5 nhân viên
qlnv.them_nhan_vien(Employee("Nguyễn Văn A", Date(15, 5, 1990), Date(1, 1, 2020)))
qlnv.them_nhan_vien(Employee("Trần Thị B", Date(20, 8, 1995), Date(15, 3, 2021)))
qlnv.them_nhan_vien(Employee("Lê Văn C", Date(10, 12, 1988), Date(1, 7, 2019)))
qlnv.them_nhan_vien(Employee("Phạm Thị D", Date(5, 3, 1992), Date(1, 9, 2022)))
qlnv.them_nhan_vien(Employee("Hoàng Văn E", Date(25, 6, 1993), Date(1, 4, 2023)))

# Hiển thị tất cả nhân viên
print("Danh sách tất cả nhân viên:")
qlnv.hien_thi_tat_ca()

#9

class DaGiac:
    def __init__(self):
        self.canh = []

    def tinh_chu_vi(self):
        return sum(self.canh)

class HinhBinhHanh(DaGiac):
    def __init__(self, a, b):
        super().__init__()
        self.canh = [a, b, a, b]

    def tinh_dien_tich(self, h):
        return self.canh[0] * h

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, a, b):
        super().__init__(a, b)

    def tinh_dien_tich(self):
        return self.canh[0] * self.canh[1]

class HinhVuong(HinhChuNhat):
    def __init__(self, a):
        super().__init__(a, a)

# Sử dụng và kiểm tra các lớp
print("Kiểm tra lớp HinhBinhHanh:")
hbh1 = HinhBinhHanh(5, 3)
hbh2 = HinhBinhHanh(7, 4)
print(f"Hình bình hành 1 - Chu vi: {hbh1.tinh_chu_vi()}, Diện tích (chiều cao 4): {hbh1.tinh_dien_tich(4)}")
print(f"Hình bình hành 2 - Chu vi: {hbh2.tinh_chu_vi()}, Diện tích (chiều cao 5): {hbh2.tinh_dien_tich(5)}")

print("\nKiểm tra lớp HinhChuNhat:")
hcn1 = HinhChuNhat(4, 6)
hcn2 = HinhChuNhat(5, 8)
print(f"Hình chữ nhật 1 - Chu vi: {hcn1.tinh_chu_vi()}, Diện tích: {hcn1.tinh_dien_tich()}")
print(f"Hình chữ nhật 2 - Chu vi: {hcn2.tinh_chu_vi()}, Diện tích: {hcn2.tinh_dien_tich()}")

print("\nKiểm tra lớp HinhVuong:")
hv1 = HinhVuong(5)
hv2 = HinhVuong(7)
print(f"Hình vuông 1 - Chu vi: {hv1.tinh_chu_vi()}, Diện tích: {hv1.tinh_dien_tich()}")
print(f"Hình vuông 2 - Chu vi: {hv2.tinh_chu_vi()}, Diện tích: {hv2.tinh_dien_tich()}")


#10

import math

class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Elip(Diem):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a  # Bán trục lớn
        self.b = b  # Bán trục nhỏ

    def tinh_dien_tich(self):
        return math.pi * self.a * self.b

class DuongTron(Elip):
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r)

# Sử dụng lớp
elip = Elip(0, 0, 5, 3)
print(f"Diện tích elip: {elip.tinh_dien_tich():.2f}")

duong_tron = DuongTron(0, 0, 5)
print(f"Diện tích đường tròn: {duong_tron.tinh_dien_tich():.2f}")

#11
import math

class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tinh_chu_vi(self):
        return self.a + self.b + self.c

    def tinh_dien_tich(self):
        p = self.tinh_chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        c = math.sqrt(a**2 + b**2)
        super().__init__(a, b, c)

class TamGiacCan(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, b)

class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a)

# Sử dụng và kiểm tra các lớp
print("Kiểm tra lớp TamGiac:")
tg1 = TamGiac(3, 4, 5)
tg2 = TamGiac(5, 6, 7)
print(f"Tam giác 1 - Chu vi: {tg1.tinh_chu_vi():.2f}, Diện tích: {tg1.tinh_dien_tich():.2f}")
print(f"Tam giác 2 - Chu vi: {tg2.tinh_chu_vi():.2f}, Diện tích: {tg2.tinh_dien_tich():.2f}")

print("\nKiểm tra lớp TamGiacVuong:")
tgv1 = TamGiacVuong(3, 4)
tgv2 = TamGiacVuong(5, 12)
print(f"Tam giác vuông 1 - Chu vi: {tgv1.tinh_chu_vi():.2f}, Diện tích: {tgv1.tinh_dien_tich():.2f}")
print(f"Tam giác vuông 2 - Chu vi: {tgv2.tinh_chu_vi():.2f}, Diện tích: {tgv2.tinh_dien_tich():.2f}")

print("\nKiểm tra lớp TamGiacCan:")
tgc1 = TamGiacCan(5, 4)
tgc2 = TamGiacCan(7, 6)
print(f"Tam giác cân 1 - Chu vi: {tgc1.tinh_chu_vi():.2f}, Diện tích: {tgc1.tinh_dien_tich():.2f}")
print(f"Tam giác cân 2 - Chu vi: {tgc2.tinh_chu_vi():.2f}, Diện tích: {tgc2.tinh_dien_tich():.2f}")

print("\nKiểm tra lớp TamGiacDeu:")
tgd1 = TamGiacDeu(5)
tgd2 = TamGiacDeu(7)
print(f"Tam giác đều 1 - Chu vi: {tgd1.tinh_chu_vi():.2f}, Diện tích: {tgd1.tinh_dien_tich():.2f}")
print(f"Tam giác đều 2 - Chu vi: {tgd2.tinh_chu_vi():.2f}, Diện tích: {tgd2.tinh_dien_tich():.2f}")