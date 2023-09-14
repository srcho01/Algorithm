import sys

input = sys.stdin.readline
a, b = map(int, input().split())
c, d = map(int, input().split())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

lcm = (b * d) // gcd(b, d)

up = a * (lcm // b) + c * (lcm // d)
down = lcm

g = gcd(up, down)
up //= g
down //= g

print(up, down)