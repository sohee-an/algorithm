# n,m 12번 문제

n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
path=[]

# 1799
def dfs(start,depth):
    if m==depth:
        print(*path)
        return
    prev=0
    for i in range(start,n):
        if prev != arr[i]:  
            prev=arr[i]
            path.append(arr[i])
            dfs(i,depth+1)
            path.pop()

dfs(0,0)

