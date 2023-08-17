import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = sorted([int(input()) for _ in range(n)])

d = [10001] * (k+1)
d[0] = 0

for i in range(coin[0], k+1):
    for c in coin:
        if i-c >= 0:
            d[i] = min(d[i], d[i-c]+1)

if d[k] == 10001:
    print(-1)
else:
    print(d[k])