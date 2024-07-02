n=int(input())
number=int(input())

nums_arr=[]
for _ in range(n):
    row=list(map(int,input().split(" ")))
    nums_arr.append(nums_arr)
    
visited=[0 * n]  
res=2140000  
# def solution(lev,total):
#     if lev==n:
#         if res>total:
#             res=total
            
#     else:
#         for i in range(n):
          
#                     visited[i]=1
#                     solution(lev+1,nums_arr[lev][])
            
def solution(lev,total):
    global res
    if lev==n:
          res=min(res,total)   
    else:
        for i in range(n):
            if visited[i]==0:
                visited[i]=1
                solution(lev+i,total+nums_arr[lev][i])  
                visited[i]=0


solution(0)