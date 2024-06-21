n=int(input())


number_list =[1,5,10,50]
temp_list=[]
result_list=[]



def solution(start):
    if len(temp_list)==n :
        sum_number=sum(temp_list)
       
        if sum_number not in result_list:
            result_list.append(sum_number)
        return
    
    for i in range(start,len(number_list)):
        temp_list.append(number_list[i])
        solution(i)
        temp_list.pop()
        
        

solution(0)

print(len(result_list))

