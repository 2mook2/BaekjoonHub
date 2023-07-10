from collections import deque

# 행, 열
n, m = map(int, input().split())

# 그래프 정보
graph = [[int(i) for i in input()] for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

# BFS 정의
def bfs():
    # 방문 정보와 거리 정보를 동시에 저장하기 위해 3차원 리스트 사용
    # visited[i][j][w]는 (i, j) 위치에 벽을 w번 부순 상태에서의 방문 여부와 최단 거리를 저장
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1  # 시작 위치 방문 표시
    
    # 큐 생성
    queue = deque()
    queue.append((0, 0, 0))  # (x, y, 벽 부순 횟수)
    
    # BFS 수행
    while queue:
        x, y, wall = queue.popleft()
        
        # 도착 지점에 도달한 경우 최단 거리 반환
        if x == n - 1 and y == m - 1:
            return visited[x][y][wall]
        
        # 상, 하, 좌, 우로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 그래프 범위를 벗어나는 경우 건너뛰기
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽이 아니고 방문한 적이 없는 경우
            if graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                visited[nx][ny][wall] = visited[x][y][wall] + 1
                queue.append((nx, ny, wall))
            
            # 벽인 경우
            elif graph[nx][ny] == 1 and wall == 0 and visited[nx][ny][1] == 0:
                visited[nx][ny][1] = visited[x][y][wall] + 1
                queue.append((nx, ny, 1))
    
    # 도착 지점에 도달할 수 없는 경우 -1 반환
    return -1

# BFS 수행
result = bfs()

# 결과 출력
print(result)
