# 2-c 안전영역
from collections import deque
n = int(input())
graph = []
tree=[]
maxNum = 0

dy=[-1,0,1,0]
dx=[0,1,0,-1]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j] 
            
def dfs(num,x,y,visited):
    
    q=deque()
    q.append((x,y))
    visited[x][y]=1
  
    
    while q :
        x,y=q.pop()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and graph[nx][ny] >num:
                visited[nx][ny]=1
                q.append((nx,ny))
                
    




result =[]


for i in range(maxNum):
    cnt=0
    visited = [[0] * n for _ in range(n)]
    
    for j in range(n):
        for k in range(n):
            if  graph[j][k] > i and visited[j][k]==0:
                cnt+=1
                dfs(i,j,k,visited)
    result.append(cnt)
                
print(max(result))
                
