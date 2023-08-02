import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
rgb = [list(input().strip()) for _ in range(n)]
dir = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우
ans = [0, 0]

visited = [[False] * n for _ in range(n)]
def normal(m, i, j):
    q = deque([(i,j)])
    color = m[i][j]
    visited[i][j] = True          
    
    while q:
        nx, ny = q.popleft()
        for dx, dy in dir:
            x = nx + dx
            y = ny + dy
            if (0 <= x < n and 0 <= y < n) and not visited[x][y] and m[x][y] == color:
                visited[x][y] = True
                q.append((x,y))

for i, line in enumerate(rgb):
    for j, c in enumerate(line):
        if not visited[i][j]:
            normal(rgb, i, j)
            ans[0] += 1
            
visited = [[False] * n for _ in range(n)]
def blind(m, i, j):
    q = deque([(i,j)])
    color = [m[i][j]]
    if m[i][j] == "R":
        color.append("G")
    elif m[i][j] == "G":
        color.append("R")
    visited[i][j] = True          
    
    while q:
        nx, ny = q.popleft()
        for dx, dy in dir:
            x = nx + dx
            y = ny + dy
            if (0 <= x < n and 0 <= y < n) and not visited[x][y] and m[x][y] in color:
                visited[x][y] = True
                q.append((x,y))

for i, line in enumerate(rgb):
    for j, c in enumerate(line):
        if not visited[i][j]:
            blind(rgb, i, j)
            ans[1] += 1
            
print(*ans)