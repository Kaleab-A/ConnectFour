col = 7
row = 6
board  = [[0 for i in range(col)] for j in range(row)]


def draw_board():
    for i in range(row):
        for j in range(col):
            item = " "
            if board[i][j] == 1:
                item = "X"
            elif board[i][j] == 2:
                item = "O"
            print("| " + item + " |" , end="")
        print("\n-----------------------------------")

def make_move(turn):
    global board
    player = 0
    if turn:  player = 1
    else: player = 2

    col_choosen = int(input("Enter the column (From 1 to 7):"))
    if col_choosen < 1 or col_choosen > col:
        print("Invalid Input")
        make_move(turn)
    elif board[0][col_choosen - 1] != 0:
        print("Column is full")
        make_move(turn)
    else:
        for i in range(row-1, -1, -1):
            if board[i][col_choosen - 1] == 0:
                board[i][col_choosen - 1] = player
                break


def isBoardFull():
    cnt = 0
    for i in board:
        for j in i:
            if j != 0:
                cnt += 1
    if cnt == row * col:
        return True
    return False   
    
def isWinner():
    for i in range(row):
        for j in range(col):
            if j + 3 < col and (board[i][j] != 0 and (board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3])):
                return board[i][j]
            elif i + 3 < row and board[i][j] != 0 and (board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j]):
                return board[i][j]
            elif i + 3 < row and j + 3 < col and board[i][j] != 0 and (board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]):
                return board[i][j]
            elif i + 3 < row and j - 3 >= 0 and board[i][j] != 0 and (board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3]):
                return board[i][j]
    return None


def main():
    turn = 0
    while not isBoardFull() and not (isWinner() != None):
        draw_board()
        print()
        make_move(turn)
        turn = 1 - turn

        
    draw_board()

    winner = isWinner()
    if winner == 1: print("Player 1 Wins")
    elif winner == 2: print("Player 2 Wins")
    else: print("Stalemate")

main()

    