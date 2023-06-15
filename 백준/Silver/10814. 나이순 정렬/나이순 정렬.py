# BOJ 10814번
import sys
input = sys.stdin.readline
N = int(input())

info = []
for i in range(N):
    age, name = input().split()
    info.append((int(age), name))
    
info.sort(key=lambda x: x[0])
for j in info:
    print(j[0], j[1])