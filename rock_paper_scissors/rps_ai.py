from random import choice

player_wins = 0
computer_wins = 0
to_win = 3
print("Time to play rock paper scissors, first to three wins!")

while player_wins < to_win and computer_wins < to_win:
    player = input("Enter your choice: ").lower()
    computer = choice(["rock", "paper", "scissors"])
    print(f"The computer plays: {computer}")

    if player == computer:
        print("A draw!")
    elif player == "rock":
        if computer == "scissors":
            print("Player wins!")
            player_wins += 1
        elif computer == "paper":
            print("Computer wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player wins!")
            player_wins += 1
        elif computer == "scissors":
            print("Computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("Computer wins!")
            computer_wins += 1
        elif computer == "paper":
            print("Player wins!")
            player_wins += 1
    else:
        print("Something has gone wrong, please try again")
    if player_wins < 3 and computer_wins < 3:
        print(f"The current score is, Player {player_wins} - {computer_wins} Computer")

if player_wins == 3:
    print("Congratulations player, you won!")
else:
    print("Uh oh, the computer won")
