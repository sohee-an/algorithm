n= int(input())


result_list=[]
def solution(start):
    if len(result_list)==n:
        print(' '.join(map(str,result_list)))
        return 
    
    for i in range(start,n+1):
        if i not in result_list:
            result_list.append(i)
            solution(i)
            result_list.pop()
        

solution(0)