# 단지번호 붙이기
from collections import deque
n =int(input())

dy=[-1,0,1,0]
dx=[0,1,0,-1]

visited=[[0]*n  for _ in range(n)]
graph=[]

for i in range(n):
    row = list(map(int, input().strip()))
    graph.append(row)
    
def bfs(i,j):
    
    q=deque()
    visited[i][j]=1
    q.append((i,j))
    
    cnt=0
    while q:
        x,y=q.popleft()
        cnt+=1
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and graph[nx][ny]==1:
                visited[nx][ny]=1
                q.append((nx,ny))
    return cnt
        
result=[]
for i in range(n):
    for j in range(n):   
        if visited[i][j]==0 and graph[i][j]==1:
            result.append(bfs(i,j))
            
            
result.sort()
print(len(result))
for r in result:
    print(r)