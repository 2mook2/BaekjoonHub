# BOJ 24511번
import sys
# from collections import deque
input = sys.stdin.readline

# 자료구조 개수
n = int(input().rstrip())

# 수열 a: 자료구조 정보
a = list(map(int, input().split())) # queue => 0, stack => 1

# 수열 b: i번 자료구조에 들어 있는 원소(각각 1개씩 들어 있음)
b = list(map(int, input().split()))

# 삽입할 수열 길이
m = int(input().rstrip())

# 삽입할 수열 c
c = list(map(int, input().split()))

"""
# (1)번 방법
# 실제로 넣었다 빼는 과정 구현 -> 시간초과
from collections import deque
b = [deque(_) for _ in b]

result = []
for i in c:
    for j in range(n):        
        if a[j]: # stack
            pass
        else: # queue
            b[j].append(i)
            i = b[j].popleft()
    result.append(i)
print(*result)

"""

"""
# (2)번 방법
# stack -> pass
# queue -> pop 원소와 자료구조 원소 바꾸기
# => 시간 초과
for i in c:
    for j in range(n):        
        if a[j]: # stack
            pass
        else: # queue
            i, b[j] = b[j], i
    print(i, end=' ')

"""

# (3)번 방법
# 처음부터 stack은 빼 버리기
# queue만 남으면 그냥 맨 마
from collections import deque
ab = zip(a, b)
result = deque()
for i in ab:
    if not i[0]:
        result.append(i[1])

answer = []
for i in c:
    result.appendleft(i)
    answer.append(result.pop())
print(*answer)