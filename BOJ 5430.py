import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    f = input().strip()
    n = int(input())
    l = input().strip()[1:-1].split(",")
    nums = [] if l[0] == '' else list(map(int, l))
    
    reverse = False
    start = 0
    end = n
    
    for cmd in f:
        if cmd == 'R':
            reverse = False if reverse else True
        else:
            if reverse:
                end -= 1
            else:
                start += 1
                
            if start > end:
                print('error')
                break
    else:
        nums = nums[start:end]
        if reverse: nums = nums[::-1]
        print(f"[{','.join(list(map(str, nums)))}]")