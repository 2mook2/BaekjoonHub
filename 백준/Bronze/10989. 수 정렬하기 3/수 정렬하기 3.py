# BOJ 10989번
import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input().rstrip())

cnt = [0] * 10001

for i in range(n):
    cnt[int(input())] += 1

for i in range(10001):
    for j in range(cnt[i]):
        print(f'{i}\n')