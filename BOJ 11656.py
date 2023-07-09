import sys

word = sys.stdin.readline().strip()

suffix = [word[i:] for i in range(len(word))]

for s in sorted(suffix):
    print(s)