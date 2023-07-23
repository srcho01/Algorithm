n, m = map(int, input().split())

arr = []

def dfs():
    for i in range(1, n+1):
        if len(arr) < m:
            arr.append(i)
            dfs()
        elif len(arr) == m:
            print(*arr)
            arr.pop()
            return
    if len(arr) > 0: arr.pop()
        
dfs()