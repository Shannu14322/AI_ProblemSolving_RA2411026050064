import math

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(player):
    win_positions = [(0,1,2),(3,4,5),(6,7,8),
                     (0,3,6),(1,4,7),(2,5,8),
                     (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==player for a,b,c in win_positions)

def is_full():
    return " " not in board

def minimax(is_max):
    if check_winner("X"):
        return -1
    if check_winner("O"):
        return 1
    if is_full():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(True))
                board[i] = " "
        return best

def ai_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            val = minimax(False)
            board[i] = " "
            if val > best_val:
                best_val = val
                move = i
    board[move] = "O"

def play():
    while True:
        print_board()
        pos = int(input("Enter position (0-8): "))
        if board[pos] == " ":
            board[pos] = "X"
        else:
            continue

        if check_winner("X"):
            print("You win!")
            break

        ai_move()

        if check_winner("O"):
            print("AI wins!")
            break

        if is_full():
            print("Draw!")
            break

play()
