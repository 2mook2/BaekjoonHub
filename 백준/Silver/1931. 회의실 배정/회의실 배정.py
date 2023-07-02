# BOJ 1931번
import sys
input = sys.stdin.readline

n = int(input())
time = []

for i in range(n):
    start, end = map(int, input().split())
    time.append((start, end))

time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])

cnt = 1
cannot = time[0][1]
for i in range(1, n):
    if time[i][0] >= cannot:
        cnt += 1
        cannot = time[i][1]

print(cnt)