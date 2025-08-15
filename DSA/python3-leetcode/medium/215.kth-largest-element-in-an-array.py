#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        for i in range(0,k) :
            m = i
            for j in range(i+1,len(nums)) :
                if nums[j] > nums[m] : 
                    m = j
            nums[i],nums[m] = nums[m],nums[i]        
        return nums[k-1]
            
        
# @lc code=end

print(Solution().findKthLargest([3,2,1,5,6,4],3))