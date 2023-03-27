n = int(input())
num = list(map(int, input().split()))
maximum = max(num)

prime = [False, False] + [True] * (maximum-1)

for i in range(2, len(prime)):
    if not prime[i]: continue
    
    for j in range(2, maximum):
        if i * j > maximum: break
        else: prime[i*j] = False
    
ans = 0
for n in num:
    if prime[n]: ans += 1
    
print(ans)