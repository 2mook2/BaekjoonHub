# BOJ 13909번
"""
처음엔 모두 닫혀있지만, 모든 수가 1의 배수이므로 all True로 시작
windows = [False] + [True] * n

창문이 열려 있으면 True
창문이 닫혀 있으면 False
=> sum(windows) 하면 되겠다!

2 => False
3 => False
4 => 2의 배수일 때 False, 4일 때 True
5 => False
6 => 2의 배수일 때 False, 3의 배수일 때 True, 6일 때 False
7 => False
8 => 2의 배수일 때 False, 4의 배수일 때 True, 8일 때 False
9 => 3의 배수일 때 False, 9일 때 True,
10 => 2의 배수일 때 False, 5의 배수일 때 True, 10일 때 False

즉, 약수의 개수가 홀수이면 False / 약수의 개수가 짝수이면 True

약수의 개수가 짝수인 경우 
    : 제곱근 존재하는 경우
"""
n = int(input())

cnt = 0
for i in range(1, int(2100000000 ** 0.5) + 1): # 문제에서 주어진 최대 범위까지
    if i ** 2 > n:
        break
    cnt += 1

print(cnt)






