from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                grid[nx][ny] = grid[x][y] + 1  # 이전 칸의 값 + 1
                q.append((nx, ny))
    
    return grid[n-1][m-1]  # 도착점의 값 반환

print(bfs(0, 0))