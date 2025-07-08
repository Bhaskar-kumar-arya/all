#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
from collections import Counter
# @lc code=start
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        bit = 0
        for num in nums :
            bit ^=  num
        return bit    
# @lc code=end

print(Solution().singleNumber([2,2,1,1,5]))