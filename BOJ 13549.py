import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

q = deque([(n, 0), (2*n, 0)])
visited = [False] * 100001
visited[n] = True
if 0 <= 2*n <= 100000:
    visited[2*n] = True
while q:
    pos, t = q.popleft()
    
    if pos == k:
        print(t)
        break
    
    if 0 <= 2*pos <= 100000 and not visited[2*pos]:
        q.append((2*pos, t))
        visited[2*pos] = True
    
    for p in [pos-1, pos+1]:
        if 0 <= p <= 100000 and not visited[p]:
            q.append((p, t+1))
            visited[p] = True