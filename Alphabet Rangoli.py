# Method 1
# def print_rangoli(size):
#     # your code goes here
#     width=size*4-3
#     string=''
#     for i in range(1,size+1):
#         for j in range(0,i):
#             string += chr(96+size-j)
#             if len(string)<width:
#                 string+='-'
#         for k in range(i-1,0,-1):
#             string+=chr(97+size-k)
#             if len(string)<width:
#                 string+='-'
#         print(string.center(width,'-'))
#         string=''
#     for i in range(size-1,0,-1):
#         string=''
#         for j in range(0,i):
#             string+=chr(96+size-j)
#             if len(string)<width:
#                 string+='-'
#         for k in range(i-1,0,-1):
#             string+=chr(96+size-k)
#             if len(string)<width:
#                string+='-'
#         print(string.center(width,'-'))
#
# Method 2
def print_rangoli(size):
    import string
    alpha=string.ascii_lowercase
    L=[]
    for i in range(n):
        s ="-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3,'-'))
    print('\n'.join(L[:0:-1]+L))
if __name__ == '__main__':
    n = int(input("Enter a number :"))
    print_rangoli(n)