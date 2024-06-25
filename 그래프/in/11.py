n,m=map(int,input().split(" "))
nums=list(map(int,input().split(" ")))

k=int(input())

result=[]
res=[]
def solution(x):
    global result
    global res
    if len(result)==m:
        if sum(result)%k==0 :
            print(result)
            res.append(result)
        # print(" ".join(map(str,result)))
        return 
    
    for i in range(x,n):
        result.append(nums[i])
        solution(i+1)
        result.pop()

solution(0)

print(len(res))