import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tech = list(map(int, input().split()))
order = deque()

for i, t in enumerate(tech[::-1]):
    if t == 1:
        order.appendleft(i+1)
    elif t == 2:
        tmp = order.popleft()
        order.appendleft(i+1)
        order.appendleft(tmp)
    else:
        order.append(i+1)
        
print(" ".join(map(str, order)))