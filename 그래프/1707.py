import sys
from collections import deque
input = sys.stdin.readline

K = int(input()) 
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
   
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * (V+1)  # 0=미방문, 1=빨강, 2=파랑

    def bfs(start):
        q = deque([start])
        color[start] = 1   # 시작은 1로 색칠

        while q:
            cur = q.popleft()

            for nxt in graph[cur]:
                if color[nxt] == 0:  # 아직 안 칠해진 경우
                    color[nxt] = 3 - color[cur]  # 반대 색
                    q.append(nxt)
                elif color[nxt] == color[cur]:  # 같은 색이면 실패
                    return False
        return True

    ok = True
    for i in range(1, V+1):
        if color[i] == 0:   # 아직 방문 안 한 정점에서 BFS 시작
            if not bfs(i):
                ok = False
                break

    print("YES" if ok else "NO")
