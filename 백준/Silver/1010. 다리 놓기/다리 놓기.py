# BOJ 1010번
import sys
from math import comb
input = sys.stdin.readline

t = int(input().rstrip())

while t:    
    n, m = map(int, input().split())
    
    answer = comb(m, n)
    
    print(answer)
    
    t -= 1
