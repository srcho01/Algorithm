t = int(input())

d = [[] for _ in range(12)]
d[1] += [(1,0,0)]
d[2] += [(2,0,0), (0,1,0)]
d[3] += [(3,0,0), (1,1,0), (0,0,1)]

for i in range(4, 11):
    for j in range(1, i//2+1):
        for a, b, c in d[j]:
            for x, y, z in d[i-j]:
                if not (a+x, b+y, c+z) in d[i]:
                    d[i].append((a+x, b+y, c+z))

def C(n, r):
    if n - r < r: r = n - r
    
    if r == 0: return 1
    
    res = 1
    for i in range(r):
        res *= (n-i)
    for i in range(1, r+1):
        res //= i
        
    return res

for _ in range(t):
    n = int(input())
    
    ans = 0
    for one, two, three in d[n]:
        total = one + two + three
        ans += C(total, one) * C(total-one, two) * C(total-one-two, three)
        
    print(ans)