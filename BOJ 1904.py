n = int(input())

a = 1
b = 1
for i in range(2, n+1):
    a, b = b, (a+b) % 15746
    
print(b)