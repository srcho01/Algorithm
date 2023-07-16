import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(me, target):
    q = [(i, 1) for i in graph[me]]
    visited = [False for _ in range(n+1)]
    for i in graph[me]:
        visited[i] = True
    
    while q:
        v, cnt = q.pop(0)
        if v == target:
            return cnt
        else:
            for i in graph[v]:
                if not visited[i]:
                    visited[i] = True
                    q.append((i, cnt+1))

bacon = []
for i in range(1, n+1):
    b = 0
    for j in range(1, n+1):
        if i == j:
            continue
        else:
            b += bfs(i, j)
    bacon.append((i, b))
    
bacon = sorted(bacon, key=lambda x: (x[1], x[0]))
print(bacon[0][0])