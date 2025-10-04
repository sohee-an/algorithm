# n.m 문제 10

n,m=map(int,input().split())
arr =list(map(int,input().split()))

arr.sort()

# 1799 /17 19 79 99

path=[]
def dfs(start,depth):
    if m==depth:
        print(*path)
        return
    prev=0
    for i in range(start,n):
        if prev!=arr[i]:
            prev=arr[i]
            path.append(arr[i])
            dfs(i+1,depth+1)
            path.pop()

dfs(0,0)