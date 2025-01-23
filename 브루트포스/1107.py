n=int(input())

m=int(input())
print(n)



button_list=list(map(int,input().split(" ")))

result=21470000
def solution(sum):
    global result
    if len(sum)==len(str(n)):
        # print("hi",sum)
        temp=abs(n-int(sum))
        # print(temp)
        if result>temp:
            result=temp
            return
        else:
            return

    for i in range(m):
        
        solution(sum+str(button_list[i]))
    


solution("")
print(result)