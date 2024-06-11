from collections import deque

n, l, r = map(int, input().split())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    
    union = [(x, y)]
    sum_population = graph[x][y]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    union.append((nx, ny))
                    sum_population += graph[nx][ny]
                    
    return union, sum_population

total_days = 0
while True:
    visited = [[0] * n for _ in range(n)]
    is_moved = False
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                union, sum_population = bfs(i, j)
                if len(union) > 1:
                    is_moved = True
                    new_population = sum_population // len(union)
                    for x, y in union:
                        graph[x][y] = new_population
    
    if not is_moved:
        break
    
    total_days += 1

print(total_days)
