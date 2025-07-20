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
        def recurse (target,index) :
            if target < 0 : return
            elif target == 0 :
                res.append(path.copy()) 
                return
            for i in range(index,len(candidates)) :
                path.append(candidates[i]) 
                recurse(target - candidates[i],i)
                path.pop()
        recurse(target,0) 
        return res
# @lc code=end
print(Solution().combinationSum([2,3,6,7],7))
