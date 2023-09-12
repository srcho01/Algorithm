import sys

input = sys.stdin.readline
n = int(input())
trie = {}

for _ in range(n):
    data = list(map(str, input().split()[1:]))
    
    t = trie
    for d in data:
        if not d in t.keys():
            t[d] = {}
        t = t[d]
    
def dfs(level, t):
    if len(t.keys()) == 0:
        return
    
    for k in sorted(t.keys()):
        print("-" * level * 2, end='')
        print(k)
        dfs(level+1, t[k])
        
dfs(0, trie)