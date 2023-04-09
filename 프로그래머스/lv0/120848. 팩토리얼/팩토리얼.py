def solution(n):
    factorial = 1
    x = 1
    while factorial <= n:
        factorial *= x
        x += 1
    answer = x - 2
    return answer