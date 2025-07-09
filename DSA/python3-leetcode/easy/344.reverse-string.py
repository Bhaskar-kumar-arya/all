#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2) :
            s[i],s[-i-1] = s[-i-1],s[i]
        return s    
# @lc code=end

print(Solution().reverseString(['a','r','g','s']))