n = int(input())
nums_list = list(map(int, input().split()))
x = int(input())

# 순서가 중요하지 않을때

# 배열을 정렬합니다.
nums_list.sort()

# 두 개의 포인터를 사용하여 문제를 해결합니다.
left = 0
right = n - 1
ans = 0

while left < right:
    current_sum = nums_list[left] + nums_list[right]
    if current_sum == x:
        ans += 1
        left += 1
        right -= 1
    elif current_sum < x:
        left += 1
    else:
        right -= 1

print(ans)
