import sys

input = sys.stdin.readline
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j] %= 1000

def matmul(A, B):
    ret = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ret[i][j] += A[i][k] * B[k][j]
            ret[i][j] %= 1000
    return ret

def dac(n):
    if n == 1:
        return A
    
    X = dac(n//2)
    if n % 2 == 0:
        return matmul(X, X)
    else:
        return matmul(matmul(X, X), A)
    
R = dac(B)
for r in R:
    print(*r)