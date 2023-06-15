
import sys
input = sys.stdin.readline

N = int(input())
people = []
for i in range(N):
    age, name = input().split()
    people.append([age, name, i])

people = sorted(people, key=lambda x: (int(x[0]), x[2]))
for p in people:
    print(p[0] + ' ' + p[1])
