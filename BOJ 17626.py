### pypy3로 제출

import math

n = int(input())

d = [50001 for _ in range(n+1)]
d[0] = 0
d[1] = 1

for i in range(2, n+1):
    if (i ** (1/2)) % 1 == 0:
        d[i] = 1
        continue
    
    for a in range(int(math.sqrt(i)) + 1): 
        d[i] = min(d[i - a**2] + 1, d[i])

print(d[n])