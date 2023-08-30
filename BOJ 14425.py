import sys

input = sys.stdin.readline
n, m = map(int, input().split())
s = set(input().rstrip() for _ in range(n))

ans = 0
for _ in range(m):
    string = input().rstrip()
    if string in s:
        ans += 1

print(ans)