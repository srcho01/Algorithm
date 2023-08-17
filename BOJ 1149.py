import sys

input = sys.stdin.readline
n = int(input())

cost = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    p= cost[i-1]
    cost[i][0] = min(p[1], p[2]) + cost[i][0]
    cost[i][1] = min(p[0], p[2]) + cost[i][1]
    cost[i][2] = min(p[0], p[1]) + cost[i][2]

print(min(cost[-1]))