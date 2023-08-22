# BOJ 25192번
import sys
input = sys.stdin.readline

n = int(input().rstrip())

answer = 0
while n:
    logs = set()
    for i in range(n):
        log = input().rstrip()
        n -= 1
        if log == "ENTER":
            break
        logs.add(log)
    result = len(logs)
    answer += result

print(answer)