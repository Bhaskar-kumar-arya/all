# @tag:TicTacTie
import copy

Board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]


def drawBoard(Board: list[list[str]]):
    for row in range(len(Board)):
        string = ""
        for column in range(len(Board[row])):
            string += Board[row][column] + " | "
        print(string)
        print("------------")


def move(row, column, isFirstPlayer):

    if not (0 <= row < 3 and 0 <= column < 3):
        print("Invalid input")
        return False  # Indicate invalid move
    if Board[row][column] != " ":
        print("already occupied")
        return False  # Indicate invalid move
    Board[row][column] = "X" if isFirstPlayer else "O"
    return True  # Indicate valid move


def evaluateWinner(Board: list[list[str]]):

    size = len(Board)

    # Check rows
    for r in range(size):
        if Board[r][0] == Board[r][1] == Board[r][2] != " ":
            return True

    # Check columns
    for c in range(size):
        if Board[0][c] == Board[1][c] == Board[2][c] != " ":
            return True

    # Check diagonals
    if Board[0][0] == Board[1][1] == Board[2][2] != " ":
        return True
    if Board[0][2] == Board[1][1] == Board[2][0] != " ":
        return True

    return False


def CheckIfDraw(Board: list[list[str]], IscurrentPlayerP1):
    for r in range(len(Board)):
        for c in range(len(Board[r])):
            if Board[r][c] == " ":
                DummyBoard = copy.deepcopy(Board)
                DummyBoard[r][c] = "X" if IscurrentPlayerP1 else "O"

                if evaluateWinner(DummyBoard):
                    return False  # Found a move that leads to a win, so it's not a draw
                else:
                    if not CheckIfDraw(DummyBoard, not IscurrentPlayerP1):  # Use "not" to negate the result
                        return False  # Found a move that doesn't lead to a draw, so it's not a draw
    return True  # All moves lead to a draw or a win for the opponent, so it's a draw

if __name__ == "__main__":
    IscurrentPlayerP1 = True
    play: bool = True
    while play:
        drawBoard(Board)
        print(f"{'p1 (X)' if IscurrentPlayerP1 else 'p2 (O)'}'s Move :")
        while True:
            try:
                row = int(input("row :"))
                column = int(input("column : "))
                if move(row, column, IscurrentPlayerP1):
                    break  # Valid move, exit the inner loop
            except ValueError:
                print("Invalid input. Please enter numbers only.")
            except IndexError:
                print("Invalid input: Row and column must be between 0 and 2.")

        if evaluateWinner(Board):
            drawBoard(Board)
            print(f"{'p1' if IscurrentPlayerP1 else 'p2'} Won")
            play = False
        elif all(" " not in row for row in Board):
            drawBoard(Board)
            print("It's a Draw!")
            play = False
        else:
             IscurrentPlayerP1 = not IscurrentPlayerP1
