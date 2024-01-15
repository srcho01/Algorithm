import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))

seq = []
def dfs():
    if len(seq) == m:
        print(" ".join(map(str, seq)))
        return

    for i in nums:
        if len(seq) == 0 or seq[-1] <= i:
            seq.append(i)
            dfs()
            seq.pop()
            
dfs()