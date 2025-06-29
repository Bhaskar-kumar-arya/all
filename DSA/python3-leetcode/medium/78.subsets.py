#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        sol = []
        def backtrack (index):
            if index == len(nums) :
                res.append(sol.copy())
                return
            backtrack(index + 1)
            sol.append(nums[index]) 
            backtrack(index+1)
            sol.pop()
        backtrack(0)
        return res        
            
# @lc code=end

print(Solution().subsets([1,2,3]))