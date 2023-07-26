import sys

input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

def dac(paper, n, w, b):
    if all(p == 0 for line in paper for p in line):
        return w + 1, b
    elif all(p == 1 for line in paper for p in line):
        return w, b + 1
    
    n //= 2
    w, b = dac([line[:n] for line in paper[:n]], n, w, b) # 위쪽 왼쪽
    w, b = dac([line[n:] for line in paper[:n]], n, w, b) # 위쪽 오른쪽
    w, b = dac([line[:n] for line in paper[n:]], n, w, b) # 아래쪽 왼쪽
    w, b = dac([line[n:] for line in paper[n:]], n, w, b) # 아래쪽 오른쪽
    
    return w, b

w, b = dac(paper, n, 0, 0)
print(w, b, sep="\n")