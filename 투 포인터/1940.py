n=int(input())
m=int(input())

nums_list=sorted(list(map(int,input().split(" "))))

left=0
right=n-1
ans=0

while left<right:
    current_sum=nums_list[left]+nums_list[right]
    if current_sum==m:
        ans+=1
        left+=1
        right+=1
    elif current_sum<m:
        left+=1
        
    elif current_sum>m:
        right-=1
        
print(ans)