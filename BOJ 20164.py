import sys

input = sys.stdin.readline

n = input().rstrip()

def bt(num):
    max_case, min_case = -1, 10 ** 8
    
    leng = len(num)
    odd = 0
    for x in num:
        if int(x) % 2 == 1:
            odd += 1
    
    if leng == 1:
        return odd, odd
    
    if leng == 2:
        mini, maxi = bt(str(int(num[0]) + int(num[1])))
        return odd + mini, odd + maxi
    
    if leng >= 3:
        for i in range(1, leng):
            for j in range(i+1, leng):
                mini, maxi = bt(str(int(num[:i]) + int(num[i:j]) + int(num[j:])))
                min_case = min(min_case, odd + mini)
                max_case = max(max_case, odd + maxi)
    
    return min_case, max_case

print(*bt(n))