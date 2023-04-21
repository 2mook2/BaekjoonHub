import re

def solution(s):
    if len(s) == 1:
        return 1
    압축문자열배열 = []
    for i in range(1, len(s)//2 + 1):
        패턴 = f'[a-z]{{1,{i}}}'
        패턴 = re.compile(패턴)
        압축문자열 = ''
        잘려진문자열 = 패턴.findall(s)
        count = 1
        for i in range(len(잘려진문자열)-1):
            if 잘려진문자열[i] == 잘려진문자열[i+1]:
                count += 1
            else:
                if count > 1:
                    압축문자열 += f'{count}{잘려진문자열[i]}'
                    count = 1 # 다음 문자열 받을 때에는 다시 count하기위해
                else:
                    압축문자열 += f'{잘려진문자열[i]}'
            if i == len(잘려진문자열)-2: 
                if count > 1:
                    if 잘려진문자열[i] == 잘려진문자열[i+1]:
                        압축문자열 += f'{count}{잘려진문자열[i]}'
                else:
                    압축문자열 += f'{잘려진문자열[i+1]}'
        압축문자열배열.append(len(압축문자열))
    return min(압축문자열배열)