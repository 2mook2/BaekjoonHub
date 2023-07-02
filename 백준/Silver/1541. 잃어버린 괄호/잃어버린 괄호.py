# BOJ 1541번
import sys
input = sys.stdin.readline

eqn = input().rstrip()
minus = eqn.split('-')

answer = sum(map(int, minus[0].split('+')))

minus = [i for i in minus[1:]]

for i in minus:
    x = sum(map(int, i.split('+')))
    answer -= x

print(answer)