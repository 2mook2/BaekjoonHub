import sys
input = sys.stdin.readline

arr = input().split()
n, b = arr[0][::-1], arr[1]

dic = dict()
for i in range(10):
    dic[str(i)] = i

for i in range(10, 36):
    dic[chr(i + 55)] = i

answer = 0
for i in range(len(n)):
    answer += dic[n[i]] * (int(b) ** i)

print(answer)