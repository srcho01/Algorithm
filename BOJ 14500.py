import sys

input = sys.stdin.readline
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

ans = 0
dir = [(-1,0), (1,0), (0,-1), (0,1)]
def dfs(x, y, tet, cnt):
    global ans
    if cnt == 4:
        ans = max(tet, ans)
        return
        
    for dx, dy in dir:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, tet + paper[nx][ny], cnt + 1)
            visited[nx][ny] = False

def pink_tet(x, y):
    global ans
    pink_dir = [[(0,-1),(0,0),(0,1),(1,0)], [(0,-1),(0,0),(0,1),(-1,0)], [(-1,0),(0,0),(1,0),(0,-1)], [(-1,0),(0,0),(1,0),(0,1)]]
    
    for d in pink_dir:
        s = 0
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                s += paper[nx][ny]
            else:
                break
        else:
            ans = max(ans, s)

visited = [[False for _ in range(m)] for _ in range(n)]                
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, paper[i][j], 1)
        visited[i][j] = False
        
        pink_tet(i, j)

print(ans)