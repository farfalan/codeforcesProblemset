#https://codeforces.com/problemset/problem/1788/B
import numpy as np
n  = 16
i = 0
n = 1206
limit = n/2

while i < limit:  
    x = n
    y = i
    i += 1
    n -= 1
    sumdigitX = 0
    for k in range(len(str(x))):
        sumdigitX += int(str(x)[k])
    #print(x,sumdigitX)
    
    sumdigitY = 0
    
    for j in range(len(str(y))):
        sumdigitY += int(str(y)[j])
    #print(y,sumdigitY)
          
    if np.abs(sumdigitX - sumdigitY) <= 1:
        print(x,y)

        

