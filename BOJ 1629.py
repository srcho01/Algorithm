import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())

def dac(a, b, c):
    if b == 1:
        return a % c
    
    n = dac(a, b//2, c)
    if b % 2 == 0:
        return (n * n) % c
    else:
        return (n * n * a) % c
    
print(dac(a, b, c))