#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)) :
            first = nums[i] 
            if i > 0 and first == nums[i-1] :
                continue
            # two sum
            l = i + 1
            r = len(nums) - 1
            while l < r :
                if l > i + 1 and nums[l-1] == nums[l] :
                    l += 1 
                    continue
                _sum = nums[l] + nums[r] + first
                if _sum == 0 : 
                    res.append([first,nums[l],nums[r]])
                    l += 1
                    r -= 1
                elif _sum > 0 : 
                    r -= 1
                else :
                    l += 1   
                     
        return res 
           
            

# @lc code=end

print(Solution().threeSum([-1,0,1,2,-1,-4]))