
# s=["h","e","l","l"]
# result=[]
# def solution(x):
#     if x>=len(s):
#         return 
#     solution(x+1)
 
#     result.append(s[x])
#     # print(s[x])
    
    
# solution(0)


c,n=map(int,input().split())

dog_list=[]
for i in range(n):
    dog_list.append(int(input()))
    
result=-1000000
    
def solution2(x,sum):
    if sum<=259:
        return
    if x==5 :
        return 
    if result<sum:
        result=sum
    
    for i in range(n):
        solution2(i+1,sum+dog_list[i])
        solution2(i+1,sum)
    
    
    

solution2(0,0)
# 259 5
# 81
# 58
# 42
# 33
# 61