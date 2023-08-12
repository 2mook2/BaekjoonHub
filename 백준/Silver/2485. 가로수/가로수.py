# BOJ 2485번
import sys
from math import gcd
input = sys.stdin.readline

n = int(input().rstrip())

trees = [int(input().rstrip()) for _ in range(n)]

dist = [trees[i + 1] - trees[i] for i in range(n - 1)]

final_gcd = gcd(dist[0], dist[1])
for i in range(2, n - 1):
    final_gcd = gcd(final_gcd, dist[i])

cnt = 0
for i in dist:
    cnt += i // final_gcd - 1

print(cnt)