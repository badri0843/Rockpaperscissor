
import random

options = ("rock", "paper", "scissors")
running = True

player_score = 0
computer_score = 0

while running:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
        
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a TIE")
    elif player == "rock" and computer == "scissors":
        print("You WON the game")
        player_score += 1
    elif player == "paper" and computer == "rock":
        print("You WON the game")
        player_score += 1
    elif player == "scissors" and computer == "paper":
        print("You WON the game")
        player_score += 1
    else:
        print("You LOSE the game")
        computer_score += 1
    
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    
    if input("Play again? (yes/no): ").lower() != "yes":
        running = False

print("Thanks for playing!")
