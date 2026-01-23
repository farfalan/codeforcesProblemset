#https://codeforces.com/problemset/problem/766/B
#x = [1,5,3,2,4]
x = [20, 1, 20]

def isInRange(m,n,o):
    if o > abs(m-n) and o < m + n:
        print(f"{m} {n} {o}: YES")
    else:
         print("NO")

for i in range(0,len(x),1):
    for j in range(i + 1,len(x),1):
        for k in range(j + 1,len(x),1):
            isInRange(x[i], x[j], x[k])



