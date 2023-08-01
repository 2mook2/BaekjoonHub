# BOJ 11478번
s = input()

result = []
for i in range(1, len(s) + 1):
    for j in range(len(s)):
        if len(s[j : j + i]) == i:
            result.append(s[j : j + i])
        else:
            break

answer = set(result)

print(len(answer))
