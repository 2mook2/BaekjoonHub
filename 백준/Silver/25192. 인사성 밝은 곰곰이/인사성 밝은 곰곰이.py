# BOJ 25192번
n = int(input())

cnt = n
answer = 0
while cnt:
    logs = set()
    for i in range(cnt):
        log = input()
        cnt -= 1
        if log == "ENTER":
            break
        logs.add(log)
    result = len(logs)
    answer += result

print(answer)