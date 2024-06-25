n, m = map(int, input().split(" "))

nums_list = list(map(int, input().split(" ")))

res = 0

def solution(x, sum):
    global res
    if x == n:
        if sum == m:
            res += 1
        return
    
    # 현재 인덱스의 값을 포함하는 경우
    solution(x + 1, sum + nums_list[x])
    
    # 현재 인덱스의 값을 포함하지 않는 경우
    solution(x + 1, sum)

solution(0, 0)

# m이 0인 경우, 공집합 제외
if m == 0:
    res -= 1

print(res)
