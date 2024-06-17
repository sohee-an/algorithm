# 
N,M=map(int,input().split(" "))

visited=[0* N]

# 3부터 n개씩 숫자를 빼야된다.



result = []

def backtrack():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, N + 1):
        if i not in result:
            
            result.append(i)
            backtrack()
            
            result.pop()

backtrack()

