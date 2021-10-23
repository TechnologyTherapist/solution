def split_and_join(line):
    string1 = ''
    # for a in line:
    #     print((a))
    a = line.split(" ")
    string = "-".join( a )
    return string

    # write your code here


if __name__ == '__main__':
    line = input("Enter a String:")
    result = split_and_join( line )
    print( result )