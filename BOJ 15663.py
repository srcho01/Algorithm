import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
nums = Counter(list(map(int, input().split())))
nums = dict(sorted(nums.items(), key=lambda x: x[0]))

def dfs(seq):
    if len(seq) == m:
        print(*seq)
        return
    
    for key, value in nums.items():
        if value > 0:
            seq.append(key)
            nums[key] -= 1
            dfs(seq)
            nums[key] += 1
            seq.pop()
        
dfs([])