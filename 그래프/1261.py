from collections import deque

M, N = map(int, input().split())  
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def bfs(x, y): 
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True   

    while q:
        cx, cy, cost = q.popleft()

        if cx == N-1 and cy == M-1: 
            return cost

        for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                if grid[nx][ny] == 0:
                    q.appendleft((nx, ny, cost))  
                else:
                    q.append((nx, ny, cost+1))     # 벽

print(bfs(0,0))
