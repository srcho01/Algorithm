import sys

input = sys.stdin.readline
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
points = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}

n = int(input())
students = []
like_students = dict()
for _ in range(n*n):
    line = list(map(int, input().split()))
    students.append(line[0])
    like_students[line[0]] = line[1:]

seat = [[0] * n for _ in range(n)]
seat[1][1] = students[0]

for student in students[1:]:
    data = []
    like_student = like_students[student]
    
    for i in range(n):
        for j in range(n):
            if seat[i][j] != 0: continue
            
            like, empty = 0, 0
            for dx, dy in direction:
                nx, ny = i + dx, j + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                
                if seat[nx][ny] == 0:
                    empty += 1
                elif seat[nx][ny] in like_student:
                    like += 1
            
            data.append((like, empty, i, j))
    
    data.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    seat[data[0][2]][data[0][3]] = student

ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in direction:
            nx, ny = i + dx, j + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if seat[nx][ny] in like_students[seat[i][j]]:
                cnt += 1
    
        ans += points[cnt]
    
print(ans)