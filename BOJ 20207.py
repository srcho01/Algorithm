import sys

input = sys.stdin.readline

n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]
max_date = max(tu[1] for tu in schedule)

level = [0] * (max_date + 2)
for s, e in schedule:
    level[s] += 1
    level[e+1] -= 1
    
for i in range(1, len(level)):
    level[i] += level[i-1]
    
w, h = 0, 0
area = 0
for l in level:
    if l == 0:
        area += w * h
        w, h = 0, 0
    else:
        w += 1
        h = max(h, l)

print(area)