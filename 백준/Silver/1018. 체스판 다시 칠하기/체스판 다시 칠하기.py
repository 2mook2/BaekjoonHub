# BOJ 1018번
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]

def diff_cnt(x, y):
    cnt = 0
    for i, j in zip(x, y):
        if i != j:
            cnt += 1
    return cnt

a1 = 'WBWBWBWBBWBWBWBW' * 4
a2 = 'BWBWBWBWWBWBWBWB' * 4
min_val = int(1e6)
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        chess = ''
        for k in range(8):
            chess += graph[i+k][j:j+8]
        diff_min = min(diff_cnt(a1, chess), diff_cnt(a2, chess))
        min_val = min(min_val, diff_min)

if n == 8 and m == 8:
    chess = ''
    for i in graph:
        chess += i
    print(min(diff_cnt(a1, chess), diff_cnt(a2, chess)))
else:
    print(min_val)