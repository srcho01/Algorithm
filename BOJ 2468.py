import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
area = []
highest = -1
for _ in range(n):
    tmp = list(map(int, input().split()))
    m = max(tmp)
    if highest < m:
        highest = m
    area.append(tmp)

def bfs(area, h):
    dir = [(-1,0), (1,0), (0,-1), (0,1)]
    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and area[i][j] > h:
                q = deque([(i,j)])
                visited[i][j] = True
                while q:
                    nx, ny = q.popleft()
                    for dx, dy in dir:
                        x = nx + dx
                        y = ny + dy
                        if 0 <= x < n and 0 <= y < n and not visited[x][y] and area[x][y] > h:
                            visited[x][y] = True
                            q.append((x,y))
                cnt += 1
    
    return cnt

ans = [1] * (highest)
for i in range(1, highest):
    ans[i] = bfs(area, i)

print(max(ans))