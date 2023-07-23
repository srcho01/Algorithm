import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
village = [list(map(int, list(input().strip()))) for _ in range(n)]
comp = []

def bfs(i, j):
    dir = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우
    q = deque([(i,j)])
    village[i][j] = 0
    cnt = 1
    
    while q:
        nx, ny = q.popleft()
        for dx, dy in dir:
            x = nx + dx
            y = ny + dy
            if (0 <= x < n and 0 <= y < n) and village[x][y] == 1:
                cnt += 1
                q.append((x,y))
                village[x][y] = 0
                
    return cnt   

for i in range(n):
    for j in range(n):
        if village[i][j] == 1:
            comp.append(bfs(i, j))

print(len(comp))
for i in sorted(comp):
    print(i)