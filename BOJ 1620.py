import sys
n, m = map(int, sys.stdin.readline().split())

encyclopedia = {}
for i in range(1, n+1):
    name = sys.stdin.readline().strip()

    encyclopedia[name] = str(i)
    encyclopedia[str(i)] = name
    
for _ in range(m):
    cmd = sys.stdin.readline().strip()
    print(encyclopedia[cmd])