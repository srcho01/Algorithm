import sys

input = sys.stdin.readline
t = int(input())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for _ in range(t):
    num = list(map(int, input().split()))
    n = num[0]
    num = num[1:]
    
    s = 0
    for i in range(n):
        for j in range(i+1, n):
            s += gcd(num[i], num[j])
            
    print(s)