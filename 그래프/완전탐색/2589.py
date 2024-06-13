
from collections import deque
# 세로 가로
n,m=map(int,input().split(" "))

dy=[-1,0,1,0]
dx=[0,1,0,-1]

visited=[[0]*m for _ in range(n)]

graph=[]

for _ in range(n):
    row= list(input())
    graph.append(row)
    
print(graph)