# BOJ 9063번
n = int(input())

x = []
y = []
for _ in range(n):
    u, v = map(int, input().split())
    x.append(u)
    y.append(v)

width = max(x) - min(x)
height = max(y) - min(y)

print(width * height)