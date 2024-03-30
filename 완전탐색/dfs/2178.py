from collections import deque

max_n = 100
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)] 

# 방문하기
visited[0][0] = 1

q = deque([(0, 0)])

while q:
    y, x = q.popleft()
    print(x,y)
   
    for i in range(4):
        ny = y + dy[i]#1 0
        print(ny)
        nx = x + dx[i]
      
        if ny < 0 or ny >= n or nx < 0 or nx >= m or a[ny][nx] == 0:
            continue
        if visited[ny][nx] != 0:
            continue
        
        visited[ny][nx] = visited[y][x] + 1
        print(visited)
        q.append((ny, nx))
        
print(visited[n-1][m-1])


# 
# 2 6
# 101111
# 111011
