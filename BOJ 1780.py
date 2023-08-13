import sys

input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

def dac(paper, ans):
    num = paper[0][0]
    f = True
    for p in paper:
        for i in p:
            if num != i:
                f = False
                break
        if not f:
            break
    else:
        ans[num+1] += 1
        return ans
            
    r = len(paper)//3
    for i in range(0, len(paper), r):
        for j in range(0, len(paper), r):
            cut_paper = [p[j:j+r] for p in paper[i:i+r]]
            ans = dac(cut_paper, ans)
    
    return ans
            
ans = [0,0,0]
ans = dac(paper, ans)
print("\n".join(list(map(str, ans))))