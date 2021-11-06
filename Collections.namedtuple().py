# collections.namedtuple()
# Basically, namedtuples are easy to create, lightweight object types.
# They turn tuples into convenient containers for simple tasks.
# With namedtuples, you don’t have to use integer indices for accessing members of a tuple.
# Example:
import collections
from collections import namedtuple
# Point=namedtuple('Point','x,y')
# pt1=Point(1,2)
# pt2=Point(3,4)
# dot_product=(pt1.x*pt2.x)+(pt1.y*pt2.y)
# print(dot_product)
# Method1
# n=int(input("How mant Students Enter:"))
# scol=','.join(input().split())
# Student=collections.namedtuple('Student',scol)
# sum=0
# for i in range(n):
#     row=input().split()
#     student=Student(*row)
#     sum+=int(student.MARKS)
# print(sum/n)
# Method 2
n= int(input("Enter number of student"))
fields=input().split()
total_marks=0
for _ in range(n):
    student=namedtuple('student',fields)
    MARKS,CLASS,NAME,ID=input().split()
    student=student(MARKS,CLASS,NAME,ID)
    total_marks+=int(student.MARKS)
print('{:.2f'.format(total_marks/n))
