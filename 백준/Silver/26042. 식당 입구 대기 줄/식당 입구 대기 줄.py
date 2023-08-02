# BOJ 26042번
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())

a = []
for i in range(n):
    info = tuple(map(int, input().split()))
    a.append(info)

# print(a)

b = deque()
c = []
max_len = 1
for j in range(len(a)):
    if a[j][0] == 1:
        b.append(a[j][1])
    if a[j][0] == 2:
        if a[j - 1][0] == 1:
            max_len = max(max_len, len(b))
            c.append((len(b), b.copy()))
        b.popleft()
    elif j == len(a) - 1:
        max_len = max(max_len, len(b))
        c.append((len(b), b.copy()))

# print(c)
# print(max_len)

min_num = int(1e5)
for i in c:
    if i[0] == max_len:
        min_num = min(min_num, i[1][-1])

print(max_len, min_num)
