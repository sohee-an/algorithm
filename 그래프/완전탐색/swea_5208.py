park_arr=list(map(int,input().split(" ")))


res=2140000
cnt_number=2140000
def solution(lev,cnt,sm):
    global res
    if  lev==len(park_arr):
        res=min(res,cnt)
    else:
        solution(lev+1,cnt+1,park_arr[lev]-1)
        if sm>0:
         solution(lev+1,cnt,park_arr[lev]-1)

solution(1,0,0)

print(res)
