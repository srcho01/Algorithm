import sys

input = sys.stdin.readline
t = int(input())

def lcm(a, b):
    ret = a * b
    while b != 0:
        r = a % b
        a = b
        b = r
    return ret // a

for _ in range(t):
    m, n, x, y = map(int, input().split())
    
    g = lcm(m, n)
    
    x_can = []
    for i in range(x, g+1, m):
        x_can.append(i)
    
    y_can = []
    for i in range(y, g+1, n):
        y_can.append(i)
    
    inter = list(set(x_can) & set(y_can))
    if len(inter) == 0:
        print(-1)
    else:
        print(min(inter))