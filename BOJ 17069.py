import sys

input = sys.stdin.readline

n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]

"""
가로 : (O X O)
세로 : (X O O)
대각선 : (O O O)
"""

def moving_pipe(n):
    if field[n-1][n-1] == 1: return 0
    
    dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
    for j in range(1, n):
        if field[0][j] == 1: break
        dp[0][j][0] = 1

    for i in range(1, n):
        for j in range(2, n):
            if field[i][j] == 1: continue
            
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2] # 가로
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2] # 세로
            if field[i-1][j] == 0 and field[i][j-1] == 0: # 대각선
                dp[i][j][2] = sum(dp[i-1][j-1])
    
    return sum(dp[n-1][n-1])

print(moving_pipe(n))