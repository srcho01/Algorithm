t = int(input())
for x in range(1, t+1):
    n, limit = map(int, input().split())
    ingredient = [tuple(map(int, input().split())) for _ in range(n)]
    
    dp = [[0] * (limit+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        point, calory = ingredient[i-1]        
        for lim in range(1, limit+1):
            if calory > lim:
                dp[i][lim] = dp[i-1][lim]
            else:
                dp[i][lim] = max(dp[i-1][lim], dp[i-1][lim-calory] + point)
    
    print(f"#{x} {dp[n][limit]}")