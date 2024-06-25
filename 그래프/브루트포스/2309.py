
nums_list=[]
for _ in range(9):
    row=int(input())
    nums_list.append(row)
    



def solution(lev,temp_list):
    if lev==9:
        if len(temp_list)==7 and sum(temp_list)==100:
            for num in sorted(temp_list):
                print(num)  
            return 
        return 
        
    else:
        solution(lev + 1, temp_list + [nums_list[lev]])
        solution(lev+1,temp_list)
            

solution(0,[])