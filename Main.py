from RockPaper import playgame
from tictactoe import play_t3
# import Game for rock paper scissors

games = {
    """1: rock paper scissor 
    2: tic tac toe 
    3: TBD"""
}


while True:
    
    print(games)
    argument = input("Here are some games please enter a number:") 
    if argument == "1":
        playgame()
        break
    elif argument == "2":
        play_t3()
        break
    else:
        print("Invalid option")
        break


    

      
    
    
