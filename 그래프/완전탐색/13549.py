# 숨바꼭질2
from collections import deque
n,k= map(int,input().split(" "))

q=deque()

def bfs(start,end):
    q.append(start)
    max_pos=100000
    visited = [0] * (max_pos + 1)
    visited[start] = 1  
    
    while q :
        current =q.popleft();
        
        if current == end:
            return visited[current] - 1 
        
        
        next_pos = current * 2
        if 0 <= next_pos <= max_pos and not visited[next_pos]:
            visited[next_pos] = visited[current] 
            q.append(next_pos)
        
        
        for next_pos in (current - 1, current + 1):
            if 0 <= next_pos <= max_pos and not visited[next_pos]:
                visited[next_pos]=visited[current]+1
                q.append(next_pos)
                
    
print(bfs(n,k))