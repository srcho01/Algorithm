import sys

input = sys.stdin.readline
n = int(input())
options = [input().strip() for _ in range(n)]
shortcut = []

def print_option(option, idx):
    for i, c in enumerate(option):
        if i == idx:
            print(f"[{c}]", end='')
        else:
            print(c, end='')
    print()

for option in options:
    option_l = option.lower().split()
    i = 0
    for word in option_l:
        if not word[0] in shortcut:
            shortcut.append(word[0])
            print_option(option, i)
            break
        i += len(word) + 1
    else:
        for i, c in enumerate(option.lower()):
            if c == ' ': continue
            if not c in shortcut:
                shortcut.append(c)
                print_option(option, i)
                break
        else:
            print(option)