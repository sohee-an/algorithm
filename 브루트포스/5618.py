n =int(input())

input_list=list(map(int,input().split(" ")))

small_num=

    

k,l=input_list

result_list=[]

for i in range(1,min(k,l)+1):
    if k%i ==0 and l%i ==0:
        result_list.append(i)
    
    

for i in range(len(result_list)):
    print(result_list[i])