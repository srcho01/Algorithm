import sys

input = sys.stdin.readline
n = int((input()))
a = sorted(list(map(int, input().split())))
x = int(input())

ans = 0
i = 0
j = n - 1
while i < j:
    s = a[i] + a[j]
    if s == x:
        ans += 1
        i += 1
        j -= 1
    elif s < x:
        i += 1
    else:
        j -= 1

print(ans)