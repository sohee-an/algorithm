grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

from  collections import deque

visited=[0 * 310 for _ in range(310)]
dy=[-1,0,1,0]
dx=[0,1,0,-1]

def numIslands(self) -> any:
    m = len(grid)
    n=len(grid[0])
    res=0
    def solution(x,y):
        q=deque()
        q.append(x,y)
        visited[x][y]=1
        
        while q:
            x,y=q.pop()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<m and 0<=ny<n and visited[nx][ny]==0:
                    q.append(nx,ny)
            
    
    
    for i in range(len(grid)):
        for j in range(len(i)):
            if visited[i][j]==0 and grid[i][j]=="1":
                solution(i,j)
                res+=1
        
    return res