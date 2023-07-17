# BOJ 1436번
n = int(input())
x = '666'
종말의수 = [i for i in range(666, 10000666) if str(i).count(x) >= 1]
print(종말의수[n - 1])