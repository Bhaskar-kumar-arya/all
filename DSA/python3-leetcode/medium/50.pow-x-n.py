#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 : return 1
        if n < 0 :
            x = 1/x
            n = -n
        if n % 2 == 0 :
            return self.myPow(x*x,n/2)
        return x*self.myPow(x*x,n//2)
        

# @lc code=end

print(Solution().myPow(0.00001,2147483647))