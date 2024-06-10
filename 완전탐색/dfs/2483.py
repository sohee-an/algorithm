# 세로, 가로, 네모 숫자
from collections import deque

n,m,k=map(int,input().split())
graph = [[0]*m for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs (x,y):
    q= deque()
    q.append((x,y))
    graph[x][y]=1
    area=0
    
    while q:
        x,y = q.popleft()
        area+=1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if(0<=nx<n and 0<=ny<m and graph[nx][ny]==0):
                graph[nx][ny]=1 
                q.append((nx,ny))
    return area


for _ in range(k):
    x1,y1,x2,y2 =map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j]=1
        




areas =[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            areas.append(bfs(i,j))
            
            
areas.sort()
print(len(areas))
print(' '.join(map(str, areas)))