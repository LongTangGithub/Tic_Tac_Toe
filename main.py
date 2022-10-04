def build_board():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = list(board)
    for i in range(len(board)):
        if 'x' in str(board[i]):
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif 'o' in str(board[i]):
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    x = board[int(position) - 1]
    return str(x).isnumeric()


def fill_spot(board, position, character):
    x = character.strip()  # get rid of any whitespace
    board[int(position) - 1] = x


def winning_game(board):
    valid = any(board[i] == board[i + 1] and board[i] == board[i + 2] for i in range(0, 7, 3))

    for i in range(3):
        if board[i] == board[i + 3] and board[i] == board[i + 6]:
            valid = True
    if (board[0] == board[4]) and (board[0] == board[8]):
        valid = True
    if (board[2] == board[4]) and (board[2] == board[6]):
        valid = True
    return valid


def game_over(board):
    if winning_game(board):
        return True
    store = 0
    for i in board:
        if not str(i).isnumeric():
            store = store + 1
    return store == 9


def get_winner(board):
    count_x = 0
    count_o = 0
    winner = ''
    for i in range(9):
        if board[i] == 'x':
            count_x += 1
        if board[i] == 'o':
            count_o += 1
    if count_x > count_o and winning_game(board):
        winner += 'x'
        print(count_x)
    if count_x == count_o and winning_game(board):
        winner += 'o'
        print(count_o)
    else:
        return 'None'
    return winner


def play(board):
    num = 1
    print('Are you ready to play?')
    keep_playing = input('Yes or No: ')
    while keep_playing in ['Yes', 'yes']:
        while not game_over(board):
            print_board(board)
            if num == -1:
                position = input("o's, choose a position: ")
                if is_legal(board, position):
                    fill_spot(board, position, 'o')
                else:
                    print("Illegal move. Try again.")
                    position = input("o's, choose a position: ")
                    if is_legal(board, position):
                        fill_spot(board, position, 'o')
            elif num == 1:
                position = input("x's, choose a position: ")
                if is_legal(board, position):
                    fill_spot(board, position, 'x')
                else:
                    print("Illegal move. Try again.")
                    position = input("x's, choose a position: ")
                    if is_legal(board, position):
                        fill_spot(board, position, 'x')
            num = num * -1
        print_board(board)
        print(f"{get_winner(board)} wins!")
        keep_playing = input("Do you want to play again? ")
        board2 = build_board()
        play(board2)


def main():
    board = build_board()
    play(board)


main()
