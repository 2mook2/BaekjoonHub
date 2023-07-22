# BOJ 2839번
n = int(input())

min_val = int(1e6)
for i in range((n // 5) + 1):
    target = n
    target -= 5 * i
    cnt = i
    if not target % 3:
        cnt += target // 3
        min_val = min(min_val, cnt)
    else:
        continue

if min_val == int(1e6):
    print(-1)
else:
    print(min_val)