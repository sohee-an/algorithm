# 8 n,m 문제 

n,m=map(int,input().split())
arr= list(map(int,input().split()))
# 1789
arr.sort()
path=[]

def dfs(start,depth):
    if m==depth:
        print(*path)
        return
    for i in range(start,n):
        path.append(arr[i])
        dfs(i,depth+1)
        path.pop()

dfs(0,0)