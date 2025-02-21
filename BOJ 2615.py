import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

def match(i, j, color):
    # 가로
    if j+4 < 19 and all(board[i][x] == color for x in range(j, j+5)):
        if (j-1 < 0 or board[i][j-1] != color) and (j+5 >= 19 or board[i][j+5] != color):
            return True
    
    # 세로
    if i+4 < 19 and all(board[x][j] == color for x in range(i, i+5)):
        if (i-1 < 0 or board[i-1][j] != color) and (i+5 >= 19 or board[i+5][j] != color):
            return True
    
    # 대각선 1
    flag = True
    for x in range(1, 5):
        if i+x >= 19 or j+x >= 19: 
            flag = False
            break
        if board[i+x][j+x] != color:
            flag = False
            break
    if flag:
        if ((i-1 < 0 or j-1 < 0) or board[i-1][j-1] != color) and ((i+5 >= 19 or j+5 >= 19) or board[i+5][j+5] != color):
            return True
    
    # 대각선 2
    flag = True
    for x in range(1, 5):
        if i-x < 0 or j+x >= 19: 
            flag = False
            break
        if board[i-x][j+x] != color:
            flag = False
            break
    if flag:
        if ((i+1 >= 19 or j-1 < 0) or board[i+1][j-1] != color) and ((i-5 < 0 or j+5 >= 19) or board[i-5][j+5] != color):
            return True
    
    return False
    
result = [0, 0, 0]
for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            if match(i, j, board[i][j]):
                result[board[i][j]] = (i+1, j+1)
                
if result[1] == 0 and result[2] == 0:
    print(0)
elif result[2] == 0:
    print(1)
    print(*result[1])
else:
    print(2)
    print(*result[2])