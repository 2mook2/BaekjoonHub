import heapq
import sys

input = sys.stdin.readline

n = int(input().rstrip())

hq = []
for i in range(n):
    x = int(input().rstrip())
    if not x:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        heapq.heappush(hq, (abs(x), x))