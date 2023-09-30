import sys

input = sys.stdin.readline
n, m = map(int, input().split())

six_price = 1001
each_price = 1001
for _ in range(m):
    a, b = map(int, input().split())
    six_price = min(six_price, a)
    each_price = min(each_price, b)

if six_price <= each_price * 6:
    print(min((n//6) * six_price + (n%6) * each_price, (n//6 + 1) * six_price))
else:
    print(n * each_price)