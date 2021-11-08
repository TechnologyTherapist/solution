# collections.namedtuple()
# Basically, namedtuples are easy to create, lightweight object types.
# They turn tuples into convenient containers for simple tasks.
# With namedtuples, you don’t have to use integer indices for accessing members of a tuple.
import collections
from collections import namedtuple
# point=namedtuple('point','x,y')
# pt1=point(1,2)
# pt2=point(3,4)
# dot_product=(pt1.x*pt2.x)+(pt1.y*pt2.y)
# print(dot_product)
# car=namedtuple('car','price mileage colour class')
# xyz=car( price=100000, mileage=30, colour='cyan' )
# print(xyz)
n=int(input("Enter a number of student"))
scol=','.join(input().split())
Student=collections.namedtuple('Student',scol)
sum=0
for i in range(n):
    row=input().split()
    student=Student(*row)
    sum+=int(student.MARKS)
print(sum/n)
