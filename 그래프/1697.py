n, k = map(int, input().split())
from collections import deque
q=deque()
dx=[-1,1,2]
# n은 수빈이 있는 위치 //// k 는  동생이 있는 위치

def bfs(n,count):
    q.append([n,count])
    while q:
        cx,c_count=q.popleft()
        for i in range(3):
            
            if i ==1:
                nx=cx+1
            if i ==2:
                nx=cx-1
            if i==3:
                nx=cx*2
            if nx!=k:
                q.append([nx,c_count+1])
        
    return c_count
                


print(bfs(n, 0))