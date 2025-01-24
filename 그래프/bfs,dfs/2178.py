from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 2번째 방법
# def bfs(x, y):
#     global result  # 전역 변수 result 사용
#     q = deque()
#     q.append((x, y))
#     grid[x][y] = 0  # 시작점 방문 처리
#     result = 1  # 시작점 포함 경로 길이 초기화
#     while q:
#         size = len(q)
#         for _ in range(size):
#             x, y = q.popleft()
#             # x, y가 끝에 도달했을 때, return
#             if x == n-1 and y == m-1:
#                 return result
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]

#                 if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
#                     q.append((nx, ny))
#                     grid[nx][ny] = 0

#         result += 1

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                grid[nx][ny] = grid[x][y] + 1  # 이전 칸의 값 + 1
                q.append((nx, ny))
    
    return grid[n-1][m-1]  # 도착점의 값 반환

print(bfs(0, 0))