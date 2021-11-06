# # A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
from collections import Counter
# list=[0,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,6,7,8,9]
# # for item in list:
# #  # data=item.count()
# #  print(item)
# print(Counter(list))
# print(Counter(list).items())
# print(Counter(list).keys())
# print(Counter(list).values())
# print(Counter(list).items())
u=input("Enter a number:")
c=Counter(map(int,input("Enter a Counter:").split()))
n=input("Enter a number:")
N=int(n)
earnings=0
for customer in range(N):
 size,x_i=map(int,input().split())
 if size in c and c[size]>0:
  c[size] -=1
  earnings+=x_i
print(earnings)

# Explanation :
# Customer 1: Purchased size 6 shoe for $55.
# Customer 2: Purchased size 6 shoe for $45.
# Customer 3: Size 6 no longer available, so no purchase.
# Customer 4: Purchased size 4 shoe for $40.
# Customer 5: Purchased size 18 shoe for $60.
# Customer 6: Size 10 not available, so no purchase.
#
# Total money earned = 55+45+40+60 = $200
