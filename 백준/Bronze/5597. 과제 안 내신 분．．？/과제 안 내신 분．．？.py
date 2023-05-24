x = [int(input()) for _ in range(1, 29)]
y = set(range(1, 31)) - set(x)
z = [_ for _ in y]

for i in sorted(z):
    print(i)