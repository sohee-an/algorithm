n,m=int(input().split(" "))

res=0
def solution(lev,lst):
    global res
    if n==lev:
        res=max(res,int("".join(map(str,lst))))

    else:
        for i in range(n):
            for j in range(i+1,n):
                slution(lev+1,)
        
solution(0,[])