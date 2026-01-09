#!/usr/bin/env python3
"""
Solution: Project 3 - Rock, Paper, Scissors Game
An interactive game
"""

import random

def get_computer_choice():
    """Generate random computer choice"""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine winner based on game rules"""
    if user_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        "rock": "scissors",      # Rock beats scissors
        "paper": "rock",         # Paper beats rock
        "scissors": "paper"      # Scissors beats paper
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"

def play_game():
    """Main game function"""
    print("Rock, Paper, Scissors Game")
    print("=========================")
    print()
    
    user_score = 0
    computer_score = 0
    
    while True:
        # Get user choice
        print("Choose: rock, paper, or scissors")
        print("Type 'quit' to exit")
        user_choice = input("Your choice: ").lower().strip()
        
        if user_choice == 'quit':
            break
        
        # Validate input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            print()
            continue
        
        # Generate computer choice
        computer_choice = get_computer_choice()
        
        # Display choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        
        # Update scores and display result
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win! 🎉")
            user_score += 1
        else:
            print("Computer wins! 💻")
            computer_score += 1
        
        # Display current scores
        print(f"\nScore - You: {user_score}, Computer: {computer_score}")
        print("-" * 40)
        print()
    
    # Display final scores
    print("\n" + "=" * 40)
    print("FINAL SCORE")
    print("=" * 40)
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    
    if user_score > computer_score:
        print("\n🏆 Congratulations! You won the game!")
    elif computer_score > user_score:
        print("\n💻 Computer won the game. Better luck next time!")
    else:
        print("\n🤝 It's a tie! Great game!")
    print("=" * 40)

if __name__ == "__main__":
    play_game()
