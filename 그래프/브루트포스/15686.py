N,M=map(int,input().split())
# 치킨집 배열
arr=[]
# 치킨집 1을 살리느냐 마느냐 ,
# 이것도 부분집합 문제중하나임 -> 이진트리로 가능함 -> 내가 치킨집중에 고를거냐 말거냐의 문제임

home=[]
chicken=[]
ans=214000
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

def cal(tlist):
    sm=0
    for hi, hj in home:
        mn=2*N # 제일 큰 값을 넣기 
        for ci,cj in tlist:
            mn=min(mn,abs(hi-ci)+abs(hj-cj))
        sm+=mn
    return sm
            

def dfs(lev,tlst):
    global ans
    if lev==CNT:
        if len(tlst)==M:
            ans = min(ans,cal(tlst))
            
        return
    dfs(lev+1,tlst+[chicken[lev]])
    dfs(lev+1,tlst)
    
    
dfs(0,[])
print(ans)