#https://codeforces.com/contest/1294/problem/C

n = 220
found = 0

for i in range(2,n + 1,1):
    if n % i == 0:
        a = n // i
        for j in range(i + 1 ,a +1, 1):
            if a % j == 0:
                b =  a // j
                for k in range(j + 1 ,b +1, 1):
                    if b % k == 0:
                        c =  b // k
                        found = 1
                        print(i ,j , k)
                        break
                break        
        break        
            
if found == 1:
    print("YES")            
else:
    print("NO")

