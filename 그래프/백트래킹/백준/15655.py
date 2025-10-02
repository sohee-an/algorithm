n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
path = []
# 1789 
# 11234

def dfs(depth, start):
    if depth == m:
        print(*path)
        return
    prev = 0
    for i in range(start, n):
        if prev == arr[i]:
            continue
        prev = arr[i]
        path.append(arr[i])
        dfs(depth+1, i)  
        path.pop()

dfs(0, 0)
