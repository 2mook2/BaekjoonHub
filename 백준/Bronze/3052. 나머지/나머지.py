# BOJ 3052번
input_num = [int(input()) for _ in range(10)]

result = [_%42 for _ in input_num]

answer = len(set(result))

print(answer)
