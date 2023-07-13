n, k = map(int, input().split())

visited = [False for _ in range(10**5+1)]
visited[n] = True
q = [(n, 0)]

while len(q) > 0:
    curr, sec = q.pop(0)
    if curr == k:
        print(sec)
        break
    
    for i in [curr-1, curr+1, 2*curr]:
        if 0 <= i <= 10**5 and not visited[i]:
            q.append((i, sec+1))
            visited[i] = True