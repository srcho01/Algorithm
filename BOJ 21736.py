import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
campus = [list(input().strip()) for _ in range(n)]

dir = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우
q = deque()

for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            q.append((i,j))
            campus[i][j] = 0

friend = 0           
while q:
    nx, ny = q.popleft()
    for dx, dy in dir:
        x = nx + dx
        y = ny + dy
        
        if 0 <= x < n and 0 <= y < m:
            if campus[x][y] == "O":
                q.append((x,y))
                campus[x][y] = 0
            elif campus[x][y] == "P":
                friend += 1
                q.append((x,y))
                campus[x][y] = 0

if friend == 0:
    print("TT")                
else:
    print(friend)