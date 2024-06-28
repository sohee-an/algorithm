n=int(input())
v=int(input())


arr_nums=[]
for i in range(n):
    row =list(map(int,input().split(" ")))
    arr_nums.append(row)
visited=[0 *n]
res=2140000
def soltuion(lev,total):

   
        if lev==n:
            if res>total:
                res=total
        else:
            for i in range(n):
                if visited[i]==0:
                    visited[i]=1
                    soltuion(lev+1,total+arr_nums[lev][i])

    
    
    
soltuion(0,0)
print(res)