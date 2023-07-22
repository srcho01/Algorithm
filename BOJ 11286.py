from queue import PriorityQueue
import sys

input = sys.stdin.readline
t = int(input())
q = PriorityQueue()

for _ in range(t):
    n = int(input())
    if n == 0:
        if q.qsize() != 0:
            print(q.get()[1])
        else:
            print(0)
    else:
        q.put((abs(n), n))