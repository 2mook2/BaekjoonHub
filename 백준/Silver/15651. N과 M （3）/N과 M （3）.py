# BOJ 15651번
n, m = map(int, input().split())

visited = [False] * (n + 1)

selected = []

def backtracking(depth):
    if depth == m:
        for x in selected:
            print(x, end=' ')
        print()
        return    
    
    for i in range(1, n + 1):
        # if not visited[i]:
        #     visited[i] = True
            selected.append(i)
            backtracking(depth + 1)
            # visited[i] = False
            selected.pop()

backtracking(0)