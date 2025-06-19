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
            