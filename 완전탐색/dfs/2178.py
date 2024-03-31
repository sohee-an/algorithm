from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())
# 
a = [] 
for _ in range(n):
    row = list(map(int, input().strip()))
    a.append(row)

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

q = deque([(0, 0)])

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and a[ny][nx] == 1 and visited[ny][nx] == 0:
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))

print(visited[n - 1][m - 1])
