import sys
from math import sqrt

n = int(sys.stdin.readline())

d = [i for i in range(n+1)]

for i in range(2, n+1):
    sqr = sqrt(i)
    if sqr % 1 == 0:
        d[i] = 1
        continue
    
    for k in range(1, int(sqr)+1):
        power = k * k
        d[i] = d[i] if d[i] < d[i-power] + 1 else d[i-power] + 1

print(d[n])