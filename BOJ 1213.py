from collections import Counter

name = list(Counter(list(input().strip())).items())
name.sort(key=lambda x: x[0])

center = ''
cnt = 0
for k, v in name:
    if v % 2 == 1:
        center = k
        cnt += 1
    if cnt > 1:
        print("I'm Sorry Hansoo")
        break
else:
    for k, v in name:
        print(k * (v//2), end='')
    print(center, end='')
    for k, v in name[::-1]:
        print(k * (v//2), end='')