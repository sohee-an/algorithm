# 
N,M=map(int,input().split(" "))

visited=[0* N]

# 3부터 n개씩 숫자를 빼야된다.



result = []
list=[]
def solution():
    if len(list)==M:
        print(' '.join(map(str,list)))
        return 
    
    
    for i in range(1,N+1):
        if i not in list:
            list.append(i) 
            solution()
            list.pop()
    

solution()

# arr = [0] * 10
# isused = [False] * 10

# def func(k):
#     if k == m:
#         print(' '.join(map(str, arr[:m])))
#         return

#     for i in range(1, n + 1):
#         if not isused[i]:
#             arr[k] = i
#             isused[i] = True
#             func(k + 1)
#             isused[i] = False

# func(0)

# def backtrack():
#     if len(result) == M:
#         print(' '.join(map(str, result)))
#         return
    
#     for i in range(1, N + 1):
#         if i not in result:
            
#             result.append(i)
#             backtrack()
            
#             result.pop()

# backtrack()

