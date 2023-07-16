import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]

a = 0
b = 0
for i in range(len(Map)):
    for j in range(len(Map[i])):
        if Map[i][j] == 2:
            a = i
            b = j

for i in range(len(Map)):
    for j in range(len(Map[i])):
        if Map[i][j] == 1:
            Map[i][j] = -1

dir = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우
visited = [[False for _ in range(m)] for _ in range(n)]
visited[a][b] = True
Map[a][b] = 0
queue = deque([(a,b)])

while queue:
    x, y = queue.popleft()
    if not (a == x and b == y) and Map[x][y] == 0: continue
    
    for dx, dy in dir:
        d = Map[x][y]
        i = x + dx
        j = y + dy
        if 0 <= i < n and 0 <= j < m and not visited[i][j]:
            visited[i][j] = True
            Map[i][j] = d + 1 if Map[i][j] == -1 else min(Map[i][j], d+1)
            queue.append((i,j))
            
for v in Map:
    print(*v)