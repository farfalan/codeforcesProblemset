#https://codeforces.com/problemset/problem/2246/A
n = int(input())

comb = []
for i,j in zip(range(2,n + 1,2),range(1,n ,2)):
    comb.append(i)
    comb.append(j)
print(comb)
