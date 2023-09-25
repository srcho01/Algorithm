import sys

input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))

i = n-2
while i >= 0 and p[i] >= p[i+1]:
    i -= 1

if i == -1:
    print(-1)
    exit()
elif i == n-1:
    j = n-1
else:
    j = i
    for k in range(i+1, n):
        if p[i] < p[k]:
            j += 1 

p[i], p[j] = p[j], p[i]
p = p[:i+1] + p[i+1:][::-1]
print(*p)