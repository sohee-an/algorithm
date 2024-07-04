n=int(input())
from collections import deque

scv_arr=list(map(int,input().split(" ")))

temp_arr=[
    [9,3,1],
    [9,1,3],
    [3,9,1],
    [3,1,9],
    [1,9,3],
    [1,3,9]
]


res=0
def solution():
    global res
    q=deque()
    scv1,scv2,scv3=scv_arr[0]
    q.append(scv1,scv2,scv3)
    
    
    while q:
        
        c_scv1,c_scv2,c_scv3=q.popleft()
        for i in range(temp_arr):
            ncv1,=c_scv1 - temp_arr[i][0]
            ncv2=c_scv2 - temp_arr[i][1]
            ncv3=c_scv3 - temp_arr[i][2]
            if ncv1 <0 and ncv2<0 and ncv3<0:
                break;
            if  ncv1 <0 and ncv2<0 and ncv3<0:
                return res
            else: 
                q.append(ncv1,ncv2,ncv3)
        
    
    
solution()