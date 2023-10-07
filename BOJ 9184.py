import sys

input = sys.stdin.readline

d = {}

def w(a, b, c):
    global d
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        if not (20, 20, 20) in d.keys():
            d[(20, 20, 20)] = w(20, 20, 20)
        return d[(20, 20, 20)]
    
    if a < b < c:
        if not (a, b, c-1) in d.keys():
            d[(a, b, c-1)] = w(a, b, c-1)
        if not (a, b-1, c-1) in d.keys():
            d[(a, b-1, c-1)] = w(a, b-1, c-1)
        if not (a, b-1, c) in d.keys():
            d[(a, b-1, c)] = w(a, b-1, c)
        
        return d[(a, b, c-1)] + d[(a, b-1, c-1)] - d[(a, b-1, c)]
    
    if not (a-1,b, c) in d.keys():
        d[(a-1,b, c)] = w(a-1,b, c)
    if not (a-1, b-1, c) in d.keys():
        d[(a-1, b-1, c)] = w(a-1, b-1, c)
    if not (a-1, b, c-1) in d.keys():
        d[(a-1, b, c-1)] = w(a-1, b, c-1)
    if not (a-1, b-1, c-1) in d.keys():
        d[(a-1, b-1, c-1)] = w(a-1, b-1, c-1)
    
    return d[(a-1,b, c)] + d[(a-1, b-1, c)] + d[(a-1, b, c-1)] - d[(a-1, b-1, c-1)]

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")