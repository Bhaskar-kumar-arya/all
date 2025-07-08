#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0 : return [-1,-1]
        def find_first_element() :
            l = 0
            r = len(nums) - 1
            while l < r :
                m = (l+r)//2
                if nums[m] > target :
                    r = m - 1
                elif nums[m] < target :
                    l = m + 1
                else :
                    r = m
            return l
        def find_second_element (first_element_index) :
            l = first_element_index
            r = len(nums) 
            while l + 1 < r :
                m = (l+r)//2
                if nums[m] > target :
                    r = m 
                else :
                    l = m  
            return l          
        first_element_index = find_first_element() 
        if nums[first_element_index] != target : return [-1,-1]      
        return [first_element_index,find_second_element(first_element_index)]  
# @lc code=end

print(Solution().searchRange([10,10,10,10,10],10))