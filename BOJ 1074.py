import sys

n, r, c = map(int, sys.stdin.readline().split())

def dac(n, r, c, ans):
    if n == 1:
        if r == 0 and c == 1:
            ans += 1
        elif r == 1 and c == 0:
            ans += 2
        elif r == 1 and c == 1:
            ans += 3
        return ans
        
    if n > 1:
        sqr = (2 ** (n-1)) ** 2
        if r < 2 ** (n-1): # 위쪽
            if c < 2 ** (n-1): # 왼쪽
                return dac(n-1, r, c, ans)
            else: # 오른쪽
                return dac(n-1, r, c - 2**(n-1), ans + sqr)
        else: # 아래쪽
            if c < 2 ** (n-1): # 왼쪽
                return dac(n-1, r - 2**(n-1), c, ans + sqr * 2)
            else: # 오른쪽
                return dac(n-1, r - 2**(n-1), c - 2**(n-1), ans + sqr * 3)

ans = 0
print(dac(n, r, c, ans))