import numpy as np
print("input:")
w = int(input())
x= np.random.randint(low=0, high=8, size=(w,))
mylist = []
for a in x:
    mylist.append(np.binary_repr(a, width=3))

print(mylist)
numbeOfones = 0
for element in mylist:
    temp =0
    for i in element:
        if i == "1": temp=1 + temp
    if  temp> 1:numbeOfones = numbeOfones +1  
    
print(numbeOfones)

