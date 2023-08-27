n, k = map(int, input().split())

s = k*(k+1) // 2
if s > n:
    print(-1)
elif s == n:
    print(k-1)
else:
    n = (n-s) % k
    if n == 0:
        print(k-1)
    else:
        print(k)