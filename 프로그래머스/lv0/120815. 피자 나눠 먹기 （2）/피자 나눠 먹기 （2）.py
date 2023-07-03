def solution(n):
    pizza = 6
    answer = 1
    while pizza % n :
        answer += 1
        pizza += 6
    return answer

# from math import lcm

# def solution(n):
#     answer = lcm(6, n) // 6
#     return answer

# print(solution(4))