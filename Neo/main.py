#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 28, 2025

# Main game loop

import character
import chapter_1
import chapter_2
import chapter_3
import chapter_4
import chapter_5

def main():
    """Main function to play the game"""
    print("Welcome to Neo's Escape - A Rock, Paper, Scissors Game!")

    # Create Neo as the main character
    neo = character.Character('Neo', ['rock', 'paper', 'idea', 'scissors'], ['slow'])
    print(f"\n{neo.get_nickname()} is ready to face the AI!")

    # Track wins, losses, and draws
    wins = 0
    losses = 0
    draws = 0

    # List of chapter functions
    chapters = [chapter_1.chapter_1, chapter_2.chapter_2, chapter_3.chapter_3, chapter_4.chapter_4, chapter_5.chapter_5]

    # Play through all chapters
    for chapter_func in chapters:  # Call the correct function
        result = chapter_func(neo)  # Pass the character object to each chapter function
        if result == "win":
            wins += 1
        elif result == "lose":
            losses += 1
        else:
            draws += 1

    # Final result
    print("\nGame Over!")
    print(f"Total Wins: {wins}, Total Losses: {losses}, Total Draws: {draws}")

    if wins >= 3:
        print(f"Congratulations {neo.get_nickname()}, You have won enough rounds and are free!")
    else:
        print(f"{neo.get_nickname()}, you have lost the game. You are trapped inside the system.")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")  # Keeps window open

