import itertools

def print_board(board):
    print('-------------')
    for row in board:
        print(f"| {' | '.join(row)} |")
        print('-------------')

def get_player_choice(player, board):
    while True:
        choice = input(f"Player {player}, enter a row and column number (e.g. 1,2): ")
        row, col = map(int, choice.split(','))
        if board[row-1][col-1] == '-':
            return row-1, col-1
        else:
            print("This position is already taken, please choose another one.")

def check_winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != '-':
            return row[0]

    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != '-':
            return board[0][col]

    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != '-':
        return board[0][0]

    if len(set([board[i][2-i] for i in range(3)])) == 1 and board[0][2] != '-':
        return board[0][2]

    return None

def play_game():
    print("Welcome to Tic Tac Toe!")

    players = itertools.cycle(['X', 'O'])
    board = [['-' for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        player = next(players)
        row, col = get_player_choice(player, board)
        board[row][col] = player
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        if all([cell != '-' for row in board for cell in row]):
            print("It's a tie!")
            break

if __name__ == '__main__':
    play_game()
