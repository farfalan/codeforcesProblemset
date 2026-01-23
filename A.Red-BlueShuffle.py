#https://codeforces.com/contest/1459/problem/A
r = int(input())
b = int(input())

reds = 0
blues = 0
print()

for i in range(len(str(r))):
    if str(r)[i] > str(b)[i]:
        reds += 1
        print(reds)
    if str(r)[i] < str(b)[i]:
        blues +=1
        print(blues)


if reds > blues:
    print('red')
if reds < blues:
    print('blue')
if reds == blues:
    print('equal')

