#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        ans = 0
        for row in range(len(matrix)) :
            for col in range(len(matrix[0])) :
                if matrix[row][col] == "0" : 
                    continue
                CanContinue = True
                c = col
                r = row
                while CanContinue :
                    c += 1
                    r += 1
                    if (r >= len(matrix) or c >= len(matrix[0])) : 
                        break
                    for i in range(r - row + 1) : 
                        if matrix[r][col+i] == "0" or matrix[row+i][c] == "0" :
                            CanContinue = False
                            break    
                ans = max(ans,(c - col)**2 )

        return ans

                
# @lc code=end

print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))