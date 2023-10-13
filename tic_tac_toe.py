import math


board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# board = [1,2,3,4,5,6,7,8,9]

def print_board(board):
    for i in range(0,4,3):
        print(f'{board[i]} | {board[i+1]} | {board[i+2]}')
        print("-"*9)
    i = 6
    print(f'{board[i]} | {board[i+1]} | {board[i+2]}')


def isGameOver(board):
    winning_combos = [[1,2,3],[4,5,6],[7,8,9],
                      [1,4,7],[2,5,8],[3,6,9],
                      [1,5,9],[3,5,7]]
    
    for combos in winning_combos:
        if board[combos[0]-1] == board[combos[1]-1] == board[combos[2]-1] != " ":
            return board[combos[0]-1]
        
    if " " not in board:
        return "draw"
    
    return None


def evaluate(board):

    winner = isGameOver(board)
    
    if winner == Player_O:
        return 1
    elif winner == Player_X:
        return -1
    else:
        return 0


def minimax(board,depth,alpha,beta,is_max):

    if isGameOver(board) is not None or depth == 0:
        return evaluate(board)
    
    if is_max:
        max_val = -math.inf
        for i in range (9):
            if board [i] == " ":
                board [i] = Player_O
                eval_val = minimax(board,depth-1,alpha,beta,False)
                board [i] = " "
                max_val = max(max_val,eval_val)
                alpha = max(alpha,eval_val)
                if alpha >= beta:
                    break
        return max_val
    
    else:
        min_val = math.inf
        for i in range (9):
            if board [i] == " ":
                board [i] = Player_X
                eval_val = minimax(board,depth-1,alpha,beta,True)
                board [i] = " "
                min_val = min(eval_val,min_val)
                beta = min(beta,eval_val)
                if alpha >= beta:
                    break
        return min_val

def best_move(board):
    best_score = -math.inf
    move = -10
    
    for i in range(9):
        if board[i] == " ":
            board[i] = Player_O
            move_score = minimax(board, 9, -math.inf, math.inf, False)
            board[i] = " "
            
            if move_score > best_score:
                best_score = move_score
                move = i
    
    return move

if __name__ == "__main__":
    Player_X = "X"
    Player_O = "O"
    k = 0
    while True:
        print_board(board)
        winner = isGameOver(board)
        
        if winner is not None:
            if winner == "draw":
                print("It's a tie!")
            else:
                print("Player", winner, "wins!")
            break
        
        if k == 0:
            # Player X's turn (User)
            while True:
                move = int(input("Enter X's move (1-9): "))
                if board[move-1] == " ":
                    k = 1
                    board[move-1] = Player_X
                    break
                else:
                    print("Invalid move! Try again.")
        else:
            # Player O's turn (AI)
            k = 0
            move = best_move(board)
            board[move] = Player_O