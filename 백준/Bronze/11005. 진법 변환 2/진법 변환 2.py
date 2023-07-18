# BOJ 11005번
n, b = map(int, input().split())

highest_degree = 0
while b ** highest_degree <= n:
    highest_degree += 1
highest_degree -= 1

quotient = []
for i in range(highest_degree, -1, -1):
    quotient.append(n // (b ** i))
    n %= (b ** i)
# print(quotient)

dic = dict()
for i in range(10):
    dic[i] = str(i)
for i in range(10, 36):
    dic[i] = chr(55 + i)
# print(dic)

for i in quotient:
    print(dic[i], end='')