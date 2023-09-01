from queue import PriorityQueue
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    k = int(input())
    max_q = PriorityQueue()
    min_q = PriorityQueue()
    q = {}
    
    for _ in range(k):
        cmd, n = input().split()        
        n = int(n)
        
        if cmd == "I":
            min_q.put(n)
            max_q.put((-n, n))
            if n in q.keys():
                q[n] += 1
            else:
                q[n] = 1
        else:
            if n == -1:
                while min_q.qsize() > 0:
                    rem = min_q.get()
                    if rem in q.keys() and q[rem] > 0:
                        q[rem] -= 1
                        break
            else:
                while max_q.qsize() > 0:
                    rem = max_q.get()[1]
                    if rem in q.keys() and q[rem] > 0:
                        q[rem] -= 1
                        break
    
    key = []
    for k, v in q.items():
        if v > 0:
            key.append(k)
    if len(key) == 0:
        print("EMPTY")
    else:
        print(max(key), min(key))