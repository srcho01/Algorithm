import sys

input = sys.stdin.readline
n, k = map(int, input().split())
num = list(map(int, input().split()))
s = sum(num[:k])
ans = s

for i in range(n-k):
    s = s - num[i] + num[i+k]
    if ans < s:
        ans = s

print(ans)