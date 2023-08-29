import sys

input = sys.stdin.readline
n = input().strip()

cnt = 0
prev = False
bar = 0
for x in n:
    if x == "(":
        bar += 1
        prev = True
    else:
        bar -= 1
        if prev:
            cnt += bar
        else:
            cnt += 1
        prev = False
        
print(cnt)