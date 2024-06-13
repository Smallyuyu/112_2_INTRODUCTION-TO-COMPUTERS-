#H24121133 統計一 陳星宇
import random

def create_board(length=30, penalty_probability=0.3):
    board = []
    for _ in range(length):
        if random.random() < penalty_probability:
            board.append('P')  # 'P' represents a penalty square
        else:
            board.append('_')  # '_' represents a safe square
    return board

def roll_dice():
    return random.randint(1, 6)

def print_board(board, player_a_pos, player_b_pos, player_a_skip, player_b_skip):
    display_board = board[:]
    if player_a_pos == player_b_pos:
        if board[player_a_pos] == '_':
            display_board[player_a_pos] = 'X'
        else:
            display_board[player_a_pos] = 'x'
    else:
        if board[player_a_pos] == '_':
            display_board[player_a_pos] = 'A' if not player_a_skip else 'a'
        else:
            display_board[player_a_pos] = 'a'
        if board[player_b_pos] == '_':
            display_board[player_b_pos] = 'B' if not player_b_skip else 'b'
        else:
            display_board[player_b_pos] = 'b'
    for i in range(len(display_board)):
        if(display_board[i] == 'P'):
            display_board[i] = '_'
    print("".join(display_board),end = ' ')
    print('(A:',player_a_pos,', B:',player_b_pos,')')

def play_game():
    board = create_board()
    player_a_pos = 0
    player_b_pos = 0
    player_a_skip = False
    player_b_skip = False
    
    while player_a_pos < len(board) - 1 and player_b_pos < len(board) - 1:
        if not player_a_skip:
            player_a_pos += roll_dice()
            if player_a_pos >= len(board) - 1:
                player_a_pos = len(board) - 1
            else:
                player_a_skip = (board[player_a_pos] == 'P')
        else:
            player_a_skip = False
        
        if not player_b_skip:
            player_b_pos += roll_dice()
            if player_b_pos >= len(board) - 1:
                player_b_pos = len(board) - 1
            else:
                player_b_skip = (board[player_b_pos] == 'P')
        else:
            player_b_skip = False
        
        print_board(board, player_a_pos, player_b_pos, player_a_skip, player_b_skip)
        
        if player_a_pos == len(board) - 1 and player_b_pos < len(board) - 1:
            if player_b_skip:
                break
        elif player_b_pos == len(board) - 1 and player_a_pos < len(board) - 1:
            if player_a_skip:
                break

    if player_a_pos == len(board) - 1 and player_b_pos == len(board) - 1:
        print("Both players win!")
    elif player_a_pos == len(board) - 1:
        print("Player A wins!")
    elif player_b_pos == len(board) - 1:
        print("Player B wins!")
    
    print_final_board(board, player_a_pos, player_b_pos)

def print_final_board(board, player_a_pos, player_b_pos):
    print('')
    display_board = board[:]
    display_board[player_a_pos] = '_'
    display_board[player_b_pos] = '_'
    print("".join(display_board))

if __name__ == "__main__":
    play_game()
