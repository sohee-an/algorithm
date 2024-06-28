t=int(input())
k=int(input())

t_type=[]
tk=[]

for i in range(k):
    a,b=list(map(int,input().split(" ")))
    t_type.append(a)
    tk.append(b)
    
res=21400000
cnt=0
def solution(lev,total):
    global cnt
    if total>t:
        return 
    if total==t:
       cnt+=1
    
    for i in range(k):    
        solution(lev+1,total+(t_type[i]*i))
    
    

solution(0,0)
print(cnt)