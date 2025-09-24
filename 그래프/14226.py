# 1.복사를 하는거
# 2. 화면에 추가하는거(붙여넣기)
# 3. 화면꺼를 삭제하는거
from collections import deque

n= int(input())


screen=1
clipboard=0
min=0
q=deque()
max=10000
visited = [[False]*(max+1) for _ in range(max+1)]
def bfs(s,c):
    count =0
    q.append([s,c,count])
    visited[s][c] = True
    while q :
        cs,cc,c_count=q.popleft()
        
        if cs==n:
            return c_count
        for ns, nc in [(cs, cs), (cs+cc, cc), (cs-1, cc)]:
            if 0<=ns<=max and 0<=nc<=max:
                visited[ns][nc] = True
                q.append([ns,nc,c_count+1])
                
                
                
            
    
    
print(bfs(screen,clipboard))



