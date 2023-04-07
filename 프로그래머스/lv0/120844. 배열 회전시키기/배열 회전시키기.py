def solution(numbers, direction):
    if direction == 'right':
        x = [numbers.pop()]
        answer = x + numbers
    elif direction == 'left':
        y = [numbers.pop(0)]
        answer = numbers + y
    return answer