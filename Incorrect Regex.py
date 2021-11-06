import  re
S=int(input("enter a number of line:"))
for _ in range(S):
    try:
        re.compile(input("Enter a String:"))
        Output=True
    except re.error:
        Output=False
    print(Output)