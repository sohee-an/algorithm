
ch=[0]*(3+1)
n=3
def dfs(v):
#    /종착점
    
    if v==n+1:
        for i in range(1,n+1):
            print(ch)
            if ch[i]==1:
                print(i, end=" ")
            
       
        
    else:
        ch[v]=1
        dfs(v+1)
        ch[v]=0
        dfs(v+1)
    
    
    
    
     
    
 
def main(n):
    # n=int(input())
     ch=[0]*(n+1)
     dfs(1)
    
main(3)    