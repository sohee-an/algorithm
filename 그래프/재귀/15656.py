
n,m=map(int,input().split(" "))

input_list=sorted(list(map(int,input().split(" "))))

temp_list=[]

def solution():
    if len(temp_list)==m:
        print(" ".join(map(str,temp_list)))
        return 
    
    
    for i in range(n):
        # if input_list[i] not in temp_list:
            temp_list.append(input_list[i])
            solution()
            temp_list.pop()

solution()