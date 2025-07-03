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
        occupiedCols = set()
        positivediags = set()
        negativediags = set() 
        state= [["."] * n for _ in range(n)] # start with empty board
        def backtrack (row) :
            # print(f"row : {row}")
            if row == n :
                res.append(["".join(row) for row in state])    
                return
            for col in range(n) :
                path[row] = col
                if col not in occupiedCols and (row + col) not in positivediags and (row - col) not in negativediags :
                    occupiedCols.add(col)
                    positivediags.add(row + col)
                    negativediags.add(row - col)
                    state[row][col]='Q'
                    backtrack(row + 1)
                    positivediags.remove(row + col)
                    negativediags.remove(row - col)
                    occupiedCols.remove(col)
                    state[row][col]='.'
                # else :
                #     print(f"invalid path : {path}")    
                path[row] = None    
 
        backtrack(0)
        return res
# @lc code=end
for path in Solution().solveNQueens(4) :
    print(path)