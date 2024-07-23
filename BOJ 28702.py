import sys

input = sys.stdin.readline

text = [input().rstrip() for _ in range(3)]

n = -1
loc = 0
for i, fb in enumerate(text):
    if fb not in ["FizzBuzz", "Fizz", "Buzz"]:
        loc = i
        n = int(fb)
        
n += 3 - loc

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)