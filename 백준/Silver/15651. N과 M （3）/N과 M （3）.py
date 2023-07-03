# BOJ 15651번
from itertools import product

n, m = map(int, input().split())

arr = [_ for _ in range(1, n + 1)]

answer = []
answer.extend(product(arr, repeat = m))

for i in answer:
    for j in i:
        print(j, end=' ')
    print()