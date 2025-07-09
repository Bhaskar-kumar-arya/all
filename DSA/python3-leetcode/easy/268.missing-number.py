#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        product_nums = 0 
        product_range = 0
        for i in range(len(nums)) :
            product_nums ^= nums[i]
            product_range ^= i + 1
        return product_nums ^ product_range
# @lc code=end

print(Solution().missingNumber([0,1,2,4]))  