n = int(input())

k = 1
for i in range(1, n+1):
    k *= i

k = str(k)
ans = 0
for i in range(len(k)-1, 0, -1):
    if k[i] == '0':
        ans += 1
    else:
        break

print(ans)