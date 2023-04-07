BOARD = {1: ' ',  2: ' ',  3: ' ',

        4: ' ',  5: ' ',  6: ' ',

        7: ' ',  8: ' ',  9: ' '}



def render():
    '''
    Returns a string describing the board in its
    current state. It should look something like this:

     1 | 2 | 3
     - + - + -
     4 | 5 | 6
     - + - + -
     7 | 8 | 9

    Returns
    -------
    board_state : str

    Implements (See also)
    ---------------------
    BOARD : dict
    '''
    board_state = BOARD[1] + '|' + BOARD[2] + '|' + BOARD[3] + '\n' + "-+-+-" + '\n' + BOARD[4] + '|' + BOARD[5] + '|' + BOARD[6] + '\n' + "-+-+-" + '\n' + BOARD[7] + '|' + BOARD[8] + '|' + BOARD[9] + '\n'
    return board_state


def get_action(player):
    '''
    Prompts the current player for a number between 1 and 9.
    Checks* the returning input to ensure that it is an integer
    between 1 and 9 AND that the chosen board space is empty.

    Parameters
    ----------
    player : str

    Returns
    -------
    action : int

    Raises
    ======
    ValueError, TypeError

    Implements (See also)
    ---------------------
    BOARD : dict

    *Note: Implementing a while loop in this function is recommended,
    but make sure you aren't coding any infinite loops.
    '''
    
    place = input("Your turn enter a number to move to that place(1-9):\n")
    if place.isdigit():
         if int(place) > 0 and int(place) < 10:
              return int(place)
         else:
            print("Value Error")
    else:
         print("Type Error")    

def victory_message(player):
    '''
    Prints the updated board and returns a victory message for the
    winning player.

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    victory_message : str

    Implements (See also)
    ---------------------
    print_t3() : func
    '''
    # ----------------
    
    print(render())
    victory_message = "Contrats " + player + " wins" + '\n'
    return victory_message            


def check_win(player):
    '''
    Checks victory conditions. If found, calls victory_message().
    This can be done with one long chain of if/elif statements, but
    it can also be condensed into a single if/else statement, among
    other strategies (pattern matching if you have python 3.10 or above).

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    True or False : bool

    Implements (See also)
    ---------------------
    BOARD : dict
    victory_message(player) : func
    '''
    if BOARD[1] == BOARD[2] == BOARD[3] == player: # across the top
        victory_message(player)
        return True              
                
    elif BOARD[4] == BOARD[5] == BOARD[6] == player: # across the middle
        victory_message(player)
        return True 

    elif BOARD[7] == BOARD[8] == BOARD[9] == player: # across the bottom
        victory_message(player)
        return True   

    elif BOARD[1] == BOARD[4] == BOARD[7] == player: # down the left side
        victory_message(player)
        return True  

    elif BOARD[2] == BOARD[5] == BOARD[8] == player: # down the middle
        victory_message(player)
        return True  

    elif BOARD[3] == BOARD[6] == BOARD[9] == player: # down the right side
        victory_message(player)
        return True         

    elif BOARD[7] == BOARD[5] == BOARD[3] == player: # diagonal
        victory_message(player)
        return True     

    elif BOARD[1] == BOARD[5] == BOARD[9] == player: # diagonal
        victory_message(player)
        return True 
    else:
        return False        

def play_t3():
    '''
    This is the main game loop that is called from the launcher (main.py)

    Implements (See also)
    ---------------------
    BOARD : dict
    render() : func
    get_action(player) : func
    check_win(player) : func
    play_t3()* : func

    *Note: this function refers to itself. Be careful about
    inescapable infinite loops.
    '''

    player = 'X'
    game_round = 0
    game_over = False

    while not game_over:


        # Print the current state of the board
        print(render())
        # Get the current player's action and assign it to a variable called 'action'.
        action = get_action(player)
        # Assign the current player ('X' or 'O') as a value to BOARD. Use the 'action' variable as the key.
        if BOARD[action] == ' ':
            BOARD[action] = player
        # Increment the game round by 1.
        game_round += 1
        # Check if the game is winnable (game_round >= 4),
            # then check for win conditions (check_win(player)),
                # and if there's a win, end the game (game_over = True),
                # and break the loop (break).
        if game_round >= 4:
             result = check_win(player)
             if result == True:
                with open("score.txt", "a") as save:
                    save.write(f" Player {player} Wins\n")
                game_over = True
                break
             
        # Check if there are any open spots left (game_round == 9),
            # and if there aren't, print a tie message,
            # end the game,
            # and break the loop.
        if game_round == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            break
        # switch players with a quick conditional loop.
        if player =='X':
            player = 'O'
        else:
            player = 'X' 

    # prompt for a restart and assign the input to a 'restart' variable.
    # if yes,
        # clear each key in the board with a for loop
    restart = input("Do want to play Again?(y/n)")
    
    if restart == "y" or restart == "Y":  
        for key in BOARD:
            BOARD[key] = " "
        play_t3()
          
    # and reinitiate the game loop (play_t3()).
        

if __name__ == "__main__":
    play_t3