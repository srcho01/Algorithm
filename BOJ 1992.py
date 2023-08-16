import sys

input = sys.stdin.readline
n = int(input())
video = [input().strip() for _ in range(n)]

def dac(v):
    num = v[0][0]
    for line in v:
        for i in line:
            if num != i:
                break
        else:
            continue
        break
    else:
        print(num, end='')
        return
    
    i = len(v) // 2
    
    print("(", end='')
    dac([k[:i] for k in v[:i]])
    dac([k[i:] for k in v[:i]])
    dac([k[:i] for k in v[i:]])
    dac([k[i:] for k in v[i:]])
    print(")", end='')
    
dac(video)