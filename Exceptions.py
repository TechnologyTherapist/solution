# Errors detected during execution are called exceptions.
l=int(input("Enter a Number of line:"))
for _ in range(l):
  a,b=input("Enter a Value:").split()
  try:
      print(int(a)//int(b))
  except(ZeroDivisionError) as e:
      print("Error Code: ",e)
  except(ValueError) as v:
      print("Error Code",v)


