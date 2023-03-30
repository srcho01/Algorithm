import sys

K, N = map(int, sys.stdin.readline().split())
line = [int(sys.stdin.readline()) for _ in range(K)]

L = 1
R = max(line)
mid = 0

while L <= R:
    mid = (L + R) // 2
    
    cnt = 0
    for l in line:
        cnt += l // mid
    
    if cnt >= N:
        L = mid + 1
    else:
        R = mid - 1
        
print(R)