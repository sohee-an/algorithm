n=int(input())
n_arr=list(map(int,input().split()))
m=int(input())
m_arr=list(map(int,input().split()))

n_arr.sort()


def bineary_search(arr,target):
    start=0
    end=len(arr)
    
    
    while start<end:
        mid=(start+end)//2
        
        if (arr[mid]==target):
            return 1
        elif (arr[mid]<target):
            start =mid+1
        else:
            end=mid
            
    return 0
    

result=[]
for i in m_arr:
    result.append(bineary_search(n_arr,i))

print(*result)