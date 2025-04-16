import sys

sys = sys.stdin.readline

n = int(input())
mp = input().rstrip()

ans = set()
for i in range(n):
    visited = [False] * n
    pointer = i
    while not visited[pointer]:
        visited[pointer] = True
        if mp[pointer] == 'E': pointer += 1
        else: pointer -= 1
    ans.add(pointer)

print(len(ans) // 2)