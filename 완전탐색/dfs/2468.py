# 2-c 안전영역
n = int(input())
graph = []
tree=[]
maxNum = 0

dx = [0 ,0, 1, -1]
dy = [1, -1, 0 ,0]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j] 




result =0;


for i in range(maxNum):
    visited = [[0] * n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if graph[j][k]>i and visited[j][k]==0
            bfs(j,k,i,visited)
                
