#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res =[]
        path = []
        used = [False]*len(nums)
        nums.sort()
        def backtrack () :
            if len(path) == len(nums) : 
                res.append(path.copy())
                return
            for i in range(len(nums)) :
                if used[i] : 
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1] : continue
                path.append(nums[i]) 
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False
        backtrack()
        return res
        
# @lc code=end
print(Solution().permuteUnique([2,2,2,3]))
