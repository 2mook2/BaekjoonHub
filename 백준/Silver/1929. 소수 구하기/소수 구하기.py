# BOJ 4134번
n, m = map(int, input().split())

def smallest_prime_num(n, m):
    cnt = 0
    
    while n + cnt <= m:
        if n + cnt == 1:
            cnt += 1
            pass
        for i in range(2, int((n + cnt) ** 0.5) + 1):
            if not (n + cnt) % i:
                break
        else:
            print(n + cnt)
        
        cnt += 1
    
    return

answer = smallest_prime_num(n, m)
