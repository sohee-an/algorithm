N=int(input())
F=int(input())

result_list=[]

# 이걸 다시 보자
N //= 100
N *= 100



for i in range(100):
    if (N + i) % F == 0:
        print(f"{i:02}") 
        break


