# BOJ 4948번
import sys
input = sys.stdin.readline

def prime_num(limit):
    primes = [False] * (limit + 1)
    
    for i in range(3, limit + 1, 2):
        for j in range(3, int(i ** 0.5) + 1, 2):
            if not i % j:
                break
        else:
            primes[i] = True

    return primes

limit = 123456 * 2

primes = prime_num(limit)

while True:
    n = int(input().rstrip())
    if not n:
        break
    if n == 1:
        answer = 1
    else:
        answer = sum(primes[n+1 : 2*n +1])
    print(answer)