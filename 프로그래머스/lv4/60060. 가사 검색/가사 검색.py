# 효율성을 고려하지 않은 풀이법 -> class로 짜야 한다!
# import re

# def solution(words, queries):
#     결과 = []
#     for q in queries:
#         패턴 = q.replace('?', '.')
#         패턴 = re.compile(패턴)
#         count = 0
#         for word in words:
#             매칭패턴 = 패턴.findall(word)
#             if 매칭패턴 and len(word) == len(q):
#                 count += 1
#         결과.append(count)
#     return 결과
class Node(object):
    def __init__(self):
        self.레벨단위연결노드 = {}
        
    def insert_data(self, 문자열):
        for 문자 in 문자열:
            if 문자 not in self.레벨단위연결노드:
                self.레벨단위연결노드[문자] = {
                     '연결노드' : Node(),
                     '개수' : 1,
                }
            else:
                self.레벨단위연결노드[문자]['개수'] += 1
            self = self.레벨단위연결노드[문자]['연결노드']
            
    def get_count(self, 문자열):
        for 문자 in 문자열:
            if 문자 == '?':
                return temp
            elif 문자 not in self.레벨단위연결노드:
                return 0
            temp = self.레벨단위연결노드[문자]['개수']
            self = self.레벨단위연결노드[문자]['연결노드']
        return self.레벨단위연결노드[문자]['개수']
            
def solution(words, queries):
    answer = []
    
    트라이 = [Node() for i in range(10001)]
    트라이역순 = [Node() for i in range(10001)]
    
    for word in words:
        트라이[len(word)].insert_data('!' + word)
        트라이역순[len(word)].insert_data('!' + word[::-1])
    
    for q in queries:
        if q[0] != '?':
            answer.append(트라이[len(q)].get_count('!' + q))
        else:
            answer.append(트라이역순[len(q)].get_count('!' + q[::-1]))
    
    return answer