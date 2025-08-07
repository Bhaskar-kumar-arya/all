#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1 : return nums[0]
        if len(nums) == 2 : return max(nums[0],nums[1])

        return max(nums[0] + self.rob(nums[2:]),nums[1] + self.rob(nums[3:]) if len(nums) > 3 else nums[1])
        
# @lc code=end

