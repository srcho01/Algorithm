import sys

input = sys.stdin.readline

n = int(input())
X = list(map(int, input().split()))

X_unique = set(X)
dic = {}
for i, x in enumerate(sorted(list(X_unique))):
    dic[x] = i
    
for x in X:
    print(dic[x], end=' ')