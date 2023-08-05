import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
move = [0] * 101

for _ in range(n+m):
    x, y = map(int, input().split())
    move[x] = y

q = deque([(1, 0)])
visited = [False] * 101
visited[1] = True

while q:
    curr, cnt = q.popleft()
    
    cnt += 1
    for i in range(1, 7):
        x = curr + i
        
        if x == 100:
            print(cnt)
            exit()
        
        if x < 100 and not visited[x]:
            if move[x] != 0:
                x = move[x]
            visited[x] = True
            q.append((x, cnt))