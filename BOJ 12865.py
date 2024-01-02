import sys

input = sys.stdin.readline

n, k = map(int, input().split())
things = [tuple(map(int, input().split())) for _ in range(n)]
d = [[0] * (k+1) for _ in range(n+1)]

for thing_idx in range(1, n+1):
    w, v = things[thing_idx-1]
    for bag in range(1, k+1):
        if bag >= w:
            d[thing_idx][bag] = max(d[thing_idx-1][bag], d[thing_idx-1][bag-w] + v)
        else:
            d[thing_idx][bag] = d[thing_idx-1][bag]
        
print(d[n][k])