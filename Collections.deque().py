# collections.deque()
# A deque is a double-ended queue. It can be used to add or remove elements from both ends.
#
# Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same (O)1 performance in either direction.
#
# Click on the link to learn more about deque() methods.
# Click on the link to learn more about various approaches to working with deques: Deque Recipes.
#
# Example
from collections import deque
# d=deque()
# d.append(1)
# print(d)
# d.appendleft(2)
# print(d)
# d.clear()
# print(d)
# d.extend('1')
# d.extendleft('234')
# print(d)
# d.count(1)
# print(d)
# d.popleft()
# print(d)
# Solution
n=int(input("Enter a line of number:"))
d=deque()
for _ in range(n):
    lst=list(input().split())
    if lst[0]=='append':
        d.append(int(lst[1]))
    elif lst[0]=='appendleft':
        d.appendleft(int(lst[1]))
    elif lst[0]=='popleft':
        d.popleft()
    elif lst[0]=='pop':
        d.pop()
for i in d:
    print(i,end=" ")