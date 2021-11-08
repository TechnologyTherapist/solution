#
# from collections import OrderedDict
# # oridinary_dictionary={}
# oridinary_dictionary=OrderedDict()
# oridinary_dictionary['a']=1
# oridinary_dictionary['b']=2
# oridinary_dictionary['c']=3
# oridinary_dictionary['d']=4
# oridinary_dictionary['e']=5
# # print(oridinary_dictionary)
#
# print(oridinary_dictionary)
# Solution
from collections import *
N=int(input("Enter a number of item:"))
d=OrderedDict()
for i in range(N):
    item=input("Enter a item name:").split()
    itemprice=int(item[-1])
    itemname=" ".join(item[:-1])
    if(d.get(itemname)):
        d[itemname]+=itemprice
    else:
        d[itemname]=itemprice
for i in d.keys():
    print(i,d[i])