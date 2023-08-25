n = sorted(input(), reverse=True)

if n[-1] == '0' and sum(list(map(int, n))) % 3 == 0:
    print("".join(n))
else:
    print(-1)