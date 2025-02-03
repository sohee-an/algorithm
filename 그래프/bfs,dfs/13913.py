from collections import deque

def bfs(N, K):
    MAX = 20  # 문제에서 주어진 범위 (0 ≤ X ≤ 100000)
    visited = [-1] * MAX  # 방문 여부 + 이전 위치 저장 (경로 추적)
    time = [0] * MAX  # 최단 시간 저장

    queue = deque([N])
    visited[N] = N  # 시작 지점은 자기 자신을 가리킴

    while queue:
        current = queue.popleft()

        # 목표 위치에 도착하면 종료
        if current == K:
            break

        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos < MAX and visited[next_pos] == -1:  # 미방문 위치 체크
                visited[next_pos] = current  # 경로 추적을 위해 부모 노드 저장
                time[next_pos] = time[current] + 1  # 최단 시간 저장
                queue.append(next_pos)
        print(visited)

    # 경로 역추적
    path = []
    pos = K
    while pos != N:
        path.append(pos)
        pos = visited[pos]
    path.append(N)  # 시작점 추가
    path.reverse()  # 역순이므로 뒤집기

    return time[K], path  # 최소 시간, 이동 경로 반환

# 입력 받기
N, K = map(int, input().split())

# BFS 실행 및 결과 출력
min_time, path = bfs(N, K)



# print(min_time)  # 최단 시간 출력
# print(" ".join(map(str, path)))  # 이동 경로 출력
