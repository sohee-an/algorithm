n,m=map(int,input().split(" "))

list =[]
def solution():
    if len(list)==m:
        print(' '.join(map(str, list)))
        return
    
    for i in range(1,n+1):
        list.append(i)
        solution()
        list.pop()
        


solution()