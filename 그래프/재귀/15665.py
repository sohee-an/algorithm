n,m=map(int,input().split(" "))

input_list=sorted(list(map(int,input().split(" "))))
list =[]

def solution():
    if len(list)==m:
        print(*list)
        return 
    
    remeber_no=0
    for i in range(n):
        if remeber_no != input_list[i]:
            list.append(input_list[i])
            remeber_no=input_list[i]
            solution()
            list.pop()


solution()