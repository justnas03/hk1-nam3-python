import os
os.system("cls")


def myfunc(n):
    M = list(range(n,0,-1))
    P = M
    print(M)
    M[0] = n+1
    print(P)
    Q = P +[10]
    Q.sort()
    print(Q)
    P.pop()
    print(P)
    return [P,M,Q]

print(myfunc(2))
