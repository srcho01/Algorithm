import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
graph_list = []

for g in graph:
    tmp = []
    for i, x in enumerate(g):
        if x == 1:
            tmp.append(i)
    graph_list.append(tmp)

def bfs(i):
    q = deque(graph_list[i])
    visited = [False] * n
    
    while q:
        k = q.popleft()
        graph[i][k] = 1
        
        for a in graph_list[k]:
            if not visited[a]:
                visited[a] = True
                q.append(a)
                
for i in range(n):
    bfs(i)

for g in graph:
    print(*g)