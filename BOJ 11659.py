import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

snum = [0 for _ in range(n+1)]
for i in range(1, n+1):
    snum[i] = snum[i-1] + num[i-1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(snum[j] - snum[i-1])