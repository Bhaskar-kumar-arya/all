#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)) :
            min_index = i
            for j in range(i + 1 , len(nums)) :
                if nums[min_index] > nums[j] :
                    min_index = j
                elif nums[min_index] == nums[j] : return True    
            nums[i],nums[min_index] = nums[min_index],nums[i]   
        return False        

        
# @lc code=end

