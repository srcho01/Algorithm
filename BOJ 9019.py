import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

def dslr(a, b):
    q = deque([(a, "")])
    visited = [False] * 10000
    
    while q:
        n, cmd = q.popleft()
        if n == b: return cmd
        
        D = (2*n) % 10000
        if not visited[D]:
            q.append((D, cmd + "D"))
            visited[D] = True
        
        S = n - 1 if n > 0 else 9999
        if not visited[S]:
            q.append((S, cmd + "S"))
            visited[S] = True
        
        L = (n%1000) * 10 + n//1000
        if not visited[L]:
            q.append((L, cmd + "L"))
            visited[L] = True
        
        R = (n%10) * 1000 + n//10
        if not visited[R]:
            q.append((R, cmd + "R"))
            visited[R] = True       

for _ in range(t):
    a, b = map(int, input().split())
    print(dslr(a, b))    