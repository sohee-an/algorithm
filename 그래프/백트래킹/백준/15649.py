n, m = map(int, input().split())
visited = [False] * (n+1)
path = []



def dfs(depth):
    if depth == m:
        print(*path)
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            path.append(i)

            dfs(depth+1)

            path.pop()          # 상태 복구
            visited[i] = False  # 상태 복구

dfs(0)
