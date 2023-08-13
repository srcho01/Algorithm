import sys

input = sys.stdin.readline
n = int(input())
num_max = list(map(int, input().split()))
num_min = num_max[:]

for _ in range(n-1):
    curr_max = list(map(int, input().split()))
    curr_min = curr_max[:]
    
    curr_max[0] = max(num_max[:2]) + curr_max[0]
    curr_max[1] = max(num_max) + curr_max[1]
    curr_max[2] = max(num_max[1:]) + curr_max[2]
    
    curr_min[0] = min(num_min[:2]) + curr_min[0]
    curr_min[1] = min(num_min) + curr_min[1]
    curr_min[2] = min(num_min[1:]) + curr_min[2]
    
    num_max = curr_max
    num_min = curr_min
    
print(max(num_max), min(num_min))