# BOJ 1427번
n = input()

cnt = [0] * 10

for i in n:
    cnt[int(i)] += 1

for i in range(9, -1, -1):
    for j in range(cnt[int(i)]):
        print(i, end='')