import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
maru = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

if d in [1,3]: d = (d+2) % 4

ans = 0
dir = [(-1,0),(0,-1),(1,0),(0,1)] # 북서남동

while True:
    if maru[r][c] == 0: # 아직 청소되지 않은 경우
        maru[r][c] = 2 # 청소
        ans += 1
    
    for i in range(1, 5):
        dx, dy = dir[(d+i) % 4]
        if maru[r+dx][c+dy] == 0:
            d = (d+i) % 4
            r += dx
            c += dy
            break
    else:
        dx, dy = dir[(d+2) % 4]
        if maru[r+dx][c+dy] == 1:
            break
        else:
            r += dx
            c += dy
            
print(ans)