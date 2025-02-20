import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())
board = [[False] * m for _ in range(n)]
direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = True

def bfs(i, j):
    global n, m
    
    queue = deque([(i, j)])
    board[i][j] = True
    area = 1
    
    while queue:
        x, y  = queue.popleft()
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            
            if not board[nx][ny]:
                board[nx][ny] = True
                queue.append((nx, ny))
                area += 1
                
    return area
        
ans = []
for i in range(n):
    for j in range(m):
        if not board[i][j]:
            ans.append(bfs(i, j))

print(len(ans))
print(*sorted(ans))