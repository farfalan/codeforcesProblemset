#https://codeforces.com/problemset/problem/476/B
# sender  = input()
# receiver = input()
import math
sender = "+--++"
receiver = "--+??"

# sender = "+++"
# receiver = "??-"

def getfinalstep(steps):
    s = 0
    for _ in steps:
        if _ == "+":
            s += 1
        elif _ == "-":
            s -=1
    return s

max = getfinalstep(receiver) + receiver.count("?")
min = getfinalstep(receiver) - receiver.count("?")

if getfinalstep(sender) <= max and getfinalstep(sender) >= min:

    # formel beschreibt wieviele steps (+) (-) sind benötigt vom atuellen Stand des receivers (temp) um auf den finalen stand des Sender (s)
    # zu kommen.
    # n beschreibt Anzahl von "?" 
    # s = k . (+1) + (n - k) (-1) + temp  => k = (s + n + temp)/2

    s = getfinalstep(sender)
    n = receiver.count("?")
    temp = getfinalstep(receiver)

    k = int((s + n - temp)/2)

    #p1 = math.comb(n, k) * (0.5)**n
    p = (math.factorial(n) / (math.factorial(k) * (math.factorial(n - k)))) * (1/2)**k * (1/2)**(n - k)

    print(p)
else:
      print("nicht im Bereich")