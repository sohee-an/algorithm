n,m=map(int,input().split(" "))

input_list=sorted(list(map(int,input().split(" "))))

list =[]
result_list=[]
def solution():
    if len(list)==m:
       
        
        result_list.append(' '.join(map(str, list)))
        # result_list.append(list.copy())
        return 
    
    for i in range(n):
        if input_list[i] not in list:
            list.append(input_list[i])
            solution()
            list.pop()


solution()

for i in result_list:
   print(i)