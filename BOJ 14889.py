import sys

input = sys.stdin.readline

n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]

def ability(member):
    global n
    
    start_team, link_team = 0, 0
    
    for i in range(n):
        for j in range(n):
            if member[i] and member[j]:
                start_team += S[i][j]
            elif not member[i] and not member[j]:
                link_team += S[i][j]
    
    return abs(start_team - link_team)    
    
visited = [False] * n
min_diff = 100 * 10 + 1
def bt(curr, cnt):
    global n, min_diff
    
    if cnt == n//2:
        min_diff = min(min_diff, ability(visited))
        return
    
    for i in range(curr, n):
        visited[i] = True
        bt(i+1, cnt+1)
        visited[i] = False

bt(0, 0)
print(min_diff)