# BOJ 2501번
n, k = map(int, input().split())

m = []
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        m.append(i)
        m.append(n // i)

m = list(set(m))
m.sort()

try:
    print(m[k - 1])
except:
    print(0)