import sys

n = int(sys.stdin.readline())
score = [0] + [int(sys.stdin.readline()) for _ in range(n)]

d = [[] for _ in range(n+1)]
d[0] = [0, 0]
d[1] = [0, score[1]]

for i in range(2, n+1):
    stair = score[i]
    d[i] = [d[i-1][1] + stair, max(d[i-2]) + stair]
    
print(max(d[n]))