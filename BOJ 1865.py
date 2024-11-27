import sys

input = sys.stdin.readline
MAX = 10**8

t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())
    graph = []
    
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))
    
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))
        
    def bellman():
        dist = [MAX] * (n+1)
        
        for i in range(1, n+1):
            for curr, nxt, time in graph:
                if dist[curr] + time < dist[nxt]:
                    dist[nxt] = dist[curr] + time
                    
                    if i == n:
                        return True
                    
        return False
    
    print("YES" if bellman() else "NO")