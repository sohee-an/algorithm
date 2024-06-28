n=int(input())

k,m=map(int,input().split(" "))

nums_list=list(map(int,input().split(' ')))


result=214000
def solution(lev,total):
    global result
    if lev==k:
        res=abs(m-total)
        if result>res:
            result=res
    else:
        
        solution(lev+1,total+nums_list[lev])
        
        solution(lev+1,total)
        
    
    
    
solution(0,0)

print(result)