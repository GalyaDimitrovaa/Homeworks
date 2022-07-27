import getpass

print(" -------------------------")
print("|   Rock Paper Scissors     |")
print(" -------------------------")
print(" Rock beats scissors.")
print(" Scissors cut paper.")
print(" Paper win's against rock.")


def rock_paper_scissors():

    Player1Score=0 
    Player2Score=0

    player_1 = input("\nPlayer 1, What's your name? ")
    player_2 = input("Player 2, What's your name? ")

    while True:

        choices = ["rock", "paper", "scissors"]

        check = True
        while check:
            player1Choice = getpass.getpass(("\n%s, Rock / Paper / Scissors " % player_1))
            if(player1Choice.lower() in choices):
                check=False
            else:
                print("Wrong Input! Enter Again! ")

        check = True
        while check:        
            player2Choice = getpass.getpass(("%s, Rock / Paper / Scissors " % player_2))
            if(player2Choice.lower() in choices):
                check=False
            else:
                print("Wrong Input! Enter Again! ")

        if player1Choice == player2Choice:
            print("Tie, try again!")
        
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
        

        print("\n=================- Score Board -=================")
        print(f"{player_1.title()}: {Player1Score} | {player_2.title()}: {Player2Score}")
        print("=================================================")
        
            

        play_again = input("Another round? [Yes / No] : ")
        if play_again.lower() != "yes":
            print("See you next time, bye ... :( ")
            break




rock_paper_scissors()