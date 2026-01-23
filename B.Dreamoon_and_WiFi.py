
# sender  = input()
# receiver = input()

# sender = "+--++"
# receiver = "+-+-?"

sender = "+++"
receiver = "??-"



print(receiver.count("?"))

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
    print("im Bereich")
else:
      print("nicht im Bereich")  

print(getfinalstep(sender))
print(getfinalstep(receiver))




