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
        rows : list[set] = [set() for i in range(9)]
        cols : list[set] = [set() for i in range(9)]
        Boxes : list[list[set]] = [[set() for i in range(3)] for i in range(3)]
        availableCandidates = []
        filled = 0
        for i in range(9) :
            for j in range(9) :
                if board[i][j] != "." :
                    filled += 1
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    Boxes[(i//3)][(j//3)].add(board[i][j])  
                else :
                    availableCandidates.append((i,j))        
        def is_valid (row,col) :
            if board[row][col] in rows[row] or board[row][col] in cols[col] : return False
            if board[row][col] in Boxes[row//3][col//3] : return False
            return True                 
        
        def backtrack(filled) :
            if filled == 81 : return True
            while availableCandidates :
                    i,j = availableCandidates[-1]
                    if board[i][j] == "." :   
                        for num in range(1,10) :
                            board[i][j] = str(num)
                            if is_valid(i,j) :
                                rows[i].add(board[i][j])
                                cols[j].add(board[i][j])
                                Boxes[(i//3)][j//3].add(board[i][j])
                                availableCandidates.pop()
                                if backtrack(filled + 1) :
                                    return True
                                rows[i].remove(board[i][j])
                                cols[j].remove(board[i][j])
                                Boxes[(i//3)][j//3].remove(board[i][j])    
                                availableCandidates.append((i,j)) 
                            board[i][j] = "."  
            return False
        backtrack(filled)
        return board

# @lc code=end
easyBoard = [["5", "3", ".", "6", "7", "8", "9", "1", "2"],
    ["6", ".", "2", "1", "9", "5", "3", "4", "8"],
    ["1", "9", "8", "3", "4", "2", "5", "6", "."],
    ["8", "5", "9", "7", "6", "1", ".", "2", "3"],
    ["4", "2", "6", "8", ".", "3", "7", "9", "1"],
    ["7", ".", "3", "9", "2", "4", "8", "5", "6"],
    ["9", "6", ".", "5", "3", "7", "2", "8", "4"],
    ["2", "8", "7", ".", "1", "9", "6", ".", "5"],
    [".", "4", "5", "2", "8", "6", "1", "7", "9"]]

difficultBoard = [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
print(Solution().solveSudoku(easyBoard))

