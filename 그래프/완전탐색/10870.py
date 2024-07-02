n=int(input())

res=0
def solution(cur,sum):
    global res
    if cur==n-1:
        res=sum
        return 
    else:
        solution(cur,cur+cur+1)

solution(0,0)
print(res)