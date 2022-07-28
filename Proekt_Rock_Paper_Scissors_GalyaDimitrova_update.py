import getpass
import sys

player_1 = input("\nPlayer 1, What's your name? ")
player_2 = input("Player 2, What's your name? ")

Player1Score = 0
Player2Score = 0


def menu():
    choice=True
    while choice:
        print("\n1) Rules", "\n2) New Game","\n3) See Scoreboard","\n4) Exit Game")

        choice = input("\nLET'S PLAY, Make a choice!  ")
        if choice=="1":
            print("\n -------------------------")
            print("|   Rock Paper Scissors     |")
            print(" -------------------------")
            print(" Rock beats scissors.")
            print(" Scissors cut paper.")
            print(" Paper win's against rock.")
           

        elif choice == "2":
            print("\nEnjoy the game")
            rock_paper_scissors()
            

        elif choice == "3":
            print("\nLet's see who is the best - You can check the scoreboard file too ...\n")
            scoreboard()
            

        elif choice=="4":
            print("\nGoodbye")
            sys.exit()
            

        else:
            print("\nInvalid input, please enter from 1 to 4 only ")
            break
    


def rock_paper_scissors():

    global Player1Score, Player2Score

    while True:

        choices = ["rock", "paper", "scissors"]

        check = True
        while check:
            player1Choice = getpass.getpass(("\n%s, Rock / Paper / Scissors " % player_1))
            if(player1Choice.lower() in choices):
                check=False
                break
            else:
                print("\nWrong Input! Enter Again! ")
           

        check = True
        while check:      

            player2Choice = getpass.getpass(("%s, Rock / Paper / Scissors " % player_2))
            if(player2Choice.lower() in choices):
                check=False
                break
            else:
                print("\nWrong Input! Enter Again! ")
            

        if player1Choice == player2Choice:
            print("\nTie, try again!")
             
        elif player1Choice == "rock" and player2Choice == "scissors": 
            print ("%s, Win\n" % player_1)
            Player1Score+=1
            
        elif player1Choice == 'scissors' and player2Choice == 'paper':
            print ("%s, Win\n" % player_1)
            Player1Score +=1
            
        elif player1Choice == 'paper' and player2Choice == 'rock':
            print ("%s, Win\n" % player_1)
            Player1Score +=1
            
        else:
            print("%s, Win\n" % player_2)
            Player2Score+=1
        
        
        play_again = input("Another round? [Yes / No] : ")
        if play_again.lower() != "yes":
            print("\nYou can EXIT the game from menu ...  ")
            break
         
def scoreboard():

    global Player1Score, Player2Score
    
    save_into_file = open('scorebored.txt', 'w')

    save_into_file.write("\n=================- Score Board -=================\n")
    save_into_file.write(f"{player_1.title()}: {Player1Score} | {player_2.title()}: {Player2Score}")
    save_into_file.write("\n=================================================")

    save_into_file.close()

    
if __name__ == "__main__":       

    menu()
    scoreboard()
    rock_paper_scissors()