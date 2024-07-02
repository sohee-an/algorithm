n=int(input())

nums_arr=[]
for _ in range(n):
    row=list(int,input().split(" "))
    nums_arr.append(row)
   

def solution(lev,alist,blist):
    if lev==n:
        if len(alist)==len(blist):
            for i in range(n):
                for j in range(n):
                    asum+=alist[i][j]
        
    else:
        solution(lev+1,alist.append(lev),blist)
        solution(lev+1,alist,blist.append(lev))

solution(0,[],[])
    