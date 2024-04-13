#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
    # dptable 优化迭代
        if n ==0:
            return 0
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
    
    
    # 备忘录优化递归
    #     memo = [0]*(n+1)
    #     return dp(n, memo)
    
    # def dp(self, n, memo):
    #     if n<2:
    #         return n        
    #     if memo[n]!=0:
    #         return memo[n]
    #     memo[n] = self.dp(n-1, memo) + self.dp(n-2, memo)
    #     return memo[n]
        
        # if n<2:
        #     return n
        # return self.fib(n-1)+self.fib(n-2)
        
# @lc code=end

