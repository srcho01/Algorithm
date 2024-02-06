import sys

input = sys.stdin.readline

n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
check = list(map(int, input().split()))

ans = []
for num in check:
    L = 0
    R = n-1
    mid = (L+R) // 2
    
    while L <= R:
        mid = (L+R) // 2
        
        if card[mid] == num:
            ans.append('1')
            break
    
        elif card[mid] < num:
            L = mid+1
        else:
            R = mid-1
    else:
        ans.append('0')
        
print(" ".join(ans))