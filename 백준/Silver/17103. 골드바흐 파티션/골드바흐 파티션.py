def is_prime(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

limit = int(1e6)
primes = is_prime(limit)

t = int(input())

for _ in range(t):
    n = int(input())

    cnt = 0
    for i in range(2, n // 2 + 1):
        if primes[i] and primes[n - i]:
            cnt += 1
    
    print(cnt)