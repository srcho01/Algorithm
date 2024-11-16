import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tanghulu = list(map(int, input().split()))

if len(set(tanghulu)) <= 2:
    print(len(tanghulu))
    exit()

queue = deque()
start = 0
ans = -1
for i, fruit in enumerate(tanghulu):
    if fruit in queue: continue
    
    if len(queue) < 2:
        queue.append(fruit)
    else:
        ans = max(ans, i-start)
        queue.popleft()
        queue.append(fruit)
        for x in range(i-1, -1, -1):
            if not tanghulu[x] in queue:
                start = x + 1
                break

ans = max(ans, len(tanghulu)-start)            
print(ans)