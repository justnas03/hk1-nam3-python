s = [2,3,5]


#s = {} #empty dict
s = set(s) #Create set() only way
print (2 in s)
print(s)

s = set("wahoo")
print(s)


s2 = []
s2 = set(s2)
print(type(s2))


print({1,2} | {1}, {1,2}.union({1})) 
print({1,2} | {1,3}, {1,2}.union({1,3})) 
s = {1,2} 
t = s | {1,3} 
print(s, t)









