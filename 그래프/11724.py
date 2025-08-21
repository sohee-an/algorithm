import sys 
from collections import deque
input = sys.stdin.readline

N,M= map(int,input().split())

g=[[]for _ in range(N+1)]

for _ in range(M):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)
    


result=0
visited=[False]*(N+1)
q=deque()

def bfs(cur):
    visited[cur]=True
    
    q.append(cur)
    while q:
        c = q.popleft()
        
        for i in g[c]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
        
    
    

# def dfs(cur):
#     visited[cur]=True
    
#     for next in g[cur]:
#         if not visited[next] :
#             dfs(next)
            
    

for i in range(1,len(g)):
    if not visited[i]:
        bfs(i)
        result+=1
print(result)