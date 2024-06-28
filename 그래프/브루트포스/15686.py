N,M=map(int,input().split())
arr=[]

home=[]
chicken=[]

for i in range(N):
    row=list(map(int,input().split()))
    arr.append(row)
    
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            home.append((i,j))
        elif arr[i][j]==2:
            chicken.append((i,j))
CNT=len(chicken)

def dfs(n,tlst):
    global ans
    if n==CNT:
        if len(tlst)==M:
            ans = min(ans,cal(tlst))
            
        return
    dfs(n+1tlst+[chi])