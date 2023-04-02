n = int(input())

dp = [1000000] * (n+1)
dp[1] = 0

for i in range(1, n):
    m = dp[i] + 1
    dp[i+1] = min(m, dp[i+1])
    if 2*i <= n: dp[2*i] = min(m, dp[2*i])
    if 3*i <= n: dp[3*i] = min(m, dp[3*i])
    
print(dp[n])