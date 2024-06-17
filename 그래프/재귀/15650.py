n,m =map(int,input().split(" "))


list=[]
result=[]
result_set=set()
def backtrack():
    if len(list) == m:
        
        sorted_tuple = tuple(sorted(list))  
        if sorted_tuple not in result_set:
            result_set.add(sorted_tuple)
            result.append(list.copy())

        return
    
    for i in range(1, n + 1):
        if i not in list:
            
            list.append(i)
            backtrack()
            
            list.pop()

backtrack()


for i in result:
       print(' '.join(map(str, i)))

