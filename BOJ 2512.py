import sys

input = sys.stdin.readline
n = int(input())
request = list(map(int, input().split()))
total = int(input())

if sum(request) <= total:
    print(max(request))
    exit()
    
L = 1
R = max(request)

while L <= R:
    mid = (L+R) // 2
    
    if sum(min(r, mid) for r in request) <= total:
        L = mid + 1
    else:
        R = mid - 1
        
print(R)