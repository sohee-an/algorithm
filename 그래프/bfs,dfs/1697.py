# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다. 
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
from collections import deque
N, K =list(map(int, input().split()))

def bfs(start, target):
    visited = [0] * 100001  # 방문 여부 및 최단 시간 저장
    queue = deque([start])  # BFS 큐 생성
    
    while queue:
        x = queue.popleft()
        
        # 목표 위치에 도착하면 종료
        if x == target:
            return visited[x] 
        
        # 이동 가능한 경우 탐색
        for next_pos in (x-1, x+1, x*2):
            if 0 <= next_pos < 100001 and visited[next_pos] == 0:  # 범위 체크 & 미방문 체크
                visited[next_pos] = visited[x] + 1  # 최단 거리 업데이트
                queue.append(next_pos)  # 큐에 추가
    
    return -1  # 이론상 실행될 일이 없음

print(bfs(N, K)) 