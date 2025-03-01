import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    
    ret = 1
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
        if bamboo[x][y] > bamboo[nx][ny]:
            ret = max(ret, dfs(nx, ny) + 1)
    
    dp[x][y] = ret
    return ret

ans = 0
for x in range(n):
    for y in range(n):
        ans = max(ans, dfs(x, y))
        
print(ans)