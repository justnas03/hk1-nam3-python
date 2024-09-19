def bai1():
    A = ['3', '27','5','123','9','1']
    print("String compare: ", sorted(A))
    print("Integer compare: ", sorted(A, key=int))


def bai2():
    a = [12,24,35,70,88,120,155]
    print(a)
    b = [value for key,value in enumerate(a) if key not in [1,2,3,6]] 
    print(b)

def bai3():
    a = [1, 2, 3, 1, 2, 5, 6, 7, 8]
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print(a)
    print(b)

def bai3_b():
    a = [1, 2, 3, 1, 2, 5, 6, 7, 8]
    b = set(a)
    print(b)

def bai4():
    A = [1,1,1,1,2,2,2,2,3,3,4,5,5]
    B = []
    for i in A:
        if i not in B:
           B.append(i)
    count = 0
    for i in B:
        for j in A:
            if i == j:
                count += 1
        print(i,count, sep=",")
        count = 0

def bai4_b():
    A = [1,1,1,1,2,2,2,2,3,3,4,5,5]
    count = dict()

    for i in A:
        if i in count:
            count[i] += 1
        else: 
            count[i] = 1

    print(count)


def bai5():
    spt = int(input("Nhap so phan tu: "))
    list = []
    for i in range(spt):
        value = int(input(f"Phan tu thu {i+1}:"))
        list.append(value)
    print(list)

def bai5_b():

    value = int(input("Nhap phan tu: "))
    a = []

    while (value != -1):
        a.append(value)
        value = int(input("Nhap phan tu: "))

    print(a)


def bai6():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []

    for i in a:
        if i in b and i not in c:
            c.append(i)

    print(c)

def bai6_b():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = set([x for x in a if x in b])
    print(c)


if __name__ == "__main__":
    bai1()
    # bai2()
    # bai3()
    # bai3_b()
    # bai4()
    # bai4_b()
    # bai5_b()
    # bai6()
    # bai6_b()
