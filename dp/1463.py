import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)
# dp[1] = 0  # 생략 가능: 1을 1로 만드는 연산 횟수는 0

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])
