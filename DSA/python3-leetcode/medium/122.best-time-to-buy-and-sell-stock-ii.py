#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(1,len(prices)) :
            if prices[i] > prices[i-1] : profit += prices[i] - prices[i-1]
        return profit    




# @lc code=end

print(Solution().maxProfit(prices=[1,2,3,4,25]))