import sys
input = sys.stdin.readline

C = int(input())

for c in range(C):
    case = list(map(int, input().split()))
    평균 = sum(case[1:]) / case[0]
    
    평균초과 = len([x for x in case[1:] if x > 평균])
    비율 = 평균초과 / len(case[1:]) * 100
    비율 = '{:.3f}'.format(비율)
    print(f'{비율}%')