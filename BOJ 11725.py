import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
tree = {}
for _ in range(n-1):
    i, j = map(int, input().split())
    if not i in tree.keys():
        tree[i] = [j]
    else:
        tree[i].append(j)
    
    if not j in tree.keys():
        tree[j] = [i]
    else:
        tree[j].append(i)
        
parent = [0] * (n+1)
q = deque([1])

while q:
    x = q.popleft()
    for i in tree[x]:
        if parent[i] == 0:
            parent[i] = x
            q.append(i)
            
print("\n".join(list(map(str, parent[2:]))))