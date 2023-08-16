import math

s = input().strip()
cnt = [0 for _ in range(9)]

for c in s:
    n = int(c)
    if n == 9:
        n = 6
    cnt[n] += 1
    
cnt[6] = math.ceil(cnt[6] / 2)
ans = []

for i in cnt:
    if i > 0:
        ans.append(i)
        
print(max(ans))