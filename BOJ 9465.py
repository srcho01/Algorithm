import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    s1 = [0] + list(map(int, input().split()))
    s2 = [0] + list(map(int, input().split()))
    
    for i in range(2, n+1):
        s1[i] += max(s2[i-2], s2[i-1])
        s2[i] += max(s1[i-2], s1[i-1])

    print(max(s1[n], s2[n]))