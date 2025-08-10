#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)) :
            for col in range(len(matrix[0])) :
                if matrix[row][col] == 0 :
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(len(matrix)) :
            if matrix[row][0] == 0 :
                matrix[row] = [0]*len(matrix[row])

        for col in range(len(matrix[0])) :
            if matrix[0][col] == 0 :
                for row in range(len(matrix)) :
                    matrix[row][col] = 0
        
        return matrix        
        
    # @lc code=end
 
print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))