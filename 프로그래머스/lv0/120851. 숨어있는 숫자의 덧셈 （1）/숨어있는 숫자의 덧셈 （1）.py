import re
def solution(my_string):
    result = re.sub(r'[^0-9]', '', my_string)
    answer = 0
    for i in result:
        answer += int(i)
    return answer
