#https://codeforces.com/contest/1294/problem/C

n = 24
found = 0

for i in range(2, n + 1, 1):
    if n % i == 0:
        a = n // i
        for j in range(2, a + 1, 1):
            if a % j == 0 and j != i:
                b =  a // j
                for k in range(2 ,b + 1, 1):
                    if b % k == 0 and k != j and k != i:
                        c =  b // k
                        if i * j * k == n:
                            found = 1
                            print(i, j, k)
                            break
                        else:
                            continue
                break        
        break        
            
if found == 1:
    print("YES")            
else:
    print("NO")

