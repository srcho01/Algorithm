n, m = map(int, input().split())

def dfs(q):
    for i in range(1, n+1):
        if len(q) == m:
            print(*q)
            q.pop()
            return
    
        elif len(q) < m and (len(q) == 0 or q[-1] <= i):
            q.append(i)
            dfs(q)
    
    if len(q) > 0:
        q.pop()
    
q = []            
dfs(q)