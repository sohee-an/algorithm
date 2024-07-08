N, M = map(int, input().split())
nums_list = list(map(int, input().split()))

left = 0
current_sum = 0
cnt = 0

for right in range(N):
    current_sum += nums_list[right]
    # 현재 포인터를 더한다.오른쪽으로 탐색하면서 누적합 한다.
    # 
    while current_sum >= M:
        if current_sum == M:
            cnt += 1
        # 첫번째 왼쪽 값을 빼고 왼쪽포인트를 왼쪽으로 옯긴다.
        current_sum -= nums_list[left]
        left += 1

print(cnt)

# 이것도 있음!

N, M = map(int, input().split())
nums_list = list(map(int, input().split()))

left = 0
right = 0
current_sum = 0
cnt = 0

while right < N:
    current_sum += nums_list[right]
    right += 1

    while current_sum >= M:
        if current_sum == M:
            cnt += 1
        current_sum -= nums_list[left]
        left += 1

print(cnt)
