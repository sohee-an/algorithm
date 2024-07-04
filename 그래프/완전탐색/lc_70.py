class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
# 이게 위에서 내려가면서 만드는 트리

# 밑에 꺼는 밑에서 올라가면서 만드는 트리
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def solution(sum):
            if sum > n:
                return 0
            if sum == n:
                return 1
            if sum in memo:
                return memo[sum]
            
            memo[sum] = solution(sum + 1) + solution(sum + 2)
            return memo[sum]

        return solution(0)
