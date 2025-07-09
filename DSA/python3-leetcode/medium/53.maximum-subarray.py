#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = 0
        max_sum = nums[0]
        for r in range(len(nums)) :
            curr_sum += nums[r]   
            max_sum = max(max_sum,curr_sum)
            if curr_sum < 0 :
                curr_sum = 0 
        return max_sum        

# @lc code=end
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
