# 유기농 배추
from collections import deque
resultarr=[]
result=0

answer=[]


visited = [[0] * 100 for _ in range(100)]
dy=[-1,0,1,0]
dx=[0,1,0,-1]



def dfs(plantarr,x,y,m,n):

    sum=1
    q = deque([(x, y)])
    visited[x][y]=1
    
    while q:
        x,y=q.pop()       
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and plantarr[nx][ny]==1 and visited[nx][ny]==0:
              
                
                q.append((nx, ny))
                visited[nx][ny]=1
                sum+=1  
    if(sum>0):
      
        resultarr.append(sum)
        sum=1
   
    return resultarr



def Solve():
    n,m,x=map(int,input().split(" "))
    re=[]
    global resultarr
    resultarr=[]
    global visited
    visited = [[0] * 100 for _ in range(100)]

  
    plantarr=[[0]*m for _ in range(n) ]

    for i in range(x):
        x, y = map(int, input("").split(" "))
        plantarr[x][y]=1
    
  
    for i in range(0, len(plantarr)): 
        for j in range(0,len(plantarr[i])):
           
            if(plantarr[i][j]==1 and visited[i][j]==0):
               
               re=  dfs(plantarr,i,j,m,n)
              
    
    
    answer.append(len(re))
   
    

count=int(input(""))
for n in range(count):
    Solve();
    
    
for num in answer:
    print(num)

# 1
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6

