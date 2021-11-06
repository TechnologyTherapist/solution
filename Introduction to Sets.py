def average(array):
    sum_array=sum(set(array))
    len_array=len(set(array))
    output=sum_array/len_array
    return output
# if__name__=='__main__':
n=int(input("Enter a array size your:"))
arr=list(map(int,input("Enter a Array value:").split()))
result=average(arr)
print(result)