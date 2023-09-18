import sys
from collections import deque

input = sys.stdin.readline
s = list(input().rstrip())
L = deque(s)
R = deque()
t = int(input())

for _ in range(t):
    cmd = input().rstrip()
    
    if cmd == "L":
        if len(L) > 0:
            R.appendleft(L.pop())
    elif cmd == "D":
        if len(R) > 0:
            L.append(R.popleft())
    elif cmd == "B":
        if len(L) > 0:
            L.pop()
    else:
        a = cmd[2]
        L.append(a)
        
print(''.join(list(L)) + ''.join(list(R)))