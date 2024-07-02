n=int(input())

nums_arr=[]
for i in range(n):
   row =list(int,input().split(" "))
   nums_arr.append(row)
vlist=[0*n]
   
res=0
def solution(lev,sum):
    if lev==n: 
         res=max(res,sum)
         
    else:
        for i in range(n):
            if not vlist[i]==1:
                solution(lev+1,sum* nums_arr[lev][i]/100)
                vlist[i]==0
   
solution(0,1000)
        
