import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
g = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

for row in g:
    row.sort()

# DFS
dfs_visited = [False] * (N + 1)
def dfs(c):
    dfs_visited[c] = True
    print(c, end=" ")
    for nxt in g[c]:
        if not dfs_visited[nxt]:
            dfs(nxt)

# BFS
def bfs(start):
    bfs_visited = [False] * (N + 1)
    q = deque([start])
    bfs_visited[start] = True

    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for nxt in g[cur]:
            if not bfs_visited[nxt]:
                bfs_visited[nxt] = True
                q.append(nxt)

dfs(V)
print()
bfs(V)
