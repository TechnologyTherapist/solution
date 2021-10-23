# def swap_case(s):
#     ln=len(s)
#     for i in range(ln):
#         if str[i] >='a' and str[i]>='z':
#            str[i] =chr(ord(str[i]-32))
#         elif str[i] >= 'A' and str[i]>='Z':
#            str[i]=chr(ord(str[i]+32))
#
#
# # if __name__ == '__main__':
# s=input("Enter a String:")
# result=swap_case(s)
# print(result)
# # print(str)
def swap_case(s):

    # sWAP cASE in Python - HackerRank Solution START
    Output = ''
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower())
        elif(char.islower()==True):
            Output += (char.upper())
        else:
            Output += char
    return Output
    # sWAP cASE in Python - HackerRank Solution END

if __name__ == '__main__':
    s = input("Enter a String:")
    result = swap_case(s)
    print(result)