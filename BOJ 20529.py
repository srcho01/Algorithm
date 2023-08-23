import sys
from itertools import combinations

input = sys.stdin.readline
t = int(input())

def dist(a, b):
    ret = 0
    for x, y in zip(a, b):
        if x != y:
            ret += 1
    return ret 

for _ in range(t):
    n = int(input())
    mbti = list(map(str, input().split()))
    
    if n > 32:
        print(0)
        continue
    
    ans = 13
    for a, b, c in set(combinations(mbti, 3)):
        d = dist(a, b) + dist(b, c) + dist(c, a)
        if d < ans:
            ans = d
    print(ans)