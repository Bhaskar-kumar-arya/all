#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        def recurse (index) :
            res.append(path.copy()) 
            if index == len(nums) : return 
            for i in range(index,len(nums)) :
                path.append(nums[i])
                recurse(i + 1)
                path.pop()

        recurse(0) 
        return res  
# @lc code=end

print(Solution().subsets([1,2,3]))