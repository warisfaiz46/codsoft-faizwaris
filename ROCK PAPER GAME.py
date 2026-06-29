import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print("=== Rock, Paper, Scissors Game ===")
    print("Instructions: Type rock, paper, or scissors to play.")
    print("Type 'quit' anytime to end the game.\n")

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower().strip()

        if user_choice == "quit":
            print("\nThanks for playing!")
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please choose rock, paper, or scissors.\n")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if result == "tie":
            print("Result: It's a tie!")
        elif result == "user":
            print("Result: You win this round!")
            user_score += 1
        else:
            print("Result: Computer wins this round!")
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}\n")

        play_again = input("Do you want to play another round? (yes/no): ").lower().strip()
        if play_again != "yes":
            print("\nThanks for playing!")
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break
        print()

play_game()
