# n=int(input())
# # 글자 수
# k=int(input())

# input_list=[]

# for _ in range(n):
#     row=int(input())
#     input_list.append(row)
    
# print(input_list)

# result=0
# result_list=[]
# list=[]
# def solution():
#     if len(list)==k:
        
#         return 
    
#     for i in range(n):
        


# solution()

def dfs(x):
    if x==0:
        return
    print(x)
    dfs(x-1)
    
n=int(input())
input_list=list(map(int,input().split()))
    
    
dfs(5)