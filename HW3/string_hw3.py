def bai1():
    s = input()
    words = s.split()
    sorted = sorted(words)
    for word in sorted:
        print(word)

def bai2():
    s=input()
    binaries = s.split(',')

    for num in binaries:
        decimal = int(num,2)
        print(decimal, end=" ")

def bai3():
    s = input()
    count = 0
    for char in s.lower():
        if char.isalpha():
            count += 1
    
    print("So tu la ki tu la:{}".format(count))

def bai4():
    s = input()
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    result = ' '.join(capitalized_words)
    print(result)
         

def bai5():
    s = input()
    count_upper = 0;
    count_lower = 0;
    for word in s.replace(" ",""):
        if word.isupper():
            count_upper += 1
        else:
            count_lower += 1
    print(count_upper, count_lower,sep=",")


def is_prime(n): # so nguyen to
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True

def bai6():
    s = input()
    num = s.split(",")
    for number in num:
        if is_prime(int(number)):
            print(number)
    




if __name__ == "__main__":
    # bai1()
    # bai2()
    # bai3()
    # bai4()
    # bai5()
    bai6()