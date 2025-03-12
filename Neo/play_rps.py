#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 28, 2025

# Handles Rock, Paper, Scissors gameplay 

import random

def play_rps(character):
    """Function to play Rock, Paper, Scissors with the AI"""
    choices = ['rock', 'paper', 'scissors']
    print(f"\n{character.get_nickname()} vs AI: Rock, Paper, Scissors! Choose your move.")

    player_choice = input("Enter rock, paper, or scissors: ").lower()
    while player_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        player_choice = input("Enter rock, paper, or scissors: ").lower()

    ai_choice = random.choice(choices)
    print(f"AI chooses {ai_choice}.")

    if player_choice == ai_choice:
        return "draw"
    elif (player_choice == "rock" and ai_choice == "scissors") or \
         (player_choice == "paper" and ai_choice == "rock") or \
         (player_choice == "scissors" and ai_choice == "paper"):
        return "win"
    else:
        return "lose"
