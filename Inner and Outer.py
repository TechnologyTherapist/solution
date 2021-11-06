# The inner tool returns the inner product of two arrays.

import numpy
# A=numpy.array([input("Enter a number:").split()],int)
# B=numpy.array([input("Enter a number:").split()],int)
A=list(map(int,input("Enter a Value of A:").split()))
B=list(map(int,input("Enter a Value Of B:").split()))
print(numpy.inner(A,B))
print(numpy.outer(A,B))