#https://codeforces.com/problemset/problem/1850/C
import numpy as np
msg = "123459"

rng = np.random.default_rng()

matrix = rng.integers(0,1,size = (8,8))

rndRng = ((9 - len(msg)) * 8) - 1

start = np.random.randint(0,rndRng + 1)

for n in range(len(msg)):
    matrix.flat[start] = msg[n]
    start += 8

print(matrix)

remsg = []
for e in matrix.flat:
   
    if  e != 0:
        remsg.append(e)

print(remsg)
