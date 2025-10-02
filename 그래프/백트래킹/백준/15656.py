# n,m문제 7
n,m=map(int,input().split())

arr= list(map(int,input().split()))
arr.sort()
# 1789
path=[]

def dfs(depth):
    if m==depth:
        print(*path)
        return
    for i in range(n):
        path.append(arr[i])
        dfs(depth+1)
        path.pop()

dfs(0)