import sys

n, m = map(int, sys.stdin.readline().split())
node = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
for u, v in node:
    graph[u].append(v)
    graph[v].append(u)

ans = 0

visited = [False] * (n+1)
for v in range(1, n+1):
    if not visited[v]:
        visited[v] = True
        queue = [v]

        while len(queue) > 0:
            curr = queue.pop(0)
            
            for i in graph[curr]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    
        ans += 1
    
print(ans)