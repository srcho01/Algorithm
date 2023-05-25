t = int(input())
for _ in range(t):
    n = int(input())
    seq = [0, 1, 1, 1, 2]
    
    if n > 4:
        for i in range(5, n+1):
            seq.append(seq[i-5] + seq[i-1])
    
    print(seq[n])