# BOJ 1546번
n = int(input())
scores = []
re_scores = []

score = list(map(int, input().split(' ')))
m = max(score)
score = [_/m*100 for _ in score]   
answer = 0
for _ in score:
    answer += _

answer = answer/n
print(answer)