# 1799
n,m =map(int,input().split(" "))

input_list=sorted(list(map(int,input().split(" "))))
list=[]
visited=[False * n]

def solution(start):
    if len(list)==m:
        print(*list)
        return 
    remember_me=0
    for i in range(start,n):
        if remember_me != input_list[i]:
            list.append(input_list[i])
            remember_me=input_list[i]
            solution(i+1)
            list.pop()
            

solution(0)