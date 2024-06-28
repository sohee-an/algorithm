n,m=map(int,input().split(" "))

nums_list=list(map(int,input().split(" ")))

res=2174000
def solution(lev,sum):
    global res
    if sum>n:
        return 
    if lev<4:
        
        if sum<=n:
            if res>sum:
                res=sum
            return 
    
    solution(lev+1,sum+nums_list[lev])
    solution(lev+1,sum)
    
solution(0,0)
print(res)