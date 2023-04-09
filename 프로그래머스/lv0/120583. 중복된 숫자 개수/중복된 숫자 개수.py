from collections import Counter

def solution(array, n):
    if Counter(array).get(n):
        answer = Counter(array).get(n)
    else:
        answer = 0
    return answer
