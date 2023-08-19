import sys

input = sys.stdin.readline
n, m = map(int, input().split())
coin = [int(input()) for _ in range(n)]
d = [0] * (m+1)
d[0] = 1

for c in coin:
    for i in range(1, m+1):
        if i-c >= 0:
            d[i] += d[i-c]
        
print(d[m])