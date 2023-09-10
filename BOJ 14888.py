import sys

input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))

ans = [-1000000001, 1000000001]

def dfs(i, a, plus, minus, multi, division):
    if i == n:
        ans[0] = max(a, ans[0])
        ans[1] = min(a, ans[1])
        return
    
    b = num[i]
    if plus:
        dfs(i+1, a + b, plus-1, minus, multi, division)
    if minus:
        dfs(i+1, a - b, plus, minus-1, multi, division)
    if multi:
        dfs(i+1, a * b, plus, minus, multi-1, division)
    if division:
        d = -((-a) // b) if a < 0 and b > 0 else a // b
        dfs(i+1, d, plus, minus, multi, division-1)

dfs(1, num[0], operator[0], operator[1], operator[2], operator[3])
print("\n".join(list(map(str, ans))))