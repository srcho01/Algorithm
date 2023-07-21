import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

ripe = deque()
n_tomato = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            ripe.append((i,j))
        elif box[i][j] == 0:
            n_tomato += 1

visited = [[False for _ in range(m)] for _ in range(n)]
for i, j in ripe:
    visited[i][j] = True
dir = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우

ans = 0
while ripe:
    nx, ny = ripe.popleft()
    tomato = box[nx][ny] + 1
    for dx, dy in dir:
        x = nx+dx
        y = ny+dy
        if (0 <= x < n and 0 <= y < m) and box[x][y] != -1 and not visited[x][y]:
            box[x][y] = tomato
            n_tomato -= 1
            ripe.append((x,y))
            ans = tomato
            visited[x][y] = True

if n_tomato == 0:
    if ans == 0: print(ans)
    else: print(ans-1)
else:
    print(-1)