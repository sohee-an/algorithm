n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]

visited = [[0] * n for _ in range(n)]
max_bishops = 0  # 놓을 수 있는 비숍 최대 개수


# ✅ (x, y)에 비숍을 둘 수 있는지 검사
def can_place(x, y):
    if graph[x][y] == 0:
        return False

    for d in range(4):
        nx, ny = x, y
        while 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 1:  # 사방팔방 대각선에 이미 비숍 있는지 확인하기
                return False
            nx += dx[d]
            ny += dy[d]
    return True


# ✅ 백트래킹 DFS
def dfs(idx, count):
    global max_bishops

    # ✅ 종료 조건: 모든 칸 탐색 완료
    if idx == n * n:
        max_bishops = max(max_bishops, count)
        return

    x, y = divmod(idx, n)

    # 이 칸에 비숍을 둘 수 있다면
    if can_place(x, y):
        visited[x][y] = 1
        dfs(idx + 1, count + 1)
        visited[x][y] = 0  # 복원

    # 안 두는 경우도 탐색
    dfs(idx + 1, count)


# ✅ 실행
dfs(0, 0)
print(max_bishops)
