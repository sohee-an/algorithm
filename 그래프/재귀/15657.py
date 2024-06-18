n,m=map(int,input().split(" "))

input_list=sorted(list(map(int,input().split(" "))))


list=[]


def solution(start):
    if len(list)==m:
        print(' '.join(map(str,list)))
        return 
    
    for i in range(start,n):
        list.append(input_list[i])
        solution(i)
        list.pop()
        
        


solution(0)

