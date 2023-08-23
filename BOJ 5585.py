import sys

input = sys.stdin.readline
n = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]

ans = 0
for c in coin:
    ans += n // c
    n %= c
    
print(ans)