import numpy
# Example
# A = numpy.array( [1,2] )
# B=numpy.array([3,4])
# print(numpy.dot(A,B))
n=int(input("Enter a Number:"))
a=numpy.array([input("Enter a Value:").split() for _ in range(n)],int)
b=numpy.array([input("Enter a Value:").split() for _ in range(n)],int)
print(numpy.dot(a,b))
