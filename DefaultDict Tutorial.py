# The defaultdict tool is a container in the collections class of Python.
# It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet.
# If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
from collections import defaultdict
# For Example
# d=defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relvent")
# d['python'].append("lenguage")
# for i in d.items():
#     print(i)
n,m=map(int,input("Enter a size of element:").split())
a=defaultdict(list)
# Method 1
# for i in range(1,n+1):
#     a=[input()].append(i)
# for i in range(1,m+1):
#     key=input()
#     if len([key])>0:
#         print(" ".join(str(c) for c in a[key]))
#     else:
#         print(-1)
# Method 2
for i in range(n):
    a[input()].append(str(i+1))
for j in range(m):
    print(' '.join(a[input()]) or -1)