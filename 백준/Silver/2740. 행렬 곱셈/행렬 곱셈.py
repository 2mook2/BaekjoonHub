n, m = map(int, input().split())

matrix_a = [[] for _ in range(n)]

for i in range(n):
    x = list(map(int, input().split()))
    matrix_a[i].extend(x)

m, k = map(int, input().split())

matrix_b = [[] for _ in range(m)]

for j in range(m):
    y = list(map(int, input().split()))
    matrix_b[j].extend(y)

result_matrix = [[0] * k for _ in range(n)]

for i in range(n):
    for l in range(k):
        for j in range(m):
            result_matrix[i][l] += matrix_a[i][j] * matrix_b[j][l]

for row in result_matrix:
    print(' '.join(map(str, row)))
