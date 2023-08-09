# BOJ 13241번
a, b = map(int, input().split())

a, b = min(a, b), max(a, b)

b의배수 = []

for i in range(1, a + 1):
    b의배수.append(b * i)

for i in b의배수:
    if not i % a:
        print(i)
        break