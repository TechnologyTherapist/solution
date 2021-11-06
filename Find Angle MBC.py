# Method 1
# import math
# AB=int(input("Enter a Degree:"))
# BC=int(input("Enter a Degree:"))
# H=math.sqrt(AB**2+BC**2)
# H=H/2.0
# adj=BC/2.0
# Output=int(round(math.degrees(math.acos(adj/H))))
# Output=str(Output)
# print(f"This is Output:{Output}°")
# Method 2
from math import atan,degrees
a=int(input())
b=int(input())
output=atan(1.0*a/b)
print(str(int(round(degrees(output))))+'°')