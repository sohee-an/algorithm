# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# n,m =map(int,input().split(" "))
list =[4,9,7,5,1]
result =0
count =0

while count <len(list):
    if list[count]+list[count+1]==14:
        result+=1
    count+=1

print(result)


