def bai1():
    num_of_tuple = int(input("Enter num of tuple: "))

    L = ()
    l = []
    for i in range(num_of_tuple):
        print(f"Tuple {i+1}")
        fruit = input("Fruit: ")
        price = float(input("Price: "))
        qty = int(input("Quantity: "))
        L += (fruit,price,qty)
        
    
    print(L)
    
bai1()