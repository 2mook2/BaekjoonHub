def solution(num_list):
    answer = [0, 0]    
    for _ in num_list:
        answer[_%2] += 1
        
    return answer