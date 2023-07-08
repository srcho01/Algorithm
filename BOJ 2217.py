import sys

n = int(sys.stdin.readline())

rope = [int(sys.stdin.readline()) for _ in range(n)]
rope.sort(reverse=True)

ans = 0

for i, r in enumerate(rope):
    weight = r * (i+1)
    if ans < weight:
        ans = weight
        
print(ans)