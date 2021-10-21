if __name__ == '__main__':
    list=[]
    for _ in range(int(input("Enter a number: "))):
        name = input("Enter a name:")
        score = float(input("Enter a marks:"))
        list.append([name,score])
    list=(sorted(list))
    print(set(list)[-2:-1])