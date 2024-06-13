from collections import deque

def bfs(start, target):
    max_pos = 100000
    visited = [0] * (max_pos + 1)
    visited[start]=1
    
    q = deque([start])
    
    while q:
        current = q.popleft()
        
        if current == target:
            return visited[current]-1
        
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= max_pos and not visited[next_pos]:
                visited[next_pos] = visited[current] + 1
                q.append(next_pos)

# 입력 받기
n, k = map(int, input().split())

print(bfs(n, k))
