#https://codeforces.com/problemset/problem/271/A
#Eingabe: Jahr (z.B. 2013)
#Ausgabe: das letzte Jahr vor dem eingegebenen Jahr, in dem alle Ziffern verschieden sind (z.B. 2013 -> 1987)
year = int(input())
flag = False
for k in range(year-1,0,-1):
    yearDigits = [int(digit) for digit in str(k)]
    print(yearDigits)
    for i in range(len(yearDigits)):
        for j in range(i+1,len(yearDigits)):
            if yearDigits[i] == yearDigits[j]:
                flag = True
                continue
        if flag == True:
            continue
    if flag == True:
        flag = False
        continue
    else:
        print(k)
        break


