import cmath
n=input("Enter a Value your:")
convert_number=complex(n)
print(cmath.polar(convert_number)[0])
print(cmath.polar(convert_number)[1])