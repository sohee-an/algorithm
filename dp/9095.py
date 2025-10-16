t = int(input())
for _ in range(t):
    n = int(input())
    
    def solution(sum_num):
        if sum_num == n:
            return 1
        if sum_num > n:
            return 0
        count = 0
        for i in range(1, 4):
            count += solution(sum_num + i)
        return count

    print(solution(0))
