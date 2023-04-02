import sys
n, m = map(int, sys.stdin.readline().split())

d = {}
for _ in range(n):
    site, password = map(str, sys.stdin.readline().split())
    d[site] = password
    
for _ in range(m):
    site = sys.stdin.readline().strip()
    print(d[site])