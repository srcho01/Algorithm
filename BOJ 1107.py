import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
k = abs(n - 100)
button = []
if m > 0:
    button = input().strip().split()
elif m == 10:
    print(k)
    exit()

for i in range(k):
    if n-i >= 0 and all(not x in button for x in str(n-i)):
        t = len(str(n-i)) + i
        print(t if t < k else k)
        break
    elif all(not x in button for x in str(n+i)):
        t = len(str(n+i)) + i
        print(t if t < k else k)
        break
else:
    print(k)