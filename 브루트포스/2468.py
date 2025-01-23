n=int(input())
from collections import deque

dy=[-1,0,1,0]
dx=[0,1,0,-1]

nums_arr=[] 
max_value=0
for i in range(n):
    row=list(map(int,input().split(" ")))
    nums_arr.append(row)
    for value in row:
        if value > max_value:
            max_value = value
    
print(max_value)


def solution():
    q=deque()
    q.append(())
    

for i in range(2,max_value+1):
    for j in range()

solution()