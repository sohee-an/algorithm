from collections import deque

# 방향 설정 (상, 하, 좌, 우)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    # 불의 단거리 
    while fire_queue:
        y, x = fire_queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < r and 0 <= nx < c and fire_time[ny][nx] == -1 and maze[ny][nx] != '#':
                fire_time[ny][nx] = fire_time[y][x] + 1
                fire_queue.append((ny, nx))
    
    while jihoon_queue:
        y, x = jihoon_queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not (0 <= ny < r and 0 <= nx < c):  # 미로를 벗어난 경우
                return jihoon_time[y][x] + 1
            if jihoon_time[ny][nx] == -1 and maze[ny][nx] == '.' and (fire_time[ny][nx] == -1 or jihoon_time[y][x] + 1 < fire_time[ny][nx]):
                jihoon_time[ny][nx] = jihoon_time[y][x] + 1
                jihoon_queue.append((ny, nx))
    return "IMPOSSIBLE"

# 입력 받기
r, c = map(int, input().split())
maze = [list(input().strip()) for _ in range(r)]

fire_queue = deque()
jihoon_queue = deque()

fire_time = [[-1] * c for _ in range(r)]
jihoon_time = [[-1] * c for _ in range(r)]

# 초기 위치 설정
for i in range(r):
    for j in range(c):
        if maze[i][j] == 'F':
            fire_queue.append((i, j))
            fire_time[i][j] = 0
        elif maze[i][j] == 'J':
            jihoon_queue.append((i, j))
            jihoon_time[i][j] = 0

# 결과 출력
print(bfs())
