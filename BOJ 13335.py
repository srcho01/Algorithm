import sys

input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

loc = [0] * n
on_load = 0
last_truck = -1
time = 0
while True:
    if loc[-1] == -1: break
    
    time += 1
        
    for i in range(last_truck, -1, -1):
        if loc[i] == -1: break
        
        loc[i] += 1
        if loc[i] == w+1:
            on_load -= trucks[i]
            loc[i] = -1
            
    if last_truck + 1 < n and on_load + trucks[last_truck+1] <= l:
        last_truck += 1
        on_load += trucks[last_truck]
        loc[last_truck] += 1
    
print(time)