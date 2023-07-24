import sys

# 입력과 출력을 모두 sys.stdin, sys.stdout를 이용하여 처리
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())

# 10,000 이하의 자연수를 카운팅할 배열
count = [0] * 10001

for i in range(n):
    x = int(input().rstrip())
    count[x] += 1

# 배열에 저장된 수만큼 해당 인덱스(수)를 출력
for num in range(1, 10001):
    if count[num] > 0:
        for _ in range(count[num]):
            print(f"{num}\n")
