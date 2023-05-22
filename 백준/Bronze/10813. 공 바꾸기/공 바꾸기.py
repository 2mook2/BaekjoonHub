n, m = map(int, input().split(' '))

answer = [_+1 for _ in range(n)]

for x in range(m):
    i, j = map(int, input().split(' '))
    k = answer[i-1]
    answer[i-1] = answer[j-1]
    answer[j-1] = k

for _ in answer:
    print(_, end=' ')