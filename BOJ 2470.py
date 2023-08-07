import sys

input = sys.stdin.readline
n = int(input())
solution = sorted(list(map(int, input().split())))

s = 0
e = len(solution) - 1
mini = 2000000000
a, b = 0, 0

while s < e:
    k = abs(solution[s] + solution[e])
    if k < mini:
        mini = k
        a = solution[s]
        b = solution[e]
        
    if solution[s] + solution[e] > 0:
        e -= 1
    elif solution[s] + solution[e] < 0:
        s += 1
    else:
        print(solution[s], solution[e])
        exit()

print(a, b)