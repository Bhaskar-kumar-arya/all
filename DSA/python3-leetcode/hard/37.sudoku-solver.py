#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        copy = []
        def is_valid (row,col) :
            # check row and col :
            curr_row = set()
            curr_col = set()
            for i in range(9) :
                if board[row][i] in curr_row or board[i][col] in curr_col :
                    return False
                if board[row][i] != "." :
                    curr_row.add(board[row][i])
                if board[i][col] != "." :
                    curr_col.add(board[i][col])  
            start_box_row = (row // 3)*3 
            start_box_col = (col // 3)*3
            curr_box = set()
            for i in range(3) :
                for j in range(3) :
                    if board[start_box_row + i][start_box_col + j] in curr_box : 
                        return False
                    if board[start_box_row + i][start_box_col + j] != "." :
                        curr_box.add(str(board[start_box_row + i][start_box_col + j]))
            return True        
        def calculatefilled () :
            filled = 0
            for i in range(9) :
                for j in range(9) :
                    if board[i][j] != "." :
                        filled += 1
            return filled            
        
        def backtrack(filled) :
            if filled == 81 : return True
            for i in range(9) : 
                for j in range(9) :
                    if board[i][j] == "." :
                        # print(f"\n filled : {filled} row,col : {i},{j} value : {board[i][j]} board :")
                        # for row in board :
                        #     print(row)    
                        for num in range(1,10) :
                            board[i][j] = str(num)
                            if is_valid(i,j) :
                                # print(f"found valid filled : {filled} added {num}")
                                if backtrack(filled + 1) :
                                    return True
                            # else :
                            #     print(f"found invalid board upon adding {num}")    
                            board[i][j] = "."      
            return False
        backtrack(calculatefilled())
        return board                

# @lc code=end
print(Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))

