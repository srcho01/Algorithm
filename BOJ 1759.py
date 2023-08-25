import sys

input = sys.stdin.readline
l, c = map(int, input().split())
k = sorted(input().strip().split())

def possible(s):
    vowel = 0
    for i in s:
        if i in ['a','e','i','o','u']:
            vowel += 1
    consonant = len(s) - vowel
            
    return True if vowel >= 1 and consonant >= 2 else False

def dfs(pwd):
    if len(pwd) == l:
        if possible(pwd):
            print(pwd)
        return
        
    for i, w in enumerate(k):
        if len(pwd) == 0 or k.index(pwd[-1]) < i:
            pwd += w
            dfs(pwd)
            pwd = pwd[:-1]
        
    if len(pwd) > 0:
        pwd = pwd[:-1]
        
dfs("")