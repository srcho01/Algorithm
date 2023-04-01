import sys

n = int(sys.stdin.readline())

S = []
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 2:
        x = int(cmd[1])
    cmd = cmd[0]
    
    if cmd == 'add':
        if not x in S:
            S.append(x)
    elif cmd == 'remove':
        if x in S:
            S.remove(x)
    elif cmd == 'check':
        if x in S: print(1)
        else: print(0)
    elif cmd == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.append(x)
    elif cmd == 'all':
        S = list(range(1, 21))
    else: # empty
        S = []