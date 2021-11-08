# Solution
n=int(input("Enter a Line Number:"))
count_dict={}
word_list=[]
for i in range(n):
    word=input("enter a word:")
    word_list.append(word)
    if word in count_dict:
        count_dict[word]+=1
    else:
        count_dict[word]=1
print(len(count_dict))
print(' '.join([str(count_dict[word]) for word in count_dict]) )