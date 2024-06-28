from collections import deque

# 입력 받기
nums_arr = [list(map(int, input().split())) for _ in range(4)]

# 방향벡터: 상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

res_set = set()

def bfs(x, y):
    q = deque()
    idx=1
    q.append((x, y,idx, str(nums_arr[x][y])))
   
    
    while q:
        cx, cy,idx, num_str = q.popleft()
        if idx ==6:
        # 7자리 숫자가 완성된 경우
            if len(num_str) == 7:
                res_set.add(num_str)
        else:
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                
                if 0 <= nx < 4 and 0 <= ny < 4:
                    q.append((nx, ny,idx+1, num_str + str(nums_arr[nx][ny])))

# 각 위치에서 시작하여 BFS 수행
for i in range(4):
    for j in range(4):
        bfs(i, j)

# 결과 출력
print(len(res_set))
