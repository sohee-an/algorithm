N,M=map(int,input().split(" "))

result=[]
def solution( n,lst):
    if n>N:
        if len(lst)==M:
            result.append(lst)
        return 
    
    solution(n+1,lst+[n])
    solution(n+1,lst)
    # for i in range(x,n+1):
    #     result.append(i)
    #     solution(i+1)
    #     result.pop()
    

solution(1,[])
print(result)
for lst in result:
    print(*lst)