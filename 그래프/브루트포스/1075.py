N=int(input())
F=int(input())

result_list=[]

N //= 100
N *= 100



for i in range(100):
    if (N + i) % F == 0:
        print(f"{i:02}") 
        break


