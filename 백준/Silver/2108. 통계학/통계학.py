# BOJ 2108번
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input().rstrip())

arr = []
cnt = [0] * 8001
for _ in range(n):
    x = int(input().rstrip())
    arr.append(x)
    cnt[x + 4000] += 1

arr = sorted(arr)
max_cnt = [i - 4000 for i in range(8001) if cnt[i] == max(cnt)]

print(int(round(sum(arr) / n, 0)))
print(arr[n//2])
print(max_cnt[0]) if len(max_cnt) == 1 else print(max_cnt[1])        
print(arr[-1] - arr[0])
