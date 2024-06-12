from collections import deque

n = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

graph = []

for _ in range(n):
    row = list(input())
    graph.append(row)

def dfs(x, y, visited, person):
    visited[x][y] = True
    q = deque([(x, y)]) 
    color = graph[x][y]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if person:
                    # 적록색약인 경우 'R'과 'G'를 같은 색상으로 취급
                    if (graph[nx][ny] == 'R' or graph[nx][ny] == 'G') != (color == 'B'):
                        
                        visited[nx][ny] = True
                        q.append((nx, ny))
                else:
                    if graph[nx][ny] == color:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            
# 적록색약이 아닌 경우
visited_normal = [[False] * n for _ in range(n)]
result_normal = 0
for i in range(n):
    for j in range(n):
        if not visited_normal[i][j]:
            dfs(i, j, visited_normal, False)
            result_normal += 1

# 적록색약인 경우
visited_red_green_blind = [[False] * n for _ in range(n)]
result_red_green_blind = 0
for i in range(n):
    for j in range(n):
        if not visited_red_green_blind[i][j]:
            dfs(i, j, visited_red_green_blind, True)
           
            result_red_green_blind += 1

print(result_normal, result_red_green_blind)
