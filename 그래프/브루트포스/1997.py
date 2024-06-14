# 입력 받기
m = int(input())
n = int(input())


perfect_squares = []


for i in range(m, n + 1):
    
    root = int(i ** 0.5)
    if root * root == i:
        perfect_squares.append(i)


if perfect_squares:
    print(sum(perfect_squares))
    print(min(perfect_squares))
else:
    print(-1)
