n, m = map(int, input("").split(" "))

input_list = []
for _ in range(n):
    input_list.append(input())

result = 0

for i in range(n):
    for j in range(m):
        # 시작점이 'W'인 경우와 'B'인 경우를 각각 계산
        if input_list[i][j] == 'W':
            # (i+j)가 짝수일 때 'W'가 나와야 함
            if (i + j) % 2 == 1:
                result += 1
        else:
           
            if (i + j) % 2 == 0:
                result += 1

print(result)
