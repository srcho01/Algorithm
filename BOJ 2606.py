import sys

c_num = int(sys.stdin.readline())
n = int(sys.stdin.readline())

network = {}
for i in range(1, c_num+1):
    network[i] = []

for _ in range(n):
    k, v = map(int, sys.stdin.readline().split())
    network[k].append(v)
    network[v].append(k)

queue = network[1]
visited = [False] * (c_num+1)
visited[1] = True
ans = 0

while queue:
    visit = queue.pop(0)
    if visited[visit]: continue
    
    ans += 1    
    visited[visit] = True
    queue += network[visit]
    
print(ans)