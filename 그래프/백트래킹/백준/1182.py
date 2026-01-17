n,s= map(int,input().split())
arr=list(map(int,input().split()))
path=[]

def dfs(start,depth,sum,count):

    for i in range(start,len(arr)):
        n_sum=sum+arr[i]
        if n_sum>0:
            dfs(i+1,depth+1,sum+arr[i+1],count)
        elif n_sum==0:   
            dfs(i+1,depth+1,sum+arr[i+1],count+1)
       




print(dfs(0,0,0,0))