data = input().split()

a = int(data[0][::-1])
b = int(data[1][::-1])

print(max(a, b))