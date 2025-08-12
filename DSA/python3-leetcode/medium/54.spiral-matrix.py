#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        c = len(matrix[0])
        r = len(matrix) - 1
        result = []
        def traverseRow(row,col,dir) :
            nonlocal c
            if c == 0 : return
            for i in range(c) :
                result.append(matrix[row][col + i*dir])
            c -= 1    
            traverseCol(row+dir,col + c*dir,dir)    

        def traverseCol(row,col,dir)  :
            nonlocal r
            if r == 0 : return
            for i in range(r) :
                result.append(matrix[row + i*dir][col])
            r -= 1
            traverseRow(row + dir*r,col - dir , -dir)    
        traverseRow(0,0,1)
        return result        

        
# @lc code=end

print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))