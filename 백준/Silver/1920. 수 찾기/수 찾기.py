# BOJ 1920번
N = int(input())
A = set((map(int, input().split(' '))))

M = int(input())
X = list(map(int, input().split(' ')))

result = set(X) - A

for i in X:
    if i in result:
        print(0)
    else:
        print(1)