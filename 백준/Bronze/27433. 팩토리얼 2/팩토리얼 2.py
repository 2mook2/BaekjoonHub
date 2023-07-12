# BOJ 27433번
n = int(input())

answer = 1
while n:
    answer *= n    
    n -= 1

print(answer)