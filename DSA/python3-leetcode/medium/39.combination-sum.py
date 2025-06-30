#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []
        candidates.sort()
        def helper(target,index) :
            if target == 0 : 
                res.append(path.copy())
                return
            for i in range(index,len(candidates)) :
                if target < candidates[i] : break
                path.append(candidates[i])
                helper(target - candidates[i],i)    
                path.pop()
        helper(target,0)      
        return res  

        
# @lc code=end
print(Solution().combinationSum([2,3,5],8))
