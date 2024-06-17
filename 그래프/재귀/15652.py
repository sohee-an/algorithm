n,m=map(int,input().split(" "))


list =[]
result=[]
result_set=set()
def solution():
    if len(list)==m:
        sorted_tuple = tuple(sorted(list))  
        # if sorted_tuple not in result_set:
        #     result_set.add(sorted_tuple)
        result.append(list.copy())

        return 
    
    for i in range(1,n+1):
      
            list.append(i)
            solution()
            list.pop()
        

solution()


for i in result:
       print(' '.join(map(str, i)))

