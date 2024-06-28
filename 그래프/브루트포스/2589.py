from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] == "L":
                visited[nx][ny] = 1
                cnt=max(cnt,visited[nx][ny])
                q.append((nx, ny))
                
    
    return cnt

n, m = map(int, input().split())
arr = []

for _ in range(n):
    row = list(input().strip())
    arr.append(row)

visited = [[0] * m for _ in range(n)]
max_distance = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == "L" and visited[i][j] == 0:
            print(bfs(i,j))
            max_distance = max(max_distance, bfs(i, j))

print(max_distance)
