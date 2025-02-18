import sys
from collections import deque

input = sys.stdin.readline

cogwheel = [0]
for _ in range(4):
    cogwheel.append(deque(list(map(int, list(input().rstrip())))))

k = int(input())

def rotate(rotate_dir):
    for i in range(1, 5):
        if rotate_dir[i] == 0: continue
        
        if rotate_dir[i] == 1:
            cogwheel[i].appendleft(cogwheel[i].pop())
        else:
            cogwheel[i].append(cogwheel[i].popleft())

for _ in range(k):
    rotate_num, direction = map(int, input().split())
    rotate_dir = [0] * 5
    rotate_dir[rotate_num] = direction
    
    d = direction
    for i in range(rotate_num, 1, -1):
        if cogwheel[i][6] == cogwheel[i-1][2]: break
        
        d *= -1
        rotate_dir[i-1] = d
    
    d = direction
    for i in range(rotate_num, 4):
        if cogwheel[i][2] == cogwheel[i+1][6]: break
        
        d *= -1
        rotate_dir[i+1] = d

    rotate(rotate_dir)

score = 0
for i in range(1, 5):
    score += 2 ** (i-1) if cogwheel[i][0] == 1 else 0

print(score)