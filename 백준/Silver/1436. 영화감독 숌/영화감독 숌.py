# BOJ 1436번
n = int(input())
target = 666
while n:
    if '666' in str(target):
        n -= 1
    target += 1

print(target - 1)