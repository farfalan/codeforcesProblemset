#https://codeforces.com/problemset/problem/2158/B
import numpy as np
#x = np.array([2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1])
x = np.array([1, 2, 3, 4, 5, 4, 1, 4, 1, 5, 4, 6])
#x = np.random.randint(1, 13, size=12)

print(x)

p = np.array([])
q = np.array([])

for i in range(len(x)):
    if i == 0:
         p = np.append(p,x[i])
    if i > 0:
        if p.size == len(x)/2:
            q = np.append(q,x[i])
            continue
        if q.size == len(x)/2:
            p = np.append(p,x[i])
            continue    
        if np.count_nonzero(p == x[i]) == 0 and  np.count_nonzero(q == x[i]) == 0:
            if p.size == q.size:
                p = np.append(p,x[i])
            elif p.size > q.size:
                q = np.append(q,x[i])
            else:
                p = np.append(p,x[i])
        elif np.count_nonzero(p == x[i]) == np.count_nonzero(q == x[i]):
             if p.size == q.size:
                p = np.append(p,x[i])
             else:
                q = np.append(q,x[i])
        elif np.count_nonzero(p == x[i]) > np.count_nonzero(q == x[i]):
              q = np.append(q,x[i])
        else: 
            p = np.append(p,x[i])
            
print(p)
print(q)

fp = 0
fq = 0


def countDigitFrequency(arr):
    digitFrequency  = {}
    for i in arr:
        digitFrequency[i] =  np.count_nonzero(arr == i)  
    return digitFrequency

def countoddDigitFrequency(dict):
    oddDigitFrequency = {}
    oddDigitFrequency = [k for k, v in dict.items() if v % 2 != 0]
    return oddDigitFrequency

fp = len(countoddDigitFrequency(countDigitFrequency(p)))
fq = len(countoddDigitFrequency(countDigitFrequency(q)))

print(fp + fq)    
    

