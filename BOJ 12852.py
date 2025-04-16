import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
dp[1] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

ans = dp[n]
print(ans)

path = []
def bt(curr):
    path.append(curr)
    
    if len(path) == ans+1:
        print(*path)
        exit()
    
    if curr % 3 == 0 and dp[curr] - 1 == dp[curr//3]:
        bt(curr//3)
        path.pop()
    if curr % 2 == 0 and dp[curr] - 1 == dp[curr//2]:
        bt(curr//2)
        path.pop()
    if dp[curr] - 1 == dp[curr-1]:
        bt(curr-1)
        path.pop()

bt(n)