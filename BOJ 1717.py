import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline
n, m = map(int, input().split())
s = [i for i in range(n+1)]

def find(k):
    if s[k] != k:
        s[k] = find(s[k])
        
    return s[k]

for _ in range(m):
    cmd, a, b = map(int, input().split())
    setA = find(a)
    setB = find(b)
    
    if cmd == 0:
        if setA < setB:
            s[setB] = setA
        elif setA > setB:
            s[setA] = setB
    else:
        if setA == setB:
            print("YES")
        else:
            print("NO")