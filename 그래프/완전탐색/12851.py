from collections import deque

def bfs(start, target):
    max_pos = 100000
    visited = [0] * (max_pos + 1)
    count = [0] * (max_pos + 1)
    visited[start] = 1
    count[start] = 1
    
    q = deque([start])
    
    while q:
        current = q.popleft()
        
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= max_pos:
                if not visited[next_pos]:
                    visited[next_pos] = visited[current] + 1
                    count[next_pos] = count[current]
                    q.append(next_pos)
                elif visited[next_pos] == visited[current] + 1:
                    count[next_pos] += count[current]
    
    return visited[target] - 1, count[target]

# 입력 받기
n, k = map(int, input().split())

# 최단 시간과 방법의 수를 구함
min_time, ways = bfs(n, k)
print(min_time)
print(ways)
