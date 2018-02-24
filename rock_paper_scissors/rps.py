print("Time to play rock paper scissors!")
player1 = input("Player 1, enter your choice: ")
player2 = input("Player 2, enter your choice: ")

if player1 == player2:
    print("A draw!")
elif player1 == "rock" and player2 == "scissors":
    print("Player 1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("Player 2 wins!")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins!")
elif player1 == "paper" and player2 == "scissors":
    print("Player 2 wins!")
elif player1 == "scissors" and player2 == "rock":
    print("Player 2 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins!")
else:
    print("Something has gone wrong, please try again")
