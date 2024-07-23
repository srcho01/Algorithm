import sys
import math

input = sys.stdin.readline

n = int(input())
tshirt = list(map(int, input().split()))
t, p = map(int, input().split())

print(sum(math.ceil(i / t)  for i in tshirt))
pen_bundle = n // p
print(n // p, n - pen_bundle * p)