game_list_row1 = ['7',' | ','8',' | ','9']
game_list_row2 = ['4',' | ','5',' | ','6']
game_list_row3 = ['1',' | ','2',' | ','3']
player1_piece = ''
player2_piece = ''
gameon = True
current_player = 'player1'
num_plays = 0
total_possible_plays = 9
wining_piece = ''

def display_game():
    global game_list_row1
    global game_list_row2
    global game_list_row3

    print('Here is the current board')
    print(' '.join(game_list_row1))
    print('---------------')
    print(' '.join(game_list_row2))
    print('---------------')
    print(' '.join(game_list_row3))

def player_piece_choice():
    global player1_piece
    global player2_piece

    choice = ''
    valid_choices = ['X', 'O']
    while choice not in valid_choices:
        choice = input('Please pick a piece (X or O): ').upper()
        if choice not in valid_choices:
            print('Sorry! That is not a valid option')
    if choice in valid_choices:
        player1_piece = choice
        if choice == 'X':
            player2_piece = 'O'
        else:
            player2_piece = 'X'

def position_choice():
    choice = 'Wrong'
    acceptable_values = ['1','2','3','4','5','6','7','8','9']

    while choice not in acceptable_values:
        print(f'{current_player.capitalize()}')
        choice = input('Pick a position 1-9: ')

        if choice not in acceptable_values:
            print('Sorry! Not a valid choice')

    return choice

def update_row(position, piece):
    global game_list_row1
    global game_list_row2
    global game_list_row3
    global num_plays

    if position in ['1','2','3']:
        if position in game_list_row3:
            game_list_row3 = [section.replace(position, piece) for section in game_list_row3]
            num_plays += 1
        else:
            print('This position has already been taken!')
            player_input()
    elif position in ['4','5','6']:
        if position in game_list_row2:
            game_list_row2 = [section.replace(position, piece) for section in game_list_row2]
            num_plays += 1
        else:
            print('This position has already been taken!')
            player_input()
    elif position in ['7','8','9']:
        if position in game_list_row1:
            game_list_row1 = [section.replace(position, piece) for section in game_list_row1]
            num_plays += 1
        else:
            print('This position has already been taken!')
            player_input()
    else:
        print('Not Found')


def replacement_position(position, player):
    if player == 'player1':
        update_row(position, player1_piece)
    else:
        update_row(position, player2_piece)
    display_game()


def player_input():
    global current_player
    position = position_choice()
    replacement_position(position, current_player)
    if current_player == 'player1':
        current_player = 'player2'
    else:
        current_player = 'player1'


def check_horizontal_rows():
    global wining_piece
    if len(set(game_list_row1)) == 2:
        wining_piece = game_list_row1[0]
        gameon = False
    elif len(set(game_list_row2)) == 2:
        wining_piece = game_list_row2[0]
        gameon = False
    elif len(set(game_list_row3)) == 2:
        wining_piece = game_list_row3[0]
        gameon = False

def check_vertical_rows():
    global wining_piece
    first_row = [game_list_row1[0], game_list_row2[0], game_list_row3[0]]
    second_row = [game_list_row1[2], game_list_row2[2], game_list_row3[2]]
    third_row = [game_list_row1[4], game_list_row2[4], game_list_row3[4]]
    if len(set(first_row)) == 1:
        wining_piece = first_row[0]
        gameon = False
    elif len(set(second_row)) == 1:
        wining_piece = second_row[0]
        gameon = False
    elif len(set(third_row)) == 1:
        wining_piece = third_row[0]
        gameon = False

def check_diagonal_rows():
    global gameon
    first_diagonal = [game_list_row1[0], game_list_row2[2], game_list_row3[4]]
    second_diagonal = [game_list_row1[4], game_list_row2[2], game_list_row3[0]]

    if set(first_diagonal) == 0:
        wining_piece = first_diagonal[0]
        gameon = False
    elif set(second_diagonal) == 0:
        wining_piece = second_diagonal
        gameon = False


def game_over():
    global gameon
    check_horizontal_rows()
    if len(wining_piece) == 0:
        check_vertical_rows()
    if len(wining_piece) == 0:
        check_diagonal_rows()
    if len(wining_piece) > 0:
        wining_player()
    if num_plays >= total_possible_plays:
        print('Cat got the game!')
        gameon = False
        continue_game()


def wining_player():
    global gameon
    if wining_piece == player1_piece:
        print('Player 1 won!! Congratulations!')
        gameon = False
        continue_game()
    elif wining_piece == player2_piece:
        print('Player 2 won!! Congratulations!')
        gameon = False
        continue_game()

def reset_board():
    global game_list_row1
    global game_list_row2
    global game_list_row3

    game_list_row1 = ['7',' | ','8',' | ','9']
    game_list_row2 = ['4',' | ','5',' | ','6']
    game_list_row3 = ['1',' | ','2',' | ','3']


def play_game():
    player_piece_choice()

    while gameon:
        display_game()
        player_input()
        game_over()

def continue_game():
    global gameon
    choice = 'Wrong'
    acceptable_values = ['Y', 'N']
    while choice not in acceptable_values:
        choice = input('Do you to play again? (Y, N): ').upper()
        if choice not in acceptable_values:
            print('I\'m sorry! I do not understand')

    if choice == 'Y':
        print('Lets go!')
        reset_board()
        gameon = True
        play_game()
    else:
        print('Thank you for playing!')


play_game()
