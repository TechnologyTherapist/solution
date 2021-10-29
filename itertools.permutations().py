from itertools import permutations
# Method 1
# s,k=input("Enter a value:").split()
# words=list(permutations(s,int(k)))
# words=sorted(words,reverse=False)
# for word in words:
#     print(*words,sep='')
# Method 2
s,n=input("Enter a String And Number:").split()
n=int(n)
vals=list(permutations(s,n))
res=[]
for x in vals:
    res.append(''.join(x))
print('\n'.join(sorted(res)))