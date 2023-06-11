# BOJ 1920번
N = int(input())
A = list(map(int, input().split(' ')))

M = int(input())
X = list(map(int, input().split(' ')))

존재하지않음 = set(X) - set(A)

for i in X:
    if i in 존재하지않음:
        print(0)
    else:
        print(1)