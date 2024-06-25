n=int(input())

nums_list=list(map(int,input().split(" ")))

nums_sum=sum(nums_list)

def solution(level,sum):
    if level==n:
        if sum ==(nums_sum-sum):
            return True
        return True 
    else:
        solution(level+1,sum+nums_list[level])
        
        solution(level+1,sum)
    
    return False
    
if solution(0,0):
    print('True')
else:
    print('false')

