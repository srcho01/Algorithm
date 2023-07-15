n = int(input())
wine = [0] + [int(input()) for _ in range(n)]

d = [0 for _ in range(n+1)]
d[0] = (0, 0, 0)
d[1] = (0, wine[1], wine[1])

for i in range(2, n+1):
    d[i] = (max(d[i-1]), max(d[i-2])+wine[i], d[i-1][1]+wine[i])

print(max(d[n]))