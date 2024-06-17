n,m=map(int,input().split(" "))

input_list=sorted(list(map(int,input().split(" "))))


list=[]
result=[]
def solution(start):
    if len(list)==m:
         print(' '.join(map(str,list)))
        # print(*list)
    
    for i in range(start,n):
        if input_list[i] not in list:
            list.append(input_list[i])
            solution(i+1)
            list.pop()


solution(0)