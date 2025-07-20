#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                # Skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res
        
# @lc code=end
print(Solution().permuteUnique([1,1,2,2,3,3,4]))
