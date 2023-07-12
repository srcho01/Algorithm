import sys

n = int(sys.stdin.readline())
scores = []
for _ in range(n):
    tmp = sys.stdin.readline().split()
    for i in range(1,4):
        tmp[i] = int(tmp[i])
    scores.append(tmp)
    
scores = sorted(scores, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for s in scores:
    print(s[0])