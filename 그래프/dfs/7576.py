# bfs 토마토
# 가로,세로
M,N =map(int, input().split())
from collections import deque

# 왼,아래,오른쪽,위
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


graph=[]
q=deque()

for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(M):
        if row[j] == 1:
            q.append((i, j))


      
while q:
    x,y=q.popleft();
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
       
        if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
            
            graph[nx][ny]=graph[x][y]+1
            q.append((nx,ny))
            
            
max_days = 0
for row in graph:
    for value in row:
        if value == 0:  # 익지 않은 토마토가 남아있으면
            print(-1)
            exit()
        max_days = max(max_days, value)
            
print(max_days-1)