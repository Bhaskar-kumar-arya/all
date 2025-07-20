#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []
        candidates.sort()
        def recurse (target,index) :
            if target == 0 :
                res.append(path.copy()) 
                return
            for i in range(index,len(candidates)) :
                if i > index and candidates[i] == candidates[i-1] : continue
                if target < candidates[i] : break
                path.append(candidates[i]) 
                recurse(target - candidates[i],i + 1)
                path.pop()
        recurse(target,0) 
        return res
        
# @lc code=end

print(Solution().combinationSum2([10,1,2,7,6,1,5],8)) # 1,1,2,5,6,7,10