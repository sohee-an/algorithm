# 배당무게 

from collections import deque
n,k=map(int,input().split(" "))
print(n)

graph=[]

for _ in range(n):
    row=list(map(int,input().split()))
    graph.append(row)

print(graph)
    
    
def dfs(curr):
    
    arr=[]
    sum=0
    
    for next_pos in graph:
        print("net",next_pos)
        if next_pos != curr and sum==k:
            sum=graph[next][0]+graph[next_pos][0]
            arr.append(sum)
    return  arr
            
            
        

result=[]

for i in range(n):
    # result.append(dfs(i))
    print(dfs(i))
        
print(result)