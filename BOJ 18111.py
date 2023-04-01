import sys
from collections import Counter

n, m, b = map(int, sys.stdin.readline().split())

tmp = []
for _ in range(n):
    tmp += list(map(int, sys.stdin.readline().split()))

land = dict(Counter(tmp))

high = max(land.keys())
low = min(land.keys())
land = land.items()

ans = [125000000, 0]
for height in range(low, high+1):
    time = 0
    used = b
    for block, cnt in land:
        used += cnt * (block - height)
        time += cnt * (height - block) if block < height else 2 * cnt * (block - height)
    
    if used < 0: continue
    
    if time <= ans[0]:
        ans = [time, height]

print(*ans)