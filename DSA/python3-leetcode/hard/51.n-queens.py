#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from collections import Counter
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        path = [None]*n

        def valid(row,col) :
            def checkDiags() :
                i,j = row - min(row,col) , col - min(row,col)
                while max(i,j) < n :
                    print(row,col,i,j)
                    if i != row and j != col :
                        if path[i] == j :
                            return False
                    i += 1 
                    j += 1  
                i,j = row + min(n - row - 1 , col)  , col - min(n - row - 1 , col)
                while max(i,j) < n :
                    print(row,col,i,j)
                    if i != row and j != col :
                        if path[i] == j :
                            return False
                    i -= 1 
                    j += 1 
                print(f"foubd valid diag set : {path}")    
                return True    
            return path.count(col) < 2  and checkDiags()

        def backtrack (row) :
            print(f"row : {row}")
            if row == n :
                sol = []
                for col in path :
                    sol.append("."*col + "Q" + "."*(n - col - 1))
                res.append(sol)    

                return
            for col in range(n) :
                path[row] = col
                if valid(row,col) :
                    backtrack(row + 1)
                else :
                    print(f"invalid path : {path}")    
                path[row] = None    
 
        backtrack(0)
        return res
# @lc code=end
for path in Solution().solveNQueens(4) :
    print(path)