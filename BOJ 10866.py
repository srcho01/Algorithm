import sys

n = int(sys.stdin.readline())

deque = []
for _ in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push_front':
        deque.insert(0, int(cmd[1]))
    elif cmd[0] == 'push_back':
        deque.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        if len(deque) == 0: 
            print(-1)
        else:
            print(deque[0])
            deque = deque[1:]
    elif cmd[0] == 'pop_back':
        if len(deque) == 0: 
            print(-1)
        else:
            print(deque[-1])
            deque = deque[:-1]
    elif cmd[0] == 'size':
        print(len(deque)) 
    elif cmd[0] == 'empty':
        print(1 if len(deque) == 0 else 0)
    elif cmd[0] == 'front':
        if len(deque) == 0: print(-1)
        else: print(deque[0])
    else: # back
        if len(deque) == 0: print(-1)
        else: print(deque[-1])