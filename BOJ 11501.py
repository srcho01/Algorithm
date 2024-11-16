import sys

input = sys.stdin.readline

t = int(input())
for x in range(1, t+1):
    n = int(input())
    money = list(map(int, input().split()))
    money = money[::-1]
    
    save = money[0]
    buy_count = 0
    buy_money = 0
    total = 0
    for today in money[1:]:
        if today < save:
            buy_count += 1
            buy_money += today
        else:
            total += buy_count * save - buy_money
            buy_count = 0
            buy_money = 0
            save = today
    
    total += buy_count * save - buy_money

    print(total)