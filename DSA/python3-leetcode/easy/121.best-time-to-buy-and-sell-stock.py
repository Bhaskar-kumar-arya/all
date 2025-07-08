#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price_index = 0
        for i in range(1,len(prices)) :
            if prices[min_price_index] < prices[i] :
                max_profit = max(max_profit,prices[i] - prices[min_price_index])
            else :
                min_price_index = i
        return max_profit            
        
# @lc code=end
print(Solution().maxProfit([3, 2, 6, 1, 4]))
