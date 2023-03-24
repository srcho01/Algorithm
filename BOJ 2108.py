import sys

n = int(sys.stdin.readline())
nums = sorted([int(sys.stdin.readline()) for _ in range(n)])

print(round(sum(nums) / n))
print(nums[n//2])

cnt = {}
for i in nums:
    if not i in cnt.keys():
        cnt[i] = 1
    else:
        cnt[i] += 1
cnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
print(cnt[1][0] if len(cnt) > 1 and cnt[0][1] == cnt[1][1] else cnt[0][0])

print(nums[-1] - nums[0])