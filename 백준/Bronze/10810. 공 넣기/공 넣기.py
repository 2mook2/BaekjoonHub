n, m = map(int, input().split(' '))

result = [0 for _ in range(n)]

for x in range(m):
    i, j, k = map(int, input().split(' '))
    for y in range(i-1,j):
        result[y] = k
    
for _ in result:
    print(_, end=' ')