import sys
from collections import deque

input = sys.stdin.readline
n, s = map(int, input().split())
num = list(map(int, input().split()))

ans = 0
li = deque()
def dfs(idx):
    global ans, s, n
    
    if len(li) > 0 and sum(li) == s:
        ans += 1
    
    for i in range(idx, n):
        li.append(num[i])
        dfs(i+1)
        li.pop()

dfs(0)
print(ans)