def solution(my_string):
    answer = ''
    for i, j in enumerate(my_string[::-1]):
        if j not in my_string[:-(i+1)]:
            answer += j
    answer = answer[::-1]
    return answer