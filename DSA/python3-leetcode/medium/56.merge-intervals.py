#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
        
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals,key=lambda x : x[0])
        result = [intervals[0]]
        for interval in intervals :
            if result[-1][1] < interval[0] :
                result.append(interval)
            else :
                result[-1][1] = max(result[-1][1],interval[1])     
        return result        



        
# @lc code=end

print(Solution().merge(
   [[1,3],[2,6],[8,10],[15,18]]
    ))
    # [[2,3],[4,5],[6,7],[8,9],[1,10]]