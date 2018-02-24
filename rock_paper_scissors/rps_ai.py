from random import choice

print("Time to play rock paper scissors!")
player = input("Enter your choice: ").lower()
computer = choice(["rock", "paper", "scissors"])
print(f"The computer plays: {computer}")

if player == computer:
    print("A draw!")
elif player == "rock":
    if computer == "scissors":
        print("Player wins!")
    elif computer == "paper":
        print("Computer wins!")
elif player == "paper":
    if computer == "rock":
        print("Player wins!")
    elif computer == "scissors":
        print("Computer wins!")
elif player == "scissors":
    if computer == "rock":
        print("Computer wins!")
    elif computer == "paper":
        print("Player wins!")
else:
    print("Something has gone wrong, please try again")
