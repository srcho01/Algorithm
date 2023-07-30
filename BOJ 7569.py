import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

n_tomato = 0
ripe = deque()
for x, b in enumerate(box):
    for y, l in enumerate(b):
        for z, t in enumerate(l):
            if t == 1:
                ripe.append((x,y,z))
            elif t == 0:
                n_tomato += 1

dir = [(0,-1,0), (0,1,0), (0,0,-1), (0,0,1), (-1,0,0), (1,0,0)] # 상하좌우 / 한층 위로, 아래로
days = 0
if n_tomato == 0:
    print(days)
    exit()
    
while ripe:
    nx, ny, nz = ripe.popleft()
    tomato = box[nx][ny][nz] + 1
    for dx, dy, dz in dir:
        x = nx + dx
        y = ny + dy
        z = nz + dz
        
        if (0 <= x < h and 0 <= y < n and 0 <= z < m) and box[x][y][z] == 0:
            box[x][y][z] = tomato
            days = tomato
            n_tomato -= 1
            ripe.append((x,y,z))

if n_tomato == 0:
    print(days-1)
else:
    print(-1)