# 단지번호 붙이기
from collections import deque
n =int(input(""))

visited=[[0]*n  for _ in range(n)]
input_list=[]
sum=0
cnt=0
answer_list=[]
for i in range(n):
    row=map(int,input("").split(" "))
    input_list.append()

def dfs (sx,sy,ex,ey):
  q=deque([sx,sy])
  visited[sx][sy]=1
  
  
  while q :
      cx,cy =q.pop(0)
      if(cx,cy)==(ex,ey):
          return 
      
      for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
          nx,ny=cx+dx,cy+dy
          if 0<nx<n and 0<ny<n and visited[nx][ny]==0 :
              if( input_list[nx][ny]==1):
                # 총합
                    q.append(nx,ny)
                    visited[nx,ny]
                    sum+=1
if cnt !=0:
        answer_list.append(cnt)
                  
            
              
            
        

    

answer=dfs(0,0,n-1,n-1)
print(answer_list)
