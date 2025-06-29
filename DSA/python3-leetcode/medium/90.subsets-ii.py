#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        sol = []
        nums.sort()
        def backtrack(index) :
            res.append(sol.copy()) 
            for i in range(index,len(nums)) :
                if i > index and nums[i] == nums[i-1] : continue
                sol.append(nums[i])
                backtrack(i+1)
                sol.pop()
        backtrack(0)        
        return res        


# @lc code=end 
print(Solution().subsetsWithDup([1,2,2,3]))
    