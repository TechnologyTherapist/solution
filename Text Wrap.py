import textwrap

# Method 1
# def wrap(string, max_width):
#     wrapper=textwrap.TextWrapper(max_width)
#     word_list=wrapper.wrap(text=string)
#     for element in word_list:
#         print(element)
#     return

# Method 2
def wrap(string,max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input("Enter a String:"), int(input("Enter a Width:"))
    result = wrap(string, max_width)
    print(result)