n, m = map(int, input().split())
path = []

def dfs(start, depth):
    if depth == m:
        print(*path)
        return
    for i in range(start, n+1):   # start부터 n까지
        path.append(i)
        dfs(i, depth+1)           # 같은 수 다시 선택 가능
        path.pop()

dfs(1, 0)
