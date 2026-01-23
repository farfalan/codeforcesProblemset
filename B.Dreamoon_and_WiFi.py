
# sender  = input()
# receiver = input()

sender = "+--++"
receiver = "+-+-?"

print(receiver.count("?"))

def getfinalstep(steps):
    s = 0
    for _ in steps:
        if _ == "+":
            s += 1
        elif _ == "-":
            s -=1
    return s

print(getfinalstep(sender))
print(getfinalstep(receiver))




