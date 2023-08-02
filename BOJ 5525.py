import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
s = input().strip()

pn = []

l = 0
for c in s:
    if c == "I":
        if l % 2 == 0:
            l += 1
        else:
            if l >= 3:
                pn.append(l)
            l = 1
    else:
        if l % 2 == 1:
            l += 1
        else:
            if l > 3:
                pn.append(l-1)
            l = 0

if l % 2 == 1 and l >= 3:
    pn.append(l)
elif l % 2 == 0 and l > 3:
    pn.append(l-1)
            
ans = 0
for i in pn:
    i = (i-1) // 2
    if i >= n:
        ans += i - (n-1)

print(ans)