if __name__ == '__main__':
    list1=[]
    for _ in range(int(input("Enter a number: "))):
        name = input("Enter a name:")
        score = float(input("Enter a marks:"))
        list1.append([name,score])
    # list=(sorted(list))
    # print(list[-1])
    # print(list[-2])
    list2=sorted(list(set([x[1] for  x in list1])))
    list3=list2[1]
    finallist=[]
    for item in list1:
        if list3==item[1]:
            finallist.append(item
                             [0])
            for item in sorted(item[0]):
                print(item)