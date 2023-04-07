def playgame():

    with open("score.txt", "a") as save:


        #loop game best of 5
        player1_score = 0
        player2_score = 0
        while player1_score < 3 or player2_score < 3:
            answers = ["r", "p", "s"]
            user1 = input("Rock(r), Papper(p) or Scissors(s)?\n")
            #if input is valid
            if user1.endswith("r") or user1.endswith("p") or user1.endswith("s"):
                print("Player 1 you chose ", user1)
            else: print("invalid option")

            user2 = input("Rock(r), Papper(p) or Scissors(s)?\n")
            if user2.endswith("r") or user2.endswith("p") or user2.endswith("s"):
                print("Player 2 you chose ", user2)
            else: print("invalid option")

            #winner selection
            if user1 == "r" and user2 == "p" or user1 == "p" and user2 == "s" or user1 == "s" and user2 == "r":
                player2_score += 1
                print("Player 2 wins score:", player2_score)
                save.write(f"Player 2 score: {player2_score}\n")
            elif user1 == user2: print("Tie game")
            else: 
                player1_score += 1
                print("Player 1 wins score:", player1_score)
                save.write(f"Player 2 score: {player2_score}\n")

            #promt play again
            repeat = input("Best of 5? play again? (y)\n")
            if repeat == "y" and player1_score < 3 and player2_score < 3:
                continue
            else: break

        if player1_score > player2_score:
            print("thank you for playing player 1 wins")
        else: print("thank you for playing player 2 wins")

if __name__ == "__main__":
    playgame()

