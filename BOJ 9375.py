import sys
from collections import Counter

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    cloth = [sys.stdin.readline().split()[1] for _ in range(n)]
    v = dict(Counter(cloth)).values()

    ans = 1
    for n in v:
        ans *= (n+1)
    print(ans-1)