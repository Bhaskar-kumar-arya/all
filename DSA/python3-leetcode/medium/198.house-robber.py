#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        a,b = 0,0
        for i in range(len(nums)) :
            a,b = max(a,b) , a + nums[i]
        return max(a,b)    
# @lc code=end

print(Solution().rob([2,7,9,3,1]))