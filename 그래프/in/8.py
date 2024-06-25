n,m=list(map(int,input().split(" ")))


def solution(x,temp_list):
    if len(temp_list)==m:
        print(' '.join(map(str,temp_list)))
        
    else:
        for i in range(x,m+1):
            solution(i+1,)
    
    
    

solution(0,[])