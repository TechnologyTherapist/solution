import numpy
# Task
#
# You are given the coefficients of a polynomial P .
# Your task is to find the value P of  at point x .
P=list(map(float,input("Enter a polynomial value:").split()))
x=float(input("Enter a x point value:"))
print(numpy.polyval(P,x))