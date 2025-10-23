n,m=map(int(input().split()))
arr=list(map(int,input().split()))

for i in range(m):
    i,j=map(int,input().split())
    sum=0
    for j in range(i+1,j+1):
        sum+=j
    print(sum)