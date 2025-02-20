import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(m)]
direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def bfs(i, j):
    queue = deque([(i, j)])
    pic[i][j] = 0
    
    area = 1
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0  or nx >= m or ny < 0 or ny >= n: continue
            
            if pic[nx][ny] == 1:
                area += 1
                pic[nx][ny] = 0
                queue.append((nx, ny))
    
    return area

cnt, max_pic = 0, 0
for i in range(m):
    for j in range(n):
        if pic[i][j] == 1:
            max_pic = max(max_pic, bfs(i, j))
            cnt += 1
            
print(cnt)
print(max_pic)