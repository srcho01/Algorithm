import sys

input = sys.stdin.readline

while True:
    t = input().strip().split()
    k = int(t[0])
    if k == 0:
        break
    S = list(map(int, t[1:]))
    
    def dfs(arr):
        if len(arr) == 6:
            print(*arr)
            arr.pop()
            return
        
        for n in S:
            if len(arr) == 0 or n > arr[-1]:
                arr.append(n)
                dfs(arr)
        
        if len(arr) > 0:
            arr.pop()
            
    dfs([])
    print()