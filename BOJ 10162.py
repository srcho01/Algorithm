t = int(input())

if t % 10 != 0:
    print(-1)
    exit()
    
for i in [300, 60, 10]:
    print(t // i, end=' ')
    t %= i