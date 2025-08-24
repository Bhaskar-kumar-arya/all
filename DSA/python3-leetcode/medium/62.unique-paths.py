#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for i in range(m)]
        dp[-1][-1] = 1
        for row in range(m-1,-1,-1) :
            for col in range(n-1,-1,-1) :   
                if col != 0 :
                    dp[row][col-1] += dp[row][col]
                if row != 0 :
                    dp[row-1][col] += dp[row][col]
        return dp[0][0]                 

            
            
            
        
        
# @lc code=end

print(Solution().uniquePaths(3,2))