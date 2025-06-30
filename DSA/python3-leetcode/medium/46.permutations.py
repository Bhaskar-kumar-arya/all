#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res =[]
        path = []
        used = [False]*len(nums)
        def backtrack () :
            if len(path) == len(nums) : 
                res.append(path.copy())
                return
            for i in range(len(nums)) :
                if used[i] : 
                    continue
                path.append(nums[i]) 
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False
        backtrack()
        return res        
        
# @lc code=end

print(Solution().permute([1,2,3]))
