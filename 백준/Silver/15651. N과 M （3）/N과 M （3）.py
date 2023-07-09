# BOJ 15651번
n, m = map(int, input().split())
arr = [_ for _ in range(1, n + 1)]
visited = [False] * n

selected = []

def backtracking(depth):
    if depth == m:
        for i in selected:
            print(i, end=' ')
        print()
        return
    
    for j in range(n):
        # if visited[j]:
        #     continue
        # visited[j] = True
        selected.append(arr[j])
        backtracking(depth + 1)
        # visited[j] = False
        selected.pop()

backtracking(0)