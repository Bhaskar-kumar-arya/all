#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1 : return n
        first,second = 1,2
        for _ in range(3,n+1) :
            first,second = second,first + second
        return second    

        
# @lc code=end

print(Solution().climbStairs(30))