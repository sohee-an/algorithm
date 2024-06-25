n=int(input())

# 동전 종류별로 값
nums_list=list(map(int,input().split(" ")))

nums_list.sort(reverse=True)
print(nums_list)
# 타겟 
m=int(input())
sum=0
res=2170000

def solution(x,sum):
    global res
 
    if sum>m:
        return 
    if sum==m:
        if x<res:
            res=x
    else:
        for i in range(n):
            print(nums_list[i])
            solution(x+1,sum+nums_list[i])
            print("끝나고 ")
           
          

        
   
    

solution(0,sum)
