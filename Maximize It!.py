from itertools import product
K,M=map(int,input("Enter a Number:").split())
N=[]
for _ in range(K):
    row=map(int,input("Enter a Number:").split()[1:])
    N.append(map(lambda x:x**2%M,row))
print(max(map(lambda x:sum(x)%M,product(*N))))
