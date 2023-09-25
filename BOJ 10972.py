import sys

input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))

i = n-2
while i >= 0 and p[i] >= p[i+1]:
    i -= 1

if i == -1:
    print(-1)
else:
    j = n-1
    for x in p[n-1:i:-1]:
        if p[i] > x:
            j -= 1
        else:
            break

    p[i], p[j] = p[j], p[i]
    p = p[:i+1] + p[i+1:][::-1]
    print(*p)