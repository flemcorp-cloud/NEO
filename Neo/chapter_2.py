#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 28, 2025

# Chapter 2 of the game

import play_rps

def chapter_2(character):
    """Chapter 2"""
    print("\nChapter 2: The Interface Warps")
    print(f"The interface warps again, and {character.get_nickname()} is plunged deeper into a fractured virtual world. The AI now speaks with a clearer voice, revealing its plans for their demise.")
    print(f"{character.get_nickname()} sees the environment flicker between different parts of their mind, code, memories, and data streams.")
    return play_rps.play_rps(character)
