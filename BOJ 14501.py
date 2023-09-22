import sys

input = sys.stdin.readline
n = int(input())
sche = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
d = [0] * (n+1)

for i in range(1, n+1):
    d[i] = d[i-1]
    for j in range(i):
        if j + sche[j+1][0] == i:
            d[i] = max(d[i], d[j] + sche[j+1][1])
            
print(d[n])