def is_square_number(n): # so chinh phuong
    if n < 0:
        return False
    for i in range(int(n**0.5) + 1):
        if i*i == n:
            return True
    return False

def is_perfect_number(n): # so hoan hao
    if n < 0:
        return False
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def is_symmetric_number(n): # so doi xung
    if n < 0:
        return False
    str_n = str(n)
    return str_n == str_n[::-1]


def is_prime(n): # so nguyen to
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True
    
def bai1():
    n = int(input("Nhap n: "))
    if is_square_number(n):
        print(n, "la so chinh phuong")
    else:
        print(n, "khong la so chinh phuong")
    if is_perfect_number(n):
        print(n, "la so hoan hao")
    else:
        print(n, "khong la so hoan hao")
    if is_symmetric_number(n):
        print(n, "la so doi xung")
    else:
        print(n, "khong la so doi xung")
    if is_prime(n):
        print(n, "la so nguyen to") 
    else:
        print(n, "khong la so nguyen to")

def bai4():
    m = int(input("Nhap m: "))
    for i in range(1, m+1):
        if is_prime(i):
            print(i, end=" ")

def bai5():
    n = int(input("Nhap n: "))
    count = 0
    i = 2
    while (count < n):
        if is_prime(i):
            print(i, end=" ")
            count += 1
        i += 1

def bai2():
    n = int(input("Nhap n: "))
    m = int(input("Nhap m: "))
    for i in range(n, m+1):
        if is_prime(i):
            print(i, end=" ")

def bai6():
    for i in range(99,999+1):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=" ")

# gcd(a,b): tim uoc so chung lon nhat
def UCLN(a,b):
    while b!= 0:
        a,b = a, a%b
    return a

def BCNN(a,b):
    return abs(a*b)//UCLN(a,b)

def UCLN_r(a,b):
    if b == 0:
        return a
    return UCLN_r(a,b)

def BCNN_r(a,b):
    return abs(a*b)//UCLN_r(a,b)


def bai3(a,b):
    print(BCNN(a,b))
    print(BCNN_r(a,b))
    print(UCLN(a,b))
    print(UCLN_r(a,b))


def bai8():
    n = int(input("Nhap so: "))
    n_str = str(n)
    print(len(n_str))
    sum = 0
    n_arr = n_str.split(" ")
    for i in n_str:
        sum += int(i)
    print(sum)


    

if __name__ == "__main__":
    # main()
    # bai5()
    bai8()
