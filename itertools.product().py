# Method 1
from itertools import  product
# A=input("Enter a Number:").split()
# A=list(map(int,A))
# B=input("Enter a Number:").split()
# B=list(map(int,B))
# for i in product(A,B):
#     print(i)

# Method 2
a=list(map(int,input("Enter a number:").split()))
b=list(map(int,input("Enter a number:").split()))
print(' '.join([str(x) for x in list(product(a,b))]))