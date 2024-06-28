n=int(input())
nums_list=list(map(int,input().split(" ")))
print(nums_list)
m=int(input())

res=2140000
def solution(lev,sum):
    global res
    if sum>m:
        return 
    if sum ==m:
        if lev<res:
            res=lev
    
    else:
        for i in range(n):
            solution(lev+1,sum+nums_list[i])
        
    


solution(0,0)
print(res)
