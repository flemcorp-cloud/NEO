#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 28, 2025

# Chapter 5 of the game

import play_rps

def chapter_5(character):
    """Chapter 5"""
    print("\nChapter 5: The Final Decision")
    print(f"Everything blurs together—the world, the code, the AI. This is {character.get_nickname()}'s final chance to play their way out of the system.")
    print(f"The virtual world becomes completely unstable as the final round of Rock, Paper, Scissors begins. {character.get_nickname()} must try to use all their wits to win or be trapped inside the system.")
    return play_rps.play_rps(character)

