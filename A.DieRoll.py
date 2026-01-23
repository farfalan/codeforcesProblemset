#https://codeforces.com/problemset/problem/9/A
y, w = map(int,input().split())

if ((6 - (max(y ,w)) + 1)) == 1 or ((6 - (max(y ,w)) + 1)) == 5:
    print(f"{((6 - (max(y ,w)) + 1))} / 6 " )
elif ((6 - (max(y ,w)) + 1)) == 2:
    print("1/3")
elif ((6 - (max(y ,w)) + 1)) == 3:
    print("1/2")
elif ((6 - (max(y ,w)) + 1)) == 4:
    print("2/3")
else:
    print("1/1")
    
    
