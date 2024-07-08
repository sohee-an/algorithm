N, M = map(int, input().split())
nums_list = list(map(int, input().split()))

# 초기 윈도우의 합 계산
current_sum = sum(nums_list[:M])
max_sum = current_sum
ans=0
left=0
right=M-1

for i in range(M,N):
    # 왼쪽꺼는 빼고 오른쪽 포인트는 더하고
    current_sum=current_sum+nums_list[i]-nums_list[i-M]
    ans=max(ans,current_sum)