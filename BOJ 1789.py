S = int(input())

if S == 1:
    print(1)
    exit()   

for n in range(1, S+1):
    if (n * (n+1)) // 2 > S:
        print(n-1)
        break