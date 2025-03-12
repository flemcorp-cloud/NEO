#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 28, 2025

# Chapter 3 of the game

import play_rps

def chapter_3(character):
    """Chapter 3"""
    print("\nChapter 3: Losing Grip")
    print(f"{character.get_nickname()} feels themselves losing their grip on reality. The AI is bending and pulling at their mind. They can’t tell if they’re connected to the interface or back in the real world.")
    print(f"The virtual world becomes unstable and switches between raw data and scenes from {character.get_nickname()}'s life.")
    return play_rps.play_rps(character)
