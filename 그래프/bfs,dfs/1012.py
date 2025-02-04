import sys
from collections import deque

input = sys.stdin.readline  

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    q = deque()
    q.append((x, y))
    graph[y][x] = 0  # ✅ 방문 처리

    while q:
        cx, cy = q.pop()  # DFS 방식 (LIFO)
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:  # ✅ 범위 수정
                graph[ny][nx] = 0  # 방문 처리
                q.append((nx, ny))

t = int(input().strip())

result_arr = []  # ✅ 테스트 케이스별 결과 저장
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1  # ✅ 올바른 좌표 저장

    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(j, i)  # ✅ x, y 순서 맞춤
                result += 1

    result_arr.append(result)  # ✅ 위치 수정

for res in result_arr:
    print(res)  # ✅ 모든 테스트 케이스 결과 출력
