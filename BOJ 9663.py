import sys

input = sys.stdin.readline

n = int(input())
ans = 0
chess = [0] * (n)

def check(r):
    for k in range(r):
        if chess[k] == chess[r] or abs(k-r) == abs(chess[k] - chess[r]):
            return False
    
    return True

def queen(row):
    global ans
    
    if row == n:
        ans += 1
        return
    
    for col in range(n):
        chess[row] = col

        if check(row):
            queen(row+1)
        
queen(0)
print(ans)