# BOJ 2903번
n = int(input())

dp = [2 ** i for i in range(15)]

result = 2
for i in range(n):
    result += dp[i]

print(result ** 2)
