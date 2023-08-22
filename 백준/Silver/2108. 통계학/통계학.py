# BOJ 2108번
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input().rstrip())

arr = []
dictionary = defaultdict(int)
for _ in range(n):
    x = int(input().rstrip())
    arr.append(x)
    dictionary[x] += 1

arr = sorted(arr)
max_cnt = max(dictionary.values())
max_cnts = []
for key, val in dictionary.items():
    if val == max_cnt:
        max_cnts.append(key)

max_cnts = sorted(max_cnts)

# mean
print(round(sum(arr) / n))
# median
print(arr[n//2])
# mode
print(max_cnts[0] if len(max_cnts) == 1 else max_cnts[1])
# range (max - min)
print(arr[-1] - arr[0])
