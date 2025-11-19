#https://codeforces.com/problemset/problem/1374/A
import numpy as np
k = -1
x, y, n = int(input()), int(input()), int(input())
if x >= 2 and x <= 10**9 and y >=0 and y < x and n >= y and n <= 10**9:
       for i in range(n + 1):
           if np.mod(i,x) == y:
                k = i
        
print(k)          

