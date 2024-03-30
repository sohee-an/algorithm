
from collections import deque
n =int(input(""))
m =int(input(""))
vertices=[[] for _ in range(n+1)]


for i in range(m):
    x,y=map(int,input(" ").split(" "))
  
    vertices[x].append(y)
    vertices[y].append(x)

visited=[False]*(n+1)
cnt=0
    
    
def dfs(start):
    global cnt;
    # 스택에 넣는다 
    stack=deque([start])
    
    while stack:
        x=stack.pop();
        visited[x]=True
        
        for next_node in vertices[x]:
            
            if  visited[next_node]==False:
                
                visited[next_node]=True
                stack.append(next_node)
                cnt+=1
                
            
    return cnt   


dfs(1)
print(str(cnt))   
    
    