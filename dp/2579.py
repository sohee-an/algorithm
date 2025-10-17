# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 
# 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.
import sys
input = sys.stdin.readline

n = int(input())
stair = [0] + [int(input()) for _ in range(n)] 

if n == 1:
    print(stair[1])
    exit()

dp = [0] * (n + 1)
dp[1] = stair[1]
# dp[2] = stair[1] + stair[2]
dp[2] = max(stair[1] + stair[2], stair[2])

for i in range(3, n + 1):
    dp[i] = max(dp[i-2] + stair[i], 
                dp[i-3] + stair[i-1] + stair[i])

print(dp[n])
