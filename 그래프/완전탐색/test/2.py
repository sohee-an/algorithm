c,n=input(" ").split(" ")
a=[0]*5
result=111
for i in range(n):
    a[i]=int(input())
        
    
def dfs(v,sum):
    if v==n:
        if sum>result:
            result=sum
    
        
    else:
        dfs(v+1,sum+a[v])
        dfs(v,sum)
        
        
        
    



    
    dfs(0,0)