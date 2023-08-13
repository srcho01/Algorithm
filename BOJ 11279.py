import sys
from queue import PriorityQueue

input = sys.stdin.readline
n = int(input())

q = PriorityQueue()
for _ in range(n):
    x = int(input())
    
    if x == 0:
        if q.qsize() == 0:
            print(0)
        else:
            print(q.get()[1])
    else:
        q.put((-x, x))