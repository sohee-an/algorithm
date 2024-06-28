# 최대점수 구하기
n,m=map(int,input().split(" "))

nums_list=[]
for _ in range(n):
    row=list(map(int,input().split(" ")))

res=0

def solution(lev,day,nums_sum):
    global res
    if lev==n:
            if res<nums_sum:
                res=nums_sum
                return
            
    else :
        solution(lev+1,day+nums_list[lev][0],sum+nums_sum[lev])
        solution(lev+1,day,sum)

solution(0,0,0)    
print(res)


