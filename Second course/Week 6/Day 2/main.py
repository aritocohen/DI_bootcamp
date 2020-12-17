"""
RULES:

The game is played on a grid that’s 3 squares by 3 squares.

Players take turns putting their marks (O or X) in empty squares.

The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.

When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
"""


def display_board(board):
    """
    **************
    *       |       |       *
    *   ---|------|----  *
    *       |       |        *
    *   ---|------|----   *
    *       |       |       *
    **************
    """
    print(f"**************")
    print(f"*   {board[0][0]}   |   {board[0][1]}  |   {board[0][2]}   *")
    print(f"*   ----|------|----  *")
    print(f"*   {board[1][0]}   |   {board[1][1]}  |   {board[1][2]}   *")
    print(f"*   ----|------|----  *")
    print(f"*   {board[2][0]}   |   {board[2][1]}  |   {board[2][2]}   *")
    print(f"**************")


def ask_for_mark(board):
    """
    Asking the user where to put the mark and return the mark coordinates
    """
    display_board(board)
    row = input("Enter row: ")
    col = input("Enter col: ")
    print("\n")
    # row and col are strings, convert them to integers
    row = int(row)
    col = int(col)

    # TODO: Check that the row and column are valid

    return [row, col]


def put_mark_in_grid(board, mark, position):
    """
    Placing a mark in the grid
    :param position: Index of the mark [row, column]
    """
    # Unpacking the list and retrieving the row and column index
    row, col = position

    # Make sure that the place is available
    if not board_place_available(board, row, col):
        # If the place is not available, stop the function and return false
        return False

    # Assigning the place in the grid to this mark 
    board[row][col] = mark

    return True  # Return True => Function is a success


def board_place_available(board, row, col):
    """
    Check if the place row,col is available in the board
    """
    if board[row][col] == "  ":
        return True
    else:
        return False


def board_full(board):
    """
    Returns true if the board is full (no places left)
    """
    # Double for loop
    for row in grid:  # The first one is iterating on the lists in the list
        for elem in row:  # The second one is iterating on the elements of the nested list

            if elem == "  ":  # At least one place is empty, so the board is not full   
                return False

    # If we finish the loop without returning false, it means that the board is full
    return True


def check_win(board):
    """
    Checks if one player won the game --> Row/Column/Diagonal is the same mark
    """
    # 1) Check every row
    for row in board:
        # Check if all the marks in the row are the same:
        if row[0] == row[1] == row[2] != "  ":
            # Return the winning mark
            return row[0]

    # 2) Check every column
    if board[0][0] == board[1][0] == board[2][0] != "  ":
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] != "  ":
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] != "  ":
        return board[0][2]

    # 3) Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "  ":
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != "  ":
        return board[0][2]

    ### Nothing has been found --> no one is winning
    return False


PLAYER_1 = "X"  # The variables are in uppercase letters
PLAYER_2 = "O"

grid = [
    ["  ", "  ", "  "],
    ["  ", "  ", "  "],
    ["  ", "  ", "  "]
]

display_board(grid)

# 4 - Do it again for the next user --> Loop
current_player = PLAYER_1

continue_game = True
while continue_game:

    # Ask the user where he wants to put his mark
    position = ask_for_mark(grid)

    # Put the mark on the board
    put_mark_in_grid(grid, current_player, position)

    # Check if there is any win/endgame
    if check_win(grid) != False:  # check_win(grid) can return "X", "O" or False
        display_board(grid)
        print(f"{current_player} WON !")
        continue_game = False
    elif board_full(grid):
        display_board(grid)
        print("Draw !")
        continue_game = False

    # Change current user
    if current_player == PLAYER_1:
        current_player = PLAYER_2
    else:  # current player is PLAYER_2
        current_player = PLAYER_1



