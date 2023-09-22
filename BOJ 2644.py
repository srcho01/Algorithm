import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
q = deque([(a, 0)])
visited = [False] * (n+1)
visited[a] = True

while q:
    curr, rel = q.pop()
    
    if curr == b:
        print(rel)
        break
    
    rel += 1
    for i in graph[curr]:
        if not visited[i]:
            visited[i] = True
            q.append((i, rel))
else:
    print(-1)