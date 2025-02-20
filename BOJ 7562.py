import sys
from collections import deque

input = sys.stdin.readline

direciton = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

n = int(input())
for _ in range(n):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    
    queue = deque([(x1, y1, 0)])
    visited = [[False] * l for _ in range(l)]
    visited[x1][y1] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if x == x2 and y == y2:
            print(cnt)
            break
    
        for dx, dy in direciton:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= l or ny < 0 or ny >= l: continue
            
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt+1))