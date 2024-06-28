n=int(input())

nums_list=[]
t=list()
p=list()

for _ in range(n):
    a,b=list(map(int,input().split(" ")))
    t.append(a)
    p.append(b)
    
res=0   
def solution(day):
    if day>7:
        return
    
    solution(day+t[i])  
    solution(day+1) 


solution(0)