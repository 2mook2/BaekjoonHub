# BOJ 4134번
import sys
input = sys.stdin.readline

t = int(input().rstrip())

def prime_num(n):
    if n <= 1 :
        return 2
    cnt = 0
    while True:        
        for i in range(2, int((n + cnt) ** 0.5) + 1):
            if not (n + cnt) % i:
                break
        else:
            return n + cnt
        cnt += 1

for _ in range(t):
    n = int(input())
    print(prime_num(n))

