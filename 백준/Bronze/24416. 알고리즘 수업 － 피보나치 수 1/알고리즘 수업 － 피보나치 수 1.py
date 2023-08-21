# BOJ 24416번
import sys
sys.setrecursionlimit(int(1e9))
n = int(input())

dp = [0] * (n + 1)
cnt = 0
def fibo(n, dp):
    global cnt
    dp[1], dp[2] = 1, 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        cnt += 1
    return cnt

fibo(n, dp)
print(dp[n], cnt)
