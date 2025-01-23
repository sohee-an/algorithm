
n,m=map(int,input().split(" "))

list=list(map(int,input().split()))


 
    
def solution(cards,n,m):
    max_sum=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                current_sum=cards[i]+cards[j]+cards[k]
                if current_sum<=m:
                    max_sum=max(max_sum,current_sum)
    return max_sum


print(solution(list,n,m))
                
        
        