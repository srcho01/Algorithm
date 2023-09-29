n = int(input())

ans = 0
i = 0

while True:
    k = 9 * (10 ** i)
    if n > k:
        ans += k * (i+1)
        n -= k
        i += 1
    else:
        ans += n * (i+1)
        break

print(ans)
    




# 1~9 10~99 100~999 1000~9999
# 9, 90, 900, 9000 ...