n, m = map(int, input().split())

board = [input() for _ in range(n)]

ans = 2501

for a in range(n-7):
    for b in range(m-7):
        white = 0
        black = 0
        
        for i in range(a, a+8):
            for j in range(b, b+8):
                c = board[i][j]
                if i % 2 == 0:
                    if j % 2 == 0:
                        if c == 'B':
                            white += 1
                        else:
                            black += 1
                    elif j % 2 == 1:
                        if c == 'W':
                            white += 1
                        else:
                            black += 1
                else:
                    if j % 2 == 0:
                        if c == 'W':
                            white += 1
                        else:
                            black += 1
                    elif j % 2 == 1:
                        if c == 'B':
                            white += 1
                        else:
                            black += 1

        ans = min(white, black, ans)

print(ans)