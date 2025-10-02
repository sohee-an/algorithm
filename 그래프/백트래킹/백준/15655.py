n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

path = []

def dfs(start, depth):
    if depth == m:
        print(*path)
        return
    for i in range(start, n):
        path.append(arr[i])
        dfs(i+1, depth+1)  # 다음은 i+1부터 시작 → 오름차순 보장
        path.pop()

dfs(0, 0)
