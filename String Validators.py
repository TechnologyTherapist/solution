# Method 1

if __name__=='__main__':
   s=input("Enter a String:")
#     for item in s:
#         if item.isalnum():
#             print(True)
#             if item.isalpha():
#                 print(True)
#                 if item.isdigit():
#                     print(True)
#                     if item.islower():
#                         print(True)
#                         if item.isupper():
#                             print(True)
#         else:
#             print(False)
#         # elif item.isalpha():
#         #     print(True)
#         # elif item.isdigit():
#         #     print(True)
#         # elif item.islower():
#         #     print(True)
#         # elif item.upper():
#         #     print(True)
#         # else:
#         #     print(False)

# Method 2
   print(any(a.isalnum() for a in s))
   print(any(a.isalpha() for a in s))
   print(any(a.isdigit() for a in s))
   print(any(a.islower() for a in s))
   print(any(a.isupper() for a in s))