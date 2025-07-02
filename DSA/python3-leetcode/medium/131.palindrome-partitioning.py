#
# @lc app=leetcode id=131 lang=python3
#
# [131] palindrome-partitioning
#

# @lc code=start
class Solution:   
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []
        def backtrack (index) :
           #print(path)
            if index == len(s) : res.append(path.copy())
            for i in range(index,len(s)) :
                #print(i,s[index:i + 1],s[index:i + 1][::-1],path)
                palindrome = True
                print(f"index : {index} i : {i}" )
                for j in range((i - index + 1)//2) :
                    if s[index + j ] != s[i-j] : 
                        palindrome = False
                #     print(f"index : {index} i : {i} j : {j} palindrome : {palindrome}" )
                # print(f"palindrome : {palindrome} , func : {self.isPalindrome(s[index:i + 1])}")    
                if palindrome : 
                    path.append(s[index:i + 1])
                    backtrack(i+1)
                    path.pop()
        backtrack(0)       
        return res       
# @lc code=end 
print(Solution().partition("aab"))

    