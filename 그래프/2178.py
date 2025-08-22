import sys
input = sys.stdin.readline
from collections import deque

N, M =map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

q=deque()
def bfs(x,y):
    q.append([x,y])
    visited[x][y]=True
   
    
    while q:
        curx,cury =q.popleft()
        for i in range(4):
            nx= dx[i]+curx
            ny= dy[i]+cury
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1 and  visited[nx][ny]==False:
              
                graph[nx][ny] = graph[curx][cury] + 1
                q.append((nx, ny))

    return graph[N-1][M-1]
    

print(bfs(0,0))

