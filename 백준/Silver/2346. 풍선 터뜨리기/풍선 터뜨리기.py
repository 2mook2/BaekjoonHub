# BOJ 2346번
from collections import deque

n = int(input())

balloon = deque(i for i in range(1, n + 1))
cmd = deque(map(int, input().split()))

while balloon:
    num = balloon.popleft()
    next = cmd.popleft()
    if next > 0:
        next -= 1
    print(num, end=' ')
    balloon.rotate(-next)
    cmd.rotate(-next)