from queue import PriorityQueue
import sys

input = sys.stdin.readline
n = int(input())

q = PriorityQueue()
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        if q.qsize() == 0:
            print(0)
        else:
            print(q.get())
    else:
        q.put(cmd)