import sys

input = sys.stdin.readline
n, l = map(int, input().split())
water = sorted(list(map(int, input().split())))

cnt = 0
tape = 0

for w in water:
    if tape <= w - 0.5:
        tape = w - 0.5
        cnt += 1
        tape += l
    elif tape < w + 0.5:
        cnt += 1
        tape += l

print(cnt)