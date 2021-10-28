def print_formatted(number):
    # your code goes here
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        decimal=str(i)
        octa=oct(i)[2:]
        hexadecimal=hex(i)[2:].upper()
        binary=bin(i)[2:]
        print(decimal.rjust(width),octa.rjust(width),hexadecimal.rjust(width),binary.rjust(width))

if __name__ == '__main__':
    n = int(input("Enter a number:"))
    print_formatted(n)