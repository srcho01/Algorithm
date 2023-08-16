from collections import deque

a, b = map(int, input().split())
q = deque([(a, 1)])

while q:
    n, cnt = q.popleft()
    
    if n == b:
        print(cnt)
        break
    
    cnt += 1
    
    if n*2 <= b:
        q.append((n*2, cnt))
    
    if int(str(n)+'1') <= b:
        q.append((int(str(n)+'1'), cnt))

else:
    print(-1)