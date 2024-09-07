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
    
def main():
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

def bai7():
    n = int(input("Nhap n: "))
    m = int(input("Nhap m: "))
    for i in range(n, m+1):
        if i % 9 == 0 and i % 7 == 0:
            print(i, end=" ")
        else:
            print("Khong co so nao thoa man dieu kien")
            break   
def bai8():
    n = int(input("Nhap n: "))
    s = str(n)
    count = 0
    sum = 0
    for i in s:
        count += 1
        sum += int(i)
    print("so co {} chu so".format(count))
    print("tong cac chu so la: {}".format(sum))
        
if __name__ == "__main__":
    # main()
    # bai5()
    # bai6()
    # bai7()
    bai8()