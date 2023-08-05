import sys

input = sys.stdin.readline
n, m = map(int, input().split())
x = list(map(int, input().split()))

q = list(range(1, n+1))

ans = 0
for i in x:
    t = q.index(i)
    ans += min(t, len(q)-t)
    if t == 0:
        q = q[1:]
    elif t == len(q) - 1:
        q = q[:t]
    else:
        q = q[t+1:] + q[:t]
        
print(ans)