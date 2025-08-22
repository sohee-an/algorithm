import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]


dx=[-1,1,0,0]
dy=[0,0,1,-1]
result=[]
def dfs(x,y):
    q=deque()
    q.append([x,y])
    
    visited[x][y]=True
    count=1
    
    while q:
        curx,cury = q.popleft()
        for i in range(4):
            nx=dx[i]+curx
            ny=dy[i]+cury
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==False and graph[nx][ny] == 1:
                visited[nx][ny]=True
                q.append([nx,ny])
                count+=1
    
    return count
                
        

for i in range(N):
    for j in range(N):
        if visited[i][j]==False and graph[i][j] == 1:
            result.append(dfs(i,j))


print(len(result))
result.sort()
for i in result:
    print(i)