# n.m 9번 문제 
n,m=map(int,input().split())
arr= list(map(int,input().split()))
# 1799 
# 17 19 71 79 91 
#  일단 같은 숫자도 고르면 안되고 , 
# 같은 수열도 안됨 
# 순서는 상관없음
arr.sort()
path =[]
visited=[False]*n
def dfs(depth):
    if m==depth:
        print(*path)
        return 
    prev=0
    for i in range(n):
        
        if prev == arr[i] :
            continue
        if visited[i]==False:
            visited[i]=True
            prev=arr[i]
            path.append(arr[i])
            dfs(depth+1)
            path.pop()
            visited[i]=False
            

dfs(0)