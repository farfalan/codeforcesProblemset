#https://codeforces.com/problemset/problem/2158/A
import sys 
n  = int(input("press the number of players: "))
if (n < 1 or n > 100):
    print("max players ≤100!")
    sys.exit()
    
y , r = map(int, input("press the number of yellow and red cards: ").split())
if r < 0 or r > n or (y + r) < 0 or (y + r) > 2 * n:
    print(f" error: check if 1≤y≤{n} and 0≤y+r≤{2 * n}")
    sys.exit()

if r + (y // 2) > n:
    print(n)
else:
    print(r + (y // 2))
        


