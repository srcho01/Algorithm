import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

q = deque()
def dfs():
    for i in num:
        if len(q) == m:
            print(*q)
            q.pop()
            return
        
        if len(q) == 0 or (len(q) < m and q[-1] <= i):
            q.append(i)
            dfs()
        
    if len(q) > 0:
        q.pop()
        
dfs()