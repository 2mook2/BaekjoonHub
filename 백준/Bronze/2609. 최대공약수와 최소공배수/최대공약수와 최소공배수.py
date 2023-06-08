N, M = map(int, input().split(' '))

n_divisors = []
for n in range(1, N+1):
    if N % n == 0:
        n_divisors.append(n)
        
m_divisors = []
for m in range(1, M+1):
    if M % m == 0:
        m_divisors.append(m)
        
common_factors = [factor for factor in n_divisors if factor in m_divisors]
max_common_factor = max(common_factors)

print(max_common_factor)

n_common_multiples = []
for n in range(N, N*M+1, N):
    n_common_multiples.append(n)

m_common_multiples = []
for m in range(M, N*M+1, M):
    m_common_multiples.append(m)
    
common_factors = [factor for factor in n_common_multiples if factor in m_common_multiples]
min_common_factor = min(common_factors)

print(min_common_factor)