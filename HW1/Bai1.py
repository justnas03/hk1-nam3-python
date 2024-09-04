def bai1():
    print("16*4 =",16*4)
    print("16**4 =",16**4)
    print("6/9 =",6/9)
    print("16//24 =",16//24)
    print("4/0 = khong duoc do chia cho 0")
    
def bai2():
    global ten 
    ten =input("Nhap ten: ")
    diachi = input("Nhap dia chi: ")
    namsinh = int(input("Nhap nam sinh: "))
    print("Thong tin ca nhan: ")
    print("+ Ten: ",ten)
    print("+ Dia chi: ",diachi)
    print("+ Nam sinh: ",namsinh)

def bai3():
    ten = "Dixon"
    print("Your name is: ", ten)
    ten = "Daryl"
    print("Your name is: ", ten)

def bai4():
    radius = float(input("Nhap ban kinh: "))
    area = 3.14 * radius**2
    print("Dien tich hinh tron la: ", area)


if __name__ == "__main__":
    # bai1()
    # bai2()
    # bai3()
    bai4()
