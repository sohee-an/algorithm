import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n + 1)
path = []
result = []

def backtrack():
    if len(path)==m:
        result.append(' '.join(map(str,path)) )
        return

    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i]=True
        path.append(i)
        
        backtrack()
        visited[i]=False
        path.pop()

backtrack()
print('\n'.join(result))