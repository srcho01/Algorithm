import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    app = [0] * n
    for _ in range(n):
        x, y = map(int, input().split())
        app[x-1] = y
    
    low = app[0]
    cnt = 1
    for i in app[1:]:
        if i < low:
            cnt += 1
            low = i
    
    print(cnt)