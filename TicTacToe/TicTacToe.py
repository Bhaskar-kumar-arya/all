# @tag:TicTacTie
import copy
Board = [
    [" " , " " , " "] , 
    [" " , " " , " "],
    [" " , " " , " "]
]

def drawBoard (Board : list[list[str]]) :
    for row in range(len(Board)) :
        string = ""
        for column in range(len(Board[row])) :
            string += Board[row][column] + " | "
        print(string)    
        print("------------")
            

def move (row,column,isFirstPlayer) :
   if Board[row][column] != " " :
       print("already occupied")
       return
   Board[row][column] = "0" if isFirstPlayer else "1"
    

# go through rows, cols, and diags 
# if values for one of them are same and not equal to " " , return true 
# else, return false , if none of  these match        
def evaluateWinner (Board : list[list[str]]) :   
    # row 
    for r in range(len(Board)) :
        prev : str = None
        for c in range(len(Board[r]) ) :
            print(f" r : {r} , c : {c} , prev : {prev} , curr : {Board[r][c]}")
            if prev and Board[r][c] == prev and prev != " " :
                if c == len(Board[r]) - 1 :
                    return True
            elif prev and  Board[r][c] != prev :
                prev = Board[r][c] 
                break   
            prev = Board[r][c]
    #col   
    for c in range(len(Board)) :
        prev : str = None
        for r in range(len(Board[r]) ) :
            print(f" r : {r} , c : {c} , prev : {prev} , curr : {Board[r][c]}")
            if prev and Board[r][c] == prev and prev != " " :
                if r == len(Board[c]) - 1 :
                    return True
            elif prev and  Board[r][c] != prev :
                prev = Board[r][c] 
                break     
            prev = Board[r][c]  
    # diag1
    prev : str = None             
    for i in range(len(Board)) :
        print(f" DIAG: r : {i} , c : {i} , prev : {prev} , curr : {Board[r][c]}")
        if prev and Board[i][i] == prev and prev != " " :
            if i == len(Board) - 1 :
                return True
        elif prev and  Board[r][c] != prev :
            prev = Board[r][c] 
            break   
        prev = Board[i][i]    
    # diag2
    prev : str = None             
    for i in range(len(Board)) :
        print(f" DIAG: r : {i} , c : {i} , prev : {prev} , curr : {Board[r][c]}")
        if prev and Board[i][len(Board) - 1 -i] == prev and prev != " " :
            if i == len(Board) - 1 :
                return True
        elif prev and  Board[r][c] != prev :
            prev = Board[r][c] 
            break       
        prev = Board[i][len(Board) - 1 - i]   
    print("eval wiinner : out of all loops, returning false")     
    return False    

# we will have to evaluate for every possible move
# if anyone recursion says its not a draw , return false 
# in a particular recursion , we are supposed to create next move and evaluate , if its not a win , reRun the func with the dummyBoard thhis time
def CheckIfDraw (Board : list[list[str]],IscurrentPlayerP1) :
    for r in range(len(Board))   :
        for c in range(len(Board[r])) :
            if Board[r][c] == " " :
                DummyBoard = copy.deepcopy(Board)
                DummyBoard[r][c] = "0" if IscurrentPlayerP1 else "1"
                print(f"dummyEntry by {'p1' if IscurrentPlayerP1 else 'p2'} at row : {r} and col : {c} as {DummyBoard[r][c]} .... dummyBoard :")
                drawBoard(DummyBoard) 
                
                if evaluateWinner(DummyBoard) :
                    return False
                else :
                    if CheckIfDraw(DummyBoard,not IscurrentPlayerP1) :
                        return False
    return False                
                    


if __name__ == "__main__":

    IscurrentPlayerP1 = True
    play : bool = True
    while play :
        drawBoard(Board)
        print(f"{'p1 (0)' if IscurrentPlayerP1 else 'p2 (1)'}'s Move :")
        move(int(input("row :")),int(input("column : ")), IscurrentPlayerP1)
        if evaluateWinner(Board) :
            print(f"{'p1' if IscurrentPlayerP1 else 'p2'} Won") 
            play = False
        IscurrentPlayerP1 = not IscurrentPlayerP1