N, K = map(int, input().split())

n = list(range(1, N + 1))
results = []
idx = K - 1

while n:
    if idx >= len(n):
        idx = idx % len(n)
    else:
        result = n.pop(idx)
        results.append(result)
        idx += K - 1

answer = '<' + ', '.join(map(str, results)) + '>'
print(answer)
