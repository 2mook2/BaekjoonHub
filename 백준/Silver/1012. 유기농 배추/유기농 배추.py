import sys
sys.setrecursionlimit(int(1e6))
t = int(input())

while t:
    n, m, k = map(int, input().split())
    
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        u, v = map(int, input().split())
        graph[u][v] = 1
    
    visited = [[False] * m for _ in range(n)]
    
    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if not visited[x][y] and graph[x][y] == 1:
            visited[x][y] = True
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
    
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    
    print(result)    
    t -= 1