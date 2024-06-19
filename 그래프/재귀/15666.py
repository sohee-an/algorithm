n,m=map(int,input().split(" "))

input_list=sorted(list(map(int,input().split(" "))))

list=[]
def solution(start):
    if len(list)==m:
        print(*list)
        return 
    remember_no=0
    
    for i in range(start,n):
        if remember_no!=input_list[i]:
            list.append(input_list[i])
            remember_no=input_list[i]
            solution(i)
            list.pop()
          
           
            
        
        

solution(0)