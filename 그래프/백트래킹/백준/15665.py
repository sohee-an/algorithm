# n,m 11번 문제

n,m=map(int,input().split())
# 1 7 9 9
arr=list(map(int,input().split()))
arr.sort()
path=[]
# visited=[False]*n


def dfs(depth):
    if m==depth:
        print(*path)
        return
    prev=0
    for i in range(n):
        if prev is not arr[i]:
            path.append(arr[i])
            prev=arr[i]
            dfs(depth+1)
            path.pop()


dfs(0)