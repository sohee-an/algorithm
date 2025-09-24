from collections import deque

n, k = map(int, input().split())
MAX = 100000
visited = [False] * (MAX + 1)
parent = [-1] * (MAX + 1)   # 수정된 부분

def bfs(n, k):
    q = deque()
    q.append([n, 0])
    visited[n] = True

    while q:
        cx, c_count = q.popleft()

        if cx == k:
            # 경로 복원
            path = []
            while cx != -1:
                path.append(cx)
                cx = parent[cx]
            path.reverse()
            return c_count, path

        for nx in (cx+1, cx-1, cx*2):
            if 0 <= nx <= MAX and not visited[nx]:
                visited[nx] = True
                parent[nx] = cx
                q.append([nx, c_count+1])

dist, path = bfs(n, k)
print(dist)
print(" ".join(map(str, path)))
