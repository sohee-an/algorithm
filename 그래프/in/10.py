n,m=map(int,input().split())


result=[]
def solution(x):
    if len(result)==m:
        print(' '.join(map(str,result)))
        return 
    else :
        for i in range(x,n+1):
           
                result.append(i)
                solution(i+1)
                result.pop()
    


# solution(1)
n, m = map(int, input().split())

result = []
# def solution(x):
#     if len(result) == m:
#         print(' '.join(map(str, result)))
#         return 
#     else:
#         for i in range(x, n + 1):
#             result.append(i)
#             solution(i + 1)
#             result.pop()

# solution(1)
