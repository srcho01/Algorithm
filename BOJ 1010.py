import sys

input = sys.stdin.readline
n = int(input())

def C(n, r):
    r = r if 2*r < n else n - r
    ret = 1
    
    for i in range(n, n-r, -1):
        ret *= i
    
    for i in range(1, r+1):
        ret //= i
        
    return ret

for _ in range(n):
    r, n = map(int, input().split())
    print(C(n, r))