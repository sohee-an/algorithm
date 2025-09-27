n, m = map(int, input().split())
path = []

def dfs(start, depth):
    if depth == m:
        print(*path)
        return
    for i in range(start, n+1):   # start부터 시작 → 오름차순 보장
        path.append(i)
        dfs(i+1, depth+1)         # 다음 숫자는 i+1부터
        path.pop()

dfs(1, 0)
