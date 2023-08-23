import sys

input = sys.stdin.readline
n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

price = oil[0]
ans = price * road[0]
for r, o in zip(road[1:], oil[1:]):
    if o < price:
        price = o
    ans += price * r
    
print(ans)