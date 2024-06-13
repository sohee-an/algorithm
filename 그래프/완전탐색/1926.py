from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    area_size = 1  # 시작점도 포함하므로 초기 크기는 1로 시작
    
    while q:
        cx, cy = q.popleft()
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx, ny))
                area_size += 1
    
    return area_size

visited = [[0] * m for _ in range(n)]
max_area = 0
count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            count += 1
            max_area = max(max_area, bfs(i, j))

print(count)  # 그림의 개수 출력
print(max_area)  # 최대 그림의 넓이 출력
