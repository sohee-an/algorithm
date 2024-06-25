n=int(input())

nums=[]

for _ in range(n):
    row =list(map(int,input().split(" ")))
    nums.append(row)


print(nums)


res=0

# def solution(sum_day,sum):
#     global res
#     if sum_day>7:
#         return 
    
#     if res<sum:
#         res=sum
    
#     for i in range(sum_day,len(nums)):
#         solution(sum_day+nums[i][0],sum+nums[i][1])
#         solution(sum_day+1,nums[i+1][1])
        

# solution(0,0)
# print(res)

def solution():


solution(l,0)