num_arr=list(map(int,input().split(" ")))


temp_arr=list(map(int,input().split(" ")))
big_res=0
small_res=2140000

def solution(lev,temp,total):
    
    
    if lev==len(num_arr):
        big_res=max(total,big_res)
        small_res=min(total,small_res)
        
    else:
        # 선택함
        if temp<0:

            solution(lev+1,temp_arr[lev]-1)
            
        solution(lev+1,temp)
        
    


solution(0)