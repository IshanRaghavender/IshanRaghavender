import math


def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def check_winner(board):
    
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None


def is_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    
    
    if winner == 'O':
        return 10 - depth  
    elif winner == 'X':
        return depth - 10  
    elif is_draw(board):
        return 0  

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score


def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


def is_valid_move(board, row, col):
    return board[row][col] == ' '


def play_game():
    
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    print("Welcome to Tic-Tac-Toe! You're playing as X.")
    print_board(board)

    while True:
        
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if is_valid_move(board, row, col):
                    board[row][col] = 'X'
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter valid integers for row and column.")

        print_board(board)

        # Check if the human player won
        if check_winner(board) == 'X':
            print("You win!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        # AI (O) turn
        print("AI is making a move...")
        best_move = get_best_move(board)
        board[best_move[0]][best_move[1]] = 'O'
        print_board(board)

        
        if check_winner(board) == 'O':
            print("AI wins!")
            break

        if is_draw(board):
            print("It's a draw!")
            break


play_game()
