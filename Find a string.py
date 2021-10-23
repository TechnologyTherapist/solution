# A = raw_input().strip()
# x = raw_input().strip()
#
# count = 0
# for i in range(len(A) - len(x) + 1):
#     if A[i:i+len(x)] == x:
#         count += 1
# print count
def count_substring(string, sub_string):
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)]==sub_string:
            count +=1

    return count


if __name__ == '__main__':
    string = input("Enter a String:").strip()
    sub_string = input("Enter a substring:").strip()

    count = count_substring( string, sub_string )
    print( count )