#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0 
        r = len(height) - 1
        m = 0
        while l < r :
            if height[l] >= height[r] :
                m = max(height[r]*(r-l),m)
                r -= 1
            else : 
                m = max(height[l]*(r-l),m)
                l += 1
        return m            
# @lc code=end


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))