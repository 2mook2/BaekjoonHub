def solution(num_list):
    answer = []
    even_num = 0
    odd_num = 0
    
    for _ in num_list:
        if _ % 2 == 0:
            even_num += 1
        if _ % 2 == 1:
            odd_num += 1
    
    answer.extend([even_num, odd_num])
            
    return answer