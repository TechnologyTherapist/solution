#
# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.
# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.
#
#
# Input Format :
# The first line will contain the number of test cases, T.
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of set A.
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of set B.
# Solution
J=int(input("Enter a Number Of test Case:"))
for _ in range(J):
    a = input("Enter a number element A:")
    A = set( input("Enter a Element A:").split() )
    b = input("Enter a Number Element B:")
    B = set( input("Enter a Element B").split() )
    print( A.issubset( B ) )
