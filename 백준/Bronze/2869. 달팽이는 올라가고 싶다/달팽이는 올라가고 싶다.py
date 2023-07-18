# BOJ 2869번
a, b, v = map(int, input().split())

if (v - a) % (a - b):
    day = (v - a) // (a - b) + 1
else:
    day = (v - a) // (a - b)

print(day + 1)