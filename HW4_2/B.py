import os
os.system("cls")


def bai1():
    s = set(x for x in range(0,201))
    print(s)

def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
    return True


def bai2():
    s = set(x for x in range(10,2001) if isPrime(x))
    print(s)

def bai3():
    import random

    size_of_s = random.randint(1,50)
    s=[]
    for i in range(0, size_of_s):
        k =random.randint(10,2000)
        s.append(k)
    s = set(s)
    
    size_of_t = random.randint(1,50)
    t=[]
    for i in range(0, size_of_t):
        k =random.randint(10,2000)
        t.append(k)
    t = set(t)

    print(f"S(size: {size_of_s}): ",s)
    print(f"T(size: {size_of_t}): ",t)

    print(f"\n- Union: {s | t}") # hội 2 tập hợp

    inter_section = s & t
    if len(inter_section)== 0:
        print(f"- Intersection: No intersection !")
    else: 
        print(f"- Intersection: {s & t}") # lấy phần giao giữa 2 tập hợp s.intersection(t)

    print(f"- Difference: {s - t}") # lấy phần tử có trên tập s mà không có trên tập t s.difference(t)
    print(f"- symmetric_different: {s^t}") #Loại bỏ phần chung của 2 tập hợp s.symmetric_different(t)
    

def bai4_5_6():
    dict = {};

    size_of_dict = int(input("Size of Dict: "))
  
    for key in range(0, size_of_dict):
        dict[key] = int(input(f"Key {key}: Value = "))

    print(dict.values())
    print("Max: ",max(dict.values()))


    values = sorted(dict.values(), reverse=True)
    print(values)
    for key,value in dict.items():
        if value == max(dict.values()):
            print(f"Key has 1st Max Value: {key}")
        if value == values[1]:
            print(f"Key has 2nd Max Value: {key}")
        

    













if __name__ == "__main__":
    bai4_5_6()