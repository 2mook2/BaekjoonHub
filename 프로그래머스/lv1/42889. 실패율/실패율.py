from collections import Counter

def solution(N, stages):
    전체인원 = len(stages)
    스테이지에_머물고_있는_사람 = Counter(stages)
    실패율 = {}
    for i in range(1, N+1):
        if 전체인원 > 0:
            실패율[i] = 스테이지에_머물고_있는_사람[i] / 전체인원
            전체인원 -= 스테이지에_머물고_있는_사람[i]
        else:
            실패율[i] = 0
    return sorted(실패율, key=lambda x:실패율[x], reverse=True)