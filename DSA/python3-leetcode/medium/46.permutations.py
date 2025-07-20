#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res =[]
        def recurse (index) :
            if index == len(nums) :
                res.append(nums.copy())
                return

            for i in range(index,len(nums)) :
                nums[index],nums[i] = nums[i],nums[index]
                recurse(index + 1)
                nums[i],nums[index] = nums[index],nums[i]
        recurse(0)
        return res
# @lc code=end

print(Solution().permute([1,2,3]))
