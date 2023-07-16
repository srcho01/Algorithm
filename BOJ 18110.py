import sys

n = int(sys.stdin.readline())
rating = [int(sys.stdin.readline()) for _ in range(n)]
rating.sort()

def r(n):
    return int(n) + 1 if n >= int(n) + 0.5 else int(n)

if n == 0:
    print(0)
    exit()

exclusion = r(n * 0.15)
print(r(sum(rating[exclusion:len(rating)-exclusion]) / (n - 2*exclusion)))