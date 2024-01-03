import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tree = []

while True:
    try:
        tree.append(int(input()))        
    except:
        break

def postorder(s, e):
    if s > e: return
        
    root = tree[s]
    idx = s+1
    for i in range(s+1, e+1):
        if tree[i] > root:
            idx = i
            break
    
    postorder(s+1, idx-1)
    postorder(idx, e)
    print(root)
    
postorder(0, len(tree)-1)