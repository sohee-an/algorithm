n= int(input())


result_list=[]
def solution():
    if len(result_list)==n:
        print(' '.join(map(str,result_list)))
        return 
    
    for i in range(1,n+1):
        if i not in result_list:
            result_list.append(i)
            solution()
            result_list.pop()
        

solution()