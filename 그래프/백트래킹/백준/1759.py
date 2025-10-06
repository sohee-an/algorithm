l,c=map(int,input().split())
arr = input().split()
arr.sort()

path=[]
모음배열= ["a","e","i","o","u"]
모음체크=0
자음체크=0


def dfs(start,depth,모음체크,자음체크):
    if l==depth and 모음체크>=1 and 자음체크>=2:
        print("".join(path))
        return
    for i in range(start,c):
        path.append(arr[i])
        if arr[i] in 모음배열:
            
            dfs(i+1,depth+1,모음체크+1,자음체크) 
        else:
             
             dfs(i+1,depth+1,모음체크,자음체크+1) 
        
        # dfs(i+1,depth+1)
        path.pop()

dfs(0, 0, 0, 0)