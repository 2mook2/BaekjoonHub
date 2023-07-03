import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())

nums = list(map(int, input().split()))

stack = deque()
result = [-1] * n

for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        result[stack.pop()] = nums[i]
    
    stack.append(i)

print(' '.join(map(str, result)))
