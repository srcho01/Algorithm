from collections import Counter

n = list(map(int, list(input())))
cnt = Counter(n)

for i in range(9, -1, -1):
    if cnt[i] > 0:
        print(str(i) * cnt[i], end='')