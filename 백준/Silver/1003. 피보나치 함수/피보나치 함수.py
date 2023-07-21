# BOJ 1003번
t = int(input())
while t:
    dp = [0] * 41
    
    dp[1] = 1
    for i in range(2, 41):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    n = int(input())
    
    if not n:
        print(1, 0)
    else:
        print(dp[n - 1], dp[n])
    t -= 1