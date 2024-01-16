import sys
import heapq as hq
from math import inf

input = sys.stdin.readline

n = int(input())
m = int(input())
city = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    city[u].append((v, w))

start, arrive = map(int, input().split())

d = [inf] * (n+1)
d[start] = 0
heap = []
hq.heappush(heap, (0, start))
    
while heap:
    curr_cost, curr = hq.heappop(heap)
    
    if d[curr] < curr_cost: continue
    
    for next, next_cost in city[curr]:
        new_cost = curr_cost + next_cost
        if new_cost < d[next]:
            d[next] = new_cost
            hq.heappush(heap, (new_cost, next))
            
print(d[arrive])