def bai1():
    S = input("Enter the String: ")
    count = 0
    for i in S:
        count += 1
    print("Lenght of the string is:", count)

def bai2():
    S = input("Enter the String: ")
    count = 0
    for i in S:
        if i == " ":
            count += 1
    print("Number of words in the string is:", count+1)

def bai3():
    S = input("Enter the String: ")
    count = 0
    S = S.lower()
    vowels = "aeiou"
    for i in S:
        if i in vowels:
            count += 1
    print("Number of vowels in the string is:", count)

if __name__ == "__main__":
    # bai1()
    # bai2()
    bai3()