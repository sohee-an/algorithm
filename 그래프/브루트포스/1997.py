# 입력 받기
m = int(input())
n = int(input())

# 완전제곱수 리스트 초기화
perfect_squares = []

# 범위 내의 모든 수에 대해 완전제곱수인지 확인
for i in range(m, n + 1):
    # 제곱근을 구한 뒤 정수인지 확인
    root = int(i ** 0.5)
    if root * root == i:
        perfect_squares.append(i)

# 완전제곱수가 있는 경우
if perfect_squares:
    print(sum(perfect_squares))
    print(min(perfect_squares))
else:
    print(-1)
