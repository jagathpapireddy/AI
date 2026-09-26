board = [" " for _ in range(9)]
def print_board():

    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")
def check_winner(b, player):
 
    row1 = b[0] == player and b[1] == player and b[2] == player
    row2 = b[3] == player and b[4] == player and b[5] == player
    row3 = b[6] == player and b[7] == player and b[8] == player
    
    col1 = b[0] == player and b[3] == player and b[6] == player
    col2 = b[1] == player and b[4] == player and b[7] == player
    col3 = b[2] == player and b[5] == player and b[8] == player
    
    diag1 = b[0] == player and b[4] == player and b[8] == player
    diag2 = b[2] == player and b[4] == player and b[6] == player

    return row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2

def get_free_spaces():

    return [i for i, spot in enumerate(board) if spot == " "]

def player_move():
    
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in get_free_spaces() and 0 <= move <= 8:
                board[move] = "X"
                break
            else:
                print("That spot is already taken or invalid! Try again.")
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

def minimax(board_state, is_maximizing):
    if check_winner(board_state, "O"):
        return 1
    if check_winner(board_state, "X"):
        return -1
    if " " not in board_state:
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board_state[i] == " ":
                board_state[i] = "O"
                score = minimax(board_state, False)
                board_state[i] = " "  # Undo move
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board_state[i] == " ":
                board_state[i] = "X"
                score = minimax(board_state, True)
                board_state[i] = " "  # Undo move
                best_score = min(score, best_score)
        return best_score

def bot_move():
    best_score = float('-inf')
    best_move = None
    
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "  # Undo move
            if score > best_score:
                best_score = score
                best_move = i
                
    if best_move is not None:
        board[best_move] = "O"

def play_game():
    print("Welcome to UNBEATABLE Tic-Tac-Toe!")
    print("Positions are ordered 1 through 9 from top-left to bottom-right.")
    print_board()

    while True:

        player_move()
        print_board()
        if check_winner(board, "X"):
            print("🎉 Wow! You beat the unbeatable bot!")
            break
        if not get_free_spaces():
            print("🤝 It's a draw!")
            break
        print("Bot is calculating the perfect move...")
        bot_move()
        print_board()
        if check_winner(board, "O"):
            print("🤖 The bot wins! It played perfectly.")
            break
        if not get_free_spaces():
            print("🤝 It's a draw!")
            break
if __name__ == "__main__":
    play_game()
